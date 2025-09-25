from playwright.sync_api import Page, expect

def test_template(page: Page):
    print("\n")
    page.get_by_role("link", name="Accordion").click()
    iframe = page.locator("iframe").content_frame
    
    sections = [
        ("Section 1", "#ui-id-2", "Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam."),
        ("Section 2", "#ui-id-4", "Sed non urna. Donec et ante. Phasellus eu ligula."),
        ("Section 3", "#ui-id-6", "Nam enim risus, molestie et, porta ac, aliquam ac, risus."),
        ("Section 4", "#ui-id-8", "Cras dictum. Pellentesque habitant morbi tristique senectus et"),
        ]
    
    for section_name, panel_id, expected_text in sections:
        print(f"{section_name} start checking...")

        # click tab and wait a bit for animation/panel open
        iframe.get_by_role("tab", name=section_name).click()
        # small wait or wait for panel attribute/visibility
        page.wait_for_timeout(800)

        panel = iframe.locator(panel_id)
        #expect(panel).to_have_attribute("aria-expanded", "true")

        # --- Preferred: get all <p> texts at once (safe) ---
        paragraphs = panel.locator("p")
        p_texts = paragraphs.all_inner_texts()  # returns list[str]
        if p_texts:
            for idx, t in enumerate(p_texts, start=1):
                print(f"Paragraph {idx} text:", t)
        else:
            print("No <p> found inside", panel_id)

        # Optional: assert the first <p> equals expected_text (if you expect one)
        if p_texts:
            # use expect if you want a Playwright-style assertion:
            expect(paragraphs.nth(0)).to_contain_text(expected_text)
            # or a plain python assertion:
            # assert p_texts[0].strip() == expected_text.strip()

        # --- Special handling for Section 3 list items (scoped to panel) ---
        if section_name == "Section 3":
            items = panel.locator("li")         # <-- IMPORTANT: scoped to panel
            li_texts = items.all_inner_texts()  # list[str]
            for li in li_texts:
                print("List item:", li)