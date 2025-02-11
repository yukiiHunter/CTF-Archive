const purpose = "Purpose: deobfuscate odttf file (extracted from M$ XPS file)"
const usage = "Usage: node deobfuscate-odttf-in-xps.js <guid-obfuscated-font-file.odttf> [<output-file.ttf>]"

const obfuscatedStartOffset = 0 //start of obfuscated bytes in font file
const obfuscatedEndOffset = 32 //start of obfuscated bytes in font file
const guidSize = 32 // length of GUID string (only hex characters included)

const fs = require('fs')
const path = require('path')

//process.argv[0] is path to node.js
//process.argv[1] is path to this script
const fontFilepath = process.argv[2]
if (fontFilepath == null) {
	console.warn(purpose)
	console.warn(usage)
	return
}

const fontFilename = path.basename(fontFilepath)
const guid = fontFilename.replace(/-/g, "").replace(/\..+$/, "")
if (guid.length !== guidSize) {
	console.warn(guid, "Error: Cannot extract GUID from font filename (ex: A5C0272A-DD4C-401C-8661-BEAD77E57818.odttf)")
	return
}

// get hex numbers from GUID
const hexStrings = guid.replace(/(..)/g,"$1 ").trim().split(" ")
const hexNumbers = hexStrings.map((hexString) => parseInt(hexString, 16))
hexNumbers.reverse()

// deobfuscate by XORing obfuscated bytes with hexNumbers
const buf = fs.readFileSync(fontFilepath)
const obfuscatedBytes = buf.slice(obfuscatedStartOffset, obfuscatedEndOffset)
const recoveredBytes = obfuscatedBytes.map((byte, i) => byte ^ hexNumbers[i % hexNumbers.length] )

// write result to a ttf file
const out = Buffer.concat([
	buf.slice(0, obfuscatedStartOffset),
	recoveredBytes,
	buf.slice(obfuscatedEndOffset)
	])
const outputFilepath = process.argv[3] || fontFilepath + '.ttf'
fs.writeFile(
	outputFilepath,
	out,
	{ encoding: null },
	(error) => { if (error) throw error; }
	)
