const fs = require('fs');
const path = require('path');
const { PDFDocument } = require('pdf-lib');

const tempDir = path.join(__dirname, 'temp');
const outputPath = path.join(__dirname, 'merged.pdf');

async function mergePDFs() {
    const mergedPdf = await PDFDocument.create();

    // 读取 temp 目录中的所有 PDF 文件
    const files = fs.readdirSync(tempDir).filter(file => file.endsWith('.pdf'));

    // 添加每个 PDF 文件到合并器中
    for (const file of files) {
        const pdfPath = path.join(tempDir, file);
        const pdfBytes = fs.readFileSync(pdfPath);
        const pdf = await PDFDocument.load(pdfBytes);
        const pages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
        pages.forEach(page => mergedPdf.addPage(page));
    }

    // 保存合并后的 PDF 文件
    const pdfBytes = await mergedPdf.save();
    fs.writeFileSync(outputPath, pdfBytes);
    console.log('PDFs merged successfully!');
}

mergePDFs().catch(error => console.error('Error merging PDFs:', error));
