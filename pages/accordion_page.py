from playwright.sync_api import Page, expect

class AccordionPage:
    sections = [
        ("Section 1", "#ui-id-2", ["Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam."]),
        ("Section 2", "#ui-id-4", ["Sed non urna. Donec et ante. Phasellus eu ligula."]),
        ("Section 3", "#ui-id-6", ["Nam enim risus, molestie et, porta ac, aliquam ac, risus."]),
        ("Section 4", "#ui-id-8", [
            "Cras dictum. Pellentesque habitant morbi tristique senectus et",
            "Suspendisse eu nisl. Nullam ut libero. Integer dignissim consequat "
        ]),
    ]

    def __init__(self, page: Page):
        self.page = page

    def load_page(self, url: str):
        """Navigate to the given URL."""
        self.page.goto(url)

    def _get_iframe(self):
        """Return the iframe's content frame."""
        return self.page.locator("iframe").content_frame

    def _print_section_paragraphs(self, section_text_all):
        print("=== Paragraphs ===")
        for i, t in enumerate(section_text_all, start=1):
            print(f"- {i}: {t}")
        print("")

    def _print_section_list_items(self, iframe):
        items = iframe.locator("li")
        count = items.count()
        for i in range(count):
            text = items.nth(i).inner_text()
            print(text)
        print("\n")

    def _validate_panel(self, panel, expected_text, check_icon=False, iframe=None):
        expect(panel).to_have_attribute("aria-hidden", "false")
        section_text = panel.locator("p")
        section_text_all = section_text.all_inner_texts()
        self._print_section_paragraphs(section_text_all)
        expect(section_text).to_contain_text(expected_text)
        if check_icon and iframe:
            icon_arrow_s = iframe.locator("span.ui-accordion-header-icon.ui-icon.ui-icon-circle-arrow-s")
            if icon_arrow_s.is_visible():
                expect(icon_arrow_s).to_be_visible()
            else:
                print("Customize icon not found")

    def _handle_section(self, iframe, section_name, section_locator, expected_text, check_icon=False):
        print(f"{section_name} start checking...")
        panel = iframe.locator(section_locator)
        attribute = panel.get_attribute("aria-hidden")
        if attribute == "false":
            self.page.wait_for_timeout(1000)
            self._validate_panel(panel, expected_text, check_icon, iframe)
            if section_name == "Section 3":
                self._print_section_list_items(iframe)
        elif attribute == "true":
            iframe.get_by_role("tab", name=section_name).click()
            self.page.wait_for_timeout(1000)
            self._validate_panel(panel, expected_text, check_icon, iframe)
            if section_name == "Section 3":
                self._print_section_list_items(iframe)
        else:
            print(f"{section_name} has no aria-hidden attribute")

    def default_functionality(self):
        """Test default accordion functionality by clicking each tab, and validate paragraph"""
        print("\n")
        iframe = self._get_iframe()
        for section_name, section_locator, expected_text in self.sections:
            self._handle_section(iframe, section_name, section_locator, expected_text)

    def collapse_content(self):
        """Test accordion collapse/expand behavior and validate panel behavior."""
        print("\n")
        iframe = self._get_iframe()
        for section_name, section_locator, expected_text in self.sections:
            self._handle_section(iframe, section_name, section_locator, expected_text)

    def customize_icons(self):
        """Test accordion with custom icons and validate icon behavior."""
        print("\n")
        iframe = self._get_iframe()
        for section_name, section_locator, expected_text in self.sections:
            self._handle_section(iframe, section_name, section_locator, expected_text, check_icon=True)

    def fill_space(self):
        """Test accordion with fill space behavior."""
        print("\n")
        iframe = self._get_iframe()
        for section_name, section_locator, expected_text in self.sections:
            self._handle_section(iframe, section_name, section_locator, expected_text)