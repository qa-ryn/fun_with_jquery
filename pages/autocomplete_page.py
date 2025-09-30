from playwright.sync_api import Page

class AutoComplete:
    words = ["C", "P", "Ja", "Jo"]
    def __init__(self, page: Page):
        self.page = page
        
    def load_page(self, url: str):
        self.page.goto(url)
        
    def _get_iframe(self):
        return self.page.locator("iframe").content_frame
        
    def _handle_input(self, iframe, word):
        tag_locator = iframe.locator("#tags")
        developer_locator = iframe.locator("#developer")
        if tag_locator.is_visible():
            input_locator = iframe.locator("#tags")
            
            input_locator.fill("")
            input_locator.type(word)
            input_locator.press("Enter")
            
            items = iframe.locator("ul.ui-autocomplete li")
            self.page.wait_for_timeout(2000)
            suggestions = items.all_inner_texts()
            for suggestion in suggestions:
                print(f"Input {word} -> Suggestions = {suggestion}")
        elif developer_locator.is_visible():
            input_locator = iframe.locator("#developer")
            
            input_locator.fill("")
            input_locator.type(word)
            input_locator.press("Enter")
            
            items = iframe.locator("ul.ui-autocomplete li")
            self.page.wait_for_timeout(2000)
            suggestions = items.all_inner_texts()
            for suggestion in suggestions:
                print(f"Input {word} -> Suggestions = {suggestion}")
        else:
            print("Code reach here")
        
    def default_functionality(self):
        iframe = self._get_iframe()
        for word in self.words:
            self._handle_input(iframe, word)
            
    def accent_folding(self):
        iframe = self._get_iframe()
        for word in self.words:
            self._handle_input(iframe, word)