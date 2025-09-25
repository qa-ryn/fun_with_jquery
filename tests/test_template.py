from playwright.sync_api import Page, expect

def test_template(page: Page):
    sections = [
    ("Section 1", "#ui-id-2"),
    ("Section 2", "#ui-id-4"),
    ("Section 3", "#ui-id-6"),
    ("Section 4", "#ui-id-8"),
    ]

    page.goto("https://jqueryui.com/accordion/#collapsible")
    iframe = page.locator("iframe").content_frame

    for name, section_id in sections:
        panel = iframe.locator(section_id)

        attribute = panel.get_attribute("aria-hidden")

        if attribute == "false":
            print(f"{name} is already expanded → Code reach here 1")
        elif attribute == "true":
            # Click the related tab, not the panel
            iframe.get_by_role("tab", name=name).click()
            print(f"{name} was collapsed, clicked to expand → Code reach here 2")
        else:
            print(f"{name} has no aria-hidden attribute → Code reach here 3")