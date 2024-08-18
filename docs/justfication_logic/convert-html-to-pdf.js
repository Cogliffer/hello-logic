const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
	
	// 获取当前脚本的目录路径
    const scriptDir = __dirname;
	
    const folderPath = 'temp';
	const files = fs.readdirSync(folderPath);

    for (const file of files) {
        if (path.extname(file) === '.html') {
            const filePath = path.join(scriptDir, folderPath, file);
            const pdfPath = path.join(folderPath, path.basename(file, '.html') + '.pdf');
            
			const fileUrl = new URL(`file://${filePath}`);
			console.log(`Navigating to: ${fileUrl}`);
			await page.goto(fileUrl.href);
			await page.pdf({
				path: pdfPath,
				format: 'A4',
				margin: {
					top: '15mm',
					bottom: '10mm',
					left: '5mm',
					right: '5mm'
				}
			});
        }
    }

    await browser.close();
})();
