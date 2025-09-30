from playwright.sync_api import Page


def test_widget_autocomplete(page: Page):
    
    words = ["C", "P", "Ja", "R"]
    
    page.goto("https://jqueryui.com/autocomplete/#default")
    iframe = page.locator("iframe").content_frame
    input_locator = iframe.locator("#tags")
    
    for word in words:
        input_locator.fill("")
        input_locator.type(word)
        input_locator.press("Enter")
        
        items = iframe.locator("ul.ui-autocomplete li")
        
        page.wait_for_timeout(2000)
        suggestions = items.all_inner_texts()
        for suggestion in suggestions:
            print(f"Input {word} -> Suggestions = {suggestion}")

    