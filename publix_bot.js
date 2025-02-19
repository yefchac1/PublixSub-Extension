const puppeteer = require('puppeteer');
const timeout = require('setTimeout');

(async () => {
    const browser = await puppeteer.launch({headless: false, args: ['--use-fake-ui-for-media-stream', '--enable-features=WebContentForceDark']});
    const path = await browser.newPage();

    const context = browser.defaultBrowserContext();
    await context.overridePermissions('https://www.publix.com', ['geolocation']);

    await path.setGeolocation({latitude: 28.2699, longitude: -82.2857});

    console.log('Opening Publix Website'); 
    await path.goto('https://www.publix.com/mc/order-ahead/order-deli-online'), {waitUntil: 'networkidle2'};
    await path.setViewport({width: 1080, height: 1024});
    
    //console.log('Waiting for location to load');
    //await path.waitForSelector('//*[@id="sidebar-close-button"]/span'), {visible : true};
    //await path.click('//*[@id="sidebar-close-button"]/span');

    // console.log('Selecting Customize Order');
    // async function customizeOrder(selector, label) {
    //     await path.waitForSelector(selector, {visible: true});
    //     await path.evaluate((sel) => document.querySelector(sel).scrollIntoView(), selector);
    //     await path.click(selector);
    // }
    // await path.waitForSelector('#customize-button-55-90355 > span', {visible: true});
    //await path.evaluate((sel) => document.querySelector(sel).scrollIntoView({behavior: 'smooth', block: 'center'}), '#customize-button-55-90355 > span');
    // await path.evaluate(selector => {
    //     const element = document.querySelector(selector);
    //     if (element) {
    //         const rect = element.getBoundingClientRect();
    //         window.scrollBy({
    //             top: rect.top + window.scrollY - window.innerHeight / 2,
    //             behavior: 'smooth'
    //         });
    //     }
    // }, '#customize-button-55-90355 > span');
    
    // await path.click('#customize-button-55-90355 > span');

    const customizeOrder = '#customize-button-55-90355 > span';
    let i; 
    for (i = 0; i < 10; i++) {
        await path.waitForTimeout(2000);

        await path.evaluate((customizeOrder, i) => {
            const element = document.querySelectorAll(customizeOrder);
            if (element) {
                element.scrollIntoView({behavior: 'smooth', block: 'center'});
            }
        }, customizeOrder, i);
    }
    



    await browser.close();
    })();