def click_action_by_name(table_locator, target_name):
    rows = table_locator.locator("tr")

    for i in range(1, rows.count()):
        name = rows.nth(i).locator("td").nth(1).inner_text()

        if name == target_name:
            rows.nth(i).get_by_role("button", name="Edit").click()
            return True

    return False