import re
from playwright.sync_api import Page, expect

def test_has_text(page: Page):
    page.goto("http://127.0.0.1:8050/")
    page.screenshot(path="playwright-tests/screenshots/has_text.png")
    expect(page.locator("body")).to_have_text(re.compile("Прогресс пользователей"))

def test_select_combobox(page: Page):
    page.goto("http://127.0.0.1:8050/")

    dropdown = page.locator("#user-dropdown")
    dropdown.click()

    page.wait_for_timeout(500)
    
    option = page.locator("div.VirtualizedSelectOption", has_text="mark")
    option.click()

    dropdown.screenshot(path="playwright-tests/screenshots/dropdown_selected.png")
    expect(dropdown).to_contain_text("mark")
