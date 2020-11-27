const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: false
    });
    const context = await browser.newContext({
        viewport: {
            width: 1920,
            height: 1080
        },
        locale: 'en-US'
    });

    // Open new page
    const page = await context.newPage();

    // Go to https://www.amazon.com/
    await page.goto('https://www.amazon.com/');

    // Click input[aria-label="Search"]
    await page.click('input[aria-label="Search"]');

    // Fill input[aria-label="Search"]
    await page.fill('input[aria-label="Search"]', 'Kindle');

    // Press Enter
    await page.press('input[aria-label="Search"]', 'Enter');
    // assert.equal(page.url(), 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias=aps&field-keywords=Kindle');

    // Go to https://www.amazon.com/s?k=Kindle&ref=nb_sb_noss_2
    await page.goto('https://www.amazon.com/s?k=Kindle&ref=nb_sb_noss_2');

    // Click text=/.*All-new Kindle Oasis - Now wit.*/
    await page.click('text=/.*All-new Kindle Oasis - Now wit.*/');
    // assert.equal(page.url(), 'https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07L5GDTYY/ref=sr_1_3?dchild=1&keywords=Kindle&qid=1604100354&sr=8-3');

    // Click input[name="submit.add-to-cart"]
    await page.click('input[name="submit.add-to-cart"]');

    // Close page
    await page.close();

    // ---------------------
    await context.close();
    await browser.close();
})();