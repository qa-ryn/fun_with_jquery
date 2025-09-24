from playwright.sync_api import Page, expect

def test_default_functionality(page: Page):
    print("\n")
    page.get_by_role("link", name="Accordion").click()
    iframe = page.locator("iframe").content_frame
    
    sections = [
        ("Section 1", "#ui-id-1"),
        ("Section 2", "#ui-id-3"),
        ("Section 3", "#ui-id-5"),
        ("Section 4", "#ui-id-7"),
        ]
    
    for section_name, panel_id in sections:
        print(f"{section_name} start checking...")
        iframe.get_by_role("tab", name=section_name).click()
        page.wait_for_timeout(5000)
        expect(iframe.locator(panel_id)).to_have_attribute("aria-expanded", "true")
        
        panel = iframe.locator(panel_id)
        list_items = panel.locator("li")
        count = list_items.count()
        
        if count > 0:
            print(f"{section_name} contains {count} list item(s):")
            for i in range(count):
                text = list_items.nth(i).inner_text()
                print(f"- {text}")
