// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.
#pragma once

class Application
{
public:
	Application(void);
	bool Create();
	virtual ~Application(void);

	bool OpenFont(std::string fileName, wchar_t errMsg[], size_t errMsgLen);
	bool OpenMemFont(void* font, uint32_t fontLen, wchar_t errMsg[], size_t errMsgLen); 
	
	bool SaveFont(std::string fileName, StripCommand strip, wchar_t errMsg[], size_t errMsgLen);
	bool SaveMemFont(void* font, uint32_t fontLen, StripCommand strip, wchar_t errMsg[], size_t errMsgLen);
	bool GetMemFont(void* font, uint32_t fontLen, wchar_t errMsg[], size_t errMsgLen);
	uint32_t GetFontSize();

	bool ImportSourceFromBinary(wchar_t errMsg[], size_t errMsgLen); 

	bool GotoFont(wchar_t errMsg[], size_t errMsgLen);
	bool GotoGlyph(int32_t code, bool isGlyphIndex);

	bool CompileTalk(int32_t* errPos, int32_t* errLen, wchar_t errMsg[], size_t errMsgLen);
	bool CompileCommon(bool legacy, bool variationCompositeGuard, int32_t* errPos, int32_t* errLen, wchar_t errMsg[], size_t errMsgLen);

	bool CompileGlyphRange(unsigned short g1, unsigned short g2, bool quiet, bool legacy, bool variationCompositeGuard, wchar_t errMsg[], size_t errMsgLen);
	bool CompileAll(bool quiet, bool legacy, bool variationCompositeGuard, wchar_t errMsg[], size_t errMsgLen);

	bool BuildFont(StripCommand strip, wchar_t errMsg[], size_t errMsgLen);

	char* wCharToChar(char out[], const wchar_t in[]); 

private:

	std::unique_ptr<TextBuffer> glyf = nullptr, prep = nullptr, talk = nullptr, fpgm = nullptr, cpgm = nullptr;
	short platformID = 3, encodingID = 1;

	wchar_t mainFont[maxLineSize], textFont[maxLineSize];

	std::unique_ptr<TrueTypeFont> font = nullptr;
	std::unique_ptr<TrueTypeGlyph> glyph = nullptr;
	std::string fileName;
	int32_t charCode = 0, glyphIndex = 0;
};

