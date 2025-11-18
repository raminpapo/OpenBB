# Documentation: openbb_platform/providers/nasdaq/tests/record/http/test_nasdaq_fetchers/test_nasdaq_equity_search_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/nasdaq/tests/record/http/test_nasdaq_fetchers/test_nasdaq_equity_search_fetcher_urllib3_v2.yaml`
- **Size**: 976,040 characters, 10,726 lines
- **Words**: 73,455
- **Extension**: .yaml
- **Classification**: Text file

## Original Source

```yaml
interactions:
- request:
    body: null
    headers:
      Accept:
      - '*/*'
      Accept-Encoding:
      - gzip, deflate
      Connection:
      - keep-alive
    method: GET
    uri: https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt
  response:
    body:
      string: "Nasdaq Traded|Symbol|Security Name|Listing Exchange|Market Category|ETF|Round
        Lot Size|Test Issue|Financial Status|CQS Symbol|NASDAQ Symbol|NextShares\r\nY|A|Agilent
        Technologies, Inc. Common Stock|N| |N|100|N||A|A|N\r\nY|AA|Alcoa Corporation
        Common Stock |N| |N|100|N||AA|AA|N\r\nY|AAA|Alternative Access First Priority
        CLO Bond ETF|P| |Y|100|N||AAA|AAA|N\r\nY|AAAU|Goldman Sachs Physical Gold
        ETF Shares|Z| |Y|100|N||AAAU|AAAU|N\r\nY|AACG|ATA Creativity Global - American
        Depositary Shares, each representing two common shares|Q|G|N|100|N|D||AACG|N\r\nY|AACI|Armada
        Acquisition Corp. I - Common Stock|Q|G|N|100|N|N||AACI|N\r\nY|AACIU|Armada
        Acquisition Corp. I - Unit|Q|G|N|100|N|N||AACIU|N\r\nY|AACIW|Armada Acquisition
        Corp. I - Warrant|Q|G|N|100|N|N||AACIW|N\r\nY|AACT|Ares Acquisition Corporation
        II Class A Ordinary Shares|N| |N|100|N||AACT|AACT|N\r\nY|AACT.U|Ares Acquisition
        Corporation II Units, each consisting of one Class A ordinary share and one-half
        of one redeemable warrant|N| |N|100|N||AACT.U|AACT=|N\r\nY|AACT.W|Ares Acquisition
        Corporation II Redeemable Warrants, each whole warrant exercisable for one
        Class A ordinary share at an exercise price of $11.50|N| |N|100|N||AACT.WS|AACT+|N\r\nY|AADI|Aadi
        Bioscience, Inc. - Common Stock|Q|S|N|100|N|N||AADI|N\r\nY|AADR|AdvisorShares
        Dorsey Wright ADR ETF|Q|G|Y|100|N|N||AADR|N\r\nY|AAGR|African Agriculture
        Holdings Inc. - Common Stock|Q|G|N|100|N|D||AAGR|N\r\nY|AAGRW|African Agriculture
        Holdings Inc. - Warrant|Q|G|N|100|N|D||AAGRW|N\r\nY|AAL|American Airlines
        Group, Inc. - Common Stock|Q|Q|N|100|N|N||AAL|N\r\nY|AAMC|Altisource Asset
        Management Corp Com|A| |N|100|N||AAMC|AAMC|N\r\nY|AAME|Atlantic American Corporation
        - Common Stock|Q|G|N|100|N|N||AAME|N\r\nY|AAN|Aarons Holdings Company, Inc.
        Common Stock |N| |N|100|N||AAN|AAN|N\r\nY|AAOI|Applied Optoelectronics, Inc.
        - Common Stock|Q|G|N|100|N|N||AAOI|N\r\nY|AAON|AAON, Inc. - Common Stock|Q|Q|N|100|N|N||AAON|N\r\nY|AAP|Advance
        Auto Parts Inc.|N| |N|100|N||AAP|AAP|N\r\nY|AAPB|GraniteShares 2x Long AAPL
        Daily ETF|Q|G|Y|100|N|N||AAPB|N\r\nY|AAPD|Direxion Daily AAPL Bear 1X Shares|Q|G|Y|100|N|N||AAPD|N\r\nY|AAPL|Apple
        Inc. - Common Stock|Q|Q|N|100|N|N||AAPL|N\r\nY|AAPR|SHL Telemedicine Ltd Innovator
        Equity Defined Protection ETF - 2 Yr to April 2026|Z| |Y|100|N||AAPR|AAPR|N\r\nY|AAPU|Direxion
        Daily AAPL Bull 2X Shares|Q|G|Y|100|N|N||AAPU|N\r\nY|AAPX|ETF Opportunities
        Trust T-Rex 2X Long Apple Daily Target ETF|Z| |Y|100|N||AAPX|AAPX|N\r\nY|AAPY|NEOS
        ETF Trust Kurv Yield Premium Strategy Apple (AAPL) ETF|Z| |Y|100|N||AAPY|AAPY|N\r\nY|AAT|American
        Assets Trust, Inc. Common Stock|N| |N|100|N||AAT|AAT|N\r\nY|AAXJ|iShares MSCI
        All Country Asia ex Japan ETF|Q|G|Y|100|N|N||AAXJ|N\r\nY|AB|AllianceBernstein
        Holding L.P.  Units|N| |N|100|N||AB|AB|N\r\nY|ABAT|American Battery Technology
        Company - Common Stock|Q|S|N|100|N|N||ABAT|N\r\nY|ABBV|AbbVie Inc. Common
        Stock|N| |N|100|N||ABBV|ABBV|N\r\nY|ABCB|Ameris Bancorp - Common Stock|Q|Q|N|100|N|N||ABCB|N\r\nY|ABCL|AbCellera
        Biologics Inc. - Common Shares|Q|Q|N|100|N|N||ABCL|N\r\nY|ABCS|Alpha Blue
        Capital US Small-Mid Cap Dynamic ETF|Q|G|Y|100|N|N||ABCS|N\r\nY|ABEO|Abeona
        Therapeutics Inc. - Common Stock|Q|S|N|100|N|N||ABEO|N\r\nY|ABEQ|Absolute
        Select Value ETF|P| |Y|100|N||ABEQ|ABEQ|N\r\nY|ABEV|Ambev S.A. American Depositary
        Shares (Each representing 1 Common Share)|N| |N|100|N||ABEV|ABEV|N\r\nY|ABG|Asbury
        Automotive Group Inc Common Stock|N| |N|100|N||ABG|ABG|N\r\nY|ABIO|ARCA biopharma,
        Inc. - Common Stock|Q|S|N|100|N|N||ABIO|N\r\nY|ABL|Abacus Life, Inc. - Class
        A Common Stock|Q|S|N|100|N|N||ABL|N\r\nY|ABLLL|Abacus Life, Inc. - 9.875%
        Fixed Rate Senior Notes due 2028|Q|G|N|100|N|N||ABLLL|N\r\nY|ABLLW|Abacus
        Life, Inc. - Warrant|Q|S|N|100|N|N||ABLLW|N\r\nY|ABLV|Able View Global Inc.
        - Class B Ordinary Shares|Q|S|N|100|N|N||ABLV|N\r\nY|ABLVW|Able View Global
        Inc. - Warrant|Q|S|N|100|N|N||ABLVW|N\r\nY|ABM|ABM Industries Incorporated
        Common Stock|N| |N|100|N||ABM|ABM|N\r\nY|ABNB|Airbnb, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||ABNB|N\r\nY|ABNY|Tidal Trust II YieldMax ABNB Option
        Income Strategy ETF|P| |Y|100|N||ABNY|ABNY|N\r\nY|ABOS|Acumen Pharmaceuticals,
        Inc. - Common Stock|Q|Q|N|100|N|N||ABOS|N\r\nY|ABR|Arbor Realty Trust Common
        Stock|N| |N|100|N||ABR|ABR|N\r\nY|ABR$D|Arbor Realty Trust 6.375% Series D
        Cumulative Redeemable Preferred Stock, Liquidation Preference $25.00 per Share|N|
        |N|100|N||ABRpD|ABR-D|N\r\nY|ABR$E|Arbor Realty Trust 6.25% Series E Cumulative
        Redeemable Preferred Stock|N| |N|100|N||ABRpE|ABR-E|N\r\nY|ABR$F|Arbor Realty
        Trust 6.25% Series F Fixed-to-Floating Rate Cumulative Redeemable Preferred
        Stock, Liquidation Preference $25.00 per share|N| |N|100|N||ABRpF|ABR-F|N\r\nY|ABSI|Absci
        Corporation - Common Stock|Q|Q|N|100|N|N||ABSI|N\r\nY|ABT|Abbott Laboratories
        Common Stock|N| |N|100|N||ABT|ABT|N\r\nY|ABTS|Abits Group Inc - Ordinary Shares|Q|S|N|100|N|D||ABTS|N\r\nY|ABUS|Arbutus
        Biopharma Corporation - Common Stock|Q|Q|N|100|N|N||ABUS|N\r\nY|ABVC|ABVC
        BioPharma, Inc. - Common Stock|Q|S|N|100|N|N||ABVC|N\r\nY|ABVX|Abivax SA -
        American Depositary Shares|Q|G|N|100|N|N||ABVX|N\r\nY|AC|Associated Capital
        Group, Inc. Common Stock|N| |N|100|N||AC|AC|N\r\nY|ACA|Arcosa, Inc. Common
        Stock |N| |N|100|N||ACA|ACA|N\r\nY|ACAB|Atlantic Coastal Acquisition Corp.
        II - Class A Common Stock|Q|G|N|100|N|H||ACAB|N\r\nY|ACABU|Atlantic Coastal
        Acquisition Corp. II - Unit|Q|G|N|100|N|E||ACABU|N\r\nY|ACABW|Atlantic Coastal
        Acquisition Corp. II - Warrant|Q|G|N|100|N|E||ACABW|N\r\nY|ACAC|Acri Capital
        Acquisition Corporation - Class A Common Stock|Q|S|N|100|N|N||ACAC|N\r\nY|ACACU|Acri
        Capital Acquisition Corporation - Unit|Q|S|N|100|N|N||ACACU|N\r\nY|ACACW|Acri
        Capital Acquisition Corporation - Warrant|Q|S|N|100|N|N||ACACW|N\r\nY|ACAD|ACADIA
        Pharmaceuticals Inc. - Common Stock|Q|Q|N|100|N|N||ACAD|N\r\nY|ACB|Aurora
        Cannabis Inc. - Common Shares|Q|S|N|100|N|N||ACB|N\r\nY|ACCD|Accolade, Inc.
        - common stock|Q|Q|N|100|N|N||ACCD|N\r\nY|ACCO|Acco Brands Corporation Common
        Stock|N| |N|100|N||ACCO|ACCO|N\r\nY|ACDC|ProFrac Holding Corp. - Class A Common
        Stock|Q|Q|N|100|N|N||ACDC|N\r\nY|ACEL|Accel Entertainment, Inc. |N| |N|100|N||ACEL|ACEL|N\r\nY|ACES|ALPS
        Clean Energy ETF|P| |Y|100|N||ACES|ACES|N\r\nY|ACET|Adicet Bio, Inc. - Common
        Stock|Q|G|N|100|N|N||ACET|N\r\nY|ACGL|Arch Capital Group Ltd. - Common Stock|Q|Q|N|100|N|N||ACGL|N\r\nY|ACGLN|Arch
        Capital Group Ltd. - Depositary Shares, each Representing a 1/1,000th Interest
        in a 4.550% Non-Cumulative Preferred Share, Series G|Q|Q|N|100|N|N||ACGLN|N\r\nY|ACGLO|Arch
        Capital Group Ltd. - Depositary Shares Each Representing 1/1,000th Interest
        in a Share of5.45% Non-Cumulative Preferred Shares, Series F|Q|Q|N|100|N|N||ACGLO|N\r\nY|ACHC|Acadia
        Healthcare Company, Inc. - Common Stock|Q|Q|N|100|N|N||ACHC|N\r\nY|ACHL|Achilles
        Therapeutics plc - American Depositary Shares|Q|Q|N|100|N|D||ACHL|N\r\nY|ACHR|Archer
        Aviation Inc. Class A Common Stock|N| |N|100|N||ACHR|ACHR|N\r\nY|ACHR.W|Archer
        Aviation Inc. Redeemable Warrants, each whole warrant exercisable for one
        Class A common stock at an exercise price of $11.50|N| |N|100|N||ACHR.WS|ACHR+|N\r\nY|ACHV|Achieve
        Life Sciences, Inc.  - Common Shares|Q|S|N|100|N|N||ACHV|N\r\nY|ACI|Albertsons
        Companies, Inc. Class A Common Stock|N| |N|100|N||ACI|ACI|N\r\nY|ACIC|American
        Coastal Insurance Corporation - Common Stock|Q|S|N|100|N|N||ACIC|N\r\nY|ACIO|Aptus
        Collared Investment Opportunity ETF|Z| |Y|100|N||ACIO|ACIO|N\r\nY|ACIU|AC
        Immune SA - Common Stock|Q|G|N|100|N|N||ACIU|N\r\nY|ACIW|ACI Worldwide, Inc.
        - Common Stock|Q|Q|N|100|N|N||ACIW|N\r\nY|ACLS|Axcelis Technologies, Inc.
        - Common Stock|Q|Q|N|100|N|N||ACLS|N\r\nY|ACLX|Arcellx, Inc. - Common Stock|Q|Q|N|100|N|N||ACLX|N\r\nY|ACM|AECOM
        Common Stock|N| |N|100|N||ACM|ACM|N\r\nY|ACMR|ACM Research, Inc. - Class A
        Common Stock|Q|G|N|100|N|N||ACMR|N\r\nY|ACN|Accenture plc Class A Ordinary
        Shares (Ireland)|N| |N|100|N||ACN|ACN|N\r\nY|ACNB|ACNB Corporation - Common
        Stock|Q|S|N|100|N|N||ACNB|N\r\nY|ACNT|Ascent Industries Co. - Common Stock|Q|G|N|100|N|N||ACNT|N\r\nY|ACON|Aclarion,
        Inc. - Common Stock|Q|S|N|100|N|D||ACON|N\r\nY|ACONW|Aclarion, Inc. - Warrant|Q|S|N|100|N|N||ACONW|N\r\nY|ACP|abrdn
        Income Credit Strategies Fund Common Shares|N| |N|100|N||ACP|ACP|N\r\nY|ACP$A|abrdn
        Income Credit Strategies Fund 5.250% Series A Perpetual Preferred Stock|N|
        |N|100|N||ACPpA|ACP-A|N\r\nY|ACR|ACRES Commercial Realty Corp. Common Stock|N|
        |N|100|N||ACR|ACR|N\r\nY|ACR$C|ACRES Commercial Realty Corp. 8.625% Fixed-to-Floating
        Series C Cumulative Redeemable Preferred Stock |N| |N|100|N||ACRpC|ACR-C|N\r\nY|ACR$D|ACRES
        Commercial Realty Corp. 7.875% Series D Cumulative Redeemable Preferred Stock|N|
        |N|100|N||ACRpD|ACR-D|N\r\nY|ACRE|Ares Commercial Real Estate Corporation
        Common Stock|N| |N|100|N||ACRE|ACRE|N\r\nY|ACRS|Aclaris Therapeutics, Inc.
        - Common Stock|Q|Q|N|100|N|N||ACRS|N\r\nY|ACRV|Acrivon Therapeutics, Inc.
        - Common Stock|Q|G|N|100|N|N||ACRV|N\r\nY|ACSI|American Customer Satisfaction
        ETF|Z| |Y|100|N||ACSI|ACSI|N\r\nY|ACST|Acasti Pharma, Inc.  - Class A Common
        Stock|Q|S|N|100|N|N||ACST|N\r\nY|ACT|Enact Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||ACT|N\r\nY|ACTG|Acacia
        Research Corporation - Common Stock|Q|Q|N|100|N|N||ACTG|N\r\nY|ACTV|LeaderShares
        Activist Leaders ETF|P| |Y|100|N||ACTV|ACTV|N\r\nY|ACU|Acme United Corporation.
        Common Stock|A| |N|100|N||ACU|ACU|N\r\nY|ACV|Virtus Diversified Income & Convertible
        Fund Common Shares of Beneficial Interest|N| |N|100|N||ACV|ACV|N\r\nY|ACVA|ACV
        Auctions Inc. - Class A Common Stock|Q|Q|N|100|N|N||ACVA|N\r\nY|ACVF|American
        Conservative Values ETF|P| |Y|100|N||ACVF|ACVF|N\r\nY|ACWI|iShares MSCI ACWI
        ETF|Q|G|Y|100|N|N||ACWI|N\r\nY|ACWV|iShares MSCI Global Min Vol Factor ETF|Z|
        |Y|100|N||ACWV|ACWV|N\r\nY|ACWX|iShares MSCI ACWI ex U.S. ETF|Q|G|Y|100|N|N||ACWX|N\r\nY|ACXP|Acurx
        Pharmaceuticals, Inc. - Common Stock|Q|S|N|100|N|N||ACXP|N\r\nY|ADAG|Adagene
        Inc. - ADS, each representing 1.25 ordinary shares|Q|G|N|100|N|N||ADAG|N\r\nY|ADAP|Adaptimmune
        Therapeutics plc - American Depositary Shares|Q|Q|N|100|N|N||ADAP|N\r\nY|ADBE|Adobe
        Inc. - Common Stock|Q|Q|N|100|N|N||ADBE|N\r\nY|ADC|Agree Realty Corporation
        Common Stock|N| |N|100|N||ADC|ADC|N\r\nY|ADC$A|Agree Realty Corporation Depositary
        Shares, each representing 1/1,000th of a 4.250% Series A Cumulative Redeemable
        Preferred Stock|N| |N|100|N||ADCpA|ADC-A|N\r\nY|ADCT|ADC Therapeutics SA Common
        Shares|N| |N|100|N||ADCT|ADCT|N\r\nY|ADD|Color Star Technology Co., Ltd. -
        Class A Ordinary Shares|Q|S|N|100|N|D||ADD|N\r\nY|ADEA|Adeia Inc.  - Common
        Stock|Q|Q|N|100|N|N||ADEA|N\r\nY|ADFI|Anfield Dynamic Fixed Income ETF|Z|
        |Y|100|N||ADFI|ADFI|N\r\nY|ADI|Analog Devices, Inc. - Common Stock|Q|Q|N|100|N|N||ADI|N\r\nY|ADIL|Adial
        Pharmaceuticals, Inc - Common Stock|Q|S|N|100|N|N||ADIL|N\r\nY|ADIV|SmartETFs
        Asia Pacific Dividend Builder ETF|P| |Y|100|N||ADIV|ADIV|N\r\nY|ADM|Archer-Daniels-Midland
        Company Common Stock|N| |N|100|N||ADM|ADM|N\r\nY|ADMA|ADMA Biologics Inc -
        Common Stock|Q|G|N|100|N|N||ADMA|N\r\nY|ADME|Aptus Drawdown Managed Equity
        ETF|Z| |Y|100|N||ADME|ADME|N\r\nY|ADN|Advent Technologies Holdings, Inc. -
        Class A Common Stock|Q|S|N|100|N|E||ADN|N\r\nY|ADNT|Adient plc Ordinary Shares
        |N| |N|100|N||ADNT|ADNT|N\r\nY|ADNWW|Advent Technologies Holdings, Inc. -
        Warrant|Q|S|N|100|N|E||ADNWW|N\r\nY|ADP|Automatic Data Processing, Inc. -
        Common Stock|Q|Q|N|100|N|N||ADP|N\r\nY|ADPT|Adaptive Biotechnologies Corporation
        - Common Stock|Q|Q|N|100|N|N||ADPT|N\r\nY|ADPV|Series Portfolios Trust Adaptiv
        Select ETF|P| |Y|100|N||ADPV|ADPV|N\r\nY|ADRT|Ault Disruptive Technologies
        Corporation Common Stock|A| |N|100|N||ADRT|ADRT|N\r\nY|ADRT.U|Ault Disruptive
        Technologies Corporation Units, each consisting of one share of Common Stock,
        and three-fourths of one Redeemable Warrant to purchase one share of Common
        Stock|A| |N|100|N||ADRT.U|ADRT=|N\r\nY|ADSE|ADS-TEC ENERGY PLC - Ordinary
        Shares|Q|S|N|100|N|N||ADSE|N\r\nY|ADSEW|ADS-TEC ENERGY PLC - Warrant|Q|S|N|100|N|N||ADSEW|N\r\nY|ADSK|Autodesk,
        Inc. - Common Stock|Q|Q|N|100|N|N||ADSK|N\r\nY|ADT|ADT Inc. Common Stock|N|
        |N|100|N||ADT|ADT|N\r\nY|ADTN|ADTRAN Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||ADTN|N\r\nY|ADTX|Aditxt,
        Inc. - Common Stock|Q|S|N|100|N|N||ADTX|N\r\nY|ADUS|Addus HomeCare Corporation
        - Common Stock|Q|Q|N|100|N|N||ADUS|N\r\nY|ADV|Advantage Solutions Inc.  -
        Class A Common Stock|Q|Q|N|100|N|N||ADV|N\r\nY|ADVE|Matthews International
        Funds Matthews Asia Dividend Active ETF|P| |Y|100|N||ADVE|ADVE|N\r\nY|ADVM|Adverum
        Biotechnologies, Inc. - Common Stock|Q|S|N|100|N|N||ADVM|N\r\nY|ADVWW|Advantage
        Solutions Inc.  - Warrant|Q|Q|N|100|N|N||ADVWW|N\r\nY|ADX|Adams Diversified
        Equity Fund Inc.|N| |N|100|N||ADX|ADX|N\r\nY|ADXN|Addex Therapeutics Ltd -
        American Depositary Shares|Q|S|N|100|N|N||ADXN|N\r\nY|AE|Adams Resources &
        Energy, Inc. Common Stock|A| |N|100|N||AE|AE|N\r\nY|AEAE|AltEnergy Acquisition
        Corp. - Class A Common Stock|Q|G|N|100|N|D||AEAE|N\r\nY|AEAEU|AltEnergy Acquisition
        Corp. - Unit|Q|G|N|100|N|N||AEAEU|N\r\nY|AEAEW|AltEnergy Acquisition Corp.
        - Warrant|Q|G|N|100|N|N||AEAEW|N\r\nY|AEE|Ameren Corporation Common Stock|N|
        |N|100|N||AEE|AEE|N\r\nY|AEF|abrdn Emerging Markets Equity Income Fund, Inc.
        Common Stock|A| |N|100|N||AEF|AEF|N\r\nY|AEFC|Aegon Funding Company LLC 5.10%
        Subordinated Notes due 2049|N| |N|100|N||AEFC|AEFC|N\r\nY|AEG|Aegon Ltd. New
        York Registry Shares|N| |N|100|N||AEG|AEG|N\r\nY|AEHL|Antelope Enterprise
        Holdings Limited - Class A Ordinary Shares|Q|S|N|100|N|N||AEHL|N\r\nY|AEHR|Aehr
        Test Systems - Common Stock|Q|S|N|100|N|N||AEHR|N\r\nY|AEI|Alset Inc. - Common
        Stock|Q|S|N|100|N|N||AEI|N\r\nY|AEIS|Advanced Energy Industries, Inc. - Common
        Stock|Q|Q|N|100|N|N||AEIS|N\r\nY|AEM|Agnico Eagle Mines Limited Common Stock|N|
        |N|100|N||AEM|AEM|N\r\nY|AEMB|American Century Emerging Markets Bond ETF|P|
        |Y|100|N||AEMB|AEMB|N\r\nY|AEMD|Aethlon Medical, Inc. - Common Stock|Q|S|N|100|N|N||AEMD|N\r\nY|AENT|Alliance
        Entertainment Holding Corporation - common stock|Q|S|N|100|N|N||AENT|N\r\nY|AENTW|Alliance
        Entertainment Holding Corporation - Warrants|Q|S|N|100|N|N||AENTW|N\r\nY|AEO|American
        Eagle Outfitters, Inc. Common Stock|N| |N|100|N||AEO|AEO|N\r\nY|AEON|AEON
        Biopharma, Inc. Class A Common Stock|A| |N|100|N||AEON|AEON|N\r\nY|AEP|American
        Electric Power Company, Inc. - Common Stock|Q|Q|N|100|N|N||AEP|N\r\nY|AER|AerCap
        Holdings N.V. Ordinary Shares|N| |N|100|N||AER|AER|N\r\nY|AERT|Aeries Technology,
        Inc. - Class A Ordinary Share|Q|S|N|100|N|N||AERT|N\r\nY|AERTW|Aeries Technology,
        Inc. - Warrant|Q|S|N|100|N|N||AERTW|N\r\nY|AES|The AES Corporation Common
        Stock|N| |N|100|N||AES|AES|N\r\nY|AESI|Atlas Energy Solutions Inc. Common
        Stock|N| |N|100|N||AESI|AESI|N\r\nY|AESR|Anfield U.S. Equity Sector Rotation
        ETF|Z| |Y|100|N||AESR|AESR|N\r\nY|AETH|Bitwise Funds Trust Bitwise Ethereum
        Strategy ETF|P| |Y|100|N||AETH|AETH|N\r\nY|AEVA|Aeva Technologies, Inc. Common
        Stock|N| |N|100|N||AEVA|AEVA|N\r\nY|AEVA.W|Aeva Technologies, Inc. Redeemable
        Warrants, each whole warrant exercisable for shares of common stock at an
        exercise price of $11.50 per share|N| |N|100|N||AEVA.WS|AEVA+|N\r\nY|AEYE|AudioEye,
        Inc. - Common Stock|Q|S|N|100|N|N||AEYE|N\r\nY|AEZS|Aeterna Zentaris Inc.
        - Common Stock|Q|S|N|100|N|N||AEZS|N\r\nY|AFAR|Aura FAT Projects Acquisition
        Corp - Class A Ordinary Shares|Q|G|N|100|N|D||AFAR|N\r\nY|AFARU|Aura FAT Projects
        Acquisition Corp - Unit|Q|G|N|100|N|D||AFARU|N\r\nY|AFARW|Aura FAT Projects
        Acquisition Corp - Warrant|Q|G|N|100|N|D||AFARW|N\r\nY|AFB|AllianceBernstein
        National Municipal Income Fund Inc|N| |N|100|N||AFB|AFB|N\r\nY|AFBI|Affinity
        Bancshares, Inc. - Common Stock|Q|S|N|100|N|N||AFBI|N\r\nY|AFCG|AFC Gamma,
        Inc. - Common Stock|Q|G|N|100|N|N||AFCG|N\r\nY|AFG|American Financial Group,
        Inc. Common Stock|N| |N|100|N||AFG|AFG|N\r\nY|AFGB|American Financial Group,
        Inc. 5.875% Subordinated Debentures due 2059|N| |N|100|N||AFGB|AFGB|N\r\nY|AFGC|American
        Financial Group, Inc. 5.125% Subordinated Debentures due 2059|N| |N|100|N||AFGC|AFGC|N\r\nY|AFGD|American
        Financial Group, Inc. 5.625% Subordinated Debentures due 2060|N| |N|100|N||AFGD|AFGD|N\r\nY|AFGE|American
        Financial Group, Inc. 4.500% Subordinated Debentures due 2060|N| |N|100|N||AFGE|AFGE|N\r\nY|AFIF|Anfield
        Universal Fixed Income ETF|Z| |Y|100|N||AFIF|AFIF|N\r\nY|AFJK|Aimei Health
        Technology Co., Ltd - Ordinary Share|Q|G|N|100|N|N||AFJK|N\r\nY|AFJKR|Aimei
        Health Technology Co., Ltd - Right|Q|G|N|100|N|N||AFJKR|N\r\nY|AFJKU|Aimei
        Health Technology Co., Ltd - Unit|Q|G|N|100|N|N||AFJKU|N\r\nY|AFK|VanEck Africa
        Index ETF|P| |Y|100|N||AFK|AFK|N\r\nY|AFL|AFLAC Incorporated Common Stock|N|
        |N|100|N||AFL|AFL|N\r\nY|AFLG|First Trust Active Factor Large Cap ETF|P| |Y|100|N||AFLG|AFLG|N\r\nY|AFMC|First
        Trust Active Factor Mid Cap ETF|P| |Y|100|N||AFMC|AFMC|N\r\nY|AFMD|Affimed
        N.V. - Common Stock|Q|G|N|100|N|N||AFMD|N\r\nY|AFRI|Forafric Global PLC -
        Ordinary Shares|Q|S|N|100|N|N||AFRI|N\r\nY|AFRIW|Forafric Global PLC - Warrants|Q|S|N|100|N|N||AFRIW|N\r\nY|AFRM|Affirm
        Holdings, Inc. - Class A Common Stock|Q|Q|N|100|N|N||AFRM|N\r\nY|AFSM|First
        Trust Active Factor Small Cap ETF|P| |Y|100|N||AFSM|AFSM|N\r\nY|AFT|Apollo
        Senior Floating Rate Fund Inc. Common Stock|N| |N|100|N||AFT|AFT|N\r\nY|AFTY|Pacer
        CSOP FTSE China A50 ETF|P| |Y|100|N||AFTY|AFTY|N\r\nY|AFYA|Afya Limited -
        Class A Common Shares|Q|Q|N|100|N|N||AFYA|N\r\nY|AG|First Majestic Silver
        Corp. Ordinary Shares (Canada)|N| |N|100|N||AG|AG|N\r\nY|AGAE|Allied Gaming
        & Entertainment Inc. - Common Stock|Q|S|N|100|N|D||AGAE|N\r\nY|AGBA|AGBA Group
        Holding Limited - Ordinary Share|Q|S|N|100|N|N||AGBA|N\r\nY|AGBAW|AGBA Group
        Holding Limited - Warrant|Q|S|N|100|N|N||AGBAW|N\r\nY|AGCO|AGCO Corporation
        Common Stock|N| |N|100|N||AGCO|AGCO|N\r\nY|AGD|abrdn Global Dynamic Dividend
        Fund Common Shares of Beneficial Interest|N| |N|100|N||AGD|AGD|N\r\nY|AGEN|Agenus
        Inc. - Common Stock|Q|S|N|100|N|N||AGEN|N\r\nY|AGFY|Agrify Corporation - Common
        Stock|Q|S|N|100|N|D||AGFY|N\r\nY|AGG|iShares Core U.S. Aggregate Bond ETF|P|
        |Y|100|N||AGG|AGG|N\r\nY|AGGH|Simplify Aggregate Bond ETF|P| |Y|100|N||AGGH|AGGH|N\r\nY|AGGS|Harbor
        ETF Trust Harbor Disciplined Bond ETF|P| |Y|100|N||AGGS|AGGS|N\r\nY|AGGY|WisdomTree
        Yield Enhanced U.S. Aggregate Bond Fund|P| |Y|100|N||AGGY|AGGY|N\r\nY|AGI|Alamos
        Gold Inc. Class A Common Shares|N| |N|100|N||AGI|AGI|N\r\nY|AGIH|iShares U.S.
        ETF Trust iShares Inflation Hedged U.S. Aggregate Bond ETF|P| |Y|100|N||AGIH|AGIH|N\r\nY|AGIO|Agios
        Pharmaceuticals, Inc. - Common Stock|Q|Q|N|100|N|N||AGIO|N\r\nY|AGL|agilon
        health, inc. Common Stock|N| |N|100|N||AGL|AGL|N\r\nY|AGM|Federal Agricultural
        Mortgage Corporation Common Stock|N| |N|100|N||AGM|AGM|N\r\nY|AGM$C|Federal
        Agricultural Mortgage Corporation Preferred Series C Fixed to Fltg|N| |N|100|N||AGMpC|AGM-C|N\r\nY|AGM$D|Federal
        Agricultural Mortgage Corporation 5.700% Non-Cumulative Preferred Stock, Series
        D|N| |N|100|N||AGMpD|AGM-D|N\r\nY|AGM$E|Federal Agricultural Mortgage Corporation
        5.750% Non-Cumulative Preferred Stock, Series E|N| |N|100|N||AGMpE|AGM-E|N\r\nY|AGM$F|Federal
        Agricultural Mortgage Corporation 5.250% Non-Cumulative Preferred Stock, Series
        F|N| |N|100|N||AGMpF|AGM-F|N\r\nY|AGM$G|Federal Agricultural Mortgage Corporation
        4.875% Non-Cumulative Preferred Stock, Series G|N| |N|100|N||AGMpG|AGM-G|N\r\nY|AGM.A|Federal
        Agricultural Mortgage Corporation Common Stock|N| |N|100|N||AGM.A|AGM.A|N\r\nY|AGMH|AGM
        Group Holdings Inc. - Class A Ordinary Shares|Q|S|N|100|N|N||AGMH|N\r\nY|AGMI|Themes
        Silver Miners ETF|Q|G|Y|100|N|N||AGMI|N\r\nY|AGNC|AGNC Investment Corp. -
        Common Stock|Q|Q|N|100|N|N||AGNC|N\r\nY|AGNCL|AGNC Investment Corp. - Depositary
        Shares Each Representing a 1/1,000th Interest in a Share of 7.75% Series G
        Fixed-Rate Reset Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||AGNCL|N\r\nY|AGNCM|AGNC
        Investment Corp. - Depositary Shares rep 6.875% Series D Fixed-to-Floating
        Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||AGNCM|N\r\nY|AGNCN|AGNC
        Investment Corp. - Depositary Shares Each Representing a 1/1,000th Interest
        in a Share of 7.00% Series C Fixed-To-Floating Rate Cumulative Redeemable
        Preferred Stock|Q|Q|N|100|N|N||AGNCN|N\r\nY|AGNCO|AGNC Investment Corp. -
        Depositary Shares, each representing a 1/1,000th interest in a share of Series
        E Fixed-to-Floating Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||AGNCO|N\r\nY|AGNCP|AGNC
        Investment Corp. - Depositary Shares Each Representing a 1/1,000th Interest
        in a Share of 6.125% Series F Fixed-to-Floating Rate Cumulative Redeemable
        Preferred Stock|Q|Q|N|100|N|N||AGNCP|N\r\nY|AGNG|Global X Aging Population
        ETF|Q|G|Y|100|N|N||AGNG|N\r\nY|AGO|Assured Guaranty Ltd. Common Stock|N| |N|100|N||AGO|AGO|N\r\nY|AGOX|Adaptive
        Alpha Opportunities ETF|P| |Y|100|N||AGOX|AGOX|N\r\nY|AGQ|ProShares Ultra
        Silver|P| |Y|100|N||AGQ|AGQ|N\r\nY|AGQI|First Trust Exchange-Traded Fund VIII
        First Trust Active Global Quality Income ETF|P| |Y|100|N||AGQI|AGQI|N\r\nY|AGR|Avangrid,
        Inc. Common Stock|N| |N|100|N||AGR|AGR|N\r\nY|AGRH|iShares U.S. ETF Trust
        iShares Interest Rate Hedged U.S. Aggregate Bond ETF|P| |Y|100|N||AGRH|AGRH|N\r\nY|AGRI|AgriFORCE
        \ Growing Systems Ltd. - Common Shares|Q|S|N|100|N|D||AGRI|N\r\nY|AGRIW|AgriFORCE
        \ Growing Systems Ltd. - Warrant|Q|S|N|100|N|N||AGRIW|N\r\nY|AGRO|Adecoagro
        S.A. Common Shares|N| |N|100|N||AGRO|AGRO|N\r\nY|AGS|PlayAGS, Inc. Common
        Stock|N| |N|100|N||AGS|AGS|N\r\nY|AGX|Argan, Inc. Common Stock|N| |N|100|N||AGX|AGX|N\r\nY|AGYS|Agilysys,
        Inc. - Common Stock|Q|Q|N|100|N|N||AGYS|N\r\nY|AGZ|iShares  Agency Bond ETF|P|
        |Y|100|N||AGZ|AGZ|N\r\nY|AGZD|WisdomTree Interest Rate Hedged U.S. Aggregate
        Bond Fund|Q|G|Y|100|N|N||AGZD|N\r\nY|AHCO|AdaptHealth Corp.  - Common Stock|Q|S|N|100|N|N||AHCO|N\r\nY|AHG|Akso
        Health Group - American Depositary Shares|Q|S|N|100|N|N||AHG|N\r\nY|AHH|Armada
        Hoffler Properties, Inc. Common Stock|N| |N|100|N||AHH|AHH|N\r\nY|AHH$A|Armada
        Hoffler Properties, Inc. 6.75% Series A Cumulative Redeemable Perpetual Preferred
        Stock|N| |N|100|N||AHHpA|AHH-A|N\r\nY|AHI|Advanced Health Intelligence Ltd.
        - American Depositary Shares|Q|S|N|100|N|D||AHI|N\r\nY|AHL$C|Aspen Insurance
        Holdings Limited 5.95% Fixed-to-Floating Rate Perpetual Non-Cumulative Preference
        Shares|N| |N|100|N||AHLpC|AHL-C|N\r\nY|AHL$D|Aspen Insurance Holdings Limited
        5.625% Perpetual Non-Cumulative Preference Shares|N| |N|100|N||AHLpD|AHL-D|N\r\nY|AHL$E|Aspen
        Insurance Holdings Limited Depositary Shares, each representing a 1/1000th
        interest in a share of 5.625% Perpetual Non-Cumulative Preference Shares|N|
        |N|100|N||AHLpE|AHL-E|N\r\nY|AHLT|American Beacon Select Funds American Beacon
        AHL Trend ETF|P| |Y|100|N||AHLT|AHLT|N\r\nY|AHOY|Tidal ETF Trust Newday Ocean
        Health ETF|P| |Y|100|N||AHOY|AHOY|N\r\nY|AHR|American Healthcare REIT, Inc.
        Common Stock|N| |N|100|N||AHR|AHR|N\r\nY|AHT|Ashford Hospitality Trust Inc
        Common Stock|N| |N|100|N||AHT|AHT|N\r\nY|AHT$D|Ashford Hospitality Trust Inc
        8.45% Series D Cumulative Preferred Stock|N| |N|100|N||AHTpD|AHT-D|N\r\nY|AHT$F|Ashford
        Hospitality Trust Inc 7.375% Series F Cumulative Preferred Stock|N| |N|100|N||AHTpF|AHT-F|N\r\nY|AHT$G|Ashford
        Hospitality Trust Inc 7.375% Series G Cumulative Preferred Stock|N| |N|100|N||AHTpG|AHT-G|N\r\nY|AHT$H|Ashford
        Hospitality Trust Inc 7.50% Series H Cumulative Preferred Stock|N| |N|100|N||AHTpH|AHT-H|N\r\nY|AHT$I|Ashford
        Hospitality Trust Inc 7.50% Series I Cumulative Preferred Stock|N| |N|100|N||AHTpI|AHT-I|N\r\nY|AHYB|American
        Century Select High Yield ETF|P| |Y|100|N||AHYB|AHYB|N\r\nY|AI|C3.ai, Inc.
        Class A Common Stock|N| |N|100|N||AI|AI|N\r\nY|AIA|iShares Asia 50 ETF|Q|G|Y|100|N|N||AIA|N\r\nY|AIBD|Direxion
        Shares ETF Trust Direxion Daily AI and Big Data Bear 2X Shares|P| |Y|100|N||AIBD|AIBD|N\r\nY|AIBU|Direxion
        Shares ETF Trust Direxion Daily AI and Big Data Bull 2X Shares|P| |Y|100|N||AIBU|AIBU|N\r\nY|AIEQ|Amplify
        ETF Trust Amplify AI Powered Equity ETF|P| |Y|100|N||AIEQ|AIEQ|N\r\nY|AIEV|Thunder
        Power Holdings, Inc. - Common Stock|Q|G|N|100|N|D||AIEV|N\r\nY|AIF|Apollo
        Tactical Income Fund Inc. Common Stock|N| |N|100|N||AIF|AIF|N\r\nY|AIFD|Engine
        No. 1 ETF Trust TCW Artificial Intelligence ETF|N| |Y|100|N||AIFD|AIFD|N\r\nY|AIG|American
        International Group, Inc. New Common Stock|N| |N|100|N||AIG|AIG|N\r\nY|AIHS|Senmiao
        Technology Limited - Common Stock|Q|S|N|100|N|N||AIHS|N\r\nY|AILE|iLearningEngines,
        Inc. - Common Stock|Q|S|N|100|N|N||AILE|N\r\nY|AILEW|iLearningEngines, Inc.
        - Warrant|Q|S|N|100|N|N||AILEW|N\r\nY|AIM|AIM ImmunoTech Inc. Common Stock|A|
        |N|100|N||AIM|AIM|N\r\nY|AIMAU|Aimfinity Investment Corp. I - Unit|Q|G|N|100|N|N||AIMAU|N\r\nY|AIMAW|Aimfinity
        Investment Corp. I - Warrant|Q|G|N|100|N|N||AIMAW|N\r\nY|AIMBU|Aimfinity Investment
        Corp. I - Subunit|Q|G|N|100|N|N||AIMBU|N\r\nY|AIMD|Ainos, Inc. - Common Stock|Q|S|N|100|N|N||AIMD|N\r\nY|AIMDW|Ainos,
        Inc. - warrants|Q|S|N|100|N|N||AIMDW|N\r\nY|AIN|Albany International Corporation
        Common Stock|N| |N|100|N||AIN|AIN|N\r\nY|AINC|Ashford Inc. (Holding Company)
        Common Stock|A| |N|100|N||AINC|AINC|N\r\nY|AIO|Virtus Artificial Intelligence
        & Technology Opportunities Fund Common Shares of Beneficial Interest|N| |N|100|N||AIO|AIO|N\r\nY|AIP|Arteris,
        Inc.  - Common Stock|Q|G|N|100|N|N||AIP|N\r\nY|AIPI|REX AI Equity Premium
        Income ETF|Q|G|Y|100|N|N||AIPI|N\r\nY|AIQ|Global X Artificial Intelligence
        & Technology ETF|Q|G|Y|100|N|N||AIQ|N\r\nY|AIR|AAR Corp. Common Stock|N| |N|100|N||AIR|AIR|N\r\nY|AIRC|Apartment
        Income REIT Corp. Common Stock|N| |N|100|N||AIRC|AIRC|N\r\nY|AIRE|reAlpha
        Tech Corp. - Common Stock|Q|S|N|100|N|N||AIRE|N\r\nY|AIRG|Airgain, Inc. -
        Common Stock|Q|S|N|100|N|N||AIRG|N\r\nY|AIRI|Air Industries Group Common Stock|A|
        |N|100|N||AIRI|AIRI|N\r\nY|AIRJ|Montana Technologies Corp - Class A Common
        Stock|Q|S|N|100|N|N||AIRJ|N\r\nY|AIRJW|Montana Technologies Corp - Warrant|Q|S|N|100|N|N||AIRJW|N\r\nY|AIRL|Themes
        Airlines ETF|Q|G|Y|100|N|N||AIRL|N\r\nY|AIRR|First Trust RBA American Industrial
        Renaissance ETF|Q|G|Y|100|N|N||AIRR|N\r\nY|AIRS|AirSculpt Technologies, Inc.
        - Common Stock|Q|G|N|100|N|N||AIRS|N\r\nY|AIRT|Air T, Inc. - Common Stock|Q|S|N|100|N|N||AIRT|N\r\nY|AIRTP|Air
        T, Inc. - Trust Preferred Securities|Q|G|N|100|N|N||AIRTP|N\r\nY|AISP|Airship
        AI Holdings, Inc - Class A Common Stock|Q|G|N|100|N|N||AISP|N\r\nY|AISPW|Airship
        AI Holdings, Inc - Warrants|Q|S|N|100|N|N||AISPW|N\r\nY|AIT|Applied Industrial
        Technologies, Inc. Common Stock|N| |N|100|N||AIT|AIT|N\r\nY|AITR|AI TRANSPORTATION
        ACQUISITION CORP - Ordinary shares|Q|S|N|100|N|N||AITR|N\r\nY|AITRR|AI TRANSPORTATION
        ACQUISITION CORP - Right|Q|S|N|100|N|N||AITRR|N\r\nY|AITRU|AI TRANSPORTATION
        ACQUISITION CORP - Unit|Q|S|N|100|N|N||AITRU|N\r\nY|AIU|Meta Data Limited
        ADS|N| |N|100|N||AIU|AIU|N\r\nY|AIV|Apartment Investment and Management Company
        Common Stock|N| |N|100|N||AIV|AIV|N\r\nY|AIVI|WisdomTree International AI
        Enhanced Value Fund|P| |Y|100|N||AIVI|AIVI|N\r\nY|AIVL|WisdomTree U.S. AI
        Enhanced Value Fund|P| |Y|100|N||AIVL|AIVL|N\r\nY|AIXI|XIAO-I Corporation
        - American Depositary Shares|Q|G|N|100|N|N||AIXI|N\r\nY|AIYY|Tidal Trust II
        YieldMax AI Option Income Strategy ETF|P| |Y|100|N||AIYY|AIYY|N\r\nY|AIZ|Assurant,
        Inc. Common Stock|N| |N|100|N||AIZ|AIZ|N\r\nY|AIZN|Assurant, Inc. 5.25% Subordinated
        Notes due 2061|N| |N|100|N||AIZN|AIZN|N\r\nY|AJAN|Innovator ETFs Trust Innovator
        Equity Defined Protection ETF - 2 Yr to January 2026|Z| |Y|100|N||AJAN|AJAN|N\r\nY|AJG|Arthur
        J. Gallagher & Co. Common Stock|N| |N|100|N||AJG|AJG|N\r\nY|AJX|Great Ajax
        Corp. Common Stock|N| |N|100|N||AJX|AJX|N\r\nY|AKA|a.k.a. Brands Holding Corp.
        Common Stock|N| |N|100|N||AKA|AKA|N\r\nY|AKAM|Akamai Technologies, Inc. -
        Common Stock|Q|Q|N|100|N|N||AKAM|N\r\nY|AKAN|Akanda Corp. - Common Shares|Q|S|N|100|N|D||AKAN|N\r\nY|AKBA|Akebia
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||AKBA|N\r\nY|AKLI|Akili, Inc.
        - Common Stock|Q|S|N|100|N|D||AKLI|N\r\nY|AKO.A|Embotelladora Andina S.A.
        Common Stock|N| |N|100|N||AKO.A|AKO.A|N\r\nY|AKO.B|Embotelladora Andina S.A.
        Common Stock|N| |N|100|N||AKO.B|AKO.B|N\r\nY|AKR|Acadia Realty Trust Common
        Stock|N| |N|100|N||AKR|AKR|N\r\nY|AKRO|Akero Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||AKRO|N\r\nY|AKTS|Akoustis
        Technologies, Inc. - Common Stock|Q|S|N|100|N|D||AKTS|N\r\nY|AKTX|Akari Therapeutics
        Plc - American Depositary Shares|Q|S|N|100|N|D||AKTX|N\r\nY|AKYA|Akoya BioSciences,
        Inc. - Common Stock|Q|Q|N|100|N|N||AKYA|N\r\nY|AL|Air Lease Corporation Class
        A Common Stock|N| |N|100|N||AL|AL|N\r\nY|AL$A|Air Lease Corporation 6.150%
        Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock, Series A|N|
        |N|100|N||ALpA|AL-A|N\r\nY|ALAB|Astera Labs, Inc. - Common Stock|Q|Q|N|100|N|N||ALAB|N\r\nY|ALAI|The
        Alger ETF Trust Alger AI Enablers & Adopters ETF|P| |Y|100|N||ALAI|ALAI|N\r\nY|ALAR|Alarum
        Technologies Ltd. - American Depositary Shares|Q|S|N|100|N|N||ALAR|N\r\nY|ALB|Albemarle
        Corporation Common Stock|N| |N|100|N||ALB|ALB|N\r\nY|ALB$A|Albemarle Corporation
        Depositary Shares each representing a 1/20th of 7.25% Series A Mandatory Convertible
        Preferred Stock|N| |N|100|N||ALBpA|ALB-A|N\r\nY|ALBT|Avalon GloboCare Corp.
        - Common Stock|Q|S|N|100|N|D||ALBT|N\r\nY|ALC|Alcon Inc. Ordinary Shares|N|
        |N|100|N||ALC|ALC|N\r\nY|ALCE|Alternus Clean Energy, Inc. - Class A Common
        Stock|Q|S|N|100|N|D||ALCE|N\r\nY|ALCO|Alico, Inc. - Common Stock|Q|Q|N|100|N|N||ALCO|N\r\nY|ALCY|Alchemy
        Investments Acquisition Corp 1 - Class A Ordinary Shares|Q|G|N|100|N|N||ALCY|N\r\nY|ALCYU|Alchemy
        Investments Acquisition Corp 1 - Units|Q|G|N|100|N|N||ALCYU|N\r\nY|ALCYW|Alchemy
        Investments Acquisition Corp 1 - Warrants|Q|G|N|100|N|N||ALCYW|N\r\nY|ALDX|Aldeyra
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||ALDX|N\r\nY|ALE|Allete, Inc.|N|
        |N|100|N||ALE|ALE|N\r\nY|ALEC|Alector, Inc. - Common Stock|Q|Q|N|100|N|N||ALEC|N\r\nY|ALEX|Alexander
        & Baldwin, Inc. Common Stock REIT Holding Company|N| |N|100|N||ALEX|ALEX|N\r\nY|ALFUU|Centurion
        Acquisition Corp. - Unit|Q|G|N|100|N|N||ALFUU|N\r\nY|ALG|Alamo Group, Inc.
        Common Stock|N| |N|100|N||ALG|ALG|N\r\nY|ALGM|Allegro MicroSystems, Inc. -
        Common Stock|Q|Q|N|100|N|N||ALGM|N\r\nY|ALGN|Align Technology, Inc. - Common
        Stock|Q|Q|N|100|N|N||ALGN|N\r\nY|ALGS|Aligos Therapeutics, Inc. - Common stock|Q|S|N|100|N|D||ALGS|N\r\nY|ALGT|Allegiant
        Travel Company - Common Stock|Q|Q|N|100|N|N||ALGT|N\r\nY|ALHC|Alignment Healthcare,
        Inc. - Common Stock|Q|Q|N|100|N|N||ALHC|N\r\nY|ALIM|Alimera Sciences, Inc.
        - Common Stock|Q|G|N|100|N|N||ALIM|N\r\nY|ALIT|Alight, Inc. Class A Common
        Stock|N| |N|100|N||ALIT|ALIT|N\r\nY|ALK|Alaska Air Group, Inc. Common Stock|N|
        |N|100|N||ALK|ALK|N\r\nY|ALKS|Alkermes plc - Ordinary Shares|Q|Q|N|100|N|N||ALKS|N\r\nY|ALKT|Alkami
        Technology, Inc. - Common Stock|Q|Q|N|100|N|N||ALKT|N\r\nY|ALL|Allstate Corporation
        (The) Common Stock|N| |N|100|N||ALL|ALL|N\r\nY|ALL$B|Allstate Corporation
        (The) 5.100% Fixed-to-Floating Rate Subordinated Debentures due 2053|N| |N|100|N||ALLpB|ALL-B|N\r\nY|ALL$H|Allstate
        Corporation (The) Depositary Shares each representing a 1/1,000th interest
        in a share of Fixed Rate Noncumulative Perpetual Preferred Stock, Series H|N|
        |N|100|N||ALLpH|ALL-H|N\r\nY|ALL$I|Allstate Corporation (The) Depositary Shares
        each representing a 1/1,000th interest in a share of Fixed Rate Noncumulative
        Perpetual Preferred Stock, Series I|N| |N|100|N||ALLpI|ALL-I|N\r\nY|ALL$J|Allstate
        Corporation (The) Depositary Shares each representing a 1/1,000th interest
        in a share of Fixed Rate Noncumulative Perpetual Preferred Stock, Series J|N|
        |N|100|N||ALLpJ|ALL-J|N\r\nY|ALLE|Allegion plc Ordinary Shares|N| |N|100|N||ALLE|ALLE|N\r\nY|ALLG|Allego
        N.V. Ordinary Share|N| |N|100|N||ALLG|ALLG|N\r\nY|ALLK|Allakos Inc. - Common
        Stock|Q|Q|N|100|N|N||ALLK|N\r\nY|ALLO|Allogene Therapeutics, Inc. - Common
        Stock|Q|Q|N|100|N|N||ALLO|N\r\nY|ALLR|Allarity Therapeutics, Inc. - Common
        stock|Q|S|N|100|N|D||ALLR|N\r\nY|ALLT|Allot Ltd. - Ordinary Shares|Q|Q|N|100|N|N||ALLT|N\r\nY|ALLY|Ally
        Financial Inc. Common Stock|N| |N|100|N||ALLY|ALLY|N\r\nY|ALNT|Allient Inc.
        - Common Stock|Q|G|N|100|N|N||ALNT|N\r\nY|ALNY|Alnylam Pharmaceuticals, Inc.
        - Common Stock|Q|Q|N|100|N|N||ALNY|N\r\nY|ALOT|AstroNova, Inc. - Common Stock|Q|G|N|100|N|N||ALOT|N\r\nY|ALPP|Alpine
        4 Holdings, Inc. - Class A Common Stock|Q|S|N|100|N|H||ALPP|N\r\nY|ALRM|Alarm.com
        Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||ALRM|N\r\nY|ALRN|Aileron Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||ALRN|N\r\nY|ALRS|Alerus Financial Corporation
        - Common Stock|Q|S|N|100|N|N||ALRS|N\r\nY|ALSA|Alpha Star Acquisition Corporation
        - Ordinary Shares|Q|G|N|100|N|E||ALSA|N\r\nY|ALSAR|Alpha Star Acquisition
        Corporation - Rights|Q|G|N|100|N|E||ALSAR|N\r\nY|ALSAU|Alpha Star Acquisition
        Corporation - Units|Q|G|N|100|N|E||ALSAU|N\r\nY|ALSAW|Alpha Star Acquisition
        Corporation - Warrants|Q|G|N|100|N|E||ALSAW|N\r\nY|ALSN|Allison Transmission
        Holdings, Inc. Common Stock|N| |N|100|N||ALSN|ALSN|N\r\nY|ALT|Altimmune, Inc.
        - Common Stock|Q|G|N|100|N|N||ALT|N\r\nY|ALTG|Alta Equipment Group Inc. Class
        A Common Stock|N| |N|100|N||ALTG|ALTG|N\r\nY|ALTG$A|Alta Equipment Group Inc.
        Depositary Shares (each representing 1/1000th in a share of 10% Series A Cumulative
        Perpetual Preferred Stock)|N| |N|100|N||ALTGpA|ALTG-A|N\r\nY|ALTI|AlTi Global,
        Inc. - Class A Common Stock|Q|S|N|100|N|N||ALTI|N\r\nY|ALTL|Pacer Lunt Large
        Cap Alternator ETF|P| |Y|100|N||ALTL|ALTL|N\r\nY|ALTM|Arcadium Lithium plc
        Ordinary Shares|N| |N|100|N||ALTM|ALTM|N\r\nY|ALTO|Alto Ingredients, Inc.
        - Common Stock|Q|S|N|100|N|N||ALTO|N\r\nY|ALTR|Altair Engineering Inc. - Class
        A Common Stock|Q|Q|N|100|N|N||ALTR|N\r\nY|ALTY|Global X Alternative Income
        ETF|Q|G|Y|100|N|N||ALTY|N\r\nY|ALUM|USCF ETF Trust USCF Aluminum Strategy
        Fund|P| |Y|100|N||ALUM|ALUM|N\r\nY|ALUR|Allurion Technologies, Inc. Common
        Stock|N| |N|100|N||ALUR|ALUR|N\r\nY|ALUR.W|Allurion Technologies, Inc. Warrants,
        each whole warrant exercisable to purchase 1.420455 shares of common stock
        at an exercise price of $8.10 per share of common stock|N| |N|100|N||ALUR.WS|ALUR+|N\r\nY|ALV|Autoliv,
        Inc. Common Stock|N| |N|100|N||ALV|ALV|N\r\nY|ALVO|Alvotech - Ordinary Shares|Q|G|N|100|N|N||ALVO|N\r\nY|ALVOW|Alvotech
        - Warrant|Q|G|N|100|N|N||ALVOW|N\r\nY|ALVR|AlloVir, Inc. - Common Stock|Q|Q|N|100|N|D||ALVR|N\r\nY|ALX|Alexander's,
        Inc. Common Stock|N| |N|100|N||ALX|ALX|N\r\nY|ALXO|ALX Oncology Holdings Inc.
        - Common Stock|Q|Q|N|100|N|N||ALXO|N\r\nY|ALZN|Alzamend Neuro, Inc. - Common
        Stock|Q|S|N|100|N|D||ALZN|N\r\nY|AM|Antero Midstream Corporation Common Stock|N|
        |N|100|N||AM|AM|N\r\nY|AMAL|Amalgamated Financial Corp. - Common Stock|Q|G|N|100|N|N||AMAL|N\r\nY|AMAT|Applied
        Materials, Inc. - Common Stock|Q|Q|N|100|N|N||AMAT|N\r\nY|AMAX|Adaptive Hedged
        Multi-Asset Income ETF|P| |Y|100|N||AMAX|AMAX|N\r\nY|AMBA|Ambarella, Inc.
        - Ordinary Shares|Q|Q|N|100|N|N||AMBA|N\r\nY|AMBC|Ambac Financial Group, Inc.
        Common Stock|N| |N|100|N||AMBC|AMBC|N\r\nY|AMBI|Ambipar Emergency Response
        Class A Ordinary Shares|A| |N|100|N||AMBI|AMBI|N\r\nY|AMBI.W|Ambipar Emergency
        Response Warrants to purchase Class A ordinary shares, each whole warrant
        exercisable for one Class A ordinary share at an exercise price of $11.50
        per share|A| |N|100|N||AMBI.WS|AMBI+|N\r\nY|AMBO|Ambow Education Holding Ltd.
        American Depository Shares (each representing twenty (20) Class A Ordinary
        Shares)|A| |N|100|N||AMBO|AMBO|N\r\nY|AMBP|Ardagh Metal Packaging S.A. Ordinary
        Shares|N| |N|100|N||AMBP|AMBP|N\r\nY|AMBP.W|Ardagh Metal Packaging S.A. Warrants,
        each exercisable for one Share at an exercise price of $11.50 per share|N|
        |N|100|N||AMBP.WS|AMBP+|N\r\nY|AMC|AMC Entertainment Holdings, Inc. Class
        A Common Stock|N| |N|100|N||AMC|AMC|N\r\nY|AMCR|Amcor plc Ordinary Shares|N|
        |N|100|N||AMCR|AMCR|N\r\nY|AMCX|AMC Networks Inc. - Class A Common Stock|Q|Q|N|100|N|N||AMCX|N\r\nY|AMD|Advanced
        Micro Devices, Inc. - Common Stock|Q|Q|N|100|N|N||AMD|N\r\nY|AMDL|GraniteShares
        2x Long AMD Daily ETF|Q|G|Y|100|N|N||AMDL|N\r\nY|AMDS|GraniteShares 1x Short
        AMD Daily ETF|Q|G|Y|100|N|N||AMDS|N\r\nY|AMDY|Tidal Trust II Yieldmax AMD
        Option Income Strategy ETF|P| |Y|100|N||AMDY|AMDY|N\r\nY|AME|AMETEK, Inc.|N|
        |N|100|N||AME|AME|N\r\nY|AMED|Amedisys Inc - Common Stock|Q|Q|N|100|N|N||AMED|N\r\nY|AMG|Affiliated
        Managers Group, Inc. Common Stock|N| |N|100|N||AMG|AMG|N\r\nY|AMGN|Amgen Inc.
        - Common Stock|Q|Q|N|100|N|N||AMGN|N\r\nY|AMH|American Homes 4 Rent Common
        Shares of Beneficial Interest|N| |N|100|N||AMH|AMH|N\r\nY|AMH$G|American Homes
        4 Rent Series G cumulative redeemable perpetual preferred shares of beneficial
        interest|N| |N|100|N||AMHpG|AMH-G|N\r\nY|AMH$H|American Homes 4 Rent Series
        H cumulative redeemable perpetual Preferred Shares of Beneficial Interest|N|
        |N|100|N||AMHpH|AMH-H|N\r\nY|AMID|Argent Mid Cap ETF|Q|G|Y|100|N|N||AMID|N\r\nY|AMIX|Autonomix
        Medical, Inc. - Common Stock|Q|S|N|100|N|N||AMIX|N\r\nY|AMJB|JPMorgan Chase
        & Co. Alerian MLP Index ETNs due January 28, 2044|P| |Y|100|N||AMJB|AMJB|N\r\nY|AMK|AssetMark
        Financial Holdings, Inc. Common Stock|N| |N|100|N||AMK|AMK|N\r\nY|AMKR|Amkor
        Technology, Inc. - Common Stock|Q|Q|N|100|N|N||AMKR|N\r\nY|AMLI|American Lithium
        Corp. - Common Stock|Q|S|N|100|N|D||AMLI|N\r\nY|AMLP|Alerian MLP ETF|P| |Y|100|N||AMLP|AMLP|N\r\nY|AMLX|Amylyx
        Pharmaceuticals, Inc. - Common Stock|Q|Q|N|100|N|N||AMLX|N\r\nY|AMN|AMN Healthcare
        Services Inc|N| |N|100|N||AMN|AMN|N\r\nY|AMNA|ETRACS Alerian Midstream Energy
        Index ETN|P| |Y|100|N||AMNA|AMNA|N\r\nY|AMND|UBS AG ETRACS Alerian Midstream
        Energy High Dividend Index ETN|P| |Y|100|N||AMND|AMND|N\r\nY|AMOM|QRAFT AI-Enhanced
        U.S. Large Cap Momentum ETF|P| |Y|100|N||AMOM|AMOM|N\r\nY|AMP|Ameriprise Financial,
        Inc. Common Stock|N| |N|100|N||AMP|AMP|N\r\nY|AMPD|Return Stacked Bonds &
        Managed Futures ETF CNIC ICE U.S. Carbon Neutral Power Futures Index ETF|P|
        |Y|100|N||AMPD|AMPD|N\r\nY|AMPG|Amplitech Group, Inc. - Common Stock|Q|S|N|100|N|N||AMPG|N\r\nY|AMPGW|Amplitech
        Group, Inc. - Warrants|Q|S|N|100|N|N||AMPGW|N\r\nY|AMPH|Amphastar Pharmaceuticals,
        Inc. - Common Stock|Q|Q|N|100|N|N||AMPH|N\r\nY|AMPL|Amplitude, Inc. - Class
        A Common Stock|Q|S|N|100|N|N||AMPL|N\r\nY|AMPS|Altus Power, Inc. Class A Common
        Stock|N| |N|100|N||AMPS|AMPS|N\r\nY|AMPX|Amprius Technologies, Inc. Common
        Stock|N| |N|100|N||AMPX|AMPX|N\r\nY|AMPX.W|Amprius Technologies, Inc. Warrants
        to purchase one share of Common Stock at an exercise price of $11.50 per share|N|
        |N|100|N||AMPX.WS|AMPX+|N\r\nY|AMPY|Amplify Energy Corp. Common Stock|N| |N|100|N||AMPY|AMPY|N\r\nY|AMR|Alpha
        Metallurgical Resources, Inc. Common Stock|N| |N|100|N||AMR|AMR|N\r\nY|AMRC|Ameresco,
        Inc. Class A Common Stock|N| |N|100|N||AMRC|AMRC|N\r\nY|AMRK|A-Mark Precious
        Metals, Inc. - Common Stock|Q|Q|N|100|N|N||AMRK|N\r\nY|AMRN|Amarin Corporation
        plc - American Depositary Shares, each representing one Ordinary Share|Q|G|N|100|N|D||AMRN|N\r\nY|AMRX|Amneal
        Pharmaceuticals, Inc. - Class A Common Stock|Q|Q|N|100|N|N||AMRX|N\r\nY|AMS|American
        Shared Hospital Services Common Stock|A| |N|100|N||AMS|AMS|N\r\nY|AMSC|American
        Superconductor Corporation - Common Stock|Q|Q|N|100|N|N||AMSC|N\r\nY|AMSF|AMERISAFE,
        Inc. - Common Stock|Q|Q|N|100|N|N||AMSF|N\r\nY|AMST|Amesite Inc. - Common
        Stock|Q|S|N|100|N|N||AMST|N\r\nY|AMSWA|American Software, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||AMSWA|N\r\nY|AMT|American Tower Corporation (REIT) Common
        Stock|N| |N|100|N||AMT|AMT|N\r\nY|AMTB|Amerant Bancorp Inc. Class A Common
        Stock|N| |N|100|N||AMTB|AMTB|N\r\nY|AMTD|AMTD IDEA Group American Depositary
        Shares, each representing six (6) Class A Ordinary Shares|N| |N|100|N||AMTD|AMTD|N\r\nY|AMTR|ETRACS
        Alerian Midstream Energy Total Return Index ETN|P| |N|100|N||AMTR|AMTR|N\r\nY|AMTX|Aemetis,
        Inc - Common Stock|Q|G|N|100|N|N||AMTX|N\r\nY|AMUB|ETRACS Alerian MLP Index
        ETN Series B due July 18, 2042|P| |N|100|N||AMUB|AMUB|N\r\nY|AMWD|American
        Woodmark Corporation - Common Stock|Q|Q|N|100|N|N||AMWD|N\r\nY|AMWL|American
        Well Corporation Class A Common Stock|N| |N|100|N||AMWL|AMWL|N\r\nY|AMX|America
        Movil, S.A.B. de C.V. American Depositary Shares (each representing the right
        to receive twenty (20) Series B Shares|N| |N|100|N||AMX|AMX|N\r\nY|AMZA|InfraCap
        MLP ETF|P| |Y|100|N||AMZA|AMZA|N\r\nY|AMZD|Direxion Daily AMZN Bear 1X Shares|Q|G|Y|100|N|N||AMZD|N\r\nY|AMZN|Amazon.com,
        Inc. - Common Stock|Q|Q|N|100|N|N||AMZN|N\r\nY|AMZP|NEOS ETF Trust Kurv Yield
        Premium Strategy Amazon (AMZN) ETF|Z| |Y|100|N||AMZP|AMZP|N\r\nY|AMZU|Direxion
        Daily AMZN Bull 2X Shares|Q|G|Y|100|N|N||AMZU|N\r\nY|AMZY|Tidal ETF Trust
        II YieldMax AMZN Option Income Strategy ETF|P| |Y|100|N||AMZY|AMZY|N\r\nY|AMZZ|GraniteShares
        2x Long AMZN Daily ETF|Q|G|Y|100|N|N||AMZZ|N\r\nY|AN|AutoNation, Inc. Common
        Stock|N| |N|100|N||AN|AN|N\r\nY|ANAB|AnaptysBio, Inc. - Common Stock|Q|Q|N|100|N|N||ANAB|N\r\nY|ANDE|The
        Andersons, Inc. - Common Stock|Q|Q|N|100|N|N||ANDE|N\r\nY|ANEB|Anebulo Pharmaceuticals,
        Inc. - Common Stock|Q|S|N|100|N|N||ANEB|N\r\nY|ANET|Arista Networks, Inc.
        Common Stock|N| |N|100|N||ANET|ANET|N\r\nY|ANEW|ProShares MSCI Transformational
        Changes ETF|P| |Y|100|N||ANEW|ANEW|N\r\nY|ANF|Abercrombie & Fitch Company
        Common Stock|N| |N|100|N||ANF|ANF|N\r\nY|ANG$A|American National Group Inc.
        Depositary Shares, each representing a 1/1,000th interest in a share of  5.95%
        Fixed-Rate Reset Non-Cumulative Preferred Stock, Series A|N| |N|100|N||ANGpA|ANG-A|N\r\nY|ANG$B|American
        National Group Inc. Depositary Shares, each representing a 1/1,000th interest
        in a share of 6.625% Fixed-Rate Reset Non-Cumulative Preferred Stock, Series
        B|N| |N|100|N||ANGpB|ANG-B|N\r\nY|ANGH|Anghami Inc. - Ordinary Shares|Q|G|N|100|N|N||ANGH|N\r\nY|ANGHW|Anghami
        Inc. - Warrants|Q|S|N|100|N|N||ANGHW|N\r\nY|ANGI|Angi Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||ANGI|N\r\nY|ANGL|VanEck Fallen Angel High Yield Bond
        ETF|Q|G|Y|100|N|N||ANGL|N\r\nY|ANGO|AngioDynamics, Inc. - Common Stock|Q|Q|N|100|N|N||ANGO|N\r\nY|ANIK|Anika
        Therapeutics Inc. - Common Stock|Q|Q|N|100|N|N||ANIK|N\r\nY|ANIP|ANI Pharmaceuticals,
        Inc. - Common Stock|Q|G|N|100|N|N||ANIP|N\r\nY|ANIX|Anixa Biosciences, Inc.
        - Common Stock|Q|S|N|100|N|N||ANIX|N\r\nY|ANL|Adlai Nortye Ltd. - American
        Depositary Shares|Q|G|N|100|N|N||ANL|N\r\nY|ANNX|Annexon, Inc. - common stock|Q|Q|N|100|N|N||ANNX|N\r\nY|ANRO|Alto
        Neuroscience, Inc. Common Stock|N| |N|100|N||ANRO|ANRO|N\r\nY|ANSC|Agriculture
        & Natural Solutions Acquisition Corporation - Class A Ordinary Shares|Q|G|N|100|N|D||ANSC|N\r\nY|ANSCU|Agriculture
        & Natural Solutions Acquisition Corporation - Unit|Q|G|N|100|N|D||ANSCU|N\r\nY|ANSCW|Agriculture
        & Natural Solutions Acquisition Corporation - Warrant|Q|G|N|100|N|D||ANSCW|N\r\nY|ANSS|ANSYS,
        Inc. - Common Stock|Q|Q|N|100|N|N||ANSS|N\r\nY|ANTE|AirNet Technology Inc.
        - American Depositary Shares, each representing one ordinary shares|Q|S|N|100|N|N||ANTE|N\r\nY|ANTX|AN2
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||ANTX|N\r\nY|ANVS|Annovis
        Bio, Inc. Common Stock|N| |N|100|N||ANVS|ANVS|N\r\nY|ANY|Sphere 3D Corp. -
        Common Shares|Q|S|N|100|N|N||ANY|N\r\nY|AOA|iShares Core Aggressive Allocation
        ETF|P| |Y|100|N||AOA|AOA|N\r\nY|AOD|abrdn Total Dynamic Dividend Fund Common
        Shares of Beneficial Interest|N| |N|100|N||AOD|AOD|N\r\nY|AOGO|Arogo Capital
        Acquisition Corp. - Class A Common Stock|Q|G|N|100|N|D||AOGO|N\r\nY|AOGOU|Arogo
        Capital Acquisition Corp. - Unit|Q|G|N|100|N|D||AOGOU|N\r\nY|AOGOW|Arogo Capital
        Acquisition Corp. - Warrant|Q|G|N|100|N|D||AOGOW|N\r\nY|AOHY|Angel Oak Funds
        Trust Angel Oak High Yield Opportunities ETF|P| |Y|100|N||AOHY|AOHY|N\r\nY|AOK|iShares
        Core Conservative Allocation ETF|P| |Y|100|N||AOK|AOK|N\r\nY|AOM|iShares Core
        Moderate Allocation ETF|P| |Y|100|N||AOM|AOM|N\r\nY|AOMR|Angel Oak Mortgage
        REIT, Inc. Common Stock|N| |N|100|N||AOMR|AOMR|N\r\nY|AON|Aon plc Class A
        Ordinary Shares (Ireland)|N| |N|100|N||AON|AON|N\r\nY|AOR|iShares Core Growth
        Allocation ETF|P| |Y|100|N||AOR|AOR|N\r\nY|AORT|Artivion, Inc. Common Stock|N|
        |N|100|N||AORT|AORT|N\r\nY|AOS|A.O. Smith Corporation Common Stock|N| |N|100|N||AOS|AOS|N\r\nY|AOSL|Alpha
        and Omega Semiconductor Limited - Common Shares|Q|Q|N|100|N|N||AOSL|N\r\nY|AOTG|AOT
        Growth and Innovation ETF|Q|G|Y|100|N|N||AOTG|N\r\nY|AOUT|American Outdoor
        Brands, Inc. - Common Stock|Q|Q|N|100|N|N||AOUT|N\r\nY|AP|Ampco-Pittsburgh
        Corporation Common Stock|N| |N|100|N||AP|AP|N\r\nY|AP.W|Ampco-Pittsburgh Corporation
        Series A Warrants to purchase Shares of common stock|A| |N|100|N||AP.WS|AP+|N\r\nY|APA|APA
        Corporation - Common Stock|Q|Q|N|100|N|N||APA|N\r\nY|APAM|Artisan Partners
        Asset Management Inc. Class A Common Stock|N| |N|100|N||APAM|APAM|N\r\nY|APCB|Trust
        for Professional Managers ActivePassive Core Bond ETF|P| |Y|100|N||APCB|APCB|N\r\nY|APCX|AppTech
        Payments Corp. - Common stock|Q|S|N|100|N|D||APCX|N\r\nY|APCXW|AppTech Payments
        Corp. - Warrant|Q|S|N|100|N|N||APCXW|N\r\nY|APD|Air Products and Chemicals,
        Inc. Common Stock|N| |N|100|N||APD|APD|N\r\nY|APDN|Applied DNA Sciences, Inc.
        - Common Stock|Q|S|N|100|N|D||APDN|N\r\nY|APEI|American Public Education,
        Inc. - Common Stock|Q|Q|N|100|N|N||APEI|N\r\nY|APG|APi Group Corporation Common
        Stock|N| |N|100|N||APG|APG|N\r\nY|APGE|Apogee Therapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||APGE|N\r\nY|APH|Amphenol Corporation Common Stock|N|
        |N|100|N||APH|APH|N\r\nY|API|Agora, Inc. - ADS|Q|Q|N|100|N|N||API|N\r\nY|APIE|Trust
        for Professional Managers ActivePassive International Equity ETF|P| |Y|100|N||APIE|APIE|N\r\nY|APLD|Applied
        Digital Corporation - Common Stock|Q|Q|N|100|N|N||APLD|N\r\nY|APLE|Apple Hospitality
        REIT, Inc. Common Shares|N| |N|100|N||APLE|APLE|N\r\nY|APLM|Apollomics Inc.
        - Class A Ordinary Shares|Q|S|N|100|N|D||APLM|N\r\nY|APLMW|Apollomics Inc.
        - Warrant|Q|S|N|100|N|N||APLMW|N\r\nY|APLS|Apellis Pharmaceuticals, Inc. -
        Common Stock|Q|Q|N|100|N|N||APLS|N\r\nY|APLT|Applied Therapeutics, Inc. -
        Common Stock|Q|G|N|100|N|N||APLT|N\r\nY|APLY|Tidal ETF Trust II YieldMax AAPL
        Option Income Strategy ETF|P| |Y|100|N||APLY|APLY|N\r\nY|APM|Aptorum Group
        Limited - Class A Ordinary Shares|Q|S|N|100|N|N||APM|N\r\nY|APMU|Trust for
        Professional Managers ActivePassive Intermediate Municipal Bond ETF|P| |Y|100|N||APMU|APMU|N\r\nY|APO|Apollo
        Global Management, Inc. (New) Common Stock|N| |N|100|N||APO|APO|N\r\nY|APO$A|Apollo
        Global Management, Inc. 6.75% Series A Mandatory Convertible Preferred Stock|N|
        |N|100|N||APOpA|APO-A|N\r\nY|APOG|Apogee Enterprises, Inc. - Common Stock|Q|Q|N|100|N|N||APOG|N\r\nY|APOS|Apollo
        Global Management, Inc. 7.625% Fixed-Rate Resettable Junior Subordinated Notes
        due 2053|N| |N|100|N||APOS|APOS|N\r\nY|APP|Applovin Corporation - Class A
        Common Stock|Q|Q|N|100|N|N||APP|N\r\nY|APPF|AppFolio, Inc. - Class A Common
        Stock|Q|G|N|100|N|N||APPF|N\r\nY|APPN|Appian Corporation - Class A Common
        Stock|Q|G|N|100|N|N||APPN|N\r\nY|APPS|Digital Turbine, Inc. - Common Stock|Q|S|N|100|N|N||APPS|N\r\nY|APRD|Innovator
        ETFs Trust Innovator Premium Income 10 Barrier ETF - April|Z| |Y|100|N||APRD|APRD|N\r\nY|APRE|Aprea
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||APRE|N\r\nY|APRH|Innovator
        ETFs Trust Innovator Premium Income 20 Barrier ETF - April|Z| |Y|100|N||APRH|APRH|N\r\nY|APRJ|Innovator
        ETFs Trust Innovator Premium Income 30 Barrier ETF - April|Z| |Y|100|N||APRJ|APRJ|N\r\nY|APRP|SHL
        Telemedicine Ltd PGIM US Large-Cap Buffer 12 ETF - April|Z| |Y|100|N||APRP|APRP|N\r\nY|APRQ|Innovator
        ETFs Trust Innovator Premium Income 40 Barrier ETF - April|Z| |Y|100|N||APRQ|APRQ|N\r\nY|APRT|AllianzIM
        U.S. Large Cap Buffer10 Apr ETF|P| |Y|100|N||APRT|APRT|N\r\nY|APRW|AllianzIM
        U.S. Large Cap Buffer20 Apr ETF|P| |Y|100|N||APRW|APRW|N\r\nY|APRZ|Trust TrueShares
        Structured Outcome (April) ETF|Z| |Y|100|N||APRZ|APRZ|N\r\nY|APT|Alpha Pro
        Tech, Ltd. Common Stock|A| |N|100|N||APT|APT|N\r\nY|APTO|Aptose Biosciences,
        Inc. - Common Shares|Q|S|N|100|N|D||APTO|N\r\nY|APTV|Aptiv PLC Ordinary Shares|N|
        |N|100|N||APTV|APTV|N\r\nY|APUE|Trust for Professional Managers ActivePassive
        U.S. Equity ETF|P| |Y|100|N||APUE|APUE|N\r\nY|APVO|Aptevo Therapeutics Inc.
        - Common Stock|Q|S|N|100|N|N||APVO|N\r\nY|APWC|Asia Pacific Wire & Cable Corporation
        Limited  - Common shares, Par value .01 per share|Q|S|N|100|N|N||APWC|N\r\nY|APXI|APx
        Acquisition Corp. I - Class A Ordinary Share|Q|G|N|100|N|E||APXI|N\r\nY|APXIU|APx
        Acquisition Corp. I - Unit|Q|G|N|100|N|E||APXIU|N\r\nY|APXIW|APx Acquisition
        Corp. I - Warrant|Q|G|N|100|N|E||APXIW|N\r\nY|APYX|Apyx Medical Corporation
        - Common Stock|Q|Q|N|100|N|N||APYX|N\r\nY|AQB|AquaBounty Technologies, Inc.
        - Common Stock|Q|S|N|100|N|N||AQB|N\r\nY|AQMS|Aqua Metals, Inc. - Common Stock|Q|S|N|100|N|D||AQMS|N\r\nY|AQN|Algonquin
        Power & Utilities Corp. Common Shares|N| |N|100|N||AQN|AQN|N\r\nY|AQNB|Algonquin
        Power & Utilities Corp. 6.20% Fixed-to-Floating Subordinated Notes Series
        2019-A due July 1, 2079|N| |N|100|N||AQNB|AQNB|N\r\nY|AQST|Aquestive Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||AQST|N\r\nY|AQU|Aquaron Acquisition Corp.
        - Common Stock|Q|S|N|100|N|H||AQU|N\r\nY|AQUNR|Aquaron Acquisition Corp. -
        Rights|Q|S|N|100|N|E||AQUNR|N\r\nY|AQUNU|Aquaron Acquisition Corp. - Units|Q|S|N|100|N|E||AQUNU|N\r\nY|AQWA|Global
        X Clean Water ETF|Q|G|Y|100|N|N||AQWA|N\r\nY|AR|Antero Resources Corporation
        Common Stock|N| |N|100|N||AR|AR|N\r\nY|ARAY|Accuray Incorporated - Common
        Stock|Q|Q|N|100|N|N||ARAY|N\r\nY|ARB|AltShares Merger Arbitrage ETF|P| |Y|100|N||ARB|ARB|N\r\nY|ARBB|ARB
        IOT Group Limited - Ordinary Shares|Q|S|N|100|N|N||ARBB|N\r\nY|ARBE|Arbe Robotics
        Ltd. - Ordinary Shares|Q|S|N|100|N|N||ARBE|N\r\nY|ARBEW|Arbe Robotics Ltd.
        - Warrant|Q|S|N|100|N|N||ARBEW|N\r\nY|ARBK|Argo Blockchain plc - American
        Depositary Shares|Q|Q|N|100|N|N||ARBK|N\r\nY|ARBKL|Argo Blockchain plc - 8.75%
        Senior Notes due 2026|Q|G|N|100|N|N||ARBKL|N\r\nY|ARC|ARC Document Solutions,
        Inc. Common Stock|N| |N|100|N||ARC|ARC|N\r\nY|ARCB|ArcBest Corporation - Common
        Stock|Q|Q|N|100|N|N||ARCB|N\r\nY|ARCC|Ares Capital Corporation - Closed End
        Fund|Q|Q|N|100|N|N||ARCC|N\r\nY|ARCH|Arch Resources, Inc. Class A Common Stock|N|
        |N|100|N||ARCH|ARCH|N\r\nY|ARCM|Arrow Reserve Capital Management ETF|Z| |Y|100|N||ARCM|ARCM|N\r\nY|ARCO|Arcos
        Dorados Holdings Inc. Class A Shares|N| |N|100|N||ARCO|ARCO|N\r\nY|ARCT|Arcturus
        Therapeutics Holdings Inc. - Common Stock|Q|G|N|100|N|N||ARCT|N\r\nY|ARDC|Ares
        Dynamic Credit Allocation Fund, Inc. Common Shares|N| |N|100|N||ARDC|ARDC|N\r\nY|ARDX|Ardelyx,
        Inc. - Common Stock|Q|G|N|100|N|N||ARDX|N\r\nY|ARE|Alexandria Real Estate
        Equities, Inc. Common Stock|N| |N|100|N||ARE|ARE|N\r\nY|AREB|American Rebel
        Holdings, Inc. - Common Stock|Q|S|N|100|N|D||AREB|N\r\nY|AREBW|American Rebel
        Holdings, Inc. - warrants|Q|S|N|100|N|D||AREBW|N\r\nY|AREC|American Resources
        Corporation - Class A Common Stock|Q|S|N|100|N|N||AREC|N\r\nY|AREN|The Arena
        Group Holdings, Inc. Common Stock|A| |N|100|N||AREN|AREN|N\r\nY|ARES|Ares
        Management Corporation Class A Common Stock|N| |N|100|N||ARES|ARES|N\r\nY|ARGD|Argo
        Group International Holdings, Ltd. 6.5% Senior Notes Due 2042|N| |N|100|N||ARGD|ARGD|N\r\nY|ARGO$A|Argo
        Group International Holdings, Inc. Depositary Shares, Each Representing a
        1/1,000th Interest in a 7.00% Resettable Fixed Rate Preference Share, Series
        A|N| |N|100|N||ARGOpA|ARGO-A|N\r\nY|ARGT|Global X MSCI Argentina ETF|P| |Y|100|N||ARGT|ARGT|N\r\nY|ARGX|argenx
        SE - American Depositary Shares|Q|Q|N|100|N|N||ARGX|N\r\nY|ARHS|Arhaus, Inc.
        - Class A Common Stock|Q|Q|N|100|N|N||ARHS|N\r\nY|ARI|Apollo Commercial Real
        Estate Finance, Inc|N| |N|100|N||ARI|ARI|N\r\nY|ARIS|Aris Water Solutions,
        Inc. Class A Common Stock|N| |N|100|N||ARIS|ARIS|N\r\nY|ARKA|EA Series Trust
        ARK 21Shares Active Bitcoin Futures Strategy ETF|Z| |Y|100|N||ARKA|ARKA|N\r\nY|ARKB|ARK
        21Shares Bitcoin ETF Common Shares of Beneficial Interests|Z| |Y|100|N||ARKB|ARKB|N\r\nY|ARKC|EA
        Series Trust ARK 21Shares Active On-Chain Bitcoin Strategy ETF|Z| |Y|100|N||ARKC|ARKC|N\r\nY|ARKD|EA
        Series Trust ARK 21Shares Blockchain and Digital Economy Innovation ETF|Z|
        |Y|100|N||ARKD|ARKD|N\r\nY|ARKF|ARK Fintech Innovation ETF|P| |Y|100|N||ARKF|ARKF|N\r\nY|ARKG|ARK
        Genomic Revolution ETF|Z| |Y|100|N||ARKG|ARKG|N\r\nY|ARKK|ARK Innovation ETF|P|
        |Y|100|N||ARKK|ARKK|N\r\nY|ARKO|ARKO Corp. - Common Stock|Q|S|N|100|N|N||ARKO|N\r\nY|ARKOW|ARKO
        Corp. - Warrant|Q|S|N|100|N|N||ARKOW|N\r\nY|ARKQ|ARK Autonomous Technology
        & Robotics ETF|Z| |Y|100|N||ARKQ|ARKQ|N\r\nY|ARKR|Ark Restaurants Corp. -
        Common Stock|Q|G|N|100|N|N||ARKR|N\r\nY|ARKW|ARK Next Generation Internet
        ETF|P| |Y|100|N||ARKW|ARKW|N\r\nY|ARKX|ARK Space Exploration & Innovation
        ETF|Z| |Y|100|N||ARKX|ARKX|N\r\nY|ARKY|EA Series Trust ARK 21Shares Active
        Bitcoin Ethereum Strategy ETF|Z| |Y|100|N||ARKY|ARKY|N\r\nY|ARKZ|EA Series
        Trust ARK 21Shares Active Ethereum Futures Strategy ETF|Z| |Y|100|N||ARKZ|ARKZ|N\r\nY|ARL|American
        Realty Investors, Inc. Common Stock|N| |N|100|N||ARL|ARL|N\r\nY|ARLO|Arlo
        Technologies, Inc. Common Stock|N| |N|100|N||ARLO|ARLO|N\r\nY|ARLP|Alliance
        Resource Partners, L.P. - Common Units Representing Limited Partnership Interests|Q|Q|N|100|N|N||ARLP|N\r\nY|ARLU|SHL
        Telemedicine Ltd AllianzIM U.S. Equity Buffer15 Uncapped Apr ETF|Z| |Y|100|N||ARLU|ARLU|N\r\nY|ARM|Arm
        Holdings plc - American Depositary Shares|Q|Q|N|100|N|N||ARM|N\r\nY|ARMK|Aramark
        Common Stock|N| |N|100|N||ARMK|ARMK|N\r\nY|ARMN|Aris Mining Corporation Common
        Shares|A| |N|100|N||ARMN|ARMN|N\r\nY|ARMP|Armata Pharmaceuticals, Inc. Common
        Stock|A| |N|100|N||ARMP|ARMP|N\r\nY|AROC|Archrock, Inc. Common Stock|N| |N|100|N||AROC|AROC|N\r\nY|AROW|Arrow
        Financial Corporation - Common Stock|Q|Q|N|100|N|N||AROW|N\r\nY|ARP|The Advisors?
        Inner Circle Fund II PMV Adaptive Risk Parity ETF|P| |Y|100|N||ARP|ARP|N\r\nY|ARQ|Arq,
        Inc. - Common Stock|Q|G|N|100|N|N||ARQ|N\r\nY|ARQQ|Arqit Quantum Inc. - Ordinary
        Shares|Q|S|N|100|N|D||ARQQ|N\r\nY|ARQQW|Arqit Quantum Inc. - Warrants|Q|S|N|100|N|N||ARQQW|N\r\nY|ARQT|Arcutis
        Biotherapeutics, Inc. - Common stock|Q|Q|N|100|N|N||ARQT|N\r\nY|ARR|ARMOUR
        Residential REIT, Inc.|N| |N|100|N||ARR|ARR|N\r\nY|ARR$C|ARMOUR Residential
        REIT, Inc. 7% Series C Cumulative Redeemable Preferred Stock (liquidation
        preference $25.00 per share)|N| |N|100|N||ARRpC|ARR-C|N\r\nY|ARRY|Array Technologies,
        Inc. - Common Stock|Q|G|N|100|N|N||ARRY|N\r\nY|ARTL|Artelo Biosciences, Inc.
        - Common Stock|Q|S|N|100|N|N||ARTL|N\r\nY|ARTNA|Artesian Resources Corporation
        - Class A Non-Voting Common Stock|Q|Q|N|100|N|N||ARTNA|N\r\nY|ARTW|Art's-Way
        Manufacturing Co., Inc. - Common Stock|Q|S|N|100|N|N||ARTW|N\r\nY|ARVN|Arvinas,
        Inc. - Common Stock|Q|Q|N|100|N|N||ARVN|N\r\nY|ARVR|First Trust Indxx Metaverse
        ETF|Q|G|Y|100|N|N||ARVR|N\r\nY|ARW|Arrow Electronics, Inc. Common Stock|N|
        |N|100|N||ARW|ARW|N\r\nY|ARWR|Arrowhead Pharmaceuticals, Inc. - Common Stock|Q|Q|N|100|N|N||ARWR|N\r\nY|ARYD|ARYA
        Sciences Acquisition Corp IV - Class A Ordinary Shares|Q|S|N|100|N|D||ARYD|N\r\nY|AS|Amer
        Sports, Inc. Ordinary Shares|N| |N|100|N||AS|AS|N\r\nY|ASA|ASA  Gold and Precious
        Metals Limited|N| |N|100|N||ASA|ASA|N\r\nY|ASAI|Sendas Distribuidora S A ADS|N|
        |N|100|N||ASAI|ASAI|N\r\nY|ASAN|Asana, Inc. Class A Common Stock|N| |N|100|N||ASAN|ASAN|N\r\nY|ASB|Associated
        Banc-Corp Common Stock|N| |N|100|N||ASB|ASB|N\r\nY|ASB$E|Associated Banc-Corp
        Depositary Shares, each representing a 1/40th interest in a share of 5.875%
        Non-Cumulative Perpetual Preferred Stock, Series E|N| |N|100|N||ASBpE|ASB-E|N\r\nY|ASB$F|Associated
        Banc-Corp Depositary Shares, each representing a 1/40th interest in a share
        of Associated Banc-Corp 5.625% Non-Cumulative Perpetual Preferred Stock, Series
        F|N| |N|100|N||ASBpF|ASB-F|N\r\nY|ASBA|Associated Banc-Corp 6.625% Fixed-Rate
        Reset Subordinated Notes due 2033|N| |N|100|N||ASBA|ASBA|N\r\nY|ASC|Ardmore
        Shipping Corporation Common Stock|N| |N|100|N||ASC|ASC|N\r\nY|ASCB|A SPAC
        II Acquisition Corp. - Ordinary Shares, Class A Common Stock|Q|G|N|100|N|D||ASCB|N\r\nY|ASCBR|A
        SPAC II Acquisition Corp. - Right|Q|G|N|100|N|N||ASCBR|N\r\nY|ASCBU|A SPAC
        II Acquisition Corp. - Unit|Q|G|N|100|N|N||ASCBU|N\r\nY|ASCBW|A SPAC II Acquisition
        Corp. - Warrant|Q|G|N|100|N|N||ASCBW|N\r\nY|ASEA|Global X FTSE Southeast Asia
        ETF|P| |Y|100|N||ASEA|ASEA|N\r\nY|ASET|FlexShares Real Assets Allocation Index
        Fund|Q|G|Y|100|N|N||ASET|N\r\nY|ASG|Liberty All-Star Growth Fund, Inc.|N|
        |N|100|N||ASG|ASG|N\r\nY|ASGI|abrdn Global Infrastructure Income Fund Common
        Shares of Beneficial Interest|N| |N|100|N||ASGI|ASGI|N\r\nY|ASGN|ASGN Incorporated
        Common Stock|N| |N|100|N||ASGN|ASGN|N\r\nY|ASH|Ashland Inc. Common Stock|N|
        |N|100|N||ASH|ASH|N\r\nY|ASHR|Xtrackers Harvest CSI 300 China A-Shares ETF|P|
        |Y|100|N||ASHR|ASHR|N\r\nY|ASHS|Xtrackers Harvest CSI 500 China A-Shares Small
        Cap ETF|P| |Y|100|N||ASHS|ASHS|N\r\nY|ASIA|Matthews International Funds Matthews
        Pacific Tiger Active ETF|P| |Y|100|N||ASIA|ASIA|N\r\nY|ASIX|AdvanSix Inc.
        Common Stock |N| |N|100|N||ASIX|ASIX|N\r\nY|ASLE|AerSale Corporation - Common
        Stock|Q|S|N|100|N|N||ASLE|N\r\nY|ASLN|ASLAN Pharmaceuticals Limited - American
        Depositary Shares|Q|S|N|100|N|D||ASLN|N\r\nY|ASM|Avino Silver & Gold Mines
        Ltd. Common Shares (Canada)|A| |N|100|N||ASM|ASM|N\r\nY|ASMB|Assembly Biosciences,
        Inc. - Common Stock|Q|Q|N|100|N|N||ASMB|N\r\nY|ASMF|Virtus ETF Trust II Virtus
        AlphaSimplex Managed Futures ETF|P| |Y|100|N||ASMF|ASMF|N\r\nY|ASML|ASML Holding
        N.V. - New York Registry Shares|Q|Q|N|100|N|N||ASML|N\r\nY|ASND|Ascendis Pharma
        A/S - American Depositary Shares|Q|Q|N|100|N|N||ASND|N\r\nY|ASNS|Actelis Networks,
        Inc. - Common Stock|Q|S|N|100|N|D||ASNS|N\r\nY|ASO|Academy Sports and Outdoors,
        Inc. - Common Stock|Q|Q|N|100|N|N||ASO|N\r\nY|ASPI|ASP Isotopes Inc. - Common
        Stock|Q|S|N|100|N|N||ASPI|N\r\nY|ASPN|Aspen Aerogels, Inc. Common Stock|N|
        |N|100|N||ASPN|ASPN|N\r\nY|ASPS|Altisource Portfolio Solutions S.A. - Common
        Stock|Q|Q|N|100|N|N||ASPS|N\r\nY|ASR|Grupo Aeroportuario del Sureste, S.A.
        de C.V. Common Stock|N| |N|100|N||ASR|ASR|N\r\nY|ASRT|Assertio Holdings, Inc.
        - Common Stock|Q|S|N|100|N|N||ASRT|N\r\nY|ASRV|AmeriServ Financial Inc. -
        Common Stock|Q|G|N|100|N|N||ASRV|N\r\nY|ASST|Asset Entities Inc. - Class B
        Common Stock|Q|S|N|100|N|D||ASST|N\r\nY|ASTC|Astrotech Corporation - Common
        Stock|Q|S|N|100|N|N||ASTC|N\r\nY|ASTE|Astec Industries, Inc. - Common Stock|Q|Q|N|100|N|N||ASTE|N\r\nY|ASTH|Astrana
        Health Inc. - Common Stock|Q|S|N|100|N|N||ASTH|N\r\nY|ASTI|Ascent Solar Technologies,
        Inc - Common Stock|Q|S|N|100|N|D||ASTI|N\r\nY|ASTL|Algoma Steel Group Inc.
        - Common Shares|Q|G|N|100|N|N||ASTL|N\r\nY|ASTLW|Algoma Steel Group Inc. -
        Warrant|Q|G|N|100|N|N||ASTLW|N\r\nY|ASTR|Astra Space, Inc. - Class A Common
        Stock|Q|S|N|100|N|D||ASTR|N\r\nY|ASTS|AST SpaceMobile, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||ASTS|N\r\nY|ASTSW|AST SpaceMobile, Inc. - Warrant|Q|Q|N|100|N|N||ASTSW|N\r\nY|ASUR|Asure
        Software Inc - Common Stock|Q|S|N|100|N|N||ASUR|N\r\nY|ASX|ASE Technology
        Holding Co., Ltd. American Depositary Shares (each representing Two Common
        Shares) |N| |N|100|N||ASX|ASX|N\r\nY|ASXC|Asensus Surgical, Inc. Common Stock|A|
        |N|100|N||ASXC|ASXC|N\r\nY|ASYS|Amtech Systems, Inc. - Common Stock|Q|Q|N|100|N|N||ASYS|N\r\nY|ATAI|ATAI
        Life Sciences N.V. - Common Shares|Q|G|N|100|N|N||ATAI|N\r\nY|ATAT|Atour Lifestyle
        Holdings Limited - American Depositary Shares|Q|Q|N|100|N|N||ATAT|N\r\nY|ATCH|AtlasClear
        Holdings, Inc. Common Stock|A| |N|100|N||ATCH|ATCH|N\r\nY|ATCO$D|Atlas Corp.
        7.95% Series D|N| |N|100|N||ATCOpD|ATCO-D|N\r\nY|ATCO$H|Atlas Corp. 7.875%
        Series H|N| |N|100|N||ATCOpH|ATCO-H|N\r\nY|ATCOL|Atlas Corp. - 7.125% Notes
        due 2027|Q|G|N|100|N|N||ATCOL|N\r\nY|ATEC|Alphatec Holdings, Inc. - Common
        Stock|Q|Q|N|100|N|N||ATEC|N\r\nY|ATEK|Athena Technology Acquisition Corp.
        II Class A Common Stock|A| |N|100|N||ATEK|ATEK|N\r\nY|ATEK.U|Athena Technology
        Acquisition Corp. II Units, each consisting of one share of Class A common
        stock, and one-half of one Redeemable Warrant|A| |N|100|N||ATEK.U|ATEK=|N\r\nY|ATEK.W|Athena
        Technology Acquisition Corp. II Redeemable Warrants|A| |N|100|N||ATEK.WS|ATEK+|N\r\nY|ATEN|A10
        Networks, Inc. Common Stock|N| |N|100|N||ATEN|ATEN|N\r\nY|ATER|Aterian, Inc.
        - Common Stock|Q|S|N|100|N|N||ATER|N\r\nY|ATEST|Tick Pilot Test Control Common
        Stock|A| |N|100|Y||ATEST|ATEST|N\r\nY|ATEST.A|Tick Pilot Test Group 1 Common
        Stock|A| |N|100|Y||ATEST.A|ATEST.A|N\r\nY|ATEST.B|Tick pilot Test 2 Common
        Stock|A| |N|100|Y||ATEST.B|ATEST.B|N\r\nY|ATEST.C|Tick Pilot Test 3 Common
        Stock|A| |N|100|Y||ATEST.C|ATEST.C|N\r\nY|ATEX|Anterix Inc. - Common Stock|Q|S|N|100|N|N||ATEX|N\r\nY|ATFV|Alger
        35 ETF|P| |Y|100|N||ATFV|ATFV|N\r\nY|ATGE|Adtalem Global Education Inc. Common
        Stock|N| |N|100|N||ATGE|ATGE|N\r\nY|ATGL|Alpha Technology Group Limited -
        Ordinary Shares|Q|S|N|100|N|N||ATGL|N\r\nY|ATH$A|Athene Holding Ltd. Depositary
        Shares, Each Representing a 1/1,000th Interest in a 6.35% Fixed-to-Floating
        Rate Perpetual Non-Cumulative Preference Share, Series A|N| |N|100|N||ATHpA|ATH-A|N\r\nY|ATH$B|Athene
        Holding Ltd. Depositary Shares, Each Representing a 1/1,000th Interest in
        a 5.625% Fixed Rate Perpetual Non- Cumulative Preference Share, Series B,
        par value $1.00 per share|N| |N|100|N||ATHpB|ATH-B|N\r\nY|ATH$C|Athene Holding
        Ltd. Depositary Shares, each representing a 1/1,000th Interest in a Share
        of 6.375% Fixed-Rate Reset Perpetual Non-Cumulative Preference Shares, Series
        C|N| |N|100|N||ATHpC|ATH-C|N\r\nY|ATH$D|Athene Holding Ltd. Depositary Shares,
        Each Representing a 1/1,000th Interest in a 4.875% Fixed-Rate Perpetual Non-Cumulative
        Preference Share, Series D|N| |N|100|N||ATHpD|ATH-D|N\r\nY|ATH$E|Athene Holding
        Ltd. Depositary Shares, Each Representing a 1/1,000th Interest in a 7.750%
        Fixed-Rate Reset Perpetual Non-Cumulative Preference Share, Series E|N| |N|100|N||ATHpE|ATH-E|N\r\nY|ATHA|Athira
        Pharma, Inc. - Common Stock|Q|Q|N|100|N|N||ATHA|N\r\nY|ATHE|Alterity Therapeutics
        Limited - American Depositary Shares|Q|S|N|100|N|N||ATHE|N\r\nY|ATHM|Autohome
        Inc. American Depositary Shares, each representing four class A ordinary shares.|N|
        |N|100|N||ATHM|ATHM|N\r\nY|ATHS|Athene Holding Ltd. 7.250% Fixed-Rate Reset
        Junior Subordinated Debentures due 2064|N| |N|100|N||ATHS|ATHS|N\r\nY|ATI|ATI
        Inc. Common Stock|N| |N|100|N||ATI|ATI|N\r\nY|ATIF|ATIF Holdings Limited -
        Ordinary Shares|Q|S|N|100|N|D||ATIF|N\r\nY|ATIP|ATI Physical Therapy, Inc.
        Class A Common Stock|N| |N|100|N||ATIP|ATIP|N\r\nY|ATKR|Atkore Inc. Common
        Stock|N| |N|100|N||ATKR|ATKR|N\r\nY|ATLC|Atlanticus Holdings Corporation -
        Common Stock|Q|Q|N|100|N|N||ATLC|N\r\nY|ATLCL|Atlanticus Holdings Corporation
        - 6.125% Senior Notes due 2026|Q|G|N|100|N|N||ATLCL|N\r\nY|ATLCP|Atlanticus
        Holdings Corporation - 7.625% Series B Cumulative Perpetual Preferred Stock,
        no par value per share|Q|Q|N|100|N|N||ATLCP|N\r\nY|ATLCZ|Atlanticus Holdings
        Corporation - 9.25% Senior Notes due 2029|Q|G|N|100|N|N||ATLCZ|N\r\nY|ATLO|Ames
        National Corporation - Common Stock|Q|S|N|100|N|N||ATLO|N\r\nY|ATLX|Atlas
        Lithium Corporation - Common Stock|Q|S|N|100|N|N||ATLX|N\r\nY|ATMC|AlphaTime
        Acquisition Corp - Ordinary Shares|Q|G|N|100|N|N||ATMC|N\r\nY|ATMCR|AlphaTime
        Acquisition Corp - Right|Q|G|N|100|N|N||ATMCR|N\r\nY|ATMCU|AlphaTime Acquisition
        Corp - Unit|Q|G|N|100|N|N||ATMCU|N\r\nY|ATMCW|AlphaTime Acquisition Corp -
        Warrant|Q|G|N|100|N|N||ATMCW|N\r\nY|ATMP|iPath Select MLP ETN|Z| |N|100|N||ATMP|ATMP|N\r\nY|ATMU|Atmus
        Filtration Technologies Inc. Common Stock|N| |N|100|N||ATMU|ATMU|N\r\nY|ATMV|AlphaVest
        Acquisition Corp - Ordinary Shares|Q|G|N|100|N|D||ATMV|N\r\nY|ATMVR|AlphaVest
        Acquisition Corp - Right|Q|G|N|100|N|D||ATMVR|N\r\nY|ATMVU|AlphaVest Acquisition
        Corp - Unit|Q|G|N|100|N|D||ATMVU|N\r\nY|ATNF|180 Life Sciences Corp. - Common
        Stock|Q|S|N|100|N|D||ATNF|N\r\nY|ATNFW|180 Life Sciences Corp. - Warrant|Q|S|N|100|N|D||ATNFW|N\r\nY|ATNI|ATN
        International, Inc. - Common Stock|Q|Q|N|100|N|N||ATNI|N\r\nY|ATNM|Actinium
        Pharmaceuticals, Inc. (Delaware) Common Stock|A| |N|100|N||ATNM|ATNM|N\r\nY|ATO|Atmos
        Energy Corporation Common Stock|N| |N|100|N||ATO|ATO|N\r\nY|ATOM|Atomera Incorporated
        - Common Stock|Q|S|N|100|N|N||ATOM|N\r\nY|ATOS|Atossa Therapeutics, Inc. -
        Common Stock|Q|S|N|100|N|N||ATOS|N\r\nY|ATPC|Agape ATP Corporation - Common
        Stock|Q|S|N|100|N|D||ATPC|N\r\nY|ATR|AptarGroup, Inc. Common Stock|N| |N|100|N||ATR|ATR|N\r\nY|ATRA|Atara
        Biotherapeutics, Inc. - Common Stock|Q|Q|N|100|N|D||ATRA|N\r\nY|ATRC|AtriCure,
        Inc. - Common Stock|Q|G|N|100|N|N||ATRC|N\r\nY|ATRI|Atrion Corporation - Common
        Stock|Q|Q|N|100|N|N||ATRI|N\r\nY|ATRO|Astronics Corporation - Common Stock|Q|Q|N|100|N|N||ATRO|N\r\nY|ATS|ATS
        Corporation Common Shares|N| |N|100|N||ATS|ATS|N\r\nY|ATSG|Air Transport Services
        Group, Inc - Common Stock|Q|Q|N|100|N|N||ATSG|N\r\nY|ATUS|Altice USA, Inc.
        Class A Common Stock|N| |N|100|N||ATUS|ATUS|N\r\nY|ATXG|Addentax Group Corp.
        - Common Stock|Q|S|N|100|N|D||ATXG|N\r\nY|ATXI|Avenue Therapeutics, Inc. -
        Common Stock|Q|S|N|100|N|D||ATXI|N\r\nY|ATXS|Astria Therapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||ATXS|N\r\nY|ATYR|aTyr Pharma, Inc. - Common Stock|Q|S|N|100|N|N||ATYR|N\r\nY|AU|AngloGold
        Ashanti PLC Ordinary Shares|N| |N|100|N||AU|AU|N\r\nY|AUB|Atlantic Union Bankshares
        Corporation Common Stock|N| |N|100|N||AUB|AUB|N\r\nY|AUB$A|Atlantic Union
        Bankshares Corporation Depositary Shares each representing a 1/400th ownership
        interest in a share of 6.875% Perpetual Non-Cumulative Preferred Stock, Series
        A|N| |N|100|N||AUBpA|AUB-A|N\r\nY|AUBN|Auburn National Bancorporation, Inc.
        - Common Stock|Q|G|N|100|N|N||AUBN|N\r\nY|AUDC|AudioCodes Ltd. - Ordinary
        Shares|Q|Q|N|100|N|N||AUDC|N\r\nY|AUGP|SHL Telemedicine Ltd PGIM US Large-Cap
        Buffer 12 ETF - August|Z| |Y|100|N||AUGP|AUGP|N\r\nY|AUGT|AIM ETF Products
        Trust AllianzIM U.S. Large Cap Buffer10 Aug ETF|P| |Y|100|N||AUGT|AUGT|N\r\nY|AUGW|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer20 Aug ETF|P| |Y|100|N||AUGW|AUGW|N\r\nY|AUGX|Augmedix,
        Inc. - Common Stock|Q|S|N|100|N|N||AUGX|N\r\nY|AUGZ|TrueShares Structured
        Outcome (August) ETF|Z| |Y|100|N||AUGZ|AUGZ|N\r\nY|AUID|authID Inc. - Common
        Stock|Q|S|N|100|N|N||AUID|N\r\nY|AULT|Ault Alliance, Inc. Common Stock|A|
        |N|100|N||AULT|AULT|N\r\nY|AULT$D|Ault Alliance, Inc. 13.00% Series D Cumulative
        Redeemable Perpetual Preferred Stock|A| |N|100|N||AULTpD|AULT-D|N\r\nY|AUMI|Themes
        Gold Miners ETF|Q|G|Y|100|N|N||AUMI|N\r\nY|AUMN|Golden Minerals Company Common
        Stock|A| |N|100|N||AUMN|AUMN|N\r\nY|AUNA|Auna SA Class A Ordinary Shares|N|
        |N|100|N||AUNA|AUNA|N\r\nY|AUPH|Aurinia Pharmaceuticals Inc - Common Shares|Q|G|N|100|N|N||AUPH|N\r\nY|AUR|Aurora
        Innovation, Inc.  - Class A Common Stock|Q|Q|N|100|N|N||AUR|N\r\nY|AURA|Aura
        Biosciences, Inc. - Common Stock|Q|G|N|100|N|N||AURA|N\r\nY|AUROW|Aurora Innovation,
        Inc.  - Warrant|Q|Q|N|100|N|N||AUROW|N\r\nY|AUSF|Global X Funds Global X Adaptive
        U.S. Factor ETF|P| |Y|100|N||AUSF|AUSF|N\r\nY|AUST|Austin Gold Corp. Common
        Shares|A| |N|100|N||AUST|AUST|N\r\nY|AUTL|Autolus Therapeutics plc - American
        Depositary Shares|Q|Q|N|100|N|N||AUTL|N\r\nY|AUUD|Auddia Inc. - Common Stock|Q|S|N|100|N|N||AUUD|N\r\nY|AUUDW|Auddia
        Inc. - Warrants|Q|S|N|100|N|N||AUUDW|N\r\nY|AVA|Avista Corporation Common
        Stock|N| |N|100|N||AVA|AVA|N\r\nY|AVAH|Aveanna Healthcare Holdings Inc. -
        Common Stock|Q|Q|N|100|N|N||AVAH|N\r\nY|AVAL|Grupo Aval Acciones y Valores
        S.A. ADR (Each representing 20 preferred shares)|N| |N|100|N||AVAL|AVAL|N\r\nY|AVAV|AeroVironment,
        Inc. - Common Stock|Q|Q|N|100|N|N||AVAV|N\r\nY|AVB|AvalonBay Communities,
        Inc. Common Stock|N| |N|100|N||AVB|AVB|N\r\nY|AVBP|ArriVent BioPharma, Inc.
        - Common Stock|Q|G|N|100|N|N||AVBP|N\r\nY|AVD|American Vanguard Corporation
        Common Stock ($0.10 Par Value)|N| |N|100|N||AVD|AVD|N\r\nY|AVDE|Avantis International
        Equity ETF|P| |Y|100|N||AVDE|AVDE|N\r\nY|AVDL|Avadel Pharmaceuticals plc -
        Ordinary Share|Q|G|N|100|N|N||AVDL|N\r\nY|AVDS|American Century ETF Trust
        Avantis International Small Cap Equity ETF|P| |Y|100|N||AVDS|AVDS|N\r\nY|AVDV|Avantis
        International Small Cap Value ETF|P| |Y|100|N||AVDV|AVDV|N\r\nY|AVDX|AvidXchange
        Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||AVDX|N\r\nY|AVEE|American Century
        ETF Trust Avantis Emerging Markets Small Cap Equity ETF|P| |Y|100|N||AVEE|AVEE|N\r\nY|AVEM|Avantis
        Emerging Markets Equity ETF|P| |Y|100|N||AVEM|AVEM|N\r\nY|AVES|Avantis Emerging
        Markets Value ETF|P| |Y|100|N||AVES|AVES|N\r\nY|AVGE|American Century ETF
        Trust Avantis All Equity Markets ETF|P| |Y|100|N||AVGE|AVGE|N\r\nY|AVGO|Broadcom
        Inc. - Common Stock|Q|Q|N|100|N|N||AVGO|N\r\nY|AVGR|Avinger, Inc. - Common
        Stock|Q|S|N|100|N|N||AVGR|N\r\nY|AVGV|American Century ETF Trust Avantis All
        Equity Markets Value ETF|P| |Y|100|N||AVGV|AVGV|N\r\nY|AVIE|American Century
        ETF Trust Avantis Inflation Focused Equity ETF|P| |Y|100|N||AVIE|AVIE|N\r\nY|AVIG|Avantis
        Core Fixed Income ETF|P| |Y|100|N||AVIG|AVIG|N\r\nY|AVIR|Atea Pharmaceuticals,
        Inc. - common stock|Q|Q|N|100|N|N||AVIR|N\r\nY|AVIV|Avantis International
        Large Cap Value ETF|P| |Y|100|N||AVIV|AVIV|N\r\nY|AVK|Advent Convertible and
        Income Fund|N| |N|100|N||AVK|AVK|N\r\nY|AVLC|American Century ETF Trust Avantis
        U.S. Large Cap Equity ETF|P| |Y|100|N||AVLC|AVLC|N\r\nY|AVLV|Avantis U.S.
        Large Cap Value ETF|P| |Y|100|N||AVLV|AVLV|N\r\nY|AVMA|American Century ETF
        Trust Avantis Moderate Allocation ETF|P| |Y|100|N||AVMA|AVMA|N\r\nY|AVMC|American
        Century ETF Trust Avantis U.S. Mid Cap Equity ETF|P| |Y|100|N||AVMC|AVMC|N\r\nY|AVMU|Avantis
        Core Municipal Fixed Income ETF|P| |Y|100|N||AVMU|AVMU|N\r\nY|AVMV|American
        Century ETF Trust Avantis U.S. Mid Cap Value ETF|P| |Y|100|N||AVMV|AVMV|N\r\nY|AVNM|American
        Century ETF Trust Avantis All International Markets Equity ETF|P| |Y|100|N||AVNM|AVNM|N\r\nY|AVNS|Avanos
        Medical, Inc. Common Stock|N| |N|100|N||AVNS|AVNS|N\r\nY|AVNT|Avient Corporation
        Common Stock|N| |N|100|N||AVNT|AVNT|N\r\nY|AVNV|American Century ETF Trust
        Avantis All International Markets Value ETF|P| |Y|100|N||AVNV|AVNV|N\r\nY|AVNW|Aviat
        Networks, Inc. - Common Stock|Q|Q|N|100|N|N||AVNW|N\r\nY|AVO|Mission Produce,
        Inc. - Common Stock|Q|Q|N|100|N|N||AVO|N\r\nY|AVPT|AvePoint, Inc. - Class
        A Common Stock|Q|Q|N|100|N|N||AVPT|N\r\nY|AVPTW|AvePoint, Inc. - Warrant|Q|Q|N|100|N|N||AVPTW|N\r\nY|AVRE|Avantis
        Real Estate ETF|P| |Y|100|N||AVRE|AVRE|N\r\nY|AVSC|American Century ETF Trust
        Avantis U.S Small Cap Equity ETF|P| |Y|100|N||AVSC|AVSC|N\r\nY|AVSD|American
        Century ETF Trust Avantis Responsible International Equity ETF|P| |Y|100|N||AVSD|AVSD|N\r\nY|AVSE|American
        Century ETF Trust Avantis Responsible Emerging Markets Equity ETF|P| |Y|100|N||AVSE|AVSE|N\r\nY|AVSF|Avantis
        Short-Term Fixed Income ETF|P| |Y|100|N||AVSF|AVSF|N\r\nY|AVSU|American Century
        ETF Trust Avantis Responsible U.S. Equity ETF|P| |Y|100|N||AVSU|AVSU|N\r\nY|AVT|Avnet,
        Inc. - Common Stock|Q|Q|N|100|N|N||AVT|N\r\nY|AVTE|Aerovate Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||AVTE|N\r\nY|AVTR|Avantor, Inc. Common Stock|N|
        |N|100|N||AVTR|AVTR|N\r\nY|AVTX|Avalo Therapeutics, Inc. - Common Stock|Q|S|N|100|N|D||AVTX|N\r\nY|AVUS|Avantis
        U.S. Equity ETF|P| |Y|100|N||AVUS|AVUS|N\r\nY|AVUV|Avantis U.S. Small Cap
        Value ETF|P| |Y|100|N||AVUV|AVUV|N\r\nY|AVXC|Avantis Emerging Markets ex-China
        Equity ETF|Q|G|Y|100|N|N||AVXC|N\r\nY|AVXL|Anavex Life Sciences Corp. - Common
        Stock|Q|Q|N|100|N|N||AVXL|N\r\nY|AVY|Avery Dennison Corporation Common Stock|N|
        |N|100|N||AVY|AVY|N\r\nY|AWAY|Amplify ETF Trust Amplify Travel Tech ETF|P|
        |Y|100|N||AWAY|AWAY|N\r\nY|AWEG|The Alger ETF Trust Alger Weatherbie Enduring
        Growth ETF|P| |Y|100|N||AWEG|AWEG|N\r\nY|AWF|Alliancebernstein Global High
        Income Fund|N| |N|100|N||AWF|AWF|N\r\nY|AWH|Aspira Women's Health Inc. - Common
        Stock|Q|S|N|100|N|N||AWH|N\r\nY|AWI|Armstrong World Industries Inc Common
        Stock|N| |N|100|N||AWI|AWI|N\r\nY|AWK|American Water Works Company, Inc. Common
        Stock|N| |N|100|N||AWK|AWK|N\r\nY|AWP|abrdn Global Premier Properties Fund
        Common Shares of Beneficial Interest|N| |N|100|N||AWP|AWP|N\r\nY|AWR|American
        States Water Company Common Stock|N| |N|100|N||AWR|AWR|N\r\nY|AWRE|Aware,
        Inc. - Common Stock|Q|G|N|100|N|N||AWRE|N\r\nY|AWX|Avalon Holdings Corporation
        Common Stock|A| |N|100|N||AWX|AWX|N\r\nY|AX|Axos Financial, Inc. Common Stock|N|
        |N|100|N||AX|AX|N\r\nY|AXDX|Accelerate Diagnostics, Inc. - Common Stock|Q|S|N|100|N|D||AXDX|N\r\nY|AXGN|Axogen,
        Inc. - Common Stock|Q|S|N|100|N|N||AXGN|N\r\nY|AXIL|AXIL Brands, Inc. Common
        Stock|A| |N|100|N||AXIL|AXIL|N\r\nY|AXL|American Axle & Manufacturing Holdings,
        Inc. Common Stock|N| |N|100|N||AXL|AXL|N\r\nY|AXNX|Axonics, Inc. - Common
        Stock|Q|Q|N|100|N|N||AXNX|N\r\nY|AXON|Axon Enterprise, Inc. - Common Stock|Q|Q|N|100|N|N||AXON|N\r\nY|AXP|American
        Express Company Common Stock|N| |N|100|N||AXP|AXP|N\r\nY|AXR|AMREP Corporation
        Common Stock|N| |N|100|N||AXR|AXR|N\r\nY|AXS|Axis Capital Holdings Limited
        Common Stock|N| |N|100|N||AXS|AXS|N\r\nY|AXS$E|Axis Capital Holdings Limited
        Depositary Shares, each representing 1/100th interest in a share of a 5.50%
        Series E Preferred Shares|N| |N|100|N||AXSpE|AXS-E|N\r\nY|AXSM|Axsome Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||AXSM|N\r\nY|AXTA|Axalta Coating Systems
        Ltd. Common Shares|N| |N|100|N||AXTA|AXTA|N\r\nY|AXTI|AXT Inc - Common Stock|Q|Q|N|100|N|N||AXTI|N\r\nY|AY|Atlantica
        Sustainable Infrastructure plc - Ordinary Shares|Q|Q|N|100|N|N||AY|N\r\nY|AYI|Acuity
        Brands, Inc. |N| |N|100|N||AYI|AYI|N\r\nY|AYRO|AYRO, Inc. - Common Stock|Q|S|N|100|N|N||AYRO|N\r\nY|AYTU|Aytu
        BioPharma, Inc.  - Common Stock|Q|S|N|100|N|N||AYTU|N\r\nY|AZ|A2Z Smart Technologies
        Corp. - Common Shares|Q|S|N|100|N|D||AZ|N\r\nY|AZEK|The AZEK Company Inc.
        Class A Common Stock|N| |N|100|N||AZEK|AZEK|N\r\nY|AZN|AstraZeneca PLC - American
        Depositary Shares|Q|Q|N|100|N|N||AZN|N\r\nY|AZO|AutoZone, Inc. Common Stock|N|
        |N|100|N||AZO|AZO|N\r\nY|AZPN|Aspen Technology, Inc. - Common Stock|Q|Q|N|100|N|N||AZPN|N\r\nY|AZTA|Azenta,
        Inc. - Common Stock|Q|Q|N|100|N|N||AZTA|N\r\nY|AZTD|Tidal ETF Trust Aztlan
        Global Stock Selection DM SMID ETF|P| |Y|100|N||AZTD|AZTD|N\r\nY|AZTR|Azitra
        Inc Common Stock|A| |N|100|N||AZTR|AZTR|N\r\nY|AZUL|Azul S.A. American Depositary
        Shares (each representing three preferred shares)|N| |N|100|N||AZUL|AZUL|N\r\nY|AZZ|AZZ
        Inc.|N| |N|100|N||AZZ|AZZ|N\r\nY|B|Barnes Group, Inc. Common Stock|N| |N|100|N||B|B|N\r\nY|BA|Boeing
        Company (The) Common Stock|N| |N|100|N||BA|BA|N\r\nY|BAB|Invesco Taxable Municipal
        Bond ETF|P| |Y|100|N||BAB|BAB|N\r\nY|BABA|Alibaba Group Holding Limited American
        Depositary Shares each representing eight Ordinary share|N| |N|100|N||BABA|BABA|N\r\nY|BABX|GraniteShares
        2x Long BABA Daily ETF|Q|G|Y|100|N|N||BABX|N\r\nY|BAC|Bank of America Corporation
        Common Stock|N| |N|100|N||BAC|BAC|N\r\nY|BAC$B|Bank of America Corporation
        Depositary Shares, each representing a 1/1,000th interest in a share of 6.000%
        Non-Cumulative Preferred Stock, Series GG|N| |N|100|N||BACpB|BAC-B|N\r\nY|BAC$E|Bank
        of America Corporation Depositary Sh repstg 1/1000th Perp Pfd Ser E|N| |N|100|N||BACpE|BAC-E|N\r\nY|BAC$K|Bank
        of America Corporation Depositary Shares, each representing a 1/1,000th interest
        in a share of 5.875% Non- Cumulative Preferred Stock, Series HH|N| |N|100|N||BACpK|BAC-K|N\r\nY|BAC$L|Bank
        of America Corporation Non Cumulative Perpetual Conv Pfd Ser L|N| |N|10|N||BACpL|BAC-L|N\r\nY|BAC$M|Bank
        of America Corporation Depositary Shares, each representing a 1/1,000th interest
        in a share of 5.375% Non-Cumulative Preferred Stock, Series KK|N| |N|100|N||BACpM|BAC-M|N\r\nY|BAC$N|Bank
        of America Corporation Depositary shares, each representing 1/1,000th interest
        in a share of 5.000% Non-Cumulative Preferred Stock, Series LL|N| |N|100|N||BACpN|BAC-N|N\r\nY|BAC$O|Bank
        of America Corporation Depositary shares, each representing 1/1,000th interest
        in a share of 4.375% Non-Cumulative Preferred Stock, Series NN|N| |N|100|N||BACpO|BAC-O|N\r\nY|BAC$P|Bank
        of America Corporation Depositary Shares, each representing a 1/1,000th interest
        in a share of 4.125% Non-Cumulative Preferred Stock, Series PP|N| |N|100|N||BACpP|BAC-P|N\r\nY|BAC$Q|Bank
        of America Corporation Depositary shares, each representing 1/1,000th interest
        in a share of 4.250% Non-Cumulative Preferred Stock, Series QQ|N| |N|100|N||BACpQ|BAC-Q|N\r\nY|BAC$S|Bank
        of America Corporation Depositary shares, each representing 1/1,000th interest
        in a share of 4.750% Non-Cumulative Preferred Stock, Series SS|N| |N|100|N||BACpS|BAC-S|N\r\nY|BACA|Berenson
        Acquisition Corp. I Class A Common Stock|A| |N|100|N||BACA|BACA|N\r\nY|BACK|IMAC
        Holdings, Inc. - Common Stock|Q|S|N|100|N|D||BACK|N\r\nY|BAER|Bridger Aerospace
        Group Holdings, Inc. - Common Stock|Q|G|N|100|N|N||BAER|N\r\nY|BAERW|Bridger
        Aerospace Group Holdings, Inc. - Warrant|Q|G|N|100|N|N||BAERW|N\r\nY|BAFN|BayFirst
        Financial Corp. - Common Stock|Q|S|N|100|N|N||BAFN|N\r\nY|BAH|Booz Allen Hamilton
        Holding Corporation Common Stock|N| |N|100|N||BAH|BAH|N\r\nY|BAK|Braskem SA
        ADR|N| |N|100|N||BAK|BAK|N\r\nY|BALI|BlackRock ETF Trust BlackRock Advantage
        Large Cap Income ETF|Z| |Y|100|N||BALI|BALI|N\r\nY|BALL|Ball Corporation Common
        Stock|N| |N|100|N||BALL|BALL|N\r\nY|BALT|Innovator Defined Wealth Shield ETF|Z|
        |Y|100|N||BALT|BALT|N\r\nY|BALY|Bally's Corporation Common Stock|N| |N|100|N||BALY|BALY|N\r\nY|BAM|Brookfield
        Asset Management Inc Class A Limited Voting Shares|N| |N|100|N||BAM|BAM|N\r\nY|BAMA|Brookstone
        Intermediate Bond ETF Brookstone Active ETF|Z| |Y|100|N||BAMA|BAMA|N\r\nY|BAMB|Brookstone
        Intermediate Bond ETF Brookstone Intermediate Bond ETF|Z| |Y|100|N||BAMB|BAMB|N\r\nY|BAMD|Brookstone
        Intermediate Bond ETF Brookstone Dividend Stock ETF|Z| |Y|100|N||BAMD|BAMD|N\r\nY|BAMG|Brookstone
        Intermediate Bond ETF Brookstone Growth Stock ETF|Z| |Y|100|N||BAMG|BAMG|N\r\nY|BAMO|Brookstone
        Intermediate Bond ETF Brookstone Opportunities ETF|Z| |Y|100|N||BAMO|BAMO|N\r\nY|BAMU|Brookstone
        Intermediate Bond ETF Brookstone Ultra-Short Bond ETF|Z| |Y|100|N||BAMU|BAMU|N\r\nY|BAMV|Brookstone
        Intermediate Bond ETF Brookstone Value Stock ETF|Z| |Y|100|N||BAMV|BAMV|N\r\nY|BAMY|Brookstone
        Intermediate Bond ETF Brookstone Yield ETF|Z| |Y|100|N||BAMY|BAMY|N\r\nY|BANC|Banc
        of California, Inc. Common Stock|N| |N|100|N||BANC|BANC|N\r\nY|BANC$F|Banc
        of California, Inc. Depositary Shares, each representing a 1/40th interest
        in a share of 7.75% non-cumulative perpetual preferred stock, Series F|N|
        |N|100|N||BANCpF|BANC-F|N\r\nY|BAND|Bandwidth Inc. - Class A Common Stock|Q|Q|N|100|N|N||BAND|N\r\nY|BANF|BancFirst
        Corporation - Common Stock|Q|Q|N|100|N|N||BANF|N\r\nY|BANFP|BancFirst Corporation
        - 7.2% Cumulative Trust Preferred Securities|Q|Q|N|100|N|N||BANFP|N\r\nY|BANL|CBL
        International Limited - Ordinary Shares|Q|S|N|100|N|N||BANL|N\r\nY|BANR|Banner
        Corporation - Common Stock|Q|Q|N|100|N|N||BANR|N\r\nY|BANX|ArrowMark Financial
        Corp. - Closed End Fund|Q|Q|N|100|N|N||BANX|N\r\nY|BAOS|Baosheng Media Group
        Holdings Limited - Ordinary shares|Q|S|N|100|N|N||BAOS|N\r\nY|BAP|Credicorp
        Ltd. Common Stock|N| |N|100|N||BAP|BAP|N\r\nY|BAPR|Innovator U.S. Equity Buffer
        ETF - April |Z| |Y|100|N||BAPR|BAPR|N\r\nY|BAR|GraniteShares Gold Trust Shares
        of Beneficial Interest|P| |N|100|N||BAR|BAR|N\r\nY|BARK|BARK, Inc. Class A
        Common Stock|N| |N|100|N||BARK|BARK|N\r\nY|BARK.W|BARK, Inc. Redeemable Warrants,
        each whole warrant exercisable for shares of Common Stock at an exercise price
        of $11.50 per share|N| |N|100|N||BARK.WS|BARK+|N\r\nY|BASE|Couchbase, Inc.
        - Common Stock|Q|Q|N|100|N|N||BASE|N\r\nY|BATL|Battalion Oil Corporation Common
        Stock|A| |N|100|N||BATL|BATL|N\r\nY|BATRA|Atlanta Braves Holdings, Inc. -
        Series A Common Stock|Q|Q|N|100|N|N||BATRA|N\r\nY|BATRK|Atlanta Braves Holdings,
        Inc. - Series C Common Stock|Q|Q|N|100|N|N||BATRK|N\r\nY|BATT|Amplify Lithium
        & Battery Technology ETF|P| |Y|100|N||BATT|BATT|N\r\nY|BAUG|Innovator U.S.
        Equity Buffer ETF - August|Z| |Y|100|N||BAUG|BAUG|N\r\nY|BAX|Baxter International
        Inc. Common Stock|N| |N|100|N||BAX|BAX|N\r\nY|BAYA|Bayview Acquisition Corp
        - Ordinary Share|Q|G|N|100|N|N||BAYA|N\r\nY|BAYAR|Bayview Acquisition Corp
        - Right|Q|G|N|100|N|N||BAYAR|N\r\nY|BAYAU|Bayview Acquisition Corp - Unit|Q|G|N|100|N|N||BAYAU|N\r\nY|BB|BlackBerry
        Limited Common Stock|N| |N|100|N||BB|BB|N\r\nY|BBAG|JPMorgan BetaBuilders
        U.S. Aggregate Bond ETF|P| |Y|100|N||BBAG|BBAG|N\r\nY|BBAI|BigBear.ai, Inc.
        Common Stock|N| |N|100|N||BBAI|BBAI|N\r\nY|BBAI.W|BigBear.ai, Inc. Redeemable
        Warrants, each exercisable for one share of Common Stock at an exercise price
        of $11.50 per share|N| |N|100|N||BBAI.WS|BBAI+|N\r\nY|BBAR|Banco BBVA Argentina
        S.A. ADS|N| |N|100|N||BBAR|BBAR|N\r\nY|BBAX|JPMorgan BetaBuilders Developed
        Asia Pacific-ex Japan ETF |Z| |Y|100|N||BBAX|BBAX|N\r\nY|BBBI|BondBloxx ETF
        Trust BondBloxx BBB Rated 5-10 Year Corporate Bond ETF|P| |Y|100|N||BBBI|BBBI|N\r\nY|BBBL|BondBloxx
        ETF Trust BondBloxx BBB Rated 10+ Year Corporate Bond ETF|P| |Y|100|N||BBBL|BBBL|N\r\nY|BBBS|BondBloxx
        ETF Trust BondBloxx BBB Rated 1-5 Year Corporate Bond ETF|P| |Y|100|N||BBBS|BBBS|N\r\nY|BBC|Virtus
        LifeSci Biotech Clinical Trials ETF|P| |Y|100|N||BBC|BBC|N\r\nY|BBCA|JPMorgan
        BetaBuilders Canada ETF |Z| |Y|100|N||BBCA|BBCA|N\r\nY|BBCB|JPMorgan BetaBuilders
        USD Investment Grade Corporate Bond ETF|P| |Y|100|N||BBCB|BBCB|N\r\nY|BBCP|Concrete
        Pumping Holdings, Inc.  - Common Stock|Q|S|N|100|N|N||BBCP|N\r\nY|BBD|Banco
        Bradesco Sa American Depositary Shares|N| |N|100|N||BBD|BBD|N\r\nY|BBDC|Barings
        BDC, Inc. Common Stock|N| |N|100|N||BBDC|BBDC|N\r\nY|BBDO|Banco Bradesco Sa
        American Depositary Shares (each representing one Common Share)|N| |N|100|N||BBDO|BBDO|N\r\nY|BBEM|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan BetaBuilders Emerging Markets Equity
        ETF|Z| |Y|100|N||BBEM|BBEM|N\r\nY|BBEU|JPMorgan BetaBuilders Europe ETF |Z|
        |Y|100|N||BBEU|BBEU|N\r\nY|BBGI|Beasley Broadcast Group, Inc. - Class A Common
        Stock|Q|S|N|100|N|D||BBGI|N\r\nY|BBH|VanEck Biotech ETF|Q|G|Y|100|N|N||BBH|N\r\nY|BBHY|JPMorgan
        BetaBuilders USD High Yield Corporate Bond ETF|Z| |Y|100|N||BBHY|BBHY|N\r\nY|BBIB|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan BetaBuilders U.S. Treasury Bond
        3-10 Year ETF|Z| |Y|100|N||BBIB|BBIB|N\r\nY|BBIN|JPMorgan BetaBuilders International
        Equity ETF|Z| |Y|100|N||BBIN|BBIN|N\r\nY|BBIO|BridgeBio Pharma, Inc. - Common
        Stock|Q|Q|N|100|N|N||BBIO|N\r\nY|BBIP|J.P. Morgan Exchange-Traded Fund Trust
        JPMorgan BetaBuilders U.S. TIPS 0-5 Year ETF|Z| |Y|100|N||BBIP|BBIP|N\r\nY|BBJP|JPMorgan
        BetaBuilders Japan ETF |Z| |Y|100|N||BBJP|BBJP|N\r\nY|BBLB|J.P. Morgan Exchange-Traded
        Fund Trust JPMorgan BetaBuilders U.S. Treasury Bond 20+ Year ETF|Z| |Y|100|N||BBLB|BBLB|N\r\nY|BBLG|Bone
        Biologics Corp - Common Stock|Q|S|N|100|N|N||BBLG|N\r\nY|BBLGW|Bone Biologics
        Corp - warrants|Q|S|N|100|N|N||BBLGW|N\r\nY|BBLU|EA Series Trust EA Bridgeway
        Blue Chip ETF|P| |Y|100|N||BBLU|BBLU|N\r\nY|BBMC|JPMorgan BetaBuilders U.S.
        Mid Cap Equity ETF|P| |Y|100|N||BBMC|BBMC|N\r\nY|BBN|BlackRock Taxable Municipal
        Bond Trust Common Shares of Beneficial Interest|N| |N|100|N||BBN|BBN|N\r\nY|BBP|Virtus
        LifeSci Biotech Products ETF|P| |Y|100|N||BBP|BBP|N\r\nY|BBRE|JPMorgan BetaBuilders
        MSCI U.S. REIT ETF |Z| |Y|100|N||BBRE|BBRE|N\r\nY|BBSA|JPMorgan BetaBuilders
        1-5 Year U.S. Aggregate Bond ETF |Z| |Y|100|N||BBSA|BBSA|N\r\nY|BBSB|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan BetaBuilders U.S. Treasury Bond
        1-3 Year ETF|Z| |Y|100|N||BBSB|BBSB|N\r\nY|BBSC|JPMorgan BetaBuilders U.S.
        Small Cap Equity ETF|P| |Y|100|N||BBSC|BBSC|N\r\nY|BBSI|Barrett Business Services,
        Inc. - Common Stock|Q|Q|N|100|N|N||BBSI|N\r\nY|BBU|Brookfield Business Partners
        L.P. Limited Partnership Units |N| |N|100|N||BBU|BBU|N\r\nY|BBUC|Brookfield
        Business Corporation Class A Exchangeable Subordinate Voting Shares|N| |N|100|N||BBUC|BBUC|N\r\nY|BBUS|JPMorgan
        BetaBuilders U.S. Equity ETF|Z| |Y|100|N||BBUS|BBUS|N\r\nY|BBVA|Banco Bilbao
        Vizcaya Argentaria S.A. Common Stock|N| |N|100|N||BBVA|BBVA|N\r\nY|BBW|Build-A-Bear
        Workshop, Inc. Common Stock|N| |N|100|N||BBW|BBW|N\r\nY|BBWI|Bath & Body Works,
        Inc.|N| |N|100|N||BBWI|BBWI|N\r\nY|BBY|Best Buy Co., Inc. Common Stock|N|
        |N|100|N||BBY|BBY|N\r\nY|BC|Brunswick Corporation Common Stock|N| |N|100|N||BC|BC|N\r\nY|BC$A|Brunswick
        Corporation 6.500% Senior Notes due 2048|N| |N|100|N||BCpA|BC-A|N\r\nY|BC$B|Brunswick
        Corporation 6.625% Senior Notes due 2049|N| |N|100|N||BCpB|BC-B|N\r\nY|BC$C|Brunswick
        Corporation 6.375% Notes due 2049|N| |N|100|N||BCpC|BC-C|N\r\nY|BCAB|BioAtla,
        Inc. - Common Stock|Q|G|N|100|N|N||BCAB|N\r\nY|BCAL|Southern California Bancorp
        - Common Stock|Q|S|N|100|N|N||BCAL|N\r\nY|BCAN|BYND Cannasoft Enterprises
        Inc. - Common Stock|Q|S|N|100|N|D||BCAN|N\r\nY|BCAT|BlackRock Capital Allocation
        Term Trust Common Shares of Beneficial Interest|N| |N|100|N||BCAT|BCAT|N\r\nY|BCBP|BCB
        Bancorp, Inc. (NJ) - Common Stock|Q|G|N|100|N|N||BCBP|N\r\nY|BCC|Boise Cascade,
        L.L.C. Common Stock|N| |N|100|N||BCC|BCC|N\r\nY|BCD|abrdn Bloomberg All Commodity
        Longer Dated Strategy K-1 Free ETF|P| |Y|100|N||BCD|BCD|N\r\nY|BCDA|BioCardia,
        Inc. - Common Stock|Q|S|N|100|N|D||BCDA|N\r\nY|BCDAW|BioCardia, Inc. - Warrant|Q|S|N|100|N|D||BCDAW|N\r\nY|BCDF|Listed
        Funds Trust Horizon Kinetics Blockchain Development ETF|P| |Y|100|N||BCDF|BCDF|N\r\nY|BCE|BCE,
        Inc. Common Stock|N| |N|100|N||BCE|BCE|N\r\nY|BCG|Binah Capital Group, Inc.
        - Common Stock|Q|G|N|100|N|N||BCG|N\r\nY|BCGWW|Binah Capital Group, Inc. -
        Warrants|Q|S|N|100|N|N||BCGWW|N\r\nY|BCH|Banco De Chile ADS|N| |N|100|N||BCH|BCH|N\r\nY|BCHP|Principal
        Exchange-Traded Funds Principal Focused Blue Chip ETF|Z| |Y|100|N||BCHP|BCHP|N\r\nY|BCI|abrdn
        Bloomberg All Commodity Strategy K-1 Free ETF|P| |Y|100|N||BCI|BCI|N\r\nY|BCIL|Exchange
        Listed Funds Trust Bancreek International Large Cap ETF|P| |Y|100|N||BCIL|BCIL|N\r\nY|BCIM|abrdn
        Bloomberg Industrial Metals Strategy K-1 Free ETF|P| |Y|100|N||BCIM|BCIM|N\r\nY|BCLI|Brainstorm
        Cell Therapeutics Inc. - Common Stock|Q|S|N|100|N|D||BCLI|N\r\nY|BCML|BayCom
        Corp - Common Stock|Q|Q|N|100|N|N||BCML|N\r\nY|BCO|Brinks Company (The) Common
        Stock|N| |N|100|N||BCO|BCO|N\r\nY|BCOV|Brightcove Inc. - Common Stock|Q|Q|N|100|N|N||BCOV|N\r\nY|BCOW|1895
        Bancorp of Wisconsin, Inc. - Common Stock|Q|S|N|100|N|N||BCOW|N\r\nY|BCPC|Balchem
        Corporation - Common Stock|Q|Q|N|100|N|N||BCPC|N\r\nY|BCRX|BioCryst Pharmaceuticals,
        Inc. - Common Stock|Q|Q|N|100|N|N||BCRX|N\r\nY|BCS|Barclays PLC Common Stock|N|
        |N|100|N||BCS|BCS|N\r\nY|BCSA|Blockchain Coinvestors Acquisition Corp. I -
        Class A Ordinary Shares|Q|G|N|100|N|N||BCSA|N\r\nY|BCSAU|Blockchain Coinvestors
        Acquisition Corp. I - Unit|Q|G|N|100|N|N||BCSAU|N\r\nY|BCSAW|Blockchain Coinvestors
        Acquisition Corp. I - Warrant|Q|G|N|100|N|N||BCSAW|N\r\nY|BCSF|Bain Capital
        Specialty Finance, Inc. Common Stock|N| |N|100|N||BCSF|BCSF|N\r\nY|BCTX|BriaCell
        Therapeutics Corp. - Common Shares|Q|S|N|100|N|N||BCTX|N\r\nY|BCTXW|BriaCell
        Therapeutics Corp. - Warrant|Q|S|N|100|N|N||BCTXW|N\r\nY|BCUS|Exchange Listed
        Funds Trust Bancreek U.S. Large Cap ETF|P| |Y|100|N||BCUS|BCUS|N\r\nY|BCV|Bancroft
        Fund, Ltd.|A| |N|100|N||BCV|BCV|N\r\nY|BCV$A|Bancroft Fund Limited 5.375%
        Series A Cumulative Preferred Shares|A| |N|100|N||BCVpA|BCV-A|N\r\nY|BCX|BlackRock
        Resources Common Shares of Beneficial Interest|N| |N|100|N||BCX|BCX|N\r\nY|BCYC|Bicycle
        Therapeutics plc - American Depositary Shares|Q|Q|N|100|N|N||BCYC|N\r\nY|BDC|Belden
        Inc Common Stock|N| |N|100|N||BDC|BDC|N\r\nY|BDCX|ETRACS Quarterly Pay 1.5x
        Leveraged MarketVector BDC Liquid Index ETN due June 10, 2050|P| |Y|100|N||BDCX|BDCX|N\r\nY|BDCZ|ETRACS
        MarketVector Business Development Companies Liquid Index ETN due April 26,
        2041|P| |N|100|N||BDCZ|BDCZ|N\r\nY|BDEC|Innovator U.S. Equity Buffer ETF -
        December|Z| |Y|100|N||BDEC|BDEC|N\r\nY|BDGS|Bridges Capital Tactical ETF|Q|G|Y|100|N|N||BDGS|N\r\nY|BDJ|Blackrock
        Enhanced Equity Dividend Trust|N| |N|100|N||BDJ|BDJ|N\r\nY|BDL|Flanigan's
        Enterprises, Inc. Common Stock|A| |N|100|N||BDL|BDL|N\r\nY|BDN|Brandywine
        Realty Trust Common Stock|N| |N|100|N||BDN|BDN|N\r\nY|BDRX|Biodexa Pharmaceuticals
        plc - American Depositary Shares|Q|S|N|100|N|N||BDRX|N\r\nY|BDRY|Amplify Commodity
        Trust Breakwave Dry Bulk Shipping ETF|P| |Y|100|N||BDRY|BDRY|N\r\nY|BDSX|Biodesix,
        Inc. - Common Stock|Q|G|N|100|N|N||BDSX|N\r\nY|BDTX|Black Diamond Therapeutics,
        Inc. - Common Stock|Q|Q|N|100|N|N||BDTX|N\r\nY|BDVG|Litman Gregory Funds Trust
        IMGP Berkshire Dividend Growth ETF|P| |Y|100|N||BDVG|BDVG|N\r\nY|BDX|Becton,
        Dickinson and Company Common Stock|N| |N|100|N||BDX|BDX|N\r\nY|BE|Bloom Energy
        Corporation Class A Common Stock|N| |N|100|N||BE|BE|N\r\nY|BEAM|Beam Therapeutics
        Inc. - Common Stock|Q|Q|N|100|N|N||BEAM|N\r\nY|BEAT|Heartbeam, Inc. - Common
        Stock|Q|S|N|100|N|N||BEAT|N\r\nY|BEATW|Heartbeam, Inc. - Warrant|Q|S|N|100|N|N||BEATW|N\r\nY|BECN|Beacon
        Roofing Supply, Inc. - Common Stock|Q|Q|N|100|N|N||BECN|N\r\nY|BECO|BlackRock
        Future Climate and Sustainable Economy ETF|P| |Y|100|N||BECO|BECO|N\r\nY|BEDU|Bright
        Scholar Education Holdings Limited American Depositary Shares, each  representing
        four Class A Ordinary Share|N| |N|100|N||BEDU|BEDU|N\r\nY|BEDZ|AdvisorShares
        Hotel ETF|P| |Y|100|N||BEDZ|BEDZ|N\r\nY|BEEM|Beam Global - Common Stock|Q|S|N|100|N|N||BEEM|N\r\nY|BEEP|Mobile
        Infrastructure Corporation Common Stock|A| |N|100|N||BEEP|BEEP|N\r\nY|BEEZ|Honeytree
        U.S. Equity ETF|Q|G|Y|100|N|N||BEEZ|N\r\nY|BEKE|KE Holdings Inc American Depositary
        Shares (each representing three Class A Ordinary Shares)|N| |N|100|N||BEKE|BEKE|N\r\nY|BELFA|Bel
        Fuse Inc. - Class A Common Stock|Q|Q|N|100|N|N||BELFA|N\r\nY|BELFB|Bel Fuse
        Inc. - Class B Common Stock|Q|Q|N|100|N|N||BELFB|N\r\nY|BELT|BlackRock Long-Term
        U.S. Equity ETF|Q|G|Y|100|N|N||BELT|N\r\nY|BEMB|iShares Trust iShares J.P.
        Morgan Broad USD Emerging Markets Bond ETF|Z| |Y|100|N||BEMB|BEMB|N\r\nY|BEN|Franklin
        Resources, Inc. Common Stock|N| |N|100|N||BEN|BEN|N\r\nY|BENF|Beneficient
        - Class A Common Stock|Q|S|N|100|N|N||BENF|N\r\nY|BENFW|Beneficient - Warrant|Q|S|N|100|N|N||BENFW|N\r\nY|BEP|Brookfield
        Renewable Partners L.P. |N| |N|100|N||BEP|BEP|N\r\nY|BEP$A|Brookfield Renewable
        Partners L.P. 5.25% Class A Preferred Limited Partnership Units, Series 17|N|
        |N|100|N||BEPpA|BEP-A|N\r\nY|BEPC|Brookfield Renewable Corporation Class A
        Subordinate Voting Shares |N| |N|100|N||BEPC|BEPC|N\r\nY|BEPH|Brookfield BRP
        Holdings (Canada) Inc. 4.625% Perpetual Subordinated Notes|N| |N|100|N||BEPH|BEPH|N\r\nY|BEPI|Brookfield
        BRP Holdings (Canada) Inc. 4.875% Perpetual Subordinated Notes|N| |N|100|N||BEPI|BEPI|N\r\nY|BEPJ|Brookfield
        BRP Holdings (Canada) Inc. 7.250% Perpetual Subordinated Notes|N| |N|100|N||BEPJ|BEPJ|N\r\nY|BERY|Berry
        Global Group, Inc. Common Stock|N| |N|100|N||BERY|BERY|N\r\nY|BERZ|MicroSectors
        FANG & Innovation -3x Inverse Leveraged ETN|P| |Y|100|N||BERZ|BERZ|N\r\nY|BEST|BEST
        Inc. American Depositary Shares, each representing twenty (20) Class A Ordinary
        Shares|N| |N|100|N||BEST|BEST|N\r\nY|BETE|ProShares Trust ProShares Bitcoin
        & Ether Equal Weight Strategy ETF|P| |Y|100|N||BETE|BETE|N\r\nY|BETH|ProShares
        Trust ProShares Bitcoin & Ether Market Cap Weight Strategy ETF|P| |Y|100|N||BETH|BETH|N\r\nY|BETR|Better
        Home & Finance Holding Company - Class A Common Stock|Q|S|N|100|N|D||BETR|N\r\nY|BETRW|Better
        Home & Finance Holding Company - Warrant|Q|S|N|100|N|N||BETRW|N\r\nY|BETZ|Roundhill
        Sports Betting & iGaming ETF|P| |Y|100|N||BETZ|BETZ|N\r\nY|BF.A|Brown Forman
        Inc Class A Common Stock|N| |N|100|N||BF.A|BF.A|N\r\nY|BF.B|Brown Forman Inc
        Class B Common Stock|N| |N|100|N||BF.B|BF.B|N\r\nY|BFAC|Battery Future Acquisition
        Corp. Class A Ordinary Shares|N| |N|100|N||BFAC|BFAC|N\r\nY|BFAC.U|Battery
        Future Acquisition Corp. Units, each consisting of one Class A ordinary share
        and one-half of one redeemable warrant|N| |N|100|N||BFAC.U|BFAC=|N\r\nY|BFAC.W|Battery
        Future Acquisition Corp. Warrants, each whole warrant exercisable for one
        Class A ordinary share at an exercise price of $11.50 per share|N| |N|100|N||BFAC.WS|BFAC+|N\r\nY|BFAM|Bright
        Horizons Family Solutions Inc. Common Stock|N| |N|100|N||BFAM|BFAM|N\r\nY|BFC|Bank
        First Corporation - Common Stock|Q|S|N|100|N|N||BFC|N\r\nY|BFEB|Innovator
        U.S. Equity Buffer ETF - February|Z| |Y|100|N||BFEB|BFEB|N\r\nY|BFH|Bread
        Financial Holdings, Inc. Common Stock|N| |N|100|N||BFH|BFH|N\r\nY|BFI|BurgerFi
        International Inc - Common Stock|Q|G|N|100|N|D||BFI|N\r\nY|BFIIW|BurgerFi
        International Inc - Warrant|Q|G|N|100|N|N||BFIIW|N\r\nY|BFIN|BankFinancial
        Corporation - Common Stock|Q|Q|N|100|N|N||BFIN|N\r\nY|BFIX|Build Funds Trust
        Build Bond Innovation ETF|P| |Y|100|N||BFIX|BFIX|N\r\nY|BFK|BlackRock Municipal
        Income Trust|N| |N|100|N||BFK|BFK|N\r\nY|BFLY|Butterfly Network, Inc. Class
        A Common Stock|N| |N|100|N||BFLY|BFLY|N\r\nY|BFLY.W|Butterfly Network, Inc.
        Warrants|N| |N|100|N||BFLY.WS|BFLY+|N\r\nY|BFOR|Barron's 400|P| |Y|100|N||BFOR|BFOR|N\r\nY|BFRG|Bullfrog
        AI Holdings, Inc. - Common Stock|Q|S|N|100|N|N||BFRG|N\r\nY|BFRGW|Bullfrog
        AI Holdings, Inc. - Warrants|Q|S|N|100|N|N||BFRGW|N\r\nY|BFRI|Biofrontera
        Inc. - Common Stock|Q|S|N|100|N|N||BFRI|N\r\nY|BFRIW|Biofrontera Inc. - Warrants|Q|S|N|100|N|N||BFRIW|N\r\nY|BFS|Saul
        Centers, Inc. Common Stock|N| |N|100|N||BFS|BFS|N\r\nY|BFS$D|Saul Centers,
        Inc. Depositary Shares, each representing 1/100th of a share of 6.125% Series
        D Cumulative Redeemable Preferred Stock|N| |N|100|N||BFSpD|BFS-D|N\r\nY|BFS$E|Saul
        Centers, Inc. Depositary shares, each representing a 1/100th fractional interest
        in a share of 6.000% Series E Cumulative Redeemable Preferred Stock|N| |N|100|N||BFSpE|BFS-E|N\r\nY|BFST|Business
        First Bancshares, Inc. - Common Stock|Q|Q|N|100|N|N||BFST|N\r\nY|BFZ|BlackRock
        California Municipal Income Trust|N| |N|100|N||BFZ|BFZ|N\r\nY|BG|Bunge Limited
        Common Shares|N| |N|100|N||BG|BG|N\r\nY|BGB|Blackstone Strategic Credit 2027
        Term Fund Common Shares of Beneficial Interest|N| |N|100|N||BGB|BGB|N\r\nY|BGC|BGC
        Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||BGC|N\r\nY|BGFV|Big 5 Sporting
        Goods Corporation - Common Stock|Q|Q|N|100|N|N||BGFV|N\r\nY|BGH|Barings Global
        Short Duration High Yield Fund Common Shares of Beneficial Interests|N| |N|100|N||BGH|BGH|N\r\nY|BGI|Birks
        Group Inc. Common Stock|A| |N|100|N||BGI|BGI|N\r\nY|BGIG|ETF Series Solutions
        Bahl & Gaynor Income Growth ETF|P| |Y|100|N||BGIG|BGIG|N\r\nY|BGLC|BioNexus
        Gene Lab Corp - Common stock|Q|S|N|100|N|D||BGLC|N\r\nY|BGLD|FT Vest Gold
        Strategy Quarterly Buffer ETF|Z| |Y|100|N||BGLD|BGLD|N\r\nY|BGNE|BeiGene,
        Ltd. - American Depositary Shares|Q|Q|N|100|N|N||BGNE|N\r\nY|BGR|BlackRock
        Energy and Resources Trust|N| |N|100|N||BGR|BGR|N\r\nY|BGRN|iShares USD Green
        Bond ETF|Q|G|Y|100|N|N||BGRN|N\r\nY|BGRO|BlackRock Large Cap Growth ETF|Q|G|Y|100|N|N||BGRO|N\r\nY|BGS|B&G
        Foods, Inc. Common Stock|N| |N|100|N||BGS|BGS|N\r\nY|BGSF|BGSF, Inc. Common
        Stock|N| |N|100|N||BGSF|BGSF|N\r\nY|BGT|BlackRock Floating Rate Income Trust|N|
        |N|100|N||BGT|BGT|N\r\nY|BGX|Blackstone Long Short Credit Income Fund Common
        Shares|N| |N|100|N||BGX|BGX|N\r\nY|BGXX|Bright Green Corporation - Common
        Stock|Q|S|N|100|N|D||BGXX|N\r\nY|BGY|Blackrock Enhanced International Dividend
        Trust|N| |N|100|N||BGY|BGY|N\r\nY|BH|Biglari Holdings Inc. Class B Common
        Stock|N| |N|10|N||BH|BH|N\r\nY|BH.A|Biglari Holdings Inc. Class A Common Stock|N|
        |N|10|N||BH.A|BH.A|N\r\nY|BHAC|Focus Impact BH3 Acquisition Company - Class
        A Common Stock|Q|G|N|100|N|N||BHAC|N\r\nY|BHACU|Focus Impact BH3 Acquisition
        Company - Units|Q|G|N|100|N|N||BHACU|N\r\nY|BHACW|Focus Impact BH3 Acquisition
        Company - Warrants|Q|G|N|100|N|N||BHACW|N\r\nY|BHAT|Blue Hat Interactive Entertainment
        Technology - Ordinary Shares|Q|S|N|100|N|N||BHAT|N\r\nY|BHB|Bar Harbor Bankshares,
        Inc. Common Stock|A| |N|100|N||BHB|BHB|N\r\nY|BHC|Bausch Health Companies
        Inc. Common Stock|N| |N|100|N||BHC|BHC|N\r\nY|BHE|Benchmark Electronics, Inc.
        Common Stock|N| |N|100|N||BHE|BHE|N\r\nY|BHF|Brighthouse Financial, Inc. -
        Common Stock|Q|Q|N|100|N|N||BHF|N\r\nY|BHFAL|Brighthouse Financial, Inc. -
        Junior Subordinated Debentures due 2058|Q|Q|N|100|N|N||BHFAL|N\r\nY|BHFAM|Brighthouse
        Financial, Inc. - Depositary shares each representing a 1/1,000th Interest
        in a Share of 4.625% Non-Cumulative Preferred Stock, Series D|Q|Q|N|100|N|N||BHFAM|N\r\nY|BHFAN|Brighthouse
        Financial, Inc. - depositary shares, each representing a 1/1,000th interest
        in a share of 5.375% Non-Cumulative Preferred Stock, Series C|Q|Q|N|100|N|N||BHFAN|N\r\nY|BHFAO|Brighthouse
        Financial, Inc. - Depositary Shares, each representing a 1/1,000th interest
        in a share of 6.750% Non-Cumulative Preferred Stock, Series B|Q|Q|N|100|N|N||BHFAO|N\r\nY|BHFAP|Brighthouse
        Financial, Inc. - Depositary Shares 6.6% Non-Cumulative Preferred Stock, Series
        A|Q|Q|N|100|N|N||BHFAP|N\r\nY|BHIL|Benson Hill, Inc. Common Stock|N| |N|100|N||BHIL|BHIL|N\r\nY|BHK|Blackrock
        Core Bond Trust|N| |N|100|N||BHK|BHK|N\r\nY|BHLB|Berkshire Hills Bancorp,
        Inc. Common Stock|N| |N|100|N||BHLB|BHLB|N\r\nY|BHM|Bluerock Homes Trust,
        Inc. Class A Common Stock|A| |N|100|N||BHM|BHM|N\r\nY|BHP|BHP Group Limited
        American Depositary Shares (Each representing two Ordinary Shares)|N| |N|100|N||BHP|BHP|N\r\nY|BHR|Braemar
        Hotels & Resorts Inc. Common Stock|N| |N|100|N||BHR|BHR|N\r\nY|BHR$B|Braemar
        Hotels & Resorts Inc. 5.50% Series B Cumulative Convertible Preferred Stock,
        par value $0.01 per share|N| |N|100|N||BHRpB|BHR-B|N\r\nY|BHR$D|Braemar Hotels
        & Resorts Inc. 8.25% Series D Cumulative Preferred Stock,  par value $0.01
        per share|N| |N|100|N||BHRpD|BHR-D|N\r\nY|BHRB|Burke & Herbert Financial Services
        Corp. - Common Stock|Q|S|N|100|N|N||BHRB|N\r\nY|BHV|BlackRock Virginia Municipal
        Bond Trust|N| |N|100|N||BHV|BHV|N\r\nY|BHVN|Biohaven Ltd. Common Shares |N|
        |N|100|N||BHVN|BHVN|N\r\nY|BHYB|DBX ETF Trust Xtrackers USD High Yield BB-B
        ex Financials ETF|Z| |Y|100|N||BHYB|BHYB|N\r\nY|BIAF|bioAffinity Technologies,
        Inc. - Common Stock|Q|S|N|100|N|N||BIAF|N\r\nY|BIAFW|bioAffinity Technologies,
        Inc. - Warrant|Q|S|N|100|N|N||BIAFW|N\r\nY|BIB|ProShares Ultra Nasdaq Biotechnology|Q|G|Y|100|N|N||BIB|N\r\nY|BIBL|Inspire
        100 ETF|P| |Y|100|N||BIBL|BIBL|N\r\nY|BIDU|Baidu, Inc. - American Depositary
        Shares, each representing 8 ordinary share|Q|Q|N|100|N|N||BIDU|N\r\nY|BIG|Big
        Lots, Inc. Common Stock|N| |N|100|N||BIG|BIG|N\r\nY|BIGC|BigCommerce Holdings,
        Inc. - Series 1 Common Stock|Q|G|N|100|N|N||BIGC|N\r\nY|BIGZ|BlackRock Innovation
        and Growth Term Trust Common Shares of Beneficial Interest|N| |N|100|N||BIGZ|BIGZ|N\r\nY|BIIB|Biogen
        Inc. - Common Stock|Q|Q|N|100|N|N||BIIB|N\r\nY|BIL|SPDR Bloomberg 1-3 Month
        T-Bill ETF|P| |Y|100|N||BIL|BIL|N\r\nY|BILD|Macquarie ETF Trust Macquarie
        Global Listed Infrastructure ETF|P| |Y|100|N||BILD|BILD|N\r\nY|BILI|Bilibili
        Inc. - American Depositary Shares|Q|Q|N|100|N|N||BILI|N\r\nY|BILL|BILL Holdings,
        Inc. Common Stock|N| |N|100|N||BILL|BILL|N\r\nY|BILS|SPDR Bloomberg 3-12 Month
        T-Bill ETF|P| |Y|100|N||BILS|BILS|N\r\nY|BILZ|PIMCO U.S. Treasury Index Fund
        PIMCO Ultra Short Government Active Exchange-Traded Fund|P| |Y|100|N||BILZ|BILZ|N\r\nY|BIMI|BIMI
        International Medical Inc. - Common Stock|Q|S|N|100|N|E||BIMI|N\r\nY|BINC|BlackRock
        ETF Trust II BlackRock Flexible Income ETF|P| |Y|100|N||BINC|BINC|N\r\nY|BINV|Brandes
        International ETF Brandes International ETF|Z| |Y|100|N||BINV|BINV|N\r\nY|BIO|Bio-Rad
        Laboratories, Inc. Class A Common Stock|N| |N|100|N||BIO|BIO|N\r\nY|BIO.B|Bio-Rad
        Laboratories, Inc. Class B  Common Stock|N| |N|100|N||BIO.B|BIO.B|N\r\nY|BIOR|Biora
        Therapeutics, Inc.  - Common Stock|Q|G|N|100|N|D||BIOR|N\r\nY|BIOX|Bioceres
        Crop Solutions Corp. - Ordinary Shares|Q|Q|N|100|N|N||BIOX|N\r\nY|BIP|Brookfield
        Infrastructure Partners LP Limited Partnership Units|N| |N|100|N||BIP|BIP|N\r\nY|BIP$A|Brookfield
        Infrastructure Partners LP 5.125% Class A Preferred Limited Partnership Units,
        Series 13|N| |N|100|N||BIPpA|BIP-A|N\r\nY|BIP$B|Brookfield Infrastructure
        Partners LP 5.000% Class A Preferred Limited Partnership Units, Series 14|N|
        |N|100|N||BIPpB|BIP-B|N\r\nY|BIPC|Brookfield Infrastructure Corporation |N|
        |N|100|N||BIPC|BIPC|N\r\nY|BIPH|Brookfield Infrastructure Corporation 5.000%
        Subordinated Notes due 2081|N| |N|100|N||BIPH|BIPH|N\r\nY|BIPI|BIP Bermuda
        Holdings I Limited 5.125% Perpetual Subordinated Notes|N| |N|100|N||BIPI|BIPI|N\r\nY|BIPJ|Brookfield
        Infrastructure Corporation 7.250% Subordinated Notes due 2084|N| |N|100|N||BIPJ|BIPJ|N\r\nY|BIRD|Allbirds,
        Inc. - Class A Common Stock|Q|Q|N|100|N|D||BIRD|N\r\nY|BIRK|Birkenstock Holding
        plc Ordinary Shares|N| |N|100|N||BIRK|BIRK|N\r\nY|BIS|ProShares UltraShort
        Nasdaq Biotechnology|Q|G|Y|100|N|N||BIS|N\r\nY|BIT|BlackRock Multi-Sector
        Income Trust Common Shares of Beneficial Interest|N| |N|100|N||BIT|BIT|N\r\nY|BITB|Bitwise
        Bitcoin ETF Common Shares of Beneficial Interest|P| |Y|100|N||BITB|BITB|N\r\nY|BITC|Bitwise
        Funds Trust Bitwise Bitcoin Strategy Optimum Roll ETF|P| |Y|100|N||BITC|BITC|N\r\nY|BITE|Bite
        Acquisition Corp. Common Stock|A| |N|100|N||BITE|BITE|N\r\nY|BITE.U|Bite Acquisition
        Corp. Units, each consisting of one share of common stock and one-half of
        one redeemable warrant|A| |N|100|N||BITE.U|BITE=|N\r\nY|BITE.W|Bite Acquisition
        Corp. Warrants, each whole warrant exercisable for one share of common stock
        at an exercise price of $11.50|A| |N|100|N||BITE.WS|BITE+|N\r\nY|BITF|Bitfarms
        Ltd. - Common Stock|Q|G|N|100|N|N||BITF|N\r\nY|BITI|ProShares Trust ProShares
        Short Bitcoin Strategy ETF|P| |Y|100|N||BITI|BITI|N\r\nY|BITO|ProShares Bitcoin
        Strategy ETF|P| |Y|100|N||BITO|BITO|N\r\nY|BITQ|Bitwise Crypto Industry Innovators
        ETF|P| |Y|100|N||BITQ|BITQ|N\r\nY|BITS|Global X Blockchain & Bitcoin Strategy
        ETF|Q|G|Y|100|N|N||BITS|N\r\nY|BITU|ProShares Trust ProShares Ultra Bitcoin
        ETF|P| |Y|100|N||BITU|BITU|N\r\nY|BITX|Volatility Shares Trust 2x Bitcoin
        Strategy ETF|Z| |Y|100|N||BITX|BITX|N\r\nY|BIV|Vanguard Intermediate-Term
        Bond ETF|P| |Y|100|N||BIV|BIV|N\r\nY|BIVI|BioVie Inc. - Common stock|Q|S|N|100|N|D||BIVI|N\r\nY|BIZD|VanEck
        BDC Income ETF |P| |Y|100|N||BIZD|BIZD|N\r\nY|BJ|BJ's Wholesale Club Holdings,
        Inc. Common Stock|N| |N|100|N||BJ|BJ|N\r\nY|BJAN|Innovator U.S. Equity Buffer
        ETF - January|Z| |Y|100|N||BJAN|BJAN|N\r\nY|BJDX|Bluejay Diagnostics, Inc.
        - Common Stock|Q|S|N|100|N|D||BJDX|N\r\nY|BJK|VanEck Gaming ETF|Q|G|Y|100|N|N||BJK|N\r\nY|BJRI|BJ's
        Restaurants, Inc. - Common Stock|Q|Q|N|100|N|N||BJRI|N\r\nY|BJUL|Innovator
        U.S. Equity Buffer ETF - July|Z| |Y|100|N||BJUL|BJUL|N\r\nY|BJUN|Innovator
        U.S. Equity Buffer ETF - June|Z| |Y|100|N||BJUN|BJUN|N\r\nY|BK|The Bank of
        New York Mellon Corporation Common Stock|N| |N|100|N||BK|BK|N\r\nY|BKAG|BNY
        Mellon Core Bond ETF|P| |Y|100|N||BKAG|BKAG|N\r\nY|BKCH|Global X Blockchain
        ETF|Q|G|Y|100|N|N||BKCH|N\r\nY|BKCI|BNY Mellon ETF Trust BNY Mellon Concentrated
        International ETF|P| |Y|100|N||BKCI|BKCI|N\r\nY|BKD|Brookdale Senior Living
        Inc. Common Stock|N| |N|100|N||BKD|BKD|N\r\nY|BKDT|Brookdale Senior Living
        Inc. 7.00% Tangible Equity Units|N| |N|100|N||BKDT|BKDT|N\r\nY|BKE|Buckle,
        Inc. (The) Common Stock|N| |N|100|N||BKE|BKE|N\r\nY|BKEM|BNY Mellon Emerging
        Markets Equity ETF|P| |Y|100|N||BKEM|BKEM|N\r\nY|BKF|iShares MSCI BIC ETF|P|
        |Y|100|N||BKF|BKF|N\r\nY|BKGI|BNY Mellon ETF Trust BNY Mellon Global Infrastructure
        Income ETF|Z| |Y|100|N||BKGI|BKGI|N\r\nY|BKH|Black Hills Corporation Common
        Stock|N| |N|100|N||BKH|BKH|N\r\nY|BKHA|Black Hawk Acquisition Corporation
        - Class A Ordinary Shares|Q|G|N|100|N|N||BKHA|N\r\nY|BKHAR|Black Hawk Acquisition
        Corporation - Rights|Q|G|N|100|N|N||BKHAR|N\r\nY|BKHAU|Black Hawk Acquisition
        Corporation - Units|Q|G|N|100|N|N||BKHAU|N\r\nY|BKHY|BNY Mellon High Yield
        Beta ETF|P| |Y|100|N||BKHY|BKHY|N\r\nY|BKIE|BNY Mellon International Equity
        ETF|P| |Y|100|N||BKIE|BKIE|N\r\nY|BKIV|BNY Mellon Innovators ETF|Q|G|Y|100|N|N||BKIV|N\r\nY|BKKT|Bakkt
        Holdings, Inc. Class A Common Stock|N| |N|100|N||BKKT|BKKT|N\r\nY|BKKT.W|Bakkt
        Holdings, Inc. Warrant|N| |N|100|N||BKKT.WS|BKKT+|N\r\nY|BKLC|BNY Mellon US
        Large Cap Core Equity ETF|P| |Y|100|N||BKLC|BKLC|N\r\nY|BKLN|Invesco Senior
        Loan ETF|P| |Y|100|N||BKLN|BKLN|N\r\nY|BKMC|BNY Mellon US Mid Cap Core Equity
        ETF|P| |Y|100|N||BKMC|BKMC|N\r\nY|BKN|BlackRock Investment Quality Municipal
        Trust Inc. (The)|N| |N|100|N||BKN|BKN|N\r\nY|BKNG|Booking Holdings Inc. -
        Common Stock|Q|Q|N|100|N|N||BKNG|N\r\nY|BKR|Baker Hughes Company - Common
        Stock|Q|Q|N|100|N|N||BKR|N\r\nY|BKSE|BNY Mellon US Small Cap Core Equity ETF|P|
        |Y|100|N||BKSE|BKSE|N\r\nY|BKSY|BlackSky Technology Inc. Class A Common Stock|N|
        |N|100|N||BKSY|BKSY|N\r\nY|BKSY.W|BlackSky Technology Inc. Redeemable Warrants,
        each whole Warrant exercisable for one share of Class A Common Stock|N| |N|100|N||BKSY.WS|BKSY+|N\r\nY|BKT|BlackRock
        Income Trust Inc. (The)|N| |N|100|N||BKT|BKT|N\r\nY|BKTI|BK Technologies Corporation
        Common Stock|A| |N|100|N||BKTI|BKTI|N\r\nY|BKU|BankUnited, Inc. Common Stock|N|
        |N|100|N||BKU|BKU|N\r\nY|BKUI|BNY Mellon Ultra Short Income ETF|P| |Y|100|N||BKUI|BKUI|N\r\nY|BKWO|BNY
        Mellon Women's Opportunities ETF|Q|G|Y|100|N|N||BKWO|N\r\nY|BKYI|BIO-key International,
        Inc. - Common Stock|Q|S|N|100|N|D||BKYI|N\r\nY|BL|BlackLine, Inc. - Common
        Stock|Q|Q|N|100|N|N||BL|N\r\nY|BLAC|Bellevue Life Sciences Acquisition Corp.
        - Common Stock|Q|S|N|100|N|D||BLAC|N\r\nY|BLACR|Bellevue Life Sciences Acquisition
        Corp. - Rights|Q|S|N|100|N|D||BLACR|N\r\nY|BLACU|Bellevue Life Sciences Acquisition
        Corp. - Unit|Q|S|N|100|N|D||BLACU|N\r\nY|BLACW|Bellevue Life Sciences Acquisition
        Corp. - Warrant|Q|S|N|100|N|D||BLACW|N\r\nY|BLBD|Blue Bird Corporation - Common
        Stock|Q|G|N|100|N|N||BLBD|N\r\nY|BLBX|Blackboxstocks Inc. - Common Stock|Q|S|N|100|N|N||BLBX|N\r\nY|BLCN|Siren
        Nasdaq NexGen Economy ETF|Q|G|Y|100|N|N||BLCN|N\r\nY|BLCO|Bausch + Lomb Corporation
        Common Shares|N| |N|100|N||BLCO|BLCO|N\r\nY|BLCR|BlackRock Large Cap Core
        ETF|Q|G|Y|100|N|N||BLCR|N\r\nY|BLCV|BlackRock ETF Trust BlackRock Large Cap
        Value ETF|P| |Y|100|N||BLCV|BLCV|N\r\nY|BLD|TopBuild Corp. Common Stock|N|
        |N|100|N||BLD|BLD|N\r\nY|BLDE|Blade Air Mobility, Inc. - Class A Common Stock|Q|S|N|100|N|N||BLDE|N\r\nY|BLDEW|Blade
        Air Mobility, Inc. - Warrants|Q|S|N|100|N|N||BLDEW|N\r\nY|BLDG|Cambria Global
        Real Estate ETF|Z| |Y|100|N||BLDG|BLDG|N\r\nY|BLDP|Ballard Power Systems,
        Inc. - Common Shares|Q|G|N|100|N|N||BLDP|N\r\nY|BLDR|Builders FirstSource,
        Inc. Common Stock|N| |N|100|N||BLDR|BLDR|N\r\nY|BLE|BlackRock Municipal Income
        Trust II|N| |N|100|N||BLE|BLE|N\r\nY|BLES|Inspire Global Hope ETF|P| |Y|100|N||BLES|BLES|N\r\nY|BLEU|bleuacacia
        ltd - Class A Ordinary Shares|Q|S|N|100|N|N||BLEU|N\r\nY|BLEUR|bleuacacia
        ltd - Rights|Q|S|N|100|N|N||BLEUR|N\r\nY|BLEUU|bleuacacia ltd - Units|Q|S|N|100|N|N||BLEUU|N\r\nY|BLEUW|bleuacacia
        ltd - Warrants|Q|S|N|100|N|N||BLEUW|N\r\nY|BLFS|BioLife Solutions, Inc. -
        Common Stock|Q|S|N|100|N|N||BLFS|N\r\nY|BLFY|Blue Foundry Bancorp - Common
        Stock|Q|Q|N|100|N|N||BLFY|N\r\nY|BLIN|Bridgeline Digital, Inc. - Common Stock|Q|S|N|100|N|N||BLIN|N\r\nY|BLK|BlackRock,
        Inc. Common Stock|N| |N|100|N||BLK|BLK|N\r\nY|BLKB|Blackbaud, Inc. - Common
        Stock|Q|Q|N|100|N|N||BLKB|N\r\nY|BLKC|Invesco Alerian Galaxy Blockchain Users
        and Decentralized Commerce ETF|Z| |Y|100|N||BLKC|BLKC|N\r\nY|BLLD|JPMorgan
        Sustainable Infrastructure ETF|Q|G|Y|100|N|N||BLLD|N\r\nY|BLMN|Bloomin' Brands,
        Inc. - Common Stock|Q|Q|N|100|N|N||BLMN|N\r\nY|BLND|Blend Labs, Inc. Class
        A Common Stock|N| |N|100|N||BLND|BLND|N\r\nY|BLNK|Blink Charging Co. - Common
        Stock|Q|S|N|100|N|N||BLNK|N\r\nY|BLOK|Amplify Transformational Data Sharing
        ETF|P| |Y|100|N||BLOK|BLOK|N\r\nY|BLRX|BioLineRx Ltd. - American Depositary
        Shares|Q|S|N|100|N|D||BLRX|N\r\nY|BLTE|Belite Bio, Inc - American Depositary
        Shares|Q|S|N|100|N|N||BLTE|N\r\nY|BLUA|BlueRiver Acquisition Corp. Class A
        Ordinary Shares|A| |N|100|N||BLUA|BLUA|N\r\nY|BLUA.U|BlueRiver Acquisition
        Corp. Units, each consisting of one Class A ordinary share, and one-third
        of a redeemable Warrant to acquire one Class A ordinary shares|A| |N|100|N||BLUA.U|BLUA=|N\r\nY|BLUA.W|BlueRiver
        Acquisition Corp. Warrants, each whole warrant exercisable for one Class A
        Ordinary Share at an exercise price of $11.50|A| |N|100|N||BLUA.WS|BLUA+|N\r\nY|BLUE|bluebird
        bio, Inc. - Common Stock|Q|Q|N|100|N|E||BLUE|N\r\nY|BLV|Vanguard Long-Term
        Bond ETF|P| |Y|100|N||BLV|BLV|N\r\nY|BLW|Blackrock Limited Duration Income
        Trust|N| |N|100|N||BLW|BLW|N\r\nY|BLX|Banco Latinoamericano de Comercio Exterior,
        S.A.|N| |N|100|N||BLX|BLX|N\r\nY|BLZE|Backblaze, Inc. - Class A Common Stock|Q|G|N|100|N|N||BLZE|N\r\nY|BMA|Banco
        Macro S.A.  ADR (representing Ten Class B Common Shares)|N| |N|100|N||BMA|BMA|N\r\nY|BMAR|Innovator
        U.S. Equity Buffer ETF - March|Z| |Y|100|N||BMAR|BMAR|N\r\nY|BMAY|Innovator
        U.S. Equity Buffer ETF - May|Z| |Y|100|N||BMAY|BMAY|N\r\nY|BMBL|Bumble Inc.
        - common stock|Q|Q|N|100|N|N||BMBL|N\r\nY|BMDL|VictoryShares WestEnd Economic
        Cycle Bond ETF|Q|G|Y|100|N|N||BMDL|N\r\nY|BME|Blackrock Health Sciences Trust|N|
        |N|100|N||BME|BME|N\r\nY|BMEA|Biomea Fusion, Inc. - Common Stock|Q|Q|N|100|N|N||BMEA|N\r\nY|BMED|BlackRock
        Future Health ETF|P| |Y|100|N||BMED|BMED|N\r\nY|BMEZ|BlackRock Health Sciences
        Term Trust Common Shares of Beneficial Interest|N| |N|100|N||BMEZ|BMEZ|N\r\nY|BMI|Badger
        Meter, Inc. Common Stock|N| |N|100|N||BMI|BMI|N\r\nY|BML$G|Bank of America
        Corporation Depositary Shares (Each representing a 1/1200th interest in a
        share of Floating Rate Non-Cumulative Preferred Stock , Series 1)|N| |N|100|N||BMLpG|BML-G|N\r\nY|BML$H|Bank
        of America Corporation Depositary Shares (Each representing a 1/1200th interest
        in a Share of Floating Rate Non-Cumulative Preferred Stock, Series 2)|N| |N|100|N||BMLpH|BML-H|N\r\nY|BML$J|Bank
        of America Corporation Depositary Shares (Each representing a 1/1200th interest
        in a Share of Floating Rate Non-Cumulative Preferred Stock, Series 4)|N| |N|100|N||BMLpJ|BML-J|N\r\nY|BML$L|Bank
        of America Corporation Depositary Shares (Each representing a 1/1200th Interest
        in a Share of Floating Rate Non-Cumulative Preferred Stock, Series 5)|N| |N|100|N||BMLpL|BML-L|N\r\nY|BMN|BlackRock
        2037 Municipal Target Term Trust Common Shares of Beneficial Interest|N| |N|100|N||BMN|BMN|N\r\nY|BMO|Bank
        Of Montreal Common Stock|N| |N|100|N||BMO|BMO|N\r\nY|BMR|Beamr Imaging Ltd.
        - Ordinary Share|Q|S|N|100|N|N||BMR|N\r\nY|BMRA|Biomerica, Inc. - Common Stock|Q|S|N|100|N|D||BMRA|N\r\nY|BMRC|Bank
        of Marin Bancorp - Common Stock|Q|S|N|100|N|N||BMRC|N\r\nY|BMRN|BioMarin Pharmaceutical
        Inc. - Common Stock|Q|Q|N|100|N|N||BMRN|N\r\nY|BMTX|BM Technologies, Inc.
        Common Stock|A| |N|100|N||BMTX|BMTX|N\r\nY|BMTX.W|BM Technologies, Inc. Warrants|A|
        |N|100|N||BMTX.WS|BMTX+|N\r\nY|BMVP|Invesco Bloomberg MVP Multi-factor ETF|P|
        |Y|100|N||BMVP|BMVP|N\r\nY|BMY|Bristol-Myers Squibb Company Common Stock|N|
        |N|100|N||BMY|BMY|N\r\nY|BN|Brookfield Corporation Class A Limited Voting
        Shares|N| |N|100|N||BN|BN|N\r\nY|BNAI|Brand Engagement Network Inc. - Common
        Stock|Q|S|N|100|N|N||BNAI|N\r\nY|BNAIW|Brand Engagement Network Inc. - Warrant|Q|S|N|100|N|N||BNAIW|N\r\nY|BND|Vanguard
        Total Bond Market ETF|Q|G|Y|100|N|N||BND|N\r\nY|BNDC|FlexShares Core Select
        Bond Fund|P| |Y|100|N||BNDC|BNDC|N\r\nY|BNDD|Quadratic Deflation ETF|P| |Y|100|N||BNDD|BNDD|N\r\nY|BNDI|NEOS
        ETF Trust NEOS Enhanced Income Aggregate Bond ETF|P| |Y|100|N||BNDI|BNDI|N\r\nY|BNDW|Vanguard
        Total World Bond ETF|Q|G|Y|100|N|N||BNDW|N\r\nY|BNDX|Vanguard Total International
        Bond ETF|Q|G|Y|100|N|N||BNDX|N\r\nY|BNE|ETF Series Solutions Blue Horizon
        BNE ETF|P| |Y|100|N||BNE|BNE|N\r\nY|BNED|Barnes & Noble Education, Inc Common
        Stock|N| |N|100|N||BNED|BNED|N\r\nY|BNGE|First Trust S-Network Streaming and
        Gaming ETF|P| |Y|100|N||BNGE|BNGE|N\r\nY|BNGO|Bionano Genomics, Inc. - Common
        Stock|Q|S|N|100|N|N||BNGO|N\r\nY|BNH|Brookfield Finance Inc. 4.625% Subordinated
        Notes due October 16, 2080|N| |N|100|N||BNH|BNH|N\r\nY|BNIX|Bannix Acquisition
        Corp. - Common Stock|Q|S|N|100|N|E||BNIX|N\r\nY|BNIXR|Bannix Acquisition Corp.
        - Right|Q|S|N|100|N|E||BNIXR|N\r\nY|BNIXW|Bannix Acquisition Corp. - Warrant|Q|S|N|100|N|E||BNIXW|N\r\nY|BNJ|Brookfield
        Finance Inc. 4.50% Perpetual Subordinated Notes|N| |N|100|N||BNJ|BNJ|N\r\nY|BNKD|MicroSectors
        U.S. Big Banks Index -3X Inverse Leveraged ETNs|P| |N|100|N||BNKD|BNKD|N\r\nY|BNKU|MicroSectors
        U.S. Big Banks Index 3X Leveraged ETNs|P| |N|100|N||BNKU|BNKU|N\r\nY|BNL|Broadstone
        Net Lease, Inc. Common Stock|N| |N|100|N||BNL|BNL|N\r\nY|BNO|United States
        Brent Oil Fund, LP ETV|P| |Y|100|N||BNO|BNO|N\r\nY|BNOV|Innovator U.S. Equity
        Buffer ETF - November|Z| |Y|100|N||BNOV|BNOV|N\r\nY|BNOX|Bionomics Limited
        - American Depository Shares|Q|G|N|100|N|N||BNOX|N\r\nY|BNR|Burning Rock Biotech
        Limited - American Depositary Shares|Q|G|N|100|N|N||BNR|N\r\nY|BNRE|Brookfield
        Reinsurance Ltd. Class A Exchangeable Limited Voting Shares|N| |N|100|N||BNRE|BNRE|N\r\nY|BNRE.A|Brookfield
        Reinsurance Ltd. Class A-1 Exchangeable Non-Voting Shares|N| |N|100|N||BNRE.A|BNRE.A|N\r\nY|BNRG|Brenmiller
        Energy Ltd - Ordinary Shares|Q|S|N|100|N|N||BNRG|N\r\nY|BNS|Bank Nova Scotia
        Halifax Pfd 3 Ordinary Shares|N| |N|100|N||BNS|BNS|N\r\nY|BNTC|Benitec Biopharma
        Inc. - Common Stock|Q|S|N|100|N|N||BNTC|N\r\nY|BNTX|BioNTech SE - American
        Depositary Shares|Q|Q|N|100|N|N||BNTX|N\r\nY|BNY|BlackRock New York Municipal
        Income Trust|N| |N|100|N||BNY|BNY|N\r\nY|BNZI|Banzai International, Inc. -
        Class A Common Stock|Q|G|N|100|N|D||BNZI|N\r\nY|BNZIW|Banzai International,
        Inc. - Warrant|Q|S|N|100|N|N||BNZIW|N\r\nY|BOAT|SonicShares Global Shipping
        ETF|P| |Y|100|N||BOAT|BOAT|N\r\nY|BOC|Boston Omaha Corporation Class A Common
        Stock|N| |N|100|N||BOC|BOC|N\r\nY|BOCN|Blue Ocean Acquisition Corp - Class
        A Ordinary Shares|Q|G|N|100|N|N||BOCN|N\r\nY|BOCNU|Blue Ocean Acquisition
        Corp - Units|Q|G|N|100|N|N||BOCNU|N\r\nY|BOCNW|Blue Ocean Acquisition Corp
        - Warrants|Q|G|N|100|N|N||BOCNW|N\r\nY|BOCT|Innovator U.S. Equity Buffer ETF
        - October|Z| |Y|100|N||BOCT|BOCT|N\r\nY|BODI|The Beachbody Company, Inc. Class
        A Common Stock|N| |N|100|N||BODI|BODI|N\r\nY|BOE|Blackrock Enhanced Global
        Dividend Trust Common Shares of Beneficial Interest|N| |N|100|N||BOE|BOE|N\r\nY|BOF|BranchOut
        Food Inc. - Common Stock|Q|S|N|100|N|D||BOF|N\r\nY|BOH|Bank of Hawaii Corporation
        Common Stock|N| |N|100|N||BOH|BOH|N\r\nY|BOH$A|Bank of Hawaii Corporation
        Depositary Shares Each Representing a 1/40th Interest in a Share of 4.375%
        Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series A|N| |N|100|N||BOHpA|BOH-A|N\r\nY|BOH$B|Bank
        of Hawaii Corporation Depositary Shares, Each Representing a 1/40th Interest
        in a Share of 8.000% Fixed Rate Non-Cumulative Perpetual Preferred Stock,
        Series B|N| |N|100|N||BOHpB|BOH-B|N\r\nY|BOIL|ProShares Ultra Bloomberg Natural
        Gas|P| |Y|100|N||BOIL|BOIL|N\r\nY|BOKF|BOK Financial Corporation - Common
        Stock|Q|Q|N|100|N|N||BOKF|N\r\nY|BOLD|Boundless Bio, Inc. - Common Stock|Q|Q|N|100|N|N||BOLD|N\r\nY|BOLT|Bolt
        Biotherapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||BOLT|N\r\nY|BON|Bon Natural
        Life Limited - Ordinary Shares|Q|S|N|100|N|N||BON|N\r\nY|BOND|PIMCO Active
        Bond Exchange-Traded Fund Exchange-Traded Fund|N| |Y|100|N||BOND|BOND|N\r\nY|BOOM|DMC
        Global Inc. - Common Stock|Q|Q|N|100|N|N||BOOM|N\r\nY|BOOT|Boot Barn Holdings,
        Inc. Common Stock|N| |N|100|N||BOOT|BOOT|N\r\nY|BORR|Borr Drilling Limited
        Common Shares|N| |N|100|N||BORR|BORR|N\r\nY|BOSC|B.O.S. Better Online Solutions
        - Ordinary Shares|Q|S|N|100|N|N||BOSC|N\r\nY|BOTJ|Bank of the James Financial
        Group, Inc. - Common Stock|Q|S|N|100|N|N||BOTJ|N\r\nY|BOTT|Themes Robotics
        & Automation ETF|Q|G|Y|100|N|N||BOTT|N\r\nY|BOTZ|Global X Robotics & Artificial
        Intelligence ETF|Q|G|Y|100|N|N||BOTZ|N\r\nY|BOUT|Innovator IBD Breakout Opportunities
        ETF|P| |Y|100|N||BOUT|BOUT|N\r\nY|BOW|Bowhead Specialty Holdings Inc. Common
        Stock|N| |N|100|N||BOW|BOW|N\r\nY|BOWL|Bowlero Corp. Class A Common Stock|N|
        |N|100|N||BOWL|BOWL|N\r\nY|BOWN|Bowen Acquisition Corp - Ordinary Shares|Q|G|N|100|N|N||BOWN|N\r\nY|BOWNR|Bowen
        Acquisition Corp - Rights|Q|G|N|100|N|N||BOWNR|N\r\nY|BOWNU|Bowen Acquisition
        Corp - Unit|Q|G|N|100|N|N||BOWNU|N\r\nY|BOX|Box, Inc. Class A Common Stock|N|
        |N|100|N||BOX|BOX|N\r\nY|BOXL|Boxlight Corporation - Class A Common Stock|Q|S|N|100|N|D||BOXL|N\r\nY|BOXX|EA
        Series Trust Alpha Architect 1-3 Month Box ETF|Z| |Y|100|N||BOXX|BOXX|N\r\nY|BP|BP
        p.l.c. Common Stock|N| |N|100|N||BP|BP|N\r\nY|BPAY|BlackRock ETF Trust BlackRock
        Future Financial and Technology ETF|P| |Y|100|N||BPAY|BPAY|N\r\nY|BPMC|Blueprint
        Medicines Corporation - Common Stock|Q|Q|N|100|N|N||BPMC|N\r\nY|BPOP|Popular,
        Inc. - Common Stock|Q|Q|N|100|N|N||BPOP|N\r\nY|BPOPM|Popular, Inc. - Popular
        Capital Trust II - 6.125% Cumulative Monthly Income Trust Preferred Securities|Q|Q|N|100|N|N||BPOPM|N\r\nY|BPRN|Princeton
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||BPRN|N\r\nY|BPT|BP Prudhoe Bay
        Royalty Trust Common Stock|N| |N|100|N||BPT|BPT|N\r\nY|BPTH|Bio-Path Holdings,
        Inc. - Common Stock|Q|S|N|100|N|D||BPTH|N\r\nY|BPYPM|Brookfield Property Partners
        L.P. - 6.25% Class A Cumulative Redeemable Preferred Units, Series 1|Q|Q|N|100|N|N||BPYPM|N\r\nY|BPYPN|Brookfield
        Property Partners L.P. - 5.750% Class A Cumulative Redeemable Perpetual Preferred
        Units, Series 3|Q|Q|N|100|N|N||BPYPN|N\r\nY|BPYPO|Brookfield Property Partners
        L.P. - 6.375% Class A Cumulative Redeemable Perpetual Preferred Units, Series
        2|Q|Q|N|100|N|N||BPYPO|N\r\nY|BPYPP|Brookfield Property Partners L.P. - 6.50%
        Class A Cumulative Redeemable Perpetual Preferred Units|Q|Q|N|100|N|N||BPYPP|N\r\nY|BQ|Boqii
        Holding Limited American Depositary Shares, representing Class A Ordinary
        Shares|A| |N|100|N||BQ|BQ|N\r\nY|BR|Broadridge Financial Solutions, Inc. Common
        Stock|N| |N|100|N||BR|BR|N\r\nY|BRAC|Broad Capital Acquisition Corp - Common
        Stock|Q|G|N|100|N|N||BRAC|N\r\nY|BRACR|Broad Capital Acquisition Corp - Rights|Q|G|N|100|N|N||BRACR|N\r\nY|BRACU|Broad
        Capital Acquisition Corp - Units|Q|G|N|100|N|N||BRACU|N\r\nY|BRAG|Bragg Gaming
        Group Inc. - Common Shares|Q|Q|N|100|N|N||BRAG|N\r\nY|BRAZ|Global X Funds
        Global X Brazil Active ETF|P| |Y|100|N||BRAZ|BRAZ|N\r\nY|BRBR|BellRing Brands,
        Inc. Common Stock |N| |N|100|N||BRBR|BRBR|N\r\nY|BRBS|Blue Ridge Bankshares,
        Inc. Common Stock|A| |N|100|N||BRBS|BRBS|N\r\nY|BRC|Brady Corporation Common
        Stock|N| |N|100|N||BRC|BRC|N\r\nY|BRCC|BRC Inc. Class A Common Stock|N| |N|100|N||BRCC|BRCC|N\r\nY|BRDG|Bridge
        Investment Group Holdings Inc. Class A Common Stock|N| |N|100|N||BRDG|BRDG|N\r\nY|BREA|Brera
        Holdings PLC - Class B Ordinary Shares|Q|S|N|100|N|E||BREA|N\r\nY|BRF|VanEck
        Brazil Small-Cap ETF|P| |Y|100|N||BRF|BRF|N\r\nY|BRFH|Barfresh Food Group
        Inc. - Common Stock|Q|S|N|100|N|N||BRFH|N\r\nY|BRFS|BRF S.A.|N| |N|100|N||BRFS|BRFS|N\r\nY|BRHY|BlackRock
        High Yield ETF|Q|G|Y|100|N|N||BRHY|N\r\nY|BRID|Bridgford Foods Corporation
        - Common Stock|Q|G|N|100|N|N||BRID|N\r\nN|BRK.A|Berkshire Hathaway Inc. Common
        Stock|N| |N|1|N||BRK.A|BRK.A|N\r\nY|BRK.B|Berkshire Hathaway Inc. New Common
        Stock|N| |N|100|N||BRK.B|BRK.B|N\r\nY|BRKH|BurTech Acquisition Corp. - Class
        A Common Stock|Q|G|N|100|N|E||BRKH|N\r\nY|BRKHU|BurTech Acquisition Corp.
        - Unit|Q|G|N|100|N|E||BRKHU|N\r\nY|BRKHW|BurTech Acquisition Corp. - Warrants|Q|G|N|100|N|E||BRKHW|N\r\nY|BRKL|Brookline
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||BRKL|N\r\nY|BRKR|Bruker Corporation
        - Common Stock|Q|Q|N|100|N|N||BRKR|N\r\nY|BRLN|BlackRock ETF Trust II BlackRock
        Floating Rate Loan ETF|Z| |Y|100|N||BRLN|BRLN|N\r\nY|BRLS|Borealis Foods Inc.
        - Class A Common Shares|Q|S|N|100|N|N||BRLS|N\r\nY|BRLSW|Borealis Foods Inc.
        - Warrant|Q|S|N|100|N|N||BRLSW|N\r\nY|BRLT|Brilliant Earth Group, Inc. - Class
        A Common Stock|Q|G|N|100|N|N||BRLT|N\r\nY|BRN|Barnwell Industries, Inc. Common
        Stock|A| |N|100|N||BRN|BRN|N\r\nY|BRNS|Barinthus Biotherapeutics plc - American
        Depositary Shares|Q|G|N|100|N|N||BRNS|N\r\nY|BRNY|Burney U.S. Factor Rotation
        ETF|Q|G|Y|100|N|N||BRNY|N\r\nY|BRO|Brown & Brown, Inc. Common Stock|N| |N|100|N||BRO|BRO|N\r\nY|BROG|Brooge
        Energy Limited  - Ordinary Shares|Q|S|N|100|N|E||BROG|N\r\nY|BROGW|Brooge
        Energy Limited  - Warrant|Q|S|N|100|N|E||BROGW|N\r\nY|BROS|Dutch Bros Inc.
        Class A Common Stock|N| |N|100|N||BROS|BROS|N\r\nY|BRRR|Valkyrie Bitcoin Fund|Q|G|Y|100|N|N||BRRR|N\r\nY|BRSH|Bruush
        Oral Care Inc. - Common Stock|Q|S|N|100|N|H||BRSH|N\r\nY|BRSHW|Bruush Oral
        Care Inc. - Warrant|Q|S|N|100|N|H||BRSHW|N\r\nY|BRSP|BrightSpire Capital,
        Inc. Class A Common Stock|N| |N|100|N||BRSP|BRSP|N\r\nY|BRT|BRT Apartments
        Corp. (MD) Common Stock|N| |N|100|N||BRT|BRT|N\r\nY|BRTR|BlackRock Total Return
        ETF|Q|G|Y|100|N|N||BRTR|N\r\nY|BRTX|BioRestorative Therapies, Inc. - Common
        Stock|Q|S|N|100|N|N||BRTX|N\r\nY|BRW|Saba Capital Income & Opportunities Fund
        SBI|N| |N|100|N||BRW|BRW|N\r\nY|BRX|Brixmor Property Group Inc. Common Stock|N|
        |N|100|N||BRX|BRX|N\r\nY|BRY|Berry Corporation (bry) - Common Stock|Q|Q|N|100|N|N||BRY|N\r\nY|BRZE|Braze,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||BRZE|N\r\nY|BRZU|Direxion Daily
        Brazil Bull 2X Shares|P| |Y|100|N||BRZU|BRZU|N\r\nY|BSAC|Banco Santander -
        Chile ADS|N| |N|100|N||BSAC|BSAC|N\r\nY|BSBK|Bogota Financial Corp. - Common
        Stock|Q|S|N|100|N|N||BSBK|N\r\nY|BSBR|Banco Santander Brasil SA American Depositary
        Shares, each representing one unit|N| |N|100|N||BSBR|BSBR|N\r\nY|BSCO|Invesco
        BulletShares 2024 Corporate Bond ETF|Q|G|Y|100|N|N||BSCO|N\r\nY|BSCP|Invesco
        BulletShares 2025 Corporate Bond ETF|Q|G|Y|100|N|N||BSCP|N\r\nY|BSCQ|Invesco
        BulletShares 2026 Corporate Bond ETF|Q|G|Y|100|N|N||BSCQ|N\r\nY|BSCR|Invesco
        BulletShares 2027 Corporate Bond ETF|Q|G|Y|100|N|N||BSCR|N\r\nY|BSCS|Invesco
        BulletShares 2028 Corporate Bond ETF|Q|G|Y|100|N|N||BSCS|N\r\nY|BSCT|Invesco
        BulletShares 2029 Corporate Bond ETF|Q|G|Y|100|N|N||BSCT|N\r\nY|BSCU|Invesco
        BulletShares 2030 Corporate Bond ETF|Q|G|Y|100|N|N||BSCU|N\r\nY|BSCV|Invesco
        BulletShares 2031 Corporate Bond ETF|Q|G|Y|100|N|N||BSCV|N\r\nY|BSCW|Invesco
        BulletShares 2032 Corporate Bond ETF|Q|G|Y|100|N|N||BSCW|N\r\nY|BSCX|Invesco
        BulletShares 2033 Corporate Bond ETF|Q|G|Y|100|N|N||BSCX|N\r\nY|BSCY|Invesco
        BulletShares 2034 Corporate Bond ETF|Q|G|Y|100|N|N||BSCY|N\r\nY|BSEP|Innovator
        U.S. Equity Buffer ETF - September|Z| |Y|100|N||BSEP|BSEP|N\r\nY|BSET|Bassett
        Furniture Industries, Incorporated - Common Stock|Q|Q|N|100|N|N||BSET|N\r\nY|BSFC|Blue
        Star Foods Corp. - Common stock|Q|S|N|100|N|N||BSFC|N\r\nY|BSIG|BrightSphere
        Investment Group Inc. Common Stock|N| |N|100|N||BSIG|BSIG|N\r\nY|BSJO|Invesco
        BulletShares 2024 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJO|N\r\nY|BSJP|Invesco
        BulletShares 2025 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJP|N\r\nY|BSJQ|Invesco
        BulletShares 2026 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJQ|N\r\nY|BSJR|Invesco
        BulletShares 2027 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJR|N\r\nY|BSJS|Invesco
        BulletShares 2028 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJS|N\r\nY|BSJT|Invesco
        BulletShares 2029 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJT|N\r\nY|BSJU|Invesco
        BulletShares 2030 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJU|N\r\nY|BSJV|Invesco
        BulletShares 2031 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJV|N\r\nY|BSJW|Invesco
        BulletShares 2032 High Yield Corporate Bond ETF|Q|G|Y|100|N|N||BSJW|N\r\nY|BSL|Blackstone
        Senior Floating Rate 2027 Term Fund Common Shares of Beneficial Interest|N|
        |N|100|N||BSL|BSL|N\r\nY|BSM|Black Stone Minerals, L.P. Common units representing
        limited partner interests|N| |N|100|N||BSM|BSM|N\r\nY|BSMC|Brandes International
        ETF Brandes U.S. Small-Mid Cap Value ETF|Z| |Y|100|N||BSMC|BSMC|N\r\nY|BSMO|Invesco
        BulletShares 2024 Municipal Bond ETF|Q|G|Y|100|N|N||BSMO|N\r\nY|BSMP|Invesco
        BulletShares 2025 Municipal Bond ETF|Q|G|Y|100|N|N||BSMP|N\r\nY|BSMQ|Invesco
        BulletShares 2026 Municipal Bond ETF|Q|G|Y|100|N|N||BSMQ|N\r\nY|BSMR|Invesco
        BulletShares 2027 Municipal Bond ETF|Q|G|Y|100|N|N||BSMR|N\r\nY|BSMS|Invesco
        BulletShares 2028 Municipal Bond ETF|Q|G|Y|100|N|N||BSMS|N\r\nY|BSMT|Invesco
        BulletShares 2029 Municipal Bond ETF|Q|G|Y|100|N|N||BSMT|N\r\nY|BSMU|Invesco
        BulletShares 2030 Municipal Bond ETF|Q|G|Y|100|N|N||BSMU|N\r\nY|BSMV|Invesco
        BulletShares 2031 Municipal Bond ETF|Q|G|Y|100|N|N||BSMV|N\r\nY|BSMW|Invesco
        BulletShares 2032 Municipal Bond ETF|Q|G|Y|100|N|N||BSMW|N\r\nY|BSR|Northern
        Lights Fund Trust II Beacon Selective Risk ETF|P| |Y|100|N||BSR|BSR|N\r\nY|BSRR|Sierra
        Bancorp - Common Stock|Q|Q|N|100|N|N||BSRR|N\r\nY|BSSX|Invesco BulletShares
        2033 Municipal Bond ETF|Q|G|Y|100|N|N||BSSX|N\r\nY|BST|BlackRock Science and
        Technology Trust Common Shares of Beneficial Interest|N| |N|100|N||BST|BST|N\r\nY|BSTP|Innovator
        ETFs Trust Innovator Buffer Step-Up Strategy ETF|P| |Y|100|N||BSTP|BSTP|N\r\nY|BSTZ|BlackRock
        Science and Technology Term Trust Common Shares of Beneficial Interest|N|
        |N|100|N||BSTZ|BSTZ|N\r\nY|BSV|Vanguard Short-Term Bond ETF|P| |Y|100|N||BSV|BSV|N\r\nY|BSVN|Bank7
        Corp. - Common stock|Q|Q|N|100|N|N||BSVN|N\r\nY|BSVO|EA Bridgeway Omni Small-Cap
        Value ETF|Q|G|Y|100|N|N||BSVO|N\r\nY|BSX|Boston Scientific Corporation Common
        Stock|N| |N|100|N||BSX|BSX|N\r\nY|BSY|Bentley Systems, Incorporated - Class
        B Common Stock|Q|Q|N|100|N|N||BSY|N\r\nY|BTA|BlackRock Long-Term Municipal
        Advantage Trust Common Shares of Beneficial Interest|N| |N|100|N||BTA|BTA|N\r\nY|BTAI|BioXcel
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||BTAI|N\r\nY|BTAL|AGF U.S.
        Market Neutral Anti-Beta Fund|P| |Y|100|N||BTAL|BTAL|N\r\nY|BTBD|BT Brands,
        Inc. - Common Stock|Q|S|N|100|N|N||BTBD|N\r\nY|BTBDW|BT Brands, Inc. - Warrant|Q|S|N|100|N|N||BTBDW|N\r\nY|BTBT|Bit
        Digital, Inc. - Ordinary Share|Q|S|N|100|N|N||BTBT|N\r\nY|BTCM|BIT Mining
        Limited ADS|N| |N|100|N||BTCM|BTCM|N\r\nY|BTCO|Invesco Galaxy Bitcoin ETF
        Common Shares of Beneficial Interest|Z| |Y|100|N||BTCO|BTCO|N\r\nY|BTCS|BTCS
        Inc. - Common Stock|Q|S|N|100|N|N||BTCS|N\r\nY|BTCT|BTC Digital Ltd. - Ordinary
        Shares|Q|S|N|100|N|N||BTCT|N\r\nY|BTCTW|BTC Digital Ltd. - Warrant|Q|S|N|100|N|N||BTCTW|N\r\nY|BTCW|WisdomTree
        Bitcoin Fund Common Shares of Beneficial Interest|Z| |Y|100|N||BTCW|BTCW|N\r\nY|BTCY|Biotricity,
        Inc. - Common Stock|Q|S|N|100|N|D||BTCY|N\r\nY|BTDR|Bitdeer Technologies Group
        - Ordinary Shares|Q|S|N|100|N|N||BTDR|N\r\nY|BTE|Baytex Energy Corp Common
        Shares|N| |N|100|N||BTE|BTE|N\r\nY|BTEC|Principal Healthcare Innovators ETF|Q|G|Y|100|N|N||BTEC|N\r\nY|BTEK|BlackRock
        Future Tech ETF|P| |Y|100|N||BTEK|BTEK|N\r\nY|BTF|Valkyrie Bitcoin and Ether
        Strategy ETF|Q|G|Y|100|N|N||BTF|N\r\nY|BTFX|Valkyrie Bitcoin Futures Leveraged
        Strategy ETF|Q|G|Y|100|N|N||BTFX|N\r\nY|BTG|B2Gold Corp Common shares (Canada)|A|
        |N|100|N||BTG|BTG|N\r\nY|BTHM|BlackRock ETF Trust BlackRock Future U.S. Themes
        ETF|P| |Y|100|N||BTHM|BTHM|N\r\nY|BTI|British American Tobacco  Industries,
        p.l.c. Common Stock ADR|N| |N|100|N||BTI|BTI|N\r\nY|BTM|Bitcoin Depot Inc.
        - Class A Common Stock|Q|S|N|100|N|N||BTM|N\r\nY|BTMD|Biote Corp. - Class
        A common stock|Q|G|N|100|N|N||BTMD|N\r\nY|BTMWW|Bitcoin Depot Inc. - Warrant|Q|S|N|100|N|N||BTMWW|N\r\nY|BTO|John
        Hancock Financial Opportunities Fund Common Stock|N| |N|100|N||BTO|BTO|N\r\nY|BTOC|Armlogi
        Holding Corp. - common stock|Q|G|N|100|N|N||BTOC|N\r\nY|BTOG|Bit Origin Limited
        - Ordinary Shares|Q|S|N|100|N|N||BTOG|N\r\nY|BTOP|Bitwise Funds Trust Bitwise
        Bitcoin and Ether Equal Weight Strategy ETF|P| |Y|100|N||BTOP|BTOP|N\r\nY|BTR|Northern
        Lights Fund Trust II Beacon Tactical Risk ETF|P| |Y|100|N||BTR|BTR|N\r\nY|BTRN|Global
        X Funds Global X Bitcoin Trend Strategy ETF|P| |Y|100|N||BTRN|BTRN|N\r\nY|BTSG|BrightSpring
        Health Services, Inc. - Common Stock|Q|Q|N|100|N|N||BTSG|N\r\nY|BTSGU|BrightSpring
        Health Services, Inc. - Tangible Equity Unit|Q|Q|N|100|N|N||BTSGU|N\r\nY|BTT|BlackRock
        Municipal 2030 Target Term Trust|N| |N|100|N||BTT|BTT|N\r\nY|BTTR|Better Choice
        Company Inc. Common Stock|A| |N|100|N||BTTR|BTTR|N\r\nY|BTU|Peabody Energy
        Corporation Common Stock |N| |N|100|N||BTU|BTU|N\r\nY|BTZ|BlackRock Credit
        Allocation Income Trust|N| |N|100|N||BTZ|BTZ|N\r\nY|BUCK|Simplify Exchange
        Traded Funds Simplify Stable Income ETF|P| |Y|100|N||BUCK|BUCK|N\r\nY|BUD|Anheuser-Busch
        Inbev SA Sponsored ADR (Belgium)|N| |N|100|N||BUD|BUD|N\r\nY|BUFB|Innovator
        ETFs Trust Innovator Laddered Allocation Buffer ETF|Z| |Y|100|N||BUFB|BUFB|N\r\nY|BUFC|AB
        Conservative Buffer ETF|Q|G|Y|100|N|N||BUFC|N\r\nY|BUFD|FT Vest Laddered Deep
        Buffer ETF|Z| |Y|100|N||BUFD|BUFD|N\r\nY|BUFF|Innovator Laddered Allocation
        Power Buffer ETF|Z| |Y|100|N||BUFF|BUFF|N\r\nY|BUFG|FT Vest Buffered Allocation
        Growth ETF|Z| |Y|100|N||BUFG|BUFG|N\r\nY|BUFP|SHL Telemedicine Ltd PGIM Laddered
        Fund of Buffer 12 ETF|Z| |Y|100|N||BUFP|BUFP|N\r\nY|BUFQ|FT Vest Laddered
        Nasdaq Buffer ETF|Z| |Y|100|N||BUFQ|BUFQ|N\r\nY|BUFR|FT Vest Laddered Buffer
        ETF|Z| |Y|100|N||BUFR|BUFR|N\r\nY|BUFS|First Trust Exchange-Traded Fund VIII
        FT Vest Laddered Small Cap Moderate Buffer ETF|Z| |Y|100|N||BUFS|BUFS|N\r\nY|BUFT|FT
        Vest Buffered Allocation Defensive ETF|Z| |Y|100|N||BUFT|BUFT|N\r\nY|BUFZ|FT
        Vest Laddered Moderate Buffer ETF|Z| |Y|100|N||BUFZ|BUFZ|N\r\nY|BUG|Global
        X Cybersecurity ETF|Q|G|Y|100|N|N||BUG|N\r\nY|BUI|BlackRock Utility, Infrastructure
        & Power Opportunities Trust|N| |N|100|N||BUI|BUI|N\r\nY|BUJA|Bukit Jalil Global
        Acquisition 1 Ltd. - Ordinary Shares|Q|S|N|100|N|N||BUJA|N\r\nY|BUJAR|Bukit
        Jalil Global Acquisition 1 Ltd. - Rights|Q|S|N|100|N|N||BUJAR|N\r\nY|BUJAU|Bukit
        Jalil Global Acquisition 1 Ltd. - Unit|Q|S|N|100|N|N||BUJAU|N\r\nY|BUJAW|Bukit
        Jalil Global Acquisition 1 Ltd. - Warrants|Q|S|N|100|N|N||BUJAW|N\r\nY|BUL|Pacer
        US Cash Cows Growth ETF|P| |Y|100|N||BUL|BUL|N\r\nY|BULD|Pacer BlueStar Engineering
        the Future ETF|Q|G|Y|100|N|N||BULD|N\r\nY|BULZ|MicroSectors FANG & Innovation
        3x Leveraged ETN|P| |Y|100|N||BULZ|BULZ|N\r\nY|BUR|Burford Capital Limited
        Ordinary Shares|N| |N|100|N||BUR|BUR|N\r\nY|BURL|Burlington Stores, Inc. Common
        Stock|N| |N|100|N||BURL|BURL|N\r\nY|BUSA|Brandes International ETF Brandes
        U.S. Value ETF|Z| |Y|100|N||BUSA|BUSA|N\r\nY|BUSE|First Busey Corporation
        - Common Stock|Q|Q|N|100|N|N||BUSE|N\r\nY|BUXX|EA Series Trust Strive Enhanced
        Income Short Maturity ETF|N| |Y|100|N||BUXX|BUXX|N\r\nY|BUYW|Northern Lights
        Fund Trust IV Main BuyWrite ETF|Z| |Y|100|N||BUYW|BUYW|N\r\nY|BUYZ|Franklin
        Disruptive Commerce ETF|Z| |Y|100|N||BUYZ|BUYZ|N\r\nY|BUZZ|VanEck Social Sentiment
        ETF|P| |Y|100|N||BUZZ|BUZZ|N\r\nY|BV|BrightView Holdings, Inc. Common Stock|N|
        |N|100|N||BV|BV|N\r\nY|BVFL|BV Financial, Inc. - Common Stock|Q|S|N|100|N|N||BVFL|N\r\nY|BVN|Buenaventura
        Mining Company Inc.|N| |N|100|N||BVN|BVN|N\r\nY|BVS|Bioventus Inc. - Class
        A Common Stock|Q|Q|N|100|N|N||BVS|N\r\nY|BW|Babcock & Wilcox Enterprises,
        Inc. Common Stock|N| |N|100|N||BW|BW|N\r\nY|BW$A|Babcock & Wilcox Enterprises,
        Inc. 7.75% Series A Cumulative Perpetual Preferred Stock|N| |N|100|N||BWpA|BW-A|N\r\nY|BWA|BorgWarner
        Inc. Common Stock|N| |N|100|N||BWA|BWA|N\r\nY|BWAQ|Blue World Acquisition
        Corporation - Class A ordinary shares|Q|G|N|100|N|D||BWAQ|N\r\nY|BWAQR|Blue
        World Acquisition Corporation - Right|Q|G|N|100|N|N||BWAQR|N\r\nY|BWAQU|Blue
        World Acquisition Corporation - Unit|Q|G|N|100|N|N||BWAQU|N\r\nY|BWAQW|Blue
        World Acquisition Corporation - Warrant|Q|G|N|100|N|N||BWAQW|N\r\nY|BWAY|BrainsWay
        Ltd. - American Depositary Shares|Q|G|N|100|N|N||BWAY|N\r\nY|BWB|Bridgewater
        Bancshares, Inc. - Common Stock|Q|S|N|100|N|N||BWB|N\r\nY|BWBBP|Bridgewater
        Bancshares, Inc. - Depositary Shares, Each Representing a 1/100th Interest
        in a Share of 5.875% Non-Cumulative Perpetual Preferred Stock, Series A|Q|S|N|100|N|N||BWBBP|N\r\nY|BWEB|Bitwise
        Funds Trust Bitwise Web3 ETF|P| |Y|100|N||BWEB|BWEB|N\r\nY|BWEN|Broadwind,
        Inc. - Common Stock|Q|S|N|100|N|N||BWEN|N\r\nY|BWET|Amplify Commodity Trust
        Breakwave Tanker Shipping ETF|P| |Y|100|N||BWET|BWET|N\r\nY|BWFG|Bankwell
        Financial Group, Inc. - Common Stock|Q|G|N|100|N|N||BWFG|N\r\nY|BWG|BrandywineGLOBAL
        Global Income Opportunities Fund Inc.|N| |N|100|N||BWG|BWG|N\r\nY|BWIN|The
        Baldwin Insurance Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||BWIN|N\r\nY|BWLP|BW
        LPG Limited Common Shares|N| |N|100|N||BWLP|BWLP|N\r\nY|BWMN|Bowman Consulting
        Group Ltd. - Common Stock|Q|G|N|100|N|N||BWMN|N\r\nY|BWMX|Betterware de Mexico,
        S.A.P.I. de C.V. Ordinary Shares|N| |N|100|N||BWMX|BWMX|N\r\nY|BWNB|Babcock
        & Wilcox Enterprises, Inc. 6.50% Senior Notes due 2026|N| |N|100|N||BWNB|BWNB|N\r\nY|BWSN|Babcock
        & Wilcox Enterprises, Inc. 8.125% Senior Notes due 2026|N| |N|100|N||BWSN|BWSN|N\r\nY|BWTG|ETF
        Opportunities Trust Brendan Wood TopGun Index ETF|Z| |Y|100|N||BWTG|BWTG|N\r\nY|BWX|SPDR
        Bloomberg International Treasury Bond ETF|P| |Y|100|N||BWX|BWX|N\r\nY|BWXT|BWX
        Technologies, Inc. Common Stock|N| |N|100|N||BWXT|BWXT|N\r\nY|BWZ|SPDR Bloomberg
        Short Term International Treasury Bond ETF|P| |Y|100|N||BWZ|BWZ|N\r\nY|BX|Blackstone
        Inc. Common Stock|N| |N|100|N||BX|BX|N\r\nY|BXC|Bluelinx Holdings Inc. Common
        Stock|N| |N|100|N||BXC|BXC|N\r\nY|BXMT|Blackstone Mortgage Trust, Inc. Common
        Stock|N| |N|100|N||BXMT|BXMT|N\r\nY|BXMX|Nuveen S&P 500 Buy-Write Income Fund
        Common Shares of Beneficial Interest|N| |N|100|N||BXMX|BXMX|N\r\nY|BXP|Boston
        Properties, Inc. Common Stock|N| |N|100|N||BXP|BXP|N\r\nY|BXSL|Blackstone
        Secured Lending Fund Common Shares of Beneficial Interest|N| |N|100|N||BXSL|BXSL|N\r\nY|BY|Byline
        Bancorp, Inc. Common Stock|N| |N|100|N||BY|BY|N\r\nY|BYD|Boyd Gaming Corporation
        Common Stock|N| |N|100|N||BYD|BYD|N\r\nY|BYFC|Broadway Financial Corporation
        - Class A Common Stock|Q|S|N|100|N|N||BYFC|N\r\nY|BYLD|iShares Yield Optimized
        Bond ETF|P| |Y|100|N||BYLD|BYLD|N\r\nY|BYM|Blackrock Municipal Income Quality
        Trust Common Shares of Beneficial Interest|N| |N|100|N||BYM|BYM|N\r\nY|BYND|Beyond
        Meat, Inc. - Common stock|Q|Q|N|100|N|N||BYND|N\r\nY|BYNO|byNordic Acquisition
        Corporation - Class A Common Stock|Q|G|N|100|N|D||BYNO|N\r\nY|BYNOU|byNordic
        Acquisition Corporation - Units|Q|G|N|100|N|N||BYNOU|N\r\nY|BYNOW|byNordic
        Acquisition Corporation - Warrant|Q|G|N|100|N|N||BYNOW|N\r\nY|BYON|Beyond,
        Inc. Common Stock|N| |N|100|N||BYON|BYON|N\r\nY|BYRE|Principal Exchange-Traded
        Funds Principal Real Estate Active Opportunities ETF|P| |Y|100|N||BYRE|BYRE|N\r\nY|BYRN|Byrna
        Technologies, Inc. - Common Stock|Q|S|N|100|N|N||BYRN|N\r\nY|BYSI|BeyondSpring,
        Inc. - Ordinary Shares|Q|S|N|100|N|N||BYSI|N\r\nY|BYU|BAIYU Holdings, Inc.
        - Common Stock|Q|S|N|100|N|N||BYU|N\r\nY|BZ|KANZHUN LIMITED - American Depository
        Shares|Q|Q|N|100|N|N||BZ|N\r\nY|BZFD|BuzzFeed, Inc. - Class A Common Stock|Q|S|N|100|N|N||BZFD|N\r\nY|BZFDW|BuzzFeed,
        Inc. - Warrant|Q|S|N|100|N|N||BZFDW|N\r\nY|BZH|Beazer Homes USA, Inc. Common
        Stock|N| |N|100|N||BZH|BZH|N\r\nY|BZQ|ProShares UltraShort MSCI Brazil Capped|P|
        |Y|100|N||BZQ|BZQ|N\r\nY|BZUN|Baozun Inc. - American Depositary Shares|Q|Q|N|100|N|N||BZUN|N\r\nY|C|Citigroup,
        Inc. Common Stock|N| |N|100|N||C|C|N\r\nY|C$N|Citigroup Capital XIII 7.875%
        Fixed rate Floating Rate trust Preferred Securities (TruPS)|N| |N|100|N||CpN|C-N|N\r\nY|CA|Xtrackers
        California Municipal Bonds ETF|Q|G|Y|100|N|N||CA|N\r\nY|CAAA|First Trust Exchange-Traded
        Fund IV First Trust Commercial Mortgage Opportunities ETF|P| |Y|100|N||CAAA|CAAA|N\r\nY|CAAP|Corporacion
        America Airports SA Common Shares|N| |N|100|N||CAAP|CAAP|N\r\nY|CAAS|China
        Automotive Systems, Inc. - Common Stock|Q|S|N|100|N|N||CAAS|N\r\nY|CABA|Cabaletta
        Bio, Inc. - Common Stock|Q|Q|N|100|N|N||CABA|N\r\nY|CABO|Cable One, Inc. Common
        Stock|N| |N|100|N||CABO|CABO|N\r\nY|CAC|Camden National Corporation - Common
        Stock|Q|Q|N|100|N|N||CAC|N\r\nY|CACC|Credit Acceptance Corporation - Common
        Stock|Q|Q|N|100|N|N||CACC|N\r\nY|CACI|CACI International, Inc. Class A Common
        Stock|N| |N|100|N||CACI|CACI|N\r\nY|CACO|Caravelle International Group - Ordinary
        Shares|Q|S|N|100|N|E||CACO|N\r\nY|CADE|Cadence Bank Common Stock|N| |N|100|N||CADE|CADE|N\r\nY|CADE$A|Cadence
        Bank 5.50% Series A |N| |N|100|N||CADEpA|CADE-A|N\r\nY|CADL|Candel Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||CADL|N\r\nY|CAE|CAE Inc. Ordinary Shares|N|
        |N|100|N||CAE|CAE|N\r\nY|CAF|Morgan Stanley China A Share Fund Inc. Common
        Stock|N| |N|100|N||CAF|CAF|N\r\nY|CAFG|Pacer US Small Cap Cash Cows Growth
        Leaders ETF|Q|G|Y|100|N|N||CAFG|N\r\nY|CAG|ConAgra Brands, Inc. Common Stock|N|
        |N|100|N||CAG|CAG|N\r\nY|CAH|Cardinal Health, Inc. Common Stock|N| |N|100|N||CAH|CAH|N\r\nY|CAKE|The
        Cheesecake Factory Incorporated - Common Stock|Q|Q|N|100|N|N||CAKE|N\r\nY|CAL|Caleres,
        Inc. Common Stock|N| |N|100|N||CAL|CAL|N\r\nY|CALB|California BanCorp - Common
        Stock|Q|Q|N|100|N|N||CALB|N\r\nY|CALC|CalciMedica, Inc. - Common Stock|Q|S|N|100|N|N||CALC|N\r\nY|CALF|Pacer
        US Small Cap Cash Cows 100 ETF|Z| |Y|100|N||CALF|CALF|N\r\nY|CALM|Cal-Maine
        Foods, Inc. - Common Stock|Q|Q|N|100|N|N||CALM|N\r\nY|CALT|Calliditas Therapeutics
        AB - American Depositary Shares|Q|Q|N|100|N|N||CALT|N\r\nY|CALX|Calix, Inc
        Common Stock|N| |N|100|N||CALX|CALX|N\r\nY|CALY|BlackRock Short-Term California
        Muni Bond ETF|Q|G|Y|100|N|N||CALY|N\r\nY|CAML|Professionally Managed Portfolios
        Congress Large Cap Growth ETF|P| |Y|100|N||CAML|CAML|N\r\nY|CAMT|Camtek Ltd.
        - Ordinary Shares|Q|G|N|100|N|N||CAMT|N\r\nY|CAMX|The Advisors? Inner Circle
        Fund Cambiar Aggressive Value ETF|P| |Y|100|N||CAMX|CAMX|N\r\nY|CAN|Canaan
        Inc. - American Depositary Shares|Q|G|N|100|N|N||CAN|N\r\nY|CANC|Tema Oncology
        ETF|Q|G|Y|100|N|N||CANC|N\r\nY|CANE|Teucrium Sugar Fund ETV|P| |Y|100|N||CANE|CANE|N\r\nY|CANF|Can-Fite
        Biopharma Ltd Sponsored ADR (Israel)|A| |N|100|N||CANF|CANF|N\r\nY|CANG|Cango
        Inc. American Depositary Shares,  each representing two (2) Class A Ordinary
        Shares|N| |N|100|N||CANG|CANG|N\r\nY|CANQ|Calamos Alternative Nasdaq & Bond
        ETF|Q|G|Y|100|N|N||CANQ|N\r\nY|CAOS|EA Series Trust Alpha Architect Tail Risk
        ETF|Z| |Y|100|N||CAOS|CAOS|N\r\nY|CAPE|DoubleLine ETF Trust DoubleLine Shiller
        CAPE U.S. Equities ETF|P| |Y|100|N||CAPE|CAPE|N\r\nY|CAPL|CrossAmerica Partners
        LP Common Units representing limited partner interests|N| |N|100|N||CAPL|CAPL|N\r\nY|CAPR|Capricor
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||CAPR|N\r\nY|CAPT|Captivision
        Inc. - Ordinary Shares|Q|G|N|100|N|N||CAPT|N\r\nY|CAPTW|Captivision Inc. -
        Warrant|Q|S|N|100|N|N||CAPTW|N\r\nY|CAR|Avis Budget Group, Inc. - Common Stock|Q|Q|N|100|N|N||CAR|N\r\nY|CARA|Cara
        Therapeutics, Inc. - Common Stock|Q|G|N|100|N|D||CARA|N\r\nY|CARD|Bank Of
        Montreal MAX Auto Industry -3x Inverse Leveraged ETN|P| |Y|100|N||CARD|CARD|N\r\nY|CARE|Carter
        Bankshares, Inc. - Common Stock|Q|Q|N|100|N|N||CARE|N\r\nY|CARG|CarGurus,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||CARG|N\r\nY|CARK|The Advisors?
        Inner Circle Fund II CastleArk Large Growth ETF|P| |Y|100|N||CARK|CARK|N\r\nY|CARM|Carisma
        Therapeutics, Inc. - Common Stock|Q|G|N|100|N|N||CARM|N\r\nY|CARR|Carrier
        Global Corporation Common Stock |N| |N|100|N||CARR|CARR|N\r\nY|CARS|Cars.com
        Inc. Common Stock |N| |N|100|N||CARS|CARS|N\r\nY|CART|Maplebear Inc. - Common
        Stock|Q|Q|N|100|N|N||CART|N\r\nY|CARU|Bank Of Montreal MAX Auto Industry 3x
        Leveraged ETN|P| |Y|100|N||CARU|CARU|N\r\nY|CARV|Carver Bancorp, Inc. - Common
        Stock|Q|S|N|100|N|N||CARV|N\r\nY|CARY|Angel Oak Funds Trust Angel Oak Income
        ETF|P| |Y|100|N||CARY|CARY|N\r\nY|CARZ|First Trust S-Network Electric & Future
        Vehicle Ecosystem ETF|Q|G|Y|100|N|N||CARZ|N\r\nY|CASH|Pathward Financial,
        Inc. - Common Stock|Q|Q|N|100|N|N||CASH|N\r\nY|CASI|CASI Pharmaceuticals,
        Inc. - Ordinary Shares|Q|S|N|100|N|N||CASI|N\r\nY|CASS|Cass Information Systems,
        Inc - Common Stock|Q|Q|N|100|N|N||CASS|N\r\nY|CASY|Caseys General Stores,
        Inc. - Common Stock|Q|Q|N|100|N|N||CASY|N\r\nY|CAT|Caterpillar, Inc. Common
        Stock|N| |N|100|N||CAT|CAT|N\r\nY|CATC|Cambridge Bancorp - Common Stock|Q|S|N|100|N|N||CATC|N\r\nY|CATH|Global
        X S&P 500 Catholic Values ETF|Q|G|Y|100|N|N||CATH|N\r\nY|CATO|Cato Corporation
        (The) Class A Common Stock|N| |N|100|N||CATO|CATO|N\r\nY|CATX|Perspective
        Therapeutics, Inc. Common Stock|A| |N|100|N||CATX|CATX|N\r\nY|CATY|Cathay
        General Bancorp - Common Stock|Q|Q|N|100|N|N||CATY|N\r\nY|CAUD|Collective
        Audience, Inc. - Common Stock|Q|G|N|100|N|H||CAUD|N\r\nY|CAVA|CAVA Group,
        Inc. Common Stock|N| |N|100|N||CAVA|CAVA|N\r\nY|CB|Chubb Limited  Common Stock|N|
        |N|100|N||CB|CB|N\r\nY|CBAN|Colony Bankcorp, Inc. - Common Stock|Q|G|N|100|N|N||CBAN|N\r\nY|CBAT|CBAK
        Energy Technology, Inc. - Common Stock|Q|S|N|100|N|N||CBAT|N\r\nY|CBFV|CB
        Financial Services, Inc. - Common Stock|Q|G|N|100|N|N||CBFV|N\r\nY|CBH|Virtus
        Convertible & Income 2024 Target Term Fund Common Shares of Beneficial Interest|N|
        |N|100|N||CBH|CBH|N\r\nY|CBL|CBL & Associates Properties, Inc. Common Stock|N|
        |N|100|N||CBL|CBL|N\r\nY|CBLS|Clough Hedged Equity ETF|P| |Y|100|N||CBLS|CBLS|N\r\nY|CBNK|Capital
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||CBNK|N\r\nY|CBO|CBO (Listing Market
        - NYSE - Networks A/E) Common Stock|N| |N|100|Y||CBO|CBO|N\r\nY|CBOE|Cboe
        Global Markets, Inc. Common Stock|Z| |N|100|N||CBOE|CBOE|N\r\nY|CBON|VanEck
        China Bond ETF|P| |Y|100|N||CBON|CBON|N\r\nY|CBRE|CBRE Group Inc Common Stock
        Class A|N| |N|100|N||CBRE|CBRE|N\r\nY|CBRG|Chain Bridge I - Class A Ordinary
        Shares|Q|S|N|100|N|N||CBRG|N\r\nY|CBRGU|Chain Bridge I - Units|Q|S|N|100|N|N||CBRGU|N\r\nY|CBRL|Cracker
        Barrel Old Country Store, Inc. - Common Stock|Q|Q|N|100|N|N||CBRL|N\r\nY|CBSE|Clough
        Select Equity ETF|P| |Y|100|N||CBSE|CBSE|N\r\nY|CBSH|Commerce Bancshares,
        Inc. - Common Stock|Q|Q|N|100|N|N||CBSH|N\r\nY|CBT|Cabot Corporation Common
        Stock|N| |N|100|N||CBT|CBT|N\r\nY|CBU|Community Financial System, Inc. Common
        Stock|N| |N|100|N||CBU|CBU|N\r\nY|CBUS|Cibus, Inc. - Class A Common Stock|Q|S|N|100|N|N||CBUS|N\r\nY|CBX|CBX
        (Listing Market NYSE Networks AE) Common Stock|N| |N|100|Y||CBX|CBX|N\r\nY|CBZ|CBIZ,
        Inc. Common Stock|N| |N|100|N||CBZ|CBZ|N\r\nY|CC|Chemours Company (The) Common
        Stock|N| |N|100|N||CC|CC|N\r\nY|CCAP|Crescent Capital BDC, Inc. - Common Stock|Q|G|N|100|N|N||CCAP|N\r\nY|CCB|Coastal
        Financial Corporation - Common Stock|Q|Q|N|100|N|N||CCB|N\r\nY|CCBG|Capital
        City Bank Group - Common Stock|Q|Q|N|100|N|E||CCBG|N\r\nY|CCCC|C4 Therapeutics,
        Inc. - Common Stock|Q|Q|N|100|N|N||CCCC|N\r\nY|CCCS|CCC Intelligent Solutions
        Holdings Inc. - Common Stock|Q|Q|N|100|N|N||CCCS|N\r\nY|CCD|Calamos Dynamic
        Convertible & Income Fund - Closed End Fund|Q|Q|N|100|N|N||CCD|N\r\nY|CCEF|Calamos
        ETF Trust Calamos CEF Income & Arbitrage ETF|P| |Y|100|N||CCEF|CCEF|N\r\nY|CCEL|Cryo-Cell
        International, Inc. Common Stock|A| |N|100|N||CCEL|CCEL|N\r\nY|CCEP|Coca-Cola
        Europacific Partners plc - Ordinary Shares|Q|Q|N|100|N|N||CCEP|N\r\nY|CCG|Cheche
        Group Inc. - Class A Ordinary Shares|Q|S|N|100|N|N||CCG|N\r\nY|CCGWW|Cheche
        Group Inc. - Warrant|Q|S|N|100|N|N||CCGWW|N\r\nY|CCI|Crown Castle Inc. Common
        Stock|N| |N|100|N||CCI|CCI|N\r\nY|CCIA|Carlyle Credit Income Fund 8.75% Series
        A Preferred Shares due 2028|N| |N|100|N||CCIA|CCIA|N\r\nY|CCIF|Carlyle Credit
        Income Fund Shares of Beneficial Interest|N| |N|100|N||CCIF|CCIF|N\r\nY|CCIX|Churchill
        Capital Corp IX - Ordinary Shares|Q|G|N|100|N|N||CCIX|N\r\nY|CCIXU|Churchill
        Capital Corp IX - Unit|Q|G|N|100|N|N||CCIXU|N\r\nY|CCIXW|Churchill Capital
        Corp IX - Warrant|Q|G|N|100|N|N||CCIXW|N\r\nY|CCJ|Cameco Corporation Common
        Stock|N| |N|100|N||CCJ|CCJ|N\r\nY|CCK|Crown Holdings, Inc.|N| |N|100|N||CCK|CCK|N\r\nY|CCL|Carnival
        Corporation Common Stock|N| |N|100|N||CCL|CCL|N\r\nY|CCLD|CareCloud, Inc.
        - Common Stock|Q|G|N|100|N|N||CCLD|N\r\nY|CCLDO|CareCloud, Inc. - 8.75% Series
        B Cumulative Redeemable Perpetual Preferred Stock|Q|G|N|100|N|N||CCLDO|N\r\nY|CCLDP|CareCloud,
        Inc. - 11% Series A Cumulative Redeemable Perpetual Preferred Stock|Q|G|N|100|N|N||CCLDP|N\r\nY|CCM|Concord
        Medical Services Holdings Limited ADS (Each represents three ordinary shares)|N|
        |N|100|N||CCM|CCM|N\r\nY|CCMG|EA Series Trust CCM Global Equity ETF|P| |Y|100|N||CCMG|CCMG|N\r\nY|CCNE|CNB
        Financial Corporation - Common Stock|Q|Q|N|100|N|N||CCNE|N\r\nY|CCNEP|CNB
        Financial Corporation - Depositary shares, each representing a 1/40th ownership
        interest in a share of 7.125% Series A Fixed- Rate Non-Cumulative Perpetual
        Preferred Stock|Q|Q|N|100|N|N||CCNEP|N\r\nY|CCO|Clear Channel Outdoor Holdings,
        Inc. Common Stock|N| |N|100|N||CCO|CCO|N\r\nY|CCOI|Cogent Communications Holdings,
        Inc. - Common Stock|Q|Q|N|100|N|N||CCOI|N\r\nY|CCOR|Core Alternative ETF|P|
        |Y|100|N||CCOR|CCOR|N\r\nY|CCRD|CoreCard Corporation Common Stock|N| |N|100|N||CCRD|CCRD|N\r\nY|CCRN|Cross
        Country Healthcare, Inc. - Common Stock|Q|Q|N|100|N|N||CCRN|N\r\nY|CCRV|iShares
        U.S. ETF Trust iShares Commodity Curve Carry Strategy ETF|P| |Y|100|N||CCRV|CCRV|N\r\nY|CCS|Century
        Communities, Inc. Common Stock|N| |N|100|N||CCS|CCS|N\r\nY|CCSB|Carbon Collective
        Short Duration Green Bond ETF|Q|G|Y|100|N|N||CCSB|N\r\nY|CCSI|Consensus Cloud
        Solutions, Inc. - Common Stock|Q|Q|N|100|N|N||CCSI|N\r\nY|CCSO|Carbon Collective
        Climate Solutions U.S. Equity ETF|Q|G|Y|100|N|N||CCSO|N\r\nY|CCTG|CCSC Technology
        International Holdings Limited - Ordinary Shares|Q|S|N|100|N|N||CCTG|N\r\nY|CCTS|Cactus
        Acquisition Corp. 1 Limited - Class A Ordinary Share|Q|G|N|100|N|D||CCTS|N\r\nY|CCTSU|Cactus
        Acquisition Corp. 1 Limited - Unit|Q|G|N|100|N|N||CCTSU|N\r\nY|CCTSW|Cactus
        Acquisition Corp. 1 Limited - Warrant|Q|G|N|100|N|N||CCTSW|N\r\nY|CCU|Compania
        Cervecerias Unidas, S.A. Common Stock|N| |N|100|N||CCU|CCU|N\r\nY|CCZ|Comcast
        Holdings ZONES|N| |N|100|N||CCZ|CCZ|N\r\nY|CDAQ|Compass Digital Acquisition
        Corp. - Class A Ordinary Shares|Q|G|N|100|N|N||CDAQ|N\r\nY|CDAQU|Compass Digital
        Acquisition Corp. - Unit|Q|G|N|100|N|N||CDAQU|N\r\nY|CDAQW|Compass Digital
        Acquisition Corp. - Warrant|Q|G|N|100|N|N||CDAQW|N\r\nY|CDC|VictoryShares
        US EQ Income Enhanced Volatility Wtd ETF|Q|G|Y|100|N|N||CDC|N\r\nY|CDE|Coeur
        Mining, Inc. Common Stock|N| |N|100|N||CDE|CDE|N\r\nY|CDEI|Morgan Stanley
        ETF Trust Calvert US Large-Cap Diversity, Equity and Inclusion Index ETF|P|
        |Y|100|N||CDEI|CDEI|N\r\nY|CDIO|Cardio Diagnostics Holdings Inc. - Common
        stock|Q|S|N|100|N|D||CDIO|N\r\nY|CDIOW|Cardio Diagnostics Holdings Inc. -
        Warrant|Q|S|N|100|N|N||CDIOW|N\r\nY|CDL|VictoryShares US Large Cap High Div
        Volatility Wtd ETF|Q|G|Y|100|N|N||CDL|N\r\nY|CDLR|Cadeler A/S American Depositary
        Share (each representing four (4) Ordinary Shares)|N| |N|100|N||CDLR|CDLR|N\r\nY|CDLX|Cardlytics,
        Inc. - Common Stock|Q|G|N|100|N|N||CDLX|N\r\nY|CDMO|Avid Bioservices, Inc.
        - Common Stock|Q|S|N|100|N|N||CDMO|N\r\nY|CDNA|CareDx, Inc. - Common Stock|Q|G|N|100|N|N||CDNA|N\r\nY|CDNS|Cadence
        Design Systems, Inc. - Common Stock|Q|Q|N|100|N|N||CDNS|N\r\nY|CDP|COPT Defense
        Properties Common Shares of Beneficial Interest|N| |N|100|N||CDP|CDP|N\r\nY|CDR$B|Cedar
        Realty Trust, Inc. 7.25% Series B Cumulative Redeemable Preferred Stock|N|
        |N|100|N||CDRpB|CDR-B|N\r\nY|CDR$C|Cedar Realty Trust, Inc. 6.50% Series C
        Cumulative Redeemable Preferred Stock|N| |N|100|N||CDRpC|CDR-C|N\r\nY|CDRE|Cadre
        Holdings, Inc. Common Stock|N| |N|100|N||CDRE|CDRE|N\r\nY|CDRO|Codere Online
        Luxembourg, S.A. - Ordinary Shares|Q|S|N|100|N|E||CDRO|N\r\nY|CDROW|Codere
        Online Luxembourg, S.A. - Warrants|Q|S|N|100|N|E||CDROW|N\r\nY|CDT|Conduit
        Pharmaceuticals Inc.  - Common Stock|Q|G|N|100|N|D||CDT|N\r\nY|CDTG|CDT Environmental
        Technology Investment Holdings Limited - ordinary shares|Q|S|N|100|N|N||CDTG|N\r\nY|CDTTW|Conduit
        Pharmaceuticals Inc.  - Warrant|Q|S|N|100|N|D||CDTTW|N\r\nY|CDTX|Cidara Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||CDTX|N\r\nY|CDW|CDW Corporation - Common
        Stock|Q|Q|N|100|N|N||CDW|N\r\nY|CDX|Simplify Exchange Traded Funds Simplify
        High Yield PLUS Credit Hedge ETF|P| |Y|100|N||CDX|CDX|N\r\nY|CDXC|ChromaDex
        Corporation - Common Stock|Q|S|N|100|N|N||CDXC|N\r\nY|CDXS|Codexis, Inc. -
        Common Stock|Q|Q|N|100|N|N||CDXS|N\r\nY|CDZI|Cadiz, Inc. - Common Stock|Q|G|N|100|N|N||CDZI|N\r\nY|CDZIP|Cadiz,
        Inc. - Depositary Shares|Q|G|N|100|N|N||CDZIP|N\r\nY|CE|Celanese Corporation
        Common Stock|N| |N|100|N||CE|CE|N\r\nY|CEAD|CEA Industries Inc. - Common Stock|Q|S|N|100|N|D||CEAD|N\r\nY|CEADW|CEA
        Industries Inc. - Warrant|Q|S|N|100|N|N||CEADW|N\r\nY|CECO|CECO Environmental
        Corp. - Common Stock|Q|Q|N|100|N|N||CECO|N\r\nY|CEE|The Central and Eastern
        Europe Fund, Inc. (The) Common Stock|N| |N|100|N||CEE|CEE|N\r\nY|CEF|Sprott
        Physical Gold and Silver Trust Units|P| |Y|100|N||CEF|CEF|N\r\nY|CEFA|Global
        X S&P Catholic Values Developed ex-U.S. ETF|Q|G|Y|100|N|N||CEFA|N\r\nY|CEFD|ETRACS
        Monthly Pay 1.5X Leveraged Closed-End Fund Index ETN|P| |Y|100|N||CEFD|CEFD|N\r\nY|CEFS|Exchange
        Listed Funds Trust ETF|Z| |Y|100|N||CEFS|CEFS|N\r\nY|CEG|Constellation Energy
        Corporation - Common Stock|Q|Q|N|100|N|N||CEG|N\r\nY|CEI|Camber Energy, Inc.
        Common Stock|A| |N|100|N||CEI|CEI|N\r\nY|CEIX|CONSOL Energy Inc. Common Stock
        |N| |N|100|N||CEIX|CEIX|N\r\nY|CELC|Celcuity Inc. - Common Stock|Q|S|N|100|N|N||CELC|N\r\nY|CELG.R|Bristol-Myers
        Squibb Company Celegne Contingent Value Rights|N| |N|100|N||CELGr|CELG^|N\r\nY|CELH|Celsius
        Holdings, Inc. - Common Stock|Q|S|N|100|N|N||CELH|N\r\nY|CELU|Celularity Inc.
        - Class A Common Stock|Q|S|N|100|N|E||CELU|N\r\nY|CELUW|Celularity Inc. -
        Warrant|Q|S|N|100|N|E||CELUW|N\r\nY|CELZ|Creative Medical Technology Holdings,
        Inc. - Common Stock|Q|S|N|100|N|N||CELZ|N\r\nY|CEM|ClearBridge MLP and Midstream
        Fund Inc. Common Stock|N| |N|100|N||CEM|CEM|N\r\nY|CEMB|iShares J.P. Morgan
        EM Corporate Bond ETF|Z| |Y|100|N||CEMB|CEMB|N\r\nY|CENN|Cenntro Inc. - Common
        Stock|Q|S|N|100|N|N||CENN|N\r\nY|CENT|Central Garden & Pet Company - Common
        Stock|Q|Q|N|100|N|N||CENT|N\r\nY|CENTA|Central Garden & Pet Company - Class
        A Common Stock Nonvoting|Q|Q|N|100|N|N||CENTA|N\r\nY|CENX|Century Aluminum
        Company - Common Stock|Q|Q|N|100|N|N||CENX|N\r\nY|CEPU|Central Puerto S.A.
        American Depositary Shares (each represents ten Common Shares)|N| |N|100|N||CEPU|CEPU|N\r\nY|CERE|Cerevel
        Therapeutics Holdings, Inc. - Common Stock|Q|S|N|100|N|N||CERE|N\r\nY|CERO|CERo
        Therapeutics Holdings, Inc. - Common Stock|Q|G|N|100|N|D||CERO|N\r\nY|CEROW|CERo
        Therapeutics Holdings, Inc. - Warrants|Q|S|N|100|N|N||CEROW|N\r\nY|CERS|Cerus
        Corporation - Common Stock|Q|G|N|100|N|N||CERS|N\r\nY|CERT|Certara, Inc. -
        Common Stock|Q|Q|N|100|N|N||CERT|N\r\nY|CET|Central Securities Corporation
        Common Stock|A| |N|100|N||CET|CET|N\r\nY|CETF|DriveWealth NYSE 100 Index ETF|P|
        |Y|100|N||CETF|CETF|N\r\nY|CETU|Cetus Capital Acquisition Corp. - Class A
        Common Stock|Q|S|N|100|N|N||CETU|N\r\nY|CETUR|Cetus Capital Acquisition Corp.
        - Right to receive 1/6 of one share of Class A Common Stock|Q|S|N|100|N|N||CETUR|N\r\nY|CETUU|Cetus
        Capital Acquisition Corp. - Unit|Q|S|N|100|N|N||CETUU|N\r\nY|CETUW|Cetus Capital
        Acquisition Corp. - Warrant|Q|S|N|100|N|N||CETUW|N\r\nY|CETX|Cemtrex Inc.
        - Common Stock|Q|S|N|100|N|D||CETX|N\r\nY|CETY|Clean Energy Technologies,
        Inc. - Common Stock|Q|S|N|100|N|N||CETY|N\r\nY|CEV|Eaton Vance California
        Municipal Income Trust Shares of Beneficial Interest|A| |N|100|N||CEV|CEV|N\r\nY|CEVA|CEVA,
        Inc. - Common Stock|Q|Q|N|100|N|N||CEVA|N\r\nY|CEW|WisdomTree Emerging Currency
        Strategy Fund|P| |Y|100|N||CEW|CEW|N\r\nY|CF|CF Industries Holdings, Inc.
        Common Stock|N| |N|100|N||CF|CF|N\r\nY|CFA|VictoryShares US 500 Volatility
        Wtd ETF|Q|G|Y|100|N|N||CFA|N\r\nY|CFB|CrossFirst Bankshares, Inc. - Common
        Stock|Q|Q|N|100|N|N||CFB|N\r\nY|CFBK|CF Bankshares Inc. - Common Stock|Q|S|N|100|N|N||CFBK|N\r\nY|CFCV|ClearBridge
        Focus Value ESG ETF|Z| |Y|100|N||CFCV|CFCV|N\r\nY|CFFI|C&F Financial Corporation
        - Common Stock|Q|Q|N|100|N|N||CFFI|N\r\nY|CFFN|Capitol Federal Financial,
        Inc. - Common Stock|Q|Q|N|100|N|N||CFFN|N\r\nY|CFFS|CF Acquisition Corp. VII
        - Class A Common Stock|Q|S|N|100|N|N||CFFS|N\r\nY|CFFSU|CF Acquisition Corp.
        VII - Unit|Q|G|N|100|N|N||CFFSU|N\r\nY|CFFSW|CF Acquisition Corp. VII - Warrant|Q|S|N|100|N|N||CFFSW|N\r\nY|CFG|Citizens
        Financial Group, Inc. Common Stock|N| |N|100|N||CFG|CFG|N\r\nY|CFG$D|Citizens
        Financial Group, Inc. Depositary Shares, each representing a 1/40th Interest
        in a Share of 6.350% Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred
        Stock, Series D|N| |N|100|N||CFGpD|CFG-D|N\r\nY|CFG$E|Citizens Financial Group,
        Inc. Depositary Shares Each Representing 1/40th Interest in a Share of 5.000%
        Fixed-Rate Non-Cumulative Perpetual Preferred Stock, Series E|N| |N|100|N||CFGpE|CFG-E|N\r\nY|CFG$H|Citizens
        Financial Group, Inc. Depositary Shares Each Representing a 1/40th Interest
        in a Share of 7.375% Fixed-Rate Non-Cumulative Perpetual Preferred Stock,
        Series H|N| |N|100|N||CFGpH|CFG-H|N\r\nY|CFLT|Confluent, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||CFLT|N\r\nY|CFO|VictoryShares US 500 Enhanced Volatility
        Wtd ETF|Q|G|Y|100|N|N||CFO|N\r\nY|CFR|Cullen/Frost Bankers, Inc. Common Stock|N|
        |N|100|N||CFR|CFR|N\r\nY|CFR$B|Cullen/Frost Bankers, Inc. Depositary Shares,
        each representing a 1/40th ownership interest in a share of 4.450% non-cumulative
        perpetual preferred stock, Series B|N| |N|100|N||CFRpB|CFR-B|N\r\nY|CFSB|CFSB
        Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||CFSB|N\r\nY|CG|The Carlyle Group
        Inc. - Common Stock|Q|Q|N|100|N|N||CG|N\r\nY|CGA|China Green Agriculture,
        Inc. Common Stock|N| |N|100|N||CGA|CGA|N\r\nY|CGABL|The Carlyle Group Inc.
        - 4.625% Subordinated Notes due 2061|Q|Q|N|100|N|N||CGABL|N\r\nY|CGAU|Centerra
        Gold Inc. Common Shares|N| |N|100|N||CGAU|CGAU|N\r\nY|CGBD|Carlyle Secured
        Lending, Inc. - Closed End Fund|Q|Q|N|100|N|N||CGBD|N\r\nY|CGBDL|Carlyle Secured
        Lending, Inc. - 8.20% Notes due 2028|Q|G|N|100|N|N||CGBDL|N\r\nY|CGBL|Capital
        Group Core Balanced ETF Capital Group Core Balanced ETF|P| |Y|100|N||CGBL|CGBL|N\r\nY|CGC|Canopy
        Growth Corporation - Common Shares|Q|Q|N|100|N|N||CGC|N\r\nY|CGCB|Capital
        Group Fixed Income ETF Trust Capital Group Core Bond ETF|P| |Y|100|N||CGCB|CGCB|N\r\nY|CGCP|Capital
        Group Core Plus Income ETF Capital Group Core Plus Income ETF|P| |Y|100|N||CGCP|CGCP|N\r\nY|CGCV|Capital
        Group Conservative Equity ETF Capital Group Conservative Equity ETF|P| |Y|100|N||CGCV|CGCV|N\r\nY|CGDG|Capital
        Group Dividend Growers ETF Capital Group Dividend Growers ETF|P| |Y|100|N||CGDG|CGDG|N\r\nY|CGDV|Capital
        Group Dividend Value ETF Capital Group Dividend Value ETF|P| |Y|100|N||CGDV|CGDV|N\r\nY|CGEM|Cullinan
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||CGEM|N\r\nY|CGEN|Compugen
        Ltd. - Ordinary Shares|Q|S|N|100|N|N||CGEN|N\r\nY|CGGE|Capital Group Global
        Equity ETF Capital Group Global Equity ETF|P| |Y|100|N||CGGE|CGGE|N\r\nY|CGGO|Capital
        Group Global Growth Equity ETF Capital Group Global Growth Equity ETF|P| |Y|100|N||CGGO|CGGO|N\r\nY|CGGR|Capital
        Group Growth ETF Capital Group Growth ETF|P| |Y|100|N||CGGR|CGGR|N\r\nY|CGHM|Capital
        Group Fixed Income ETF Trust Capital Group Municipal High-Income ETF|P| |Y|100|N||CGHM|CGHM|N\r\nY|CGIB|Capital
        Group Fixed Income ETF Trust Capital Group International Bond ETF (USD-Hedged)|P|
        |Y|100|N||CGIB|CGIB|N\r\nY|CGIC|Capital Group International Core Equity ETF
        Capital Group International Core Equity ETF|P| |Y|100|N||CGIC|CGIC|N\r\nY|CGIE|Capital
        Group International Equity ETF Capital Group International Equity ETF|P| |Y|100|N||CGIE|CGIE|N\r\nY|CGMS|Capital
        Group Fixed Income ETF Trust Capital Group U.S. Multi-Sector Income ETF|P|
        |Y|100|N||CGMS|CGMS|N\r\nY|CGMU|Capital Group Fixed Income ETF Trust Capital
        Group Municipal Income ETF|P| |Y|100|N||CGMU|CGMU|N\r\nY|CGNG|Capital Group
        New Geography Equity ETF Capital Group New Geography Equity ETF|P| |Y|100|N||CGNG|CGNG|N\r\nY|CGNT|Cognyte
        Software Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CGNT|N\r\nY|CGNX|Cognex Corporation
        - Common Stock|Q|Q|N|100|N|N||CGNX|N\r\nY|CGO|Calamos Global Total Return
        Fund - Closed End Fund|Q|Q|N|100|N|N||CGO|N\r\nY|CGON|CG Oncology, Inc. -
        Common stock|Q|Q|N|100|N|N||CGON|N\r\nY|CGRO|Tidal Trust II CoreValues Alpha
        Greater China Growth ETF|P| |Y|100|N||CGRO|CGRO|N\r\nY|CGSD|Capital Group
        Fixed Income ETF Trust Capital Group Short Duration Income ETF|P| |Y|100|N||CGSD|CGSD|N\r\nY|CGSM|Capital
        Group Fixed Income ETF Trust Capital Group Short Duration Municipal Income
        ETF|P| |Y|100|N||CGSM|CGSM|N\r\nY|CGTX|Cognition Therapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||CGTX|N\r\nY|CGUI|Capital Group Fixed Income ETF Trust
        Capital Group Ultra Short Income ETF|P| |Y|100|N||CGUI|CGUI|N\r\nY|CGUS|Capital
        Group Core Equity ETF Capital Group Core Equity ETF|P| |Y|100|N||CGUS|CGUS|N\r\nY|CGV|Two
        Roads Shared Trust Conductor Global Equity Value ETF|N| |Y|100|N||CGV|CGV|N\r\nY|CGW|Invesco
        S&P Global Water Index ETF|P| |Y|100|N||CGW|CGW|N\r\nY|CGXU|Capital Group
        International Focus Equity ETF Capital Group International Focus Equity ETF|P|
        |Y|100|N||CGXU|CGXU|N\r\nY|CHAA|Catcha Investment Corp. Class A Ordinary Shares|A|
        |N|100|N||CHAA|CHAA|N\r\nY|CHAT|Return Stacked Bonds & Managed Futures ETF
        Roundhill Generative AI & Technology ETF|P| |Y|100|N||CHAT|CHAT|N\r\nY|CHAU|Direxion
        Daily CSI 300 China A Share Bull 2X Shares|P| |Y|100|N||CHAU|CHAU|N\r\nY|CHCI|Comstock
        Holding Companies, Inc. - Class A Common Stock|Q|S|N|100|N|N||CHCI|N\r\nY|CHCO|City
        Holding Company - Common Stock|Q|Q|N|100|N|N||CHCO|N\r\nY|CHCT|Community Healthcare
        Trust Incorporated Common Stock|N| |N|100|N||CHCT|CHCT|N\r\nY|CHD|Church &
        Dwight Company, Inc. Common Stock|N| |N|100|N||CHD|CHD|N\r\nY|CHDN|Churchill
        Downs, Incorporated - Common Stock|Q|Q|N|100|N|N||CHDN|N\r\nY|CHE|Chemed Corp|N|
        |N|100|N||CHE|CHE|N\r\nY|CHEB.U|Chenghe Acquisition II Co. Units, each consisting
        of one Class A ordinary share and one-half of one redeemable warrant|A| |N|100|N||CHEB.U|CHEB=|N\r\nY|CHEF|The
        Chefs' Warehouse, Inc. - Common Stock|Q|Q|N|100|N|N||CHEF|N\r\nY|CHEK|Check-Cap
        Ltd. - Ordinary Share|Q|S|N|100|N|N||CHEK|N\r\nY|CHGG|Chegg, Inc. Common Stock|N|
        |N|100|N||CHGG|CHGG|N\r\nY|CHGX|AXS Change Finance ESG ETF|P| |Y|100|N||CHGX|CHGX|N\r\nY|CHH|Choice
        Hotels International, Inc. Common Stock|N| |N|100|N||CHH|CHH|N\r\nY|CHI|Calamos
        Convertible Opportunities and Income Fund - Closed End Fund|Q|Q|N|100|N|N||CHI|N\r\nY|CHIQ|Global
        X MSCI China Consumer Discretionary ETF|P| |Y|100|N||CHIQ|CHIQ|N\r\nY|CHK|Chesapeake
        Energy Corporation - Common Stock|Q|Q|N|100|N|N||CHK|N\r\nY|CHKEL|Chesapeake
        Energy Corporation - Class C Warrants|Q|Q|N|100|N|N||CHKEL|N\r\nY|CHKEW|Chesapeake
        Energy Corporation - Class A Warrants|Q|S|N|100|N|N||CHKEW|N\r\nY|CHKEZ|Chesapeake
        Energy Corporation - Class B Warrants|Q|S|N|100|N|N||CHKEZ|N\r\nY|CHKP|Check
        Point Software Technologies Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CHKP|N\r\nY|CHMG|Chemung
        Financial Corp  - Common Stock|Q|Q|N|100|N|N||CHMG|N\r\nY|CHMI|Cherry Hill
        Mortgage Investment Corporation Common Stock|N| |N|100|N||CHMI|CHMI|N\r\nY|CHMI$A|Cherry
        Hill Mortgage Investment Corporation 8.20% Series A Cumulative Redeemable
        Preferred Stock|N| |N|100|N||CHMIpA|CHMI-A|N\r\nY|CHMI$B|Cherry Hill Mortgage
        Investment Corporation 8.250% Series B Fixed-to-Floating Rate Cumulative Redeemable
        Preferred Stock|N| |N|100|N||CHMIpB|CHMI-B|N\r\nY|CHN|China Fund, Inc. (The)
        Common Stock|N| |N|100|N||CHN|CHN|N\r\nY|CHNR|China Natural Resources, Inc.
        - Common Shares|Q|S|N|100|N|N||CHNR|N\r\nY|CHPS|Xtrackers Semiconductor Select
        Equity ETF|Q|G|Y|100|N|N||CHPS|N\r\nY|CHPT|ChargePoint Holdings, Inc. Common
        Stock|N| |N|100|N||CHPT|CHPT|N\r\nY|CHR|Cheer Holding, Inc.  - Ordinary Share|Q|S|N|100|N|N||CHR|N\r\nY|CHRD|Chord
        Energy Corporation - Common Stock|Q|Q|N|100|N|N||CHRD|N\r\nY|CHRO|Chromocell
        Therapeutics Corporation Common Stock|A| |N|100|N||CHRO|CHRO|N\r\nY|CHRS|Coherus
        BioSciences, Inc. - Common Stock|Q|G|N|100|N|N||CHRS|N\r\nY|CHRW|C.H. Robinson
        Worldwide, Inc. - Common Stock|Q|Q|N|100|N|N||CHRW|N\r\nY|CHSCL|CHS Inc -
        Class B Cumulative Redeemable Preferred Stock, Series 4|Q|Q|N|100|N|N||CHSCL|N\r\nY|CHSCM|CHS
        Inc - Class B Reset Rate Cumulative Redeemable Preferred Stock, Series 3|Q|Q|N|100|N|N||CHSCM|N\r\nY|CHSCN|CHS
        Inc - Preferred Class B Series 2 Reset Rate|Q|Q|N|100|N|N||CHSCN|N\r\nY|CHSCO|CHS
        Inc - Class B Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||CHSCO|N\r\nY|CHSCP|CHS
        Inc - 8%  Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||CHSCP|N\r\nY|CHSN|Chanson
        International Holding - Class A Ordinary Shares|Q|S|N|100|N|N||CHSN|N\r\nY|CHT|Chunghwa
        Telecom Co., Ltd.|N| |N|100|N||CHT|CHT|N\r\nY|CHTR|Charter Communications,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||CHTR|N\r\nY|CHUY|Chuy's Holdings,
        Inc. - Common Stock|Q|Q|N|100|N|N||CHUY|N\r\nY|CHW|Calamos Global Dynamic
        Income Fund - Closed End Fund|Q|Q|N|100|N|N||CHW|N\r\nY|CHWY|Chewy, Inc. Class
        A Common Stock|N| |N|100|N||CHWY|CHWY|N\r\nY|CHX|ChampionX Corporation - Common
        Stock|Q|Q|N|100|N|N||CHX|N\r\nY|CHY|Calamos Convertible and High Income Fund
        - Closed End Fund|Q|Q|N|100|N|N||CHY|N\r\nY|CI|The Cigna Group Common Stock|N|
        |N|100|N||CI|CI|N\r\nY|CIA|Citizens, Inc. Class A Common Stock ($1.00 Par)|N|
        |N|100|N||CIA|CIA|N\r\nY|CIB|BanColombia S.A. Common Stock|N| |N|100|N||CIB|CIB|N\r\nY|CIBR|First
        Trust NASDAQ Cybersecurity ETF|Q|G|Y|100|N|N||CIBR|N\r\nY|CID|VictoryShares
        International High Div Volatility Wtd ETF|Q|G|Y|100|N|N||CID|N\r\nY|CIEN|Ciena
        Corporation Common Stock|N| |N|100|N||CIEN|CIEN|N\r\nY|CIF|MFS Intermediate
        High Income Fund Common Stock|N| |N|100|N||CIF|CIF|N\r\nY|CIFR|Cipher Mining
        Inc. - Common Stock|Q|Q|N|100|N|N||CIFR|N\r\nY|CIFRW|Cipher Mining Inc. -
        Warrant|Q|Q|N|100|N|N||CIFRW|N\r\nY|CIG|Comp En De Mn Cemig ADS American Depositary
        Shares|N| |N|100|N||CIG|CIG|N\r\nY|CIG.C|Comp En De Mn Cemig ADS American
        Depositary Receipts|N| |N|100|N||CIG.C|CIG.C|N\r\nY|CIGI|Colliers International
        Group Inc.  - Subordinate Voting Shares|Q|Q|N|100|N|N||CIGI|N\r\nY|CII|Blackrock
        Capital and Income Fund, Inc.|N| |N|100|N||CII|CII|N\r\nY|CIK|Credit Suisse
        Asset Management Income Fund, Inc. Common Stock|A| |N|100|N||CIK|CIK|N\r\nY|CIL|VictoryShares
        International Volatility Wtd ETF|Q|G|Y|100|N|N||CIL|N\r\nY|CIM|Chimera Investment
        Corporation Common Stock|N| |N|100|N||CIM|CIM|N\r\nY|CIM$A|Chimera Investment
        Corporation 8.00% Series A Cumulative Redeemable Preferred Stock|N| |N|100|N||CIMpA|CIM-A|N\r\nY|CIM$B|Chimera
        Investment Corporation 8.00% Series B Fixed-to-Floating Rate Cumulative Redeemable
        Preferred Stock|N| |N|100|N||CIMpB|CIM-B|N\r\nY|CIM$C|Chimera Investment Corporation
        7.75% Series C Fixed-to-Floating Rate  Cumulative Redeemable  Preferred Stock|N|
        |N|100|N||CIMpC|CIM-C|N\r\nY|CIM$D|Chimera Investment Corporation 8.00% Series
        D Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|N| |N|100|N||CIMpD|CIM-D|N\r\nY|CIMN|Chimera
        Investment Corporation 9.000% Senior Notes due 2029|N| |N|100|N||CIMN|CIMN|N\r\nY|CINF|Cincinnati
        Financial Corporation - Common Stock|Q|Q|N|100|N|N||CINF|N\r\nY|CING|Cingulate
        Inc. - Common Stock|Q|S|N|100|N|D||CING|N\r\nY|CINGW|Cingulate Inc. - Warrants|Q|S|N|100|N|N||CINGW|N\r\nY|CINT|CI&T
        Inc Class A Common Shares|N| |N|100|N||CINT|CINT|N\r\nY|CIO|City Office REIT,
        Inc. Common Stock|N| |N|100|N||CIO|CIO|N\r\nY|CIO$A|City Office REIT, Inc.
        6.625% Series A Cumulative Redeemable Preferred Stock|N| |N|100|N||CIOpA|CIO-A|N\r\nY|CION|CION
        Investment Corporation Common Stock|N| |N|100|N||CION|CION|N\r\nY|CISO|CISO
        Global, Inc. - Common Stock|Q|S|N|100|N|N||CISO|N\r\nY|CISS|C3is Inc. - Common
        Stock|Q|S|N|100|N|N||CISS|N\r\nY|CITE|Cartica Acquisition Corp - Class A Ordinary
        Shares|Q|G|N|100|N|D||CITE|N\r\nY|CITEU|Cartica Acquisition Corp - Unit|Q|G|N|100|N|N||CITEU|N\r\nY|CITEW|Cartica
        Acquisition Corp - Warrant|Q|G|N|100|N|N||CITEW|N\r\nY|CIVB|Civista Bancshares,
        Inc.  - Common Stock|Q|S|N|100|N|N||CIVB|N\r\nY|CIVI|Civitas Resources, Inc.
        Common Stock|N| |N|100|N||CIVI|CIVI|N\r\nY|CIX|CompX International Inc. Common
        Stock|A| |N|100|N||CIX|CIX|N\r\nY|CIZ|VictoryShares Developed Enhanced Volatility
        Wtd ETF|Q|G|Y|100|N|N||CIZ|N\r\nY|CJET|Chijet Motor Company, Inc. - Ordinary
        Shares|Q|G|N|100|N|D||CJET|N\r\nY|CJJD|China Jo-Jo Drugstores, Inc. - Ordinary
        Shares|Q|S|N|100|N|N||CJJD|N\r\nY|CKPT|Checkpoint Therapeutics, Inc. - Common
        Stock|Q|S|N|100|N|N||CKPT|N\r\nY|CKX|CKX Lands, Inc. Common Stock|A| |N|100|N||CKX|CKX|N\r\nY|CL|Colgate-Palmolive
        Company Common Stock|N| |N|100|N||CL|CL|N\r\nY|CLAR|Clarus Corporation - Common
        Stock|Q|Q|N|100|N|N||CLAR|N\r\nY|CLB|Core Laboratories Inc. Common Stock|N|
        |N|100|N||CLB|CLB|N\r\nY|CLBK|Columbia Financial, Inc. - Common Stock|Q|Q|N|100|N|N||CLBK|N\r\nY|CLBR|Colombier
        Acquisition Corp. II Class A Ordinary Shares|N| |N|100|N||CLBR|CLBR|N\r\nY|CLBR.U|Colombier
        Acquisition Corp. II Units, each consisting of one Class A ordinary share
        and one-third of one redeemable warrant|N| |N|100|N||CLBR.U|CLBR=|N\r\nY|CLBR.W|Colombier
        Acquisition Corp. II Warrants, each whole warrant exercisable for one Class
        A Ordinary Share at an exercise price of $11.50 per share|N| |N|100|N||CLBR.WS|CLBR+|N\r\nY|CLBT|Cellebrite
        DI Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CLBT|N\r\nY|CLBTW|Cellebrite DI Ltd.
        - Warrants|Q|Q|N|100|N|N||CLBTW|N\r\nY|CLCO|Cool Company Ltd. Common Shares|N|
        |N|100|N||CLCO|CLCO|N\r\nY|CLDI|Calidi Biotherapeutics, Inc. Common Stock|A|
        |N|100|N||CLDI|CLDI|N\r\nY|CLDI.W|Calidi Biotherapeutics, Inc. Redeemable
        Warrants, each whole warrant exercisable for one share of Class A common stock
        at an exercise price of $11.50 per share|A| |N|100|N||CLDI.WS|CLDI+|N\r\nY|CLDL|Direxion
        Daily Cloud Computing Bull 2X Shares|P| |Y|100|N||CLDL|CLDL|N\r\nY|CLDT|Chatham
        Lodging Trust (REIT) Common Shares of Beneficial Interest|N| |N|100|N||CLDT|CLDT|N\r\nY|CLDT$A|Chatham
        Lodging Trust (REIT) 6.625% Series A Cumulative Redeemable Preferred Shares
        of Beneficial Interest|N| |N|100|N||CLDTpA|CLDT-A|N\r\nY|CLDX|Celldex Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||CLDX|N\r\nY|CLEU|China Liberal Education
        Holdings Limited - Ordinary Shares|Q|S|N|100|N|N||CLEU|N\r\nY|CLF|Cleveland-Cliffs
        Inc. Common Stock|N| |N|100|N||CLF|CLF|N\r\nY|CLFD|Clearfield, Inc. - Common
        Stock|Q|G|N|100|N|N||CLFD|N\r\nY|CLGN|CollPlant Biotechnologies Ltd. - Ordinary
        Shares|Q|G|N|100|N|N||CLGN|N\r\nY|CLH|Clean Harbors, Inc. Common Stock|N|
        |N|100|N||CLH|CLH|N\r\nY|CLIA|Return Stacked Bonds & Managed Futures ETF Veridien
        Climate Action ETF|P| |Y|100|N||CLIA|CLIA|N\r\nY|CLIP|Global X Funds Global
        X 1-3 Month T-Bill ETF|P| |Y|100|N||CLIP|CLIP|N\r\nY|CLIR|ClearSign Technologies
        Corporation - Common Stock|Q|S|N|100|N|D||CLIR|N\r\nY|CLIX|ProShares Long
        Online/Short Stores ETF|P| |Y|100|N||CLIX|CLIX|N\r\nY|CLLS|Cellectis S.A.
        - American Depositary Shares|Q|G|N|100|N|N||CLLS|N\r\nY|CLM|Cornerstone Strategic
        Value Fund, Inc. New Common Stock|A| |N|100|N||CLM|CLM|N\r\nY|CLMB|Climb Global
        Solutions, Inc. - Common Stock|Q|G|N|100|N|N||CLMB|N\r\nY|CLMT|Calumet Specialty
        Products Partners, L.P. - Common units representing limited partner interests|Q|Q|N|100|N|N||CLMT|N\r\nY|CLNE|Clean
        Energy Fuels Corp. - Common Stock|Q|Q|N|100|N|N||CLNE|N\r\nY|CLNN|Clene Inc.
        - Common Stock|Q|S|N|100|N|D||CLNN|N\r\nY|CLNNW|Clene Inc. - Warrant|Q|S|N|100|N|N||CLNNW|N\r\nY|CLNR|IQ
        Cleaner Transport ETF|P| |Y|100|N||CLNR|CLNR|N\r\nY|CLOA|BlackRock AAA CLO
        ETF|Q|G|Y|100|N|N||CLOA|N\r\nY|CLOD|Themes Cloud Computing ETF|Q|G|Y|100|N|N||CLOD|N\r\nY|CLOE|Clover
        Leaf Capital Corp. - Class A Common Stock|Q|S|N|100|N|D||CLOE|N\r\nY|CLOER|Clover
        Leaf Capital Corp. - Rights|Q|S|N|100|N|D||CLOER|N\r\nY|CLOEU|Clover Leaf
        Capital Corp. - Unit|Q|S|N|100|N|D||CLOEU|N\r\nY|CLOI|VanEck ETF Trust VanEck
        CLO ETF|P| |Y|100|N||CLOI|CLOI|N\r\nY|CLOU|Global X Cloud Computing ETF|Q|G|Y|100|N|N||CLOU|N\r\nY|CLOV|Clover
        Health Investments, Corp.  - Class A Common stock|Q|Q|N|100|N|N||CLOV|N\r\nY|CLOX|Series
        Portfolios Trust Panagram AAA CLO ETF|P| |Y|100|N||CLOX|CLOX|N\r\nY|CLOZ|Series
        Portfolios Trust Panagram BBB-B CLO ETF|P| |Y|100|N||CLOZ|CLOZ|N\r\nY|CLPR|Clipper
        Realty Inc. Common Stock|N| |N|100|N||CLPR|CLPR|N\r\nY|CLPS|CLPS Incorporation
        - Common Stock|Q|G|N|100|N|D||CLPS|N\r\nY|CLPT|ClearPoint Neuro Inc. - Common
        Stock|Q|S|N|100|N|N||CLPT|N\r\nY|CLRB|Cellectar Biosciences, Inc. - Common
        Stock|Q|S|N|100|N|N||CLRB|N\r\nY|CLRC|ClimateRock - Class A Ordinary Shares|Q|G|N|100|N|D||CLRC|N\r\nY|CLRCR|ClimateRock
        - Right|Q|G|N|100|N|N||CLRCR|N\r\nY|CLRCU|ClimateRock - Unit|Q|G|N|100|N|N||CLRCU|N\r\nY|CLRCW|ClimateRock
        - Warrant|Q|G|N|100|N|N||CLRCW|N\r\nY|CLRO|ClearOne, Inc. - Common Stock|Q|S|N|100|N|N||CLRO|N\r\nY|CLS|Celestica,
        Inc. Common Stock|N| |N|100|N||CLS|CLS|N\r\nY|CLSD|Clearside Biomedical, Inc.
        - Common Stock|Q|G|N|100|N|N||CLSD|N\r\nY|CLSE|Trust for Professional Managers
        Convergence Long/Short Equity ETF|Z| |Y|100|N||CLSE|CLSE|N\r\nY|CLSK|CleanSpark,
        Inc. - Common Stock|Q|S|N|100|N|N||CLSK|N\r\nY|CLSM|Cabana Target Leading
        Sector Moderate ETF|Q|G|Y|100|N|N||CLSM|N\r\nY|CLST|Catalyst Bancorp, Inc.
        - common stock|Q|S|N|100|N|N||CLST|N\r\nY|CLVT|Clarivate Plc Ordinary Shares|N|
        |N|100|N||CLVT|CLVT|N\r\nY|CLW|Clearwater Paper Corporation Common Stock|N|
        |N|100|N||CLW|CLW|N\r\nY|CLWT|Euro Tech Holdings Company Limited - Ordinary
        Shares|Q|S|N|100|N|N||CLWT|N\r\nY|CLX|Clorox Company (The) Common Stock|N|
        |N|100|N||CLX|CLX|N\r\nY|CM|Canadian Imperial Bank of Commerce Common Stock|N|
        |N|100|N||CM|CM|N\r\nY|CMA|Comerica Incorporated Common Stock|N| |N|100|N||CMA|CMA|N\r\nY|CMAX|CareMax,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||CMAX|N\r\nY|CMAXW|CareMax, Inc.
        - Warrant|Q|Q|N|100|N|N||CMAXW|N\r\nY|CMBM|Cambium Networks Corporation -
        Ordinary Shares|Q|G|N|100|N|N||CMBM|N\r\nY|CMBS|iShares CMBS Bond ETF|P| |Y|100|N||CMBS|CMBS|N\r\nY|CMC|Commercial
        Metals Company Common Stock|N| |N|100|N||CMC|CMC|N\r\nY|CMCI|VanEck ETF Trust
        VanEck CMCI Commodity Strategy ETF|Z| |Y|100|N||CMCI|CMCI|N\r\nY|CMCL|Caledonia
        Mining Corporation Plc Common Shares|A| |N|100|N||CMCL|CMCL|N\r\nY|CMCM|Cheetah
        Mobile Inc. American Depositary Shares, each representing fifty (50) Class
        A Ordinary Shares|N| |N|100|N||CMCM|CMCM|N\r\nY|CMCO|Columbus McKinnon Corporation
        - Common Stock|Q|Q|N|100|N|N||CMCO|N\r\nY|CMCSA|Comcast Corporation - Class
        A Common Stock|Q|Q|N|100|N|N||CMCSA|N\r\nY|CMCT|Creative Media & Community
        Trust Corporation - Common Stock|Q|G|N|100|N|N||CMCT|N\r\nY|CMDT|PIMCO U.S.
        Treasury Index Fund PIMCO Commodity Strategy Active Exchange-Traded Fund|P|
        |Y|100|N||CMDT|CMDT|N\r\nY|CMDY|iShares Bloomberg Roll Select Commodity Strategy
        ETF|P| |Y|100|N||CMDY|CMDY|N\r\nY|CME|CME Group Inc. - Class A Common Stock|Q|Q|N|100|N|N||CME|N\r\nY|CMF|iShares
        California Muni Bond ETF|P| |Y|100|N||CMF|CMF|N\r\nY|CMG|Chipotle Mexican
        Grill, Inc. Common Stock|N| |N|100|N||CMG|CMG|N\r\nY|CMI|Cummins Inc. Common
        Stock|N| |N|100|N||CMI|CMI|N\r\nY|CMLS|Cumulus Media Inc. - Class A Common
        Stock|Q|G|N|100|N|N||CMLS|N\r\nY|CMMB|Chemomab Therapeutics Ltd.  - American
        Depositary Shares|Q|S|N|100|N|D||CMMB|N\r\nY|CMND|Clearmind Medicine Inc.
        - Common Shares|Q|S|N|100|N|N||CMND|N\r\nY|CMP|Compass Minerals Intl Inc Common
        Stock|N| |N|100|N||CMP|CMP|N\r\nY|CMPO|CompoSecure, Inc.  - Class A Common
        Stock|Q|G|N|100|N|N||CMPO|N\r\nY|CMPOW|CompoSecure, Inc.  - Warrant|Q|G|N|100|N|N||CMPOW|N\r\nY|CMPR|Cimpress
        plc - Ordinary Shares|Q|Q|N|100|N|N||CMPR|N\r\nY|CMPS|COMPASS Pathways Plc
        - American Depository Shares|Q|Q|N|100|N|N||CMPS|N\r\nY|CMPX|Compass Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||CMPX|N\r\nY|CMRE|Costamare Inc. Common
        Stock $0.0001 par value|N| |N|100|N||CMRE|CMRE|N\r\nY|CMRE$B|Costamare Inc.
        Perpetual Preferred Stock Series B (Marshall Islands)|N| |N|100|N||CMREpB|CMRE-B|N\r\nY|CMRE$C|Costamare
        Inc. Perpetual Preferred Series C (Marshall Islands)|N| |N|100|N||CMREpC|CMRE-C|N\r\nY|CMRE$D|Costamare
        Inc. 8.75% Series D Cumulative Redeemable Perpetual Preferred Stock|N| |N|100|N||CMREpD|CMRE-D|N\r\nY|CMRE$E|Costamare
        Inc. 8.875% Series E Cumulative Redeemable Perpetual Preferred Stock, par
        value $0.0001|N| |N|100|N||CMREpE|CMRE-E|N\r\nY|CMRX|Chimerix, Inc. - Common
        Stock|Q|G|N|100|N|N||CMRX|N\r\nY|CMS|CMS Energy Corporation Common Stock|N|
        |N|100|N||CMS|CMS|N\r\nY|CMS$B|CMS Energy Corporation Preferred Stock|N| |N|10|N||CMSpB|CMS-B|N\r\nY|CMS$C|CMS
        Energy Corporation Depositary Shares, each representing a 1/1,000th interest
        in a share of 4.200% Cumulative Redeemable Perpetual Preferred Stock, Series
        C|N| |N|100|N||CMSpC|CMS-C|N\r\nY|CMSA|CMS Energy Corporation 5.625% Junior
        Subordinated Notes due 2078|N| |N|100|N||CMSA|CMSA|N\r\nY|CMSC|CMS Energy
        Corporation 5.875% Junior Subordinated Notes due 2078|N| |N|100|N||CMSC|CMSC|N\r\nY|CMSD|CMS
        Energy Corporation 5.875% Junior Subordinated Notes due 2079|N| |N|100|N||CMSD|CMSD|N\r\nY|CMT|Core
        Molding Technologies Inc Common Stock|A| |N|100|N||CMT|CMT|N\r\nY|CMTG|Claros
        Mortgage Trust, Inc. Common Stock|N| |N|100|N||CMTG|CMTG|N\r\nY|CMTL|Comtech
        Telecommunications Corp. - Common Stock|Q|Q|N|100|N|N||CMTL|N\r\nY|CMU|MFS
        Municipal Income Trust Common Stock|N| |N|100|N||CMU|CMU|N\r\nY|CNA|CNA Financial
        Corporation Common Stock|N| |N|100|N||CNA|CNA|N\r\nY|CNBS|Amplify Seymour
        Cannabis ETF|P| |Y|100|N||CNBS|CNBS|N\r\nY|CNC|Centene Corporation Common
        Stock|N| |N|100|N||CNC|CNC|N\r\nY|CNCR|Range Cancer Therapeutics ETF|Q|G|Y|100|N|N||CNCR|N\r\nY|CNDA|Concord
        Acquisition Corp II Class A Common Stock|A| |N|100|N||CNDA|CNDA|N\r\nY|CNDA.U|Concord
        Acquisition Corp II Units|A| |N|100|N||CNDA.U|CNDA=|N\r\nY|CNDA.W|Concord
        Acquisition Corp II Warrants, each whole warrant exercisable for one share
        of Class A Common Stock at an exercise price of $11.50|A| |N|100|N||CNDA.WS|CNDA+|N\r\nY|CNDT|Conduent
        Incorporated - Common Stock|Q|Q|N|100|N|N||CNDT|N\r\nY|CNEQ|The Alger ETF
        Trust Alger Concentrated Equity ETF|P| |Y|100|N||CNEQ|CNEQ|N\r\nY|CNET|ZW
        Data Action Technologies Inc. - Common Stock|Q|S|N|100|N|H||CNET|N\r\nY|CNEY|CN
        Energy Group Inc. - Class A Ordinary Shares|Q|S|N|100|N|D||CNEY|N\r\nY|CNF|CNFinance
        Holdings Limited American Depositary Shares, each representing  twenty (20)
        Ordinary Shares|N| |N|100|N||CNF|CNF|N\r\nY|CNFR|Conifer Holdings, Inc. -
        Common Stock|Q|S|N|100|N|N||CNFR|N\r\nY|CNFRZ|Conifer Holdings, Inc. - 9.75%
        Senior Unsecured Notes due 2028|Q|G|N|100|N|N||CNFRZ|N\r\nY|CNGL|Canna-Global
        Acquisition Corp - Class A Common Stock|Q|S|N|100|N|H||CNGL|N\r\nY|CNGLU|Canna-Global
        Acquisition Corp - Unit|Q|S|N|100|N|H||CNGLU|N\r\nY|CNGLW|Canna-Global Acquisition
        Corp - Warrant|Q|S|N|100|N|H||CNGLW|N\r\nY|CNH|CNH Industrial N.V. Common
        Shares|N| |N|100|N||CNH|CNH|N\r\nY|CNI|Canadian National Railway Company Common
        Stock|N| |N|100|N||CNI|CNI|N\r\nY|CNK|Cinemark Holdings Inc Cinemark Holdings,
        Inc. Common Stock|N| |N|100|N||CNK|CNK|N\r\nY|CNM|Core & Main, Inc. Class
        A Common Stock|N| |N|100|N||CNM|CNM|N\r\nY|CNMD|CONMED Corporation Common
        Stock|N| |N|100|N||CNMD|CNMD|N\r\nY|CNNE|Cannae Holdings, Inc. Common Stock|N|
        |N|100|N||CNNE|CNNE|N\r\nY|CNO|CNO Financial Group, Inc. Common Stock|N| |N|100|N||CNO|CNO|N\r\nY|CNO$A|CNO
        Financial Group, Inc. 5.125% Subordinated Debentures due 2060|N| |N|100|N||CNOpA|CNO-A|N\r\nY|CNOB|ConnectOne
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||CNOB|N\r\nY|CNOBP|ConnectOne Bancorp,
        Inc. - Depositary Shares (each representing a 1/40th interest in a share of
        5.25% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series A,
        par value $0.00 per share)|Q|Q|N|100|N|N||CNOBP|N\r\nY|CNP|CenterPoint Energy,
        Inc (Holding Co) Common Stock|N| |N|100|N||CNP|CNP|N\r\nY|CNQ|Canadian Natural
        Resources Limited Common Stock|N| |N|100|N||CNQ|CNQ|N\r\nY|CNRG|SPDR S&P Kensho
        Clean Power ETF|P| |Y|100|N||CNRG|CNRG|N\r\nY|CNS|Cohen & Steers Inc Common
        Stock|N| |N|100|N||CNS|CNS|N\r\nY|CNSL|Consolidated Communications Holdings,
        Inc. - Common Stock|Q|Q|N|100|N|N||CNSL|N\r\nY|CNSP|CNS Pharmaceuticals, Inc.
        - Common Stock|Q|S|N|100|N|D||CNSP|N\r\nY|CNTA|Centessa Pharmaceuticals plc
        - American Depositary Shares|Q|Q|N|100|N|N||CNTA|N\r\nY|CNTB|Connect Biopharma
        Holdings Limited - American Depositary Shares|Q|G|N|100|N|N||CNTB|N\r\nY|CNTG|Centogene
        N.V. - Common Shares|Q|G|N|100|N|D||CNTG|N\r\nY|CNTX|Context Therapeutics
        Inc. - Common Stock|Q|S|N|100|N|N||CNTX|N\r\nY|CNTY|Century Casinos, Inc.
        - Common Stock|Q|S|N|100|N|N||CNTY|N\r\nY|CNVS|Cineverse Corp. - Class A Common
        Stock|Q|S|N|100|N|N||CNVS|N\r\nY|CNX|CNX Resources Corporation Common Stock|N|
        |N|100|N||CNX|CNX|N\r\nY|CNXC|Concentrix Corporation - Common Stock|Q|Q|N|100|N|N||CNXC|N\r\nY|CNXN|PC
        Connection, Inc. - Common Stock|Q|Q|N|100|N|N||CNXN|N\r\nY|CNXT|VanEck ChiNext
        ETF|P| |Y|100|N||CNXT|CNXT|N\r\nY|CNYA|iShares MSCI China A ETF|Z| |Y|100|N||CNYA|CNYA|N\r\nY|COAL|Exchange
        Traded Concepts Trust Range Global Coal Index ETF|P| |Y|100|N||COAL|COAL|N\r\nY|COCH|Envoy
        Medical, Inc. - Class A Common Stock|Q|S|N|100|N|N||COCH|N\r\nY|COCHW|Envoy
        Medical, Inc. - Warrant|Q|S|N|100|N|N||COCHW|N\r\nY|COCO|The Vita Coco Company,
        Inc. - Common Stock|Q|Q|N|100|N|N||COCO|N\r\nY|COCP|Cocrystal Pharma, Inc.
        - Common Stock|Q|S|N|100|N|N||COCP|N\r\nY|CODA|Coda Octopus Group, Inc. -
        Common stock|Q|S|N|100|N|N||CODA|N\r\nY|CODI|D/B/A Compass Diversified Holdings
        Shares of Beneficial Interest|N| |N|100|N||CODI|CODI|N\r\nY|CODI$A|Compass
        Diversified Holdings 7.250% Series A Preferred Shares representing beneficial
        interest in Compass Diversified Holdings|N| |N|100|N||CODIpA|CODI-A|N\r\nY|CODI$B|Compass
        Diversified Holdings 7.875% Series B Fixed-to-Floating Rate Cumulative Preferred
        Shares representing beneficial interests in Compass Diversified Holdings|N|
        |N|100|N||CODIpB|CODI-B|N\r\nY|CODI$C|Compass Diversified Holdings 7.875%
        Series C Cumulative Preferred Shares|N| |N|100|N||CODIpC|CODI-C|N\r\nY|CODX|Co-Diagnostics,
        Inc. - Common Stock|Q|S|N|100|N|N||CODX|N\r\nY|COE|51Talk Online Education
        Group American depositary shares, each representing 60 Class A ordinary shares|A|
        |N|100|N||COE|COE|N\r\nY|COEP|Coeptis Therapeutics Holdings, Inc. - Common
        Stock|Q|S|N|100|N|D||COEP|N\r\nY|COEPW|Coeptis Therapeutics Holdings, Inc.
        - Warrants|Q|S|N|100|N|N||COEPW|N\r\nY|COF|Capital One Financial Corporation
        Common Stock|N| |N|100|N||COF|COF|N\r\nY|COF$I|Capital One Financial Corporation
        Depositary shares each representing a 1/40th interest in a share of Fixed
        Rate Non-Cumulative Perpetual Preferred Stock, Series I of the Issuer|N| |N|100|N||COFpI|COF-I|N\r\nY|COF$J|Capital
        One Financial Corporation Depositary Shares, Each Representing a 1/40th Interest
        in a Share of Fixed Rate Non- Cumulative Perpetual Preferred Stock, Series
        J|N| |N|100|N||COFpJ|COF-J|N\r\nY|COF$K|Capital One Financial Corporation
        Depositary Shares, Each Representing a 1/40th Ownership Interest in a Share
        of Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series K|N| |N|100|N||COFpK|COF-K|N\r\nY|COF$L|Capital
        One Financial Corporation Depositary Shares, Each Representing a 1/40th Interest
        in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series
        L|N| |N|100|N||COFpL|COF-L|N\r\nY|COF$N|Capital One Financial Corporation
        Depositary Shares, Each Representing a 1/40th Ownership Interest in a Share
        of Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series N|N| |N|100|N||COFpN|COF-N|N\r\nY|COFS|ChoiceOne
        Financial Services, Inc. - Common Stock|Q|S|N|100|N|N||COFS|N\r\nY|COGT|Cogent
        Biosciences, Inc. - Common Stock|Q|Q|N|100|N|N||COGT|N\r\nY|COHN|Cohen & Company
        Inc.|A| |N|100|N||COHN|COHN|N\r\nY|COHR|Coherent Corp. Common Stock|N| |N|100|N||COHR|COHR|N\r\nY|COHU|Cohu,
        Inc. - Common Stock|Q|Q|N|100|N|N||COHU|N\r\nY|COIN|Coinbase Global, Inc.
        - Class A Common Stock|Q|Q|N|100|N|N||COIN|N\r\nY|COKE|Coca-Cola Consolidated,
        Inc. - Common Stock|Q|Q|N|100|N|N||COKE|N\r\nY|COLB|Columbia Banking System,
        Inc. - Common Stock|Q|Q|N|100|N|N||COLB|N\r\nY|COLD|Americold Realty Trust,
        Inc. Common Stock|N| |N|100|N||COLD|COLD|N\r\nY|COLL|Collegium Pharmaceutical,
        Inc. - Common Stock|Q|Q|N|100|N|N||COLL|N\r\nY|COLM|Columbia Sportswear Company
        - Common Stock|Q|Q|N|100|N|N||COLM|N\r\nY|COM|Direxion Auspice Broad Commodity
        Strategy ETF|P| |Y|100|N||COM|COM|N\r\nY|COMB|GraniteShares Bloomberg Commodity
        Broad Strategy No K-1 ETF|P| |Y|100|N||COMB|COMB|N\r\nY|COMM|CommScope Holding
        Company, Inc. - Common Stock|Q|Q|N|100|N|N||COMM|N\r\nY|COMP|Compass, Inc.
        Class A Common Stock|N| |N|100|N||COMP|COMP|N\r\nY|COMT|iShares GSCI Commodity
        Dynamic Roll Strategy ETF|Q|G|Y|100|N|N||COMT|N\r\nY|CONL|GraniteShares 2x
        Long COIN Daily ETF|Q|G|Y|100|N|N||CONL|N\r\nY|CONN|Conn's, Inc. - Common
        Stock|Q|Q|N|100|N|N||CONN|N\r\nY|CONY|Tidal ETF Trust II YieldMax COIN Option
        Income Strategy ETF|P| |Y|100|N||CONY|CONY|N\r\nY|COO|The Cooper Companies,
        Inc.  - Common Stock|Q|Q|N|100|N|N||COO|N\r\nY|COOK|Traeger, Inc. Common Stock|N|
        |N|100|N||COOK|COOK|N\r\nY|COOP|Mr. Cooper Group Inc. - Common Stock|Q|S|N|100|N|N||COOP|N\r\nY|COOT|Australian
        Oilseeds Holdings Limited - Ordinary Shares|Q|G|N|100|N|N||COOT|N\r\nY|COOTW|Australian
        Oilseeds Holdings Limited - Warrant|Q|G|N|100|N|N||COOTW|N\r\nY|COP|ConocoPhillips
        Common Stock|N| |N|100|N||COP|COP|N\r\nY|COPJ|Sprott Junior Copper Miners
        ETF|Q|G|Y|100|N|N||COPJ|N\r\nY|COPP|Sprott Copper Miners ETF|Q|G|Y|100|N|N||COPP|N\r\nY|COPX|Global
        X Copper Miners ETF|P| |Y|100|N||COPX|COPX|N\r\nY|COR|Cencora, Inc. Common
        Stock|N| |N|100|N||COR|COR|N\r\nY|CORN|Teucrium Corn Fund ETV|P| |Y|100|N||CORN|CORN|N\r\nY|CORP|Pimco
        Investment Grade Corporate Bond Index Exchange-Traded Fund|P| |Y|100|N||CORP|CORP|N\r\nY|CORT|Corcept
        Therapeutics Incorporated - Common Stock|Q|S|N|100|N|N||CORT|N\r\nY|CORZ|Core
        Scientific, Inc. - Common Stock|Q|Q|N|100|N|N||CORZ|N\r\nY|CORZW|Core Scientific,
        Inc. - Tranche 1 Warrants|Q|Q|N|100|N|N||CORZW|N\r\nY|CORZZ|Core Scientific,
        Inc. - Tranche 2 Warrants|Q|Q|N|100|N|N||CORZZ|N\r\nY|COSM|Cosmos Health Inc.
        - Common Stock|Q|S|N|100|N|H||COSM|N\r\nY|COST|Costco Wholesale Corporation
        - Common Stock|Q|Q|N|100|N|N||COST|N\r\nY|COTY|Coty Inc. Class A Common Stock|N|
        |N|100|N||COTY|COTY|N\r\nY|COUR|Coursera, Inc. Common Stock|N| |N|100|N||COUR|COUR|N\r\nY|COWG|Pacer
        US Large Cap Cash Cows Growth Leaders ETF|Q|G|Y|100|N|N||COWG|N\r\nY|COWS|Amplify
        Cash Flow Dividend Leaders ETF|Q|G|Y|100|N|N||COWS|N\r\nY|COWZ|Pacer US Cash
        Cows 100 ETF|Z| |Y|100|N||COWZ|COWZ|N\r\nY|COYA|Coya Therapeutics, Inc. -
        Common Stock|Q|S|N|100|N|N||COYA|N\r\nY|CP|Canadian Pacific Kansas City Limited
        Common Shares|N| |N|100|N||CP|CP|N\r\nY|CPA|Copa Holdings, S.A. Class A Common
        Stock|N| |N|100|N||CPA|CPA|N\r\nY|CPAC|Cementos Pacasmayo S.A.A. American
        Depositary Shares (Each representing five Common Shares)|N| |N|100|N||CPAC|CPAC|N\r\nY|CPAI|Northern
        Lights Fund Trust III Counterpoint Quantitative Equity ETF|P| |Y|100|N||CPAI|CPAI|N\r\nY|CPAY|Corpay,
        Inc. Common Stock|N| |N|100|N||CPAY|CPAY|N\r\nY|CPB|Campbell Soup Company
        Common Stock|N| |N|100|N||CPB|CPB|N\r\nY|CPBI|Central Plains Bancshares, Inc.
        - Common Stock|Q|S|N|100|N|N||CPBI|N\r\nY|CPER|United States Copper Index
        Fund ETV|P| |Y|100|N||CPER|CPER|N\r\nY|CPF|Central Pacific Financial Corp
        New|N| |N|100|N||CPF|CPF|N\r\nY|CPHC|Canterbury Park Holding Corporation -
        Common Stock|Q|G|N|100|N|N||CPHC|N\r\nY|CPHI|China Pharma Holdings, Inc. Common
        Stock|A| |N|100|N||CPHI|CPHI|N\r\nY|CPII|Tidal ETF Trust Ionic Inflation Protection
        ETF|P| |Y|100|N||CPII|CPII|N\r\nY|CPIX|Cumberland Pharmaceuticals Inc. - Common
        Stock|Q|Q|N|100|N|N||CPIX|N\r\nY|CPK|Chesapeake Utilities Corporation Common
        Stock|N| |N|100|N||CPK|CPK|N\r\nY|CPLP|Capital Product Partners L.P. - Common
        Units representing limited partner interests|Q|Q|N|100|N|N||CPLP|N\r\nY|CPLS|AB
        Core Plus Bond ETF|Q|G|Y|100|N|N||CPLS|N\r\nY|CPNG|Coupang, Inc. Class A Common
        Stock|N| |N|100|N||CPNG|CPNG|N\r\nY|CPNJ|Calamos ETF Trust Calamos Nasdaq
        - 100 Structured Alt Protection ETF -June|P| |Y|100|N||CPNJ|CPNJ|N\r\nY|CPOP|Pop
        Culture Group Co., Ltd - Class A Ordinary Shares|Q|S|N|100|N|N||CPOP|N\r\nY|CPRI|Capri
        Holdings Limited Ordinary Shares|N| |N|100|N||CPRI|CPRI|N\r\nY|CPRT|Copart,
        Inc. - Common Stock|Q|Q|N|100|N|N||CPRT|N\r\nY|CPRX|Catalyst Pharmaceuticals,
        Inc. - Common Stock|Q|S|N|100|N|N||CPRX|N\r\nY|CPS|Cooper-Standard Holdings
        Inc. Common Stock|N| |N|100|N||CPS|CPS|N\r\nY|CPSH|CPS Technologies Corp.
        - Common Stock|Q|S|N|100|N|N||CPSH|N\r\nY|CPSM|Calamos ETF Trust Calamos S&P
        500 Structured Alt Protection ETF  May|P| |Y|100|N||CPSM|CPSM|N\r\nY|CPSS|Consumer
        Portfolio Services, Inc. - Common Stock|Q|G|N|100|N|N||CPSS|N\r\nY|CPT|Camden
        Property Trust Common Stock|N| |N|100|N||CPT|CPT|N\r\nY|CPTN|Cepton, Inc.
        - Common Stock|Q|S|N|100|N|N||CPTN|N\r\nY|CPTNW|Cepton, Inc. - Warrant|Q|S|N|100|N|N||CPTNW|N\r\nY|CPZ|Calamos
        Long/Short Equity & Dynamic Income Trust - Closed End Fund|Q|Q|N|100|N|N||CPZ|N\r\nY|CQP|Cheniere
        Energy Partners, LP Common Units|N| |N|100|N||CQP|CQP|N\r\nY|CQQQ|Invesco
        China Technology ETF|P| |Y|100|N||CQQQ|CQQQ|N\r\nY|CR|Crane Company Common
        Stock|N| |N|100|N||CR|CR|N\r\nY|CRAI|CRA International,Inc. - Common Stock|Q|Q|N|100|N|N||CRAI|N\r\nY|CRAK|VanEck
        Oil Refiners ETF|P| |Y|100|N||CRAK|CRAK|N\r\nY|CRBG|Corebridge Financial Inc.
        Common Stock|N| |N|100|N||CRBG|CRBG|N\r\nY|CRBN|iShares MSCI ACWI Low Carbon
        Target ETF|P| |Y|100|N||CRBN|CRBN|N\r\nY|CRBP|Corbus Pharmaceuticals Holdings,
        Inc. - Common Stock|Q|S|N|100|N|N||CRBP|N\r\nY|CRBU|Caribou Biosciences, Inc.
        - Common Stock|Q|Q|N|100|N|N||CRBU|N\r\nY|CRC|California Resources Corporation
        Common Stock|N| |N|100|N||CRC|CRC|N\r\nY|CRCT|Cricut, Inc. - Class A common
        stock|Q|Q|N|100|N|N||CRCT|N\r\nY|CRD.A|Crawford & Company Common Stock|N|
        |N|100|N||CRD.A|CRD.A|N\r\nY|CRD.B|Crawford & Company Common Stock|N| |N|100|N||CRD.B|CRD.B|N\r\nY|CRDF|Cardiff
        Oncology, Inc. - Common Stock|Q|S|N|100|N|N||CRDF|N\r\nY|CRDL|Cardiol Therapeutics
        Inc. - Class A Common Shares|Q|S|N|100|N|N||CRDL|N\r\nY|CRDO|Credo Technology
        Group Holding Ltd - Ordinary Shares|Q|Q|N|100|N|N||CRDO|N\r\nY|CRDT|Simplify
        Exchange Traded Funds Simplify Opportunistic Income ETF|P| |Y|100|N||CRDT|CRDT|N\r\nY|CRED|Columbia
        ETF Trust I Columbia Research Enhanced Real Estate ETF|P| |Y|100|N||CRED|CRED|N\r\nY|CREG|Smart
        Powerr Corp. - Common Stock|Q|S|N|100|N|N||CREG|N\r\nY|CRESW|Cresud S.A.C.I.F.
        y A. - Warrant|Q|S|N|100|N|N||CRESW|N\r\nY|CRESY|Cresud S.A.C.I.F. y A. -
        American Depositary Shares, each representing ten shares of Common Stock|Q|Q|N|100|N|N||CRESY|N\r\nY|CREV|Carbon
        Revolution Public Limited Company - Ordinary Shares|Q|G|N|100|N|N||CREV|N\r\nY|CREVW|Carbon
        Revolution Public Limited Company - Warrant|Q|S|N|100|N|N||CREVW|N\r\nY|CREX|Creative
        Realities, Inc. - Common Stock|Q|S|N|100|N|N||CREX|N\r\nY|CRF|Cornerstone
        Total Return Fund, Inc. (The) Common Stock|A| |N|100|N||CRF|CRF|N\r\nY|CRGO|Freightos
        Limited - Ordinary shares|Q|S|N|100|N|N||CRGO|N\r\nY|CRGOW|Freightos Limited
        - Warrants|Q|S|N|100|N|N||CRGOW|N\r\nY|CRGX|CARGO Therapeutics, Inc. - Common
        Stock|Q|Q|N|100|N|N||CRGX|N\r\nY|CRGY|Crescent Energy Company Class A Common
        Stock|N| |N|100|N||CRGY|CRGY|N\r\nY|CRH|CRH PLC Ordinary Shares|N| |N|100|N||CRH|CRH|N\r\nY|CRI|Carter's,
        Inc. Common Stock|N| |N|100|N||CRI|CRI|N\r\nY|CRIS|Curis, Inc. - Common Stock|Q|S|N|100|N|N||CRIS|N\r\nY|CRIT|Exchange
        Traded Concepts Trust Optica Rare Earths & Critical Materials ETF|P| |Y|100|N||CRIT|CRIT|N\r\nY|CRK|Comstock
        Resources, Inc. Common Stock|N| |N|100|N||CRK|CRK|N\r\nY|CRKN|Crown Electrokinetics
        Corp. - Common Stock|Q|S|N|100|N|D||CRKN|N\r\nY|CRL|Charles River Laboratories
        International, Inc. Common Stock|N| |N|100|N||CRL|CRL|N\r\nY|CRM|Salesforce,
        Inc. Common Stock|N| |N|100|N||CRM|CRM|N\r\nY|CRMD|CorMedix Inc. - Common
        Stock|Q|G|N|100|N|N||CRMD|N\r\nY|CRML|Critical Metals Corp. - Ordinary Shares|Q|G|N|100|N|N||CRML|N\r\nY|CRMLW|Critical
        Metals Corp. - Warrants|Q|S|N|100|N|N||CRMLW|N\r\nY|CRMT|America's Car-Mart,
        Inc. - Common Stock|Q|Q|N|100|N|N||CRMT|N\r\nY|CRNC|Cerence Inc. - Common
        Stock|Q|Q|N|100|N|N||CRNC|N\r\nY|CRNT|Ceragon Networks Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CRNT|N\r\nY|CRNX|Crinetics
        Pharmaceuticals, Inc. - Common Stock|Q|Q|N|100|N|N||CRNX|N\r\nY|CRON|Cronos
        Group Inc. - Common Share|Q|G|N|100|N|N||CRON|N\r\nY|CROX|Crocs, Inc. - Common
        Stock|Q|Q|N|100|N|N||CROX|N\r\nY|CRPT|First Trust SkyBridge Crypto Industry
        and Digital Economy ETF|P| |Y|100|N||CRPT|CRPT|N\r\nY|CRS|Carpenter Technology
        Corporation Common Stock|N| |N|100|N||CRS|CRS|N\r\nY|CRSH|Tidal Trust II YieldMax
        Short TSLA Option Income Strategy ETF|P| |Y|100|N||CRSH|CRSH|N\r\nY|CRSP|CRISPR
        Therapeutics AG - Common Shares|Q|G|N|100|N|N||CRSP|N\r\nY|CRSR|Corsair Gaming,
        Inc. - Common Stock|Q|Q|N|100|N|N||CRSR|N\r\nY|CRT|Cross Timbers Royalty Trust
        Common Stock|N| |N|100|N||CRT|CRT|N\r\nY|CRTC|DBX ETF Trust Xtrackers US National
        Critical Technologies ETF|P| |Y|100|N||CRTC|CRTC|N\r\nY|CRTO|Criteo S.A. -
        American Depositary Shares|Q|Q|N|100|N|N||CRTO|N\r\nY|CRUS|Cirrus Logic, Inc.
        - Common Stock|Q|Q|N|100|N|N||CRUS|N\r\nY|CRUZ|Defiance Hotel, Airline, and
        Cruise ETF|P| |Y|100|N||CRUZ|CRUZ|N\r\nY|CRVL|CorVel Corp. - Common Stock|Q|Q|N|100|N|N||CRVL|N\r\nY|CRVO|CervoMed
        Inc. - Common Stock|Q|S|N|100|N|N||CRVO|N\r\nY|CRVS|Corvus Pharmaceuticals,
        Inc. - Common Stock|Q|G|N|100|N|N||CRVS|N\r\nY|CRWD|CrowdStrike Holdings,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||CRWD|N\r\nY|CRWS|Crown Crafts,
        Inc. - Common Stock|Q|S|N|100|N|N||CRWS|N\r\nY|CSA|VictoryShares US Small
        Cap Volatility Wtd ETF|Q|G|Y|100|N|N||CSA|N\r\nY|CSAN|Cosan S.A. ADS|N| |N|100|N||CSAN|CSAN|N\r\nY|CSB|VictoryShares
        US Small Cap High Div Volatility Wtd ETF|Q|G|Y|100|N|N||CSB|N\r\nY|CSBR|Champions
        Oncology, Inc. - Common Stock|Q|S|N|100|N|N||CSBR|N\r\nY|CSCO|Cisco Systems,
        Inc. - Common Stock|Q|Q|N|100|N|N||CSCO|N\r\nY|CSD|Invesco S&P Spin-Off ETF|P|
        |Y|100|N||CSD|CSD|N\r\nY|CSF|VictoryShares US Discovery Enhanced Volatility
        Wtd ETF|Q|G|Y|100|N|N||CSF|N\r\nY|CSGP|CoStar Group, Inc. - Common Stock|Q|Q|N|100|N|N||CSGP|N\r\nY|CSGS|CSG
        Systems International, Inc. - Common Stock|Q|Q|N|100|N|N||CSGS|N\r\nY|CSHI|NEOS
        Enhanced Income 1-3 Month T-Bill ETF|P| |Y|100|N||CSHI|CSHI|N\r\nY|CSIQ|Canadian
        Solar Inc. - Common Shares|Q|Q|N|100|N|N||CSIQ|N\r\nY|CSL|Carlisle Companies
        Incorporated Common Stock|N| |N|100|N||CSL|CSL|N\r\nY|CSLM|CSLM Acquisition
        Corp. - Class A Ordinary Share|Q|S|N|100|N|N||CSLM|N\r\nY|CSLMR|CSLM Acquisition
        Corp. - Right|Q|S|N|100|N|N||CSLMR|N\r\nY|CSLMU|CSLM Acquisition Corp. - Unit|Q|S|N|100|N|N||CSLMU|N\r\nY|CSLMW|CSLM
        Acquisition Corp. - Warrant|Q|S|N|100|N|N||CSLMW|N\r\nY|CSLR|Complete Solaria,
        Inc. - Common Stock|Q|G|N|100|N|N||CSLR|N\r\nY|CSLRW|Complete Solaria, Inc.
        - Warrant|Q|S|N|100|N|N||CSLRW|N\r\nY|CSM|ProShares Large Cap Core Plus|Z|
        |Y|100|N||CSM|CSM|N\r\nY|CSMD|Professionally Managed Portfolios Congress SMid
        Growth ETF|P| |Y|100|N||CSMD|CSMD|N\r\nY|CSPI|CSP Inc. - Common Stock|Q|G|N|100|N|N||CSPI|N\r\nY|CSQ|Calamos
        Strategic Total Return Fund - Closed End Fund|Q|Q|N|100|N|N||CSQ|N\r\nY|CSR|D/B/A
        Centerspace Common Stock|N| |N|100|N||CSR|CSR|N\r\nY|CSR$C|D/B/A Centerspace
        6.625% Series C |N| |N|100|N||CSRpC|CSR-C|N\r\nY|CSSE|Chicken Soup for the
        Soul Entertainment, Inc. - Class A Common Stock|Q|G|N|100|N|D||CSSE|N\r\nY|CSSEL|Chicken
        Soup for the Soul Entertainment, Inc. - Warrant|Q|G|N|100|N|D||CSSEL|N\r\nY|CSSEN|Chicken
        Soup for the Soul Entertainment, Inc. - 9.50% Notes due 2025|Q|G|N|100|N|D||CSSEN|N\r\nY|CSSEP|Chicken
        Soup for the Soul Entertainment, Inc. - 9.75% Series A Cumulative Redeemable
        Perpetual Preferred Stock|Q|G|N|100|N|D||CSSEP|N\r\nY|CSTE|Caesarstone Ltd.
        - Ordinary Shares|Q|Q|N|100|N|N||CSTE|N\r\nY|CSTL|Castle Biosciences, Inc.
        - Common stock|Q|G|N|100|N|N||CSTL|N\r\nY|CSTM|Constellium SE Ordinary Shares
        (France)|N| |N|100|N||CSTM|CSTM|N\r\nY|CSV|Carriage Services, Inc. Common
        Stock|N| |N|100|N||CSV|CSV|N\r\nY|CSWC|Capital Southwest Corporation - Common
        Stock|Q|Q|N|100|N|N||CSWC|N\r\nY|CSWCZ|Capital Southwest Corporation - 7.75%
        Notes due 2028|Q|Q|N|100|N|N||CSWCZ|N\r\nY|CSWI|CSW Industrials, Inc. - Common
        Stock|Q|Q|N|100|N|N||CSWI|N\r\nY|CSX|CSX Corporation - Common Stock|Q|Q|N|100|N|N||CSX|N\r\nY|CTA|Simplify
        Exchange Traded Funds Simplify Managed Futures Strategy ETF|P| |Y|100|N||CTA|CTA|N\r\nY|CTA$A|EIDP,
        Inc. Preferred Stock $3.50 Series|N| |N|100|N||CTApA|CTA-A|N\r\nY|CTA$B|EIDP,
        Inc. Preferred Stock $4.50 Series|N| |N|100|N||CTApB|CTA-B|N\r\nY|CTAS|Cintas
        Corporation - Common Stock|Q|Q|N|100|N|N||CTAS|N\r\nY|CTBB|Qwest Corporation
        6.5% Notes due 2056|N| |N|100|N||CTBB|CTBB|N\r\nY|CTBI|Community Trust Bancorp,
        Inc. - Common Stock|Q|Q|N|100|N|N||CTBI|N\r\nY|CTCX|Carmell Corporation -
        Common Stock|Q|S|N|100|N|N||CTCX|N\r\nY|CTCXW|Carmell Corporation - Warrant|Q|S|N|100|N|N||CTCXW|N\r\nY|CTDD|Qwest
        Corporation 6.75% Notes due 2057|N| |N|100|N||CTDD|CTDD|N\r\nY|CTEC|Global
        X CleanTech ETF|Q|G|Y|100|N|N||CTEC|N\r\nY|CTEST|NYSE Test One Common Stock|N|
        |N|100|Y||CTEST|CTEST|N\r\nY|CTEST.E|NYSE Test One Common Stock|N| |N|100|Y||CTEST.E|CTEST.E|N\r\nY|CTEST.G|NYSE
        Test One Common Stock|N| |N|100|Y||CTEST.G|CTEST.G|N\r\nY|CTEST.L|NYSE Test
        One Common Stock|N| |N|100|Y||CTEST.L|CTEST.L|N\r\nY|CTEST.O|NYSE Test One
        Common Stock|N| |N|100|Y||CTEST.O|CTEST.O|N\r\nY|CTEST.S|NYSE Test Six Common
        Stock|N| |N|100|Y||CTEST.S|CTEST.S|N\r\nY|CTEST.V|NYSE Test One Common Stock|N|
        |N|100|Y||CTEST.V|CTEST.V|N\r\nY|CTEX|ProShares S&P Kensho Cleantech ETF|P|
        |Y|100|N||CTEX|CTEX|N\r\nY|CTGO|Contango ORE, Inc. Common Stock|A| |N|100|N||CTGO|CTGO|N\r\nY|CTHR|Charles
        & Colvard Ltd. - Common Stock|Q|S|N|100|N|N||CTHR|N\r\nY|CTKB|Cytek Biosciences,
        Inc. - Common Stock|Q|Q|N|100|N|N||CTKB|N\r\nY|CTLP|Cantaloupe, Inc. - Common
        Stock|Q|Q|N|100|N|N||CTLP|N\r\nY|CTLT|Catalent, Inc. Common Stock|N| |N|100|N||CTLT|CTLT|N\r\nY|CTM|Castellum,
        Inc. Common Stock|A| |N|100|N||CTM|CTM|N\r\nY|CTMX|CytomX Therapeutics, Inc.
        - Common Stock|Q|Q|N|100|N|N||CTMX|N\r\nY|CTNM|Contineum Therapeutics, Inc.
        - Common stock|Q|Q|N|100|N|N||CTNM|N\r\nY|CTNT|Cheetah Net Supply Chain Service
        Inc. - Class A Common Stock|Q|S|N|100|N|N||CTNT|N\r\nY|CTO|CTO Realty Growth,
        Inc. Common Stock|N| |N|100|N||CTO|CTO|N\r\nY|CTO$A|CTO Realty Growth, Inc.
        6.375% Series A Cumulative Redeemable Preferred Stock|N| |N|100|N||CTOpA|CTO-A|N\r\nY|CTOS|Custom
        Truck One Source, Inc. Common Stock|N| |N|100|N||CTOS|CTOS|N\r\nY|CTR|ClearBridge
        MLP and Midstream Total Return Fund Inc. Common Stock|N| |N|100|N||CTR|CTR|N\r\nY|CTRA|Coterra
        Energy Inc. Common Stock|N| |N|100|N||CTRA|CTRA|N\r\nY|CTRE|CareTrust REIT,
        Inc. Common Stock|N| |N|100|N||CTRE|CTRE|N\r\nY|CTRI|Centuri Holdings, Inc.
        Common Stock|N| |N|100|N||CTRI|CTRI|N\r\nY|CTRM|Castor Maritime Inc. - Common
        Shares|Q|S|N|100|N|N||CTRM|N\r\nY|CTRN|Citi Trends, Inc. - Common Stock|Q|Q|N|100|N|N||CTRN|N\r\nY|CTS|CTS
        Corporation Common Stock|N| |N|100|N||CTS|CTS|N\r\nY|CTSH|Cognizant Technology
        Solutions Corporation - Class A Common Stock|Q|Q|N|100|N|N||CTSH|N\r\nY|CTSO|Cytosorbents
        Corporation - Common Stock|Q|S|N|100|N|D||CTSO|N\r\nY|CTV|Innovid Corp. Common
        Stock|N| |N|100|N||CTV|CTV|N\r\nY|CTV.W|Innovid Corp. Warrants, each whole
        warrant exercisable for one share of Common Stock at an exercise price of
        $11.50 per share|N| |N|100|N||CTV.WS|CTV+|N\r\nY|CTVA|Corteva, Inc. Common
        Stock |N| |N|100|N||CTVA|CTVA|N\r\nY|CTXR|Citius Pharmaceuticals, Inc. - Common
        Stock|Q|S|N|100|N|D||CTXR|N\r\nY|CUBA|The Herzfeld Caribbean Basin Fund, Inc.
        - Closed End Fund|Q|S|N|100|N|N||CUBA|N\r\nY|CUBB|Customers Bancorp, Inc 5.375%
        Subordinated Notes Due 2034|N| |N|100|N||CUBB|CUBB|N\r\nY|CUBE|CubeSmart Common
        Shares|N| |N|100|N||CUBE|CUBE|N\r\nY|CUBI|Customers Bancorp, Inc Common Stock|N|
        |N|100|N||CUBI|CUBI|N\r\nY|CUBI$E|Customers Bancorp, Inc Fixed-to-Floating
        Rate Non-Cumulative Perpetual Preferred Stock, Series E|N| |N|100|N||CUBIpE|CUBI-E|N\r\nY|CUBI$F|Customers
        Bancorp, Inc Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock,
        Series F|N| |N|100|N||CUBIpF|CUBI-F|N\r\nY|CUBWU|Lionheart Holdings - Unit|Q|G|N|100|N|N||CUBWU|N\r\nY|CUE|Cue
        Biopharma, Inc. - Common Stock|Q|S|N|100|N|N||CUE|N\r\nY|CUK|Carnival Plc
        ADS ADS|N| |N|100|N||CUK|CUK|N\r\nY|CULL|Cullman Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||CULL|N\r\nY|CULP|Culp,
        Inc. Common Stock|N| |N|100|N||CULP|CULP|N\r\nY|CURE|Direxion Daily Healthcare
        Bull 3X Shares|P| |Y|100|N||CURE|CURE|N\r\nY|CURI|CuriosityStream Inc.  -
        Class A Common Stock|Q|S|N|100|N|N||CURI|N\r\nY|CURIW|CuriosityStream Inc.
        \ - Warrant|Q|S|N|100|N|N||CURIW|N\r\nY|CURV|Torrid Holdings Inc. Common Stock|N|
        |N|100|N||CURV|CURV|N\r\nY|CUT|Invesco MSCI Global Timber ETF|P| |Y|100|N||CUT|CUT|N\r\nY|CUTR|Cutera,
        Inc. - Common Stock|Q|Q|N|100|N|N||CUTR|N\r\nY|CUZ|Cousins Properties Incorporated
        Common Stock|N| |N|100|N||CUZ|CUZ|N\r\nY|CVAC|CureVac N.V. - Ordinary Shares|Q|G|N|100|N|N||CVAC|N\r\nY|CVAR|ETF
        Opportunities Trust Cultivar ETF|Z| |Y|100|N||CVAR|CVAR|N\r\nY|CVBF|CVB Financial
        Corporation - Common Stock|Q|Q|N|100|N|N||CVBF|N\r\nY|CVCO|Cavco Industries,
        Inc. - Common Stock|Q|Q|N|100|N|N||CVCO|N\r\nY|CVE|Cenovus Energy Inc Common
        Stock|N| |N|100|N||CVE|CVE|N\r\nY|CVE.W|Cenovus Energy Inc Warrants (each
        warrant entitles the holder to purchase one common share at an exercise price
        of C$6.54 per share)|N| |N|100|N||CVE.WS|CVE+|N\r\nY|CVEO|Civeo Corporation
        (Canada) Common Shares|N| |N|100|N||CVEO|CVEO|N\r\nY|CVGI|Commercial Vehicle
        Group, Inc. - Common Stock|Q|Q|N|100|N|N||CVGI|N\r\nY|CVGW|Calavo Growers,
        Inc. - Common Stock|Q|Q|N|100|N|N||CVGW|N\r\nY|CVI|CVR Energy Inc. Common
        Stock|N| |N|100|N||CVI|CVI|N\r\nY|CVIE|Morgan Stanley ETF Trust Calvert International
        Responsible Index ETF|P| |Y|100|N||CVIE|CVIE|N\r\nY|CVII|Churchill Capital
        Corp VII - Class A Common Stock|Q|G|N|100|N|D||CVII|N\r\nY|CVIIU|Churchill
        Capital Corp VII - Unit|Q|G|N|100|N|D||CVIIU|N\r\nY|CVIIW|Churchill Capital
        Corp VII - Warrant|Q|G|N|100|N|D||CVIIW|N\r\nY|CVKD|Cadrenal Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|D||CVKD|N\r\nY|CVLC|Morgan Stanley ETF Trust
        Calvert US Large-Cap Core Responsible Index ETF|P| |Y|100|N||CVLC|CVLC|N\r\nY|CVLG|Covenant
        Logistics Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||CVLG|N\r\nY|CVLT|Commvault
        Systems, Inc. - Common Stock|Q|Q|N|100|N|N||CVLT|N\r\nY|CVLY|Codorus Valley
        Bancorp, Inc - Common Stock|Q|G|N|100|N|N||CVLY|N\r\nY|CVM|Cel-Sci Corporation
        Common Stock|A| |N|100|N||CVM|CVM|N\r\nY|CVMC|Morgan Stanley ETF Trust Calvert
        US Mid-Cap Core Responsible Index ETF|P| |Y|100|N||CVMC|CVMC|N\r\nY|CVNA|Carvana
        Co. Class A Common Stock|N| |N|100|N||CVNA|CVNA|N\r\nY|CVR|Chicago Rivet &
        Machine Co. Common Stock|A| |N|100|N||CVR|CVR|N\r\nY|CVRD|Madison ETFs Trust
        Madison Covered Call ETF|P| |Y|100|N||CVRD|CVRD|N\r\nY|CVRT|Calamos ETF Trust
        Calamos Convertible Equity Alternative ETF|P| |Y|100|N||CVRT|CVRT|N\r\nY|CVRX|CVRx,
        Inc. - Common Stock|Q|Q|N|100|N|N||CVRX|N\r\nY|CVS|CVS Health Corporation
        Common Stock|N| |N|100|N||CVS|CVS|N\r\nY|CVSB|Morgan Stanley ETF Trust Calvert
        Ultra-Short Investment Grade ETF|P| |Y|100|N||CVSB|CVSB|N\r\nY|CVSE|Morgan
        Stanley ETF Trust Calvert US Select Equity ETF|P| |Y|100|N||CVSE|CVSE|N\r\nY|CVU|CPI
        Aerostructures, Inc. Common Stock|A| |N|100|N||CVU|CVU|N\r\nY|CVV|CVD Equipment
        Corporation - Common Stock|Q|S|N|100|N|N||CVV|N\r\nY|CVX|Chevron Corporation
        Common Stock|N| |N|100|N||CVX|CVX|N\r\nY|CVY|Invesco Zacks Multi-Asset Income
        ETF|P| |Y|100|N||CVY|CVY|N\r\nY|CW|Curtiss-Wright Corporation Common Stock|N|
        |N|100|N||CW|CW|N\r\nY|CWAN|Clearwater Analytics Holdings, Inc. Class A Common
        Stock|N| |N|100|N||CWAN|CWAN|N\r\nY|CWB|SPDR Bloomberg Convertible Securities
        ETF|P| |Y|100|N||CWB|CWB|N\r\nY|CWBC|Community West Bancshares - Common Stock|Q|S|N|100|N|N||CWBC|N\r\nY|CWCO|Consolidated
        Water Co. Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CWCO|N\r\nY|CWD|CaliberCos
        Inc. - Class A Common Stock|Q|S|N|100|N|D||CWD|N\r\nY|CWEB|Direxion Daily
        CSI China Internet Index Bull 2X Shares|P| |Y|100|N||CWEB|CWEB|N\r\nY|CWEN|Clearway
        Energy, Inc. Class C Common Stock|N| |N|100|N||CWEN|CWEN|N\r\nY|CWEN.A|Clearway
        Energy, Inc. Class A Common Stock|N| |N|100|N||CWEN.A|CWEN.A|N\r\nY|CWH|Camping
        World Holdings, Inc. Class A Common Stock|N| |N|100|N||CWH|CWH|N\r\nY|CWI|SPDR
        MSCI ACWI ex-US ETF|P| |Y|100|N||CWI|CWI|N\r\nY|CWK|Cushman & Wakefield plc
        Ordinary Shares|N| |N|100|N||CWK|CWK|N\r\nY|CWS|AdvisorShares Focused Equity
        ETF|P| |Y|100|N||CWS|CWS|N\r\nY|CWST|Casella Waste Systems, Inc. - Class A
        Common Stock|Q|Q|N|100|N|N||CWST|N\r\nY|CWT|California Water Service Group
        Common Stock|N| |N|100|N||CWT|CWT|N\r\nY|CX|Cemex, S.A.B. de C.V. Sponsored
        ADR|N| |N|100|N||CX|CX|N\r\nY|CXAI|CXApp Inc. - Class A Common Stock|Q|S|N|100|N|N||CXAI|N\r\nY|CXAIW|CXApp
        Inc. - Warrant|Q|S|N|100|N|N||CXAIW|N\r\nY|CXDO|Crexendo, Inc. - Common Stock|Q|S|N|100|N|N||CXDO|N\r\nY|CXE|MFS
        High Income Municipal Trust Common Stock|N| |N|100|N||CXE|CXE|N\r\nY|CXH|MFS
        Investment Grade Municipal Trust Common Stock|N| |N|100|N||CXH|CXH|N\r\nY|CXM|Sprinklr,
        Inc. Class A Common Stock|N| |N|100|N||CXM|CXM|N\r\nY|CXSE|WisdomTree China
        ex-State-Owned Enterprises Fund|Q|G|Y|100|N|N||CXSE|N\r\nY|CXT|Crane NXT,
        Co. Common Stock|N| |N|100|N||CXT|CXT|N\r\nY|CXW|CoreCivic, Inc. Common Stock|N|
        |N|100|N||CXW|CXW|N\r\nY|CYBN|Cybin Inc. Common Shares|A| |N|100|N||CYBN|CYBN|N\r\nY|CYBR|CyberArk
        Software Ltd. - Ordinary Shares|Q|Q|N|100|N|N||CYBR|N\r\nY|CYCC|Cyclacel Pharmaceuticals,
        Inc. - Common Stock|Q|S|N|100|N|D||CYCC|N\r\nY|CYCCP|Cyclacel Pharmaceuticals,
        Inc. - 6% Convertible Preferred Stock|Q|S|N|100|N|D||CYCCP|N\r\nY|CYCN|Cyclerion
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||CYCN|N\r\nY|CYD|China Yuchai
        International Limited Common Stock|N| |N|100|N||CYD|CYD|N\r\nY|CYH|Community
        Health Systems, Inc. Common Stock|N| |N|100|N||CYH|CYH|N\r\nY|CYN|Cyngn Inc.
        - Common stock|Q|S|N|100|N|D||CYN|N\r\nY|CYRX|CryoPort, Inc. - Common Stock|Q|S|N|100|N|N||CYRX|N\r\nY|CYTH|Cyclo
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||CYTH|N\r\nY|CYTHW|Cyclo Therapeutics,
        Inc. - Warrant|Q|S|N|100|N|N||CYTHW|N\r\nY|CYTK|Cytokinetics, Incorporated
        - Common Stock|Q|Q|N|100|N|N||CYTK|N\r\nY|CYTO|Altamira Therapeutics Ltd.
        - Common Shares|Q|S|N|100|N|N||CYTO|N\r\nY|CZA|Invesco Zacks Mid-Cap ETF|P|
        |Y|100|N||CZA|CZA|N\r\nY|CZAR|Themes Natural Monopoly ETF|Q|G|Y|100|N|N||CZAR|N\r\nY|CZFS|Citizens
        Financial Services, Inc. - Common Stock|Q|S|N|100|N|N||CZFS|N\r\nY|CZNC|Citizens
        & Northern Corp - Common Stock|Q|S|N|100|N|N||CZNC|N\r\nY|CZR|Caesars Entertainment,
        Inc. - Common Stock|Q|Q|N|100|N|N||CZR|N\r\nY|CZWI|Citizens Community Bancorp,
        Inc. - Common Stock|Q|G|N|100|N|N||CZWI|N\r\nY|D|Dominion Energy, Inc. Common
        Stock|N| |N|100|N||D|D|N\r\nY|DAC|Danaos Corporation Common Stock|N| |N|100|N||DAC|DAC|N\r\nY|DADA|Dada
        Nexus Limited - American Depositary Shares|Q|Q|N|100|N|N||DADA|N\r\nY|DAIO|Data
        I/O Corporation - Common Stock|Q|S|N|100|N|N||DAIO|N\r\nY|DAKT|Daktronics,
        Inc. - Common Stock|Q|Q|N|100|N|N||DAKT|N\r\nY|DAL|Delta Air Lines, Inc. Common
        Stock|N| |N|100|N||DAL|DAL|N\r\nY|DALI|First Trust Dorsey Wright DALI 1 ETF|Q|G|Y|100|N|N||DALI|N\r\nY|DALN|DallasNews
        Corporation - Series A Common Stock|Q|S|N|100|N|D||DALN|N\r\nY|DAN|Dana Incorporated
        Common Stock |N| |N|100|N||DAN|DAN|N\r\nY|DAO|Youdao, Inc. American Depositary
        Shares, each representing one Class A Ordinary Share|N| |N|100|N||DAO|DAO|N\r\nY|DAPP|VanEck
        Digital Transformation ETF|Q|G|Y|100|N|N||DAPP|N\r\nY|DAPR|FT Vest U.S. Equity
        Deep Buffer ETF - April|Z| |Y|100|N||DAPR|DAPR|N\r\nY|DAR|Darling Ingredients
        Inc. Common Stock|N| |N|100|N||DAR|DAR|N\r\nY|DARE|Dare Bioscience, Inc. -
        Common Stock|Q|S|N|100|N|D||DARE|N\r\nY|DARP|Return Stacked Bonds & Managed
        Futures ETF Grizzle Growth ETF|P| |Y|100|N||DARP|DARP|N\r\nY|DASH|DoorDash,
        Inc. - Common Stock|Q|Q|N|100|N|N||DASH|N\r\nY|DAT|ProShares Big Data Refiners
        ETF|P| |Y|100|N||DAT|DAT|N\r\nY|DATS|DatChat, Inc. - Common Stock|Q|S|N|100|N|N||DATS|N\r\nY|DATSW|DatChat,
        Inc. - Series A Warrant|Q|S|N|100|N|N||DATSW|N\r\nY|DAUG|FT Vest U.S. Equity
        Deep Buffer ETF - August|Z| |Y|100|N||DAUG|DAUG|N\r\nY|DAVA|Endava plc American
        Depositary Shares (each representing one Class A Ordinary Share)|N| |N|100|N||DAVA|DAVA|N\r\nY|DAVE|Dave
        Inc.  - Class A Common Stock|Q|G|N|100|N|N||DAVE|N\r\nY|DAVEW|Dave Inc.  -
        Warrants|Q|G|N|100|N|N||DAVEW|N\r\nY|DAWN|Day One Biopharmaceuticals, Inc.
        - Common Stock|Q|Q|N|100|N|N||DAWN|N\r\nY|DAX|Global X DAX Germany ETF|Q|G|Y|100|N|N||DAX|N\r\nY|DAY|Dayforce,
        Inc. Common Stock|N| |N|100|N||DAY|DAY|N\r\nY|DB|Deutsche Bank AG Common Stock|N|
        |N|100|N||DB|DB|N\r\nY|DBA|Invesco DB Agriculture Fund|P| |Y|100|N||DBA|DBA|N\r\nY|DBAW|Xtrackers
        MSCI All World ex US Hedged Equity ETF|P| |Y|100|N||DBAW|DBAW|N\r\nY|DBB|Invesco
        DB Base Metals Fund|P| |Y|100|N||DBB|DBB|N\r\nY|DBC|Invesco DB Commodity Index
        Tracking Fund|P| |Y|100|N||DBC|DBC|N\r\nY|DBD|Diebold Nixdorf Incorporated
        Common stock|N| |N|100|N||DBD|DBD|N\r\nY|DBE|Invesco DB Energy Fund|P| |Y|100|N||DBE|DBE|N\r\nY|DBEF|Xtrackers
        MSCI EAFE Hedged Equity ETF|P| |Y|100|N||DBEF|DBEF|N\r\nY|DBEH|iMGP DBi Hedge
        Strategy ETF|P| |Y|100|N||DBEH|DBEH|N\r\nY|DBEM|Xtrackers MSCI Emerging Markets
        Hedged Equity ETF|P| |Y|100|N||DBEM|DBEM|N\r\nY|DBEU|Xtrackers MSCI Europe
        Hedged Equity ETF|P| |Y|100|N||DBEU|DBEU|N\r\nY|DBEZ|Xtrackers MSCI Eurozone
        Hedged Equity ETF|P| |Y|100|N||DBEZ|DBEZ|N\r\nY|DBGI|Digital Brands Group,
        Inc. - Common Stock|Q|S|N|100|N|N||DBGI|N\r\nY|DBGIW|Digital Brands Group,
        Inc. - Warrant|Q|S|N|100|N|N||DBGIW|N\r\nY|DBI|Designer Brands Inc. Class
        A Common Stock|N| |N|100|N||DBI|DBI|N\r\nY|DBJP|Xtrackers MSCI Japan Hedged
        Equity ETF|P| |Y|100|N||DBJP|DBJP|N\r\nY|DBL|DoubleLine Opportunistic Credit
        Fund Common Shares of Beneficial Interest|N| |N|100|N||DBL|DBL|N\r\nY|DBMF|iMGP
        DBi Managed Futures Strategy ETF|P| |Y|100|N||DBMF|DBMF|N\r\nY|DBND|DoubleLine
        ETF Trust DoubleLine Opportunistic Bond ETF|P| |Y|100|N||DBND|DBND|N\r\nY|DBO|Invesco
        DB Oil Fund|P| |Y|100|N||DBO|DBO|N\r\nY|DBP|Invesco DB Precious Metals Fund|P|
        |Y|100|N||DBP|DBP|N\r\nY|DBRG|DigitalBridge Group, Inc.|N| |N|100|N||DBRG|DBRG|N\r\nY|DBRG$H|DigitalBridge
        Group, Inc. 7.125% Series H |N| |N|100|N||DBRGpH|DBRG-H|N\r\nY|DBRG$I|DigitalBridge
        Group, Inc. 7.15% Series I |N| |N|100|N||DBRGpI|DBRG-I|N\r\nY|DBRG$J|DigitalBridge
        Group, Inc. 7.125% Series J |N| |N|100|N||DBRGpJ|DBRG-J|N\r\nY|DBVT|DBV Technologies
        S.A. - American Depositary Shares|Q|S|N|100|N|D||DBVT|N\r\nY|DBX|Dropbox,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||DBX|N\r\nY|DC|Dakota Gold Corp.
        Common Stock|A| |N|100|N||DC|DC|N\r\nY|DC.W|Dakota Gold Corp. Warrants, each
        warrant exercisable for one Common Share at an exercise price of $2.08|A|
        |N|100|N||DC.WS|DC+|N\r\nY|DCBO|Docebo Inc. - Common Shares|Q|Q|N|100|N|N||DCBO|N\r\nY|DCF|BNY
        Mellon Alcentra Global Credit Income 2024 Target Term Fund, Inc. Common Stock|N|
        |N|100|N||DCF|DCF|N\r\nY|DCGO|DocGo Inc. - Common Stock|Q|S|N|100|N|N||DCGO|N\r\nY|DCI|Donaldson
        Company, Inc. Common Stock|N| |N|100|N||DCI|DCI|N\r\nY|DCMT|DoubleLine ETF
        Trust DoubleLine Commodity Strategy ETF|P| |Y|100|N||DCMT|DCMT|N\r\nY|DCO|Ducommun
        Incorporated Common Stock|N| |N|100|N||DCO|DCO|N\r\nY|DCOM|Dime Community
        Bancshares, Inc. - Common Stock|Q|Q|N|100|N|N||DCOM|N\r\nY|DCOMP|Dime Community
        Bancshares, Inc. - Fixed-Rate Non-Cumulative Perpetual Preferred Stock, Series
        A|Q|Q|N|100|N|N||DCOMP|N\r\nY|DCOR|Dimensional ETF Trust Dimensional US Core
        Equity 1 ETF|P| |Y|100|N||DCOR|DCOR|N\r\nY|DCRE|DoubleLine ETF Trust DoubleLine
        Commercial Real Estate ETF|P| |Y|100|N||DCRE|DCRE|N\r\nY|DCTH|Delcath Systems,
        Inc. - Common Stock|Q|S|N|100|N|D||DCTH|N\r\nY|DD|DuPont de Nemours, Inc.
        Common Stock|N| |N|100|N||DD|DD|N\r\nY|DDC|DDC Enterprise Limited Class A
        Ordinary Shares|A| |N|100|N||DDC|DDC|N\r\nY|DDD|3D Systems Corporation Common
        Stock|N| |N|100|N||DDD|DDD|N\r\nY|DDEC|FT Vest U.S. Equity Deep Buffer ETF
        - December|Z| |Y|100|N||DDEC|DDEC|N\r\nY|DDI|DoubleDown Interactive Co., Ltd.
        - American Depository Shares|Q|Q|N|100|N|N||DDI|N\r\nY|DDIV|First Trust Dorsey
        Wright Momentum & Dividend ETF|Q|G|Y|100|N|N||DDIV|N\r\nY|DDL|Dingdong (Cayman)
        Limited American Depositary Shares (each two representing three Ordinary Shares)|N|
        |N|100|N||DDL|DDL|N\r\nY|DDLS|WisdomTree Dynamic Currency Hedged International
        SmallCap Equity Fund|Z| |Y|100|N||DDLS|DDLS|N\r\nY|DDM|ProShares Ultra Dow30|P|
        |Y|100|N||DDM|DDM|N\r\nY|DDOG|Datadog, Inc. - Class A Common Stock|Q|Q|N|100|N|N||DDOG|N\r\nY|DDS|Dillard's,
        Inc. Common Stock|N| |N|100|N||DDS|DDS|N\r\nY|DDT|Dillard's Capital Trust
        I|N| |N|100|N||DDT|DDT|N\r\nY|DDWM|WisdomTree Dynamic Currency Hedged International
        Equity Fund|Z| |Y|100|N||DDWM|DDWM|N\r\nY|DE|Deere & Company Common Stock|N|
        |N|100|N||DE|DE|N\r\nY|DEA|Easterly Government Properties, Inc. Common Stock|N|
        |N|100|N||DEA|DEA|N\r\nY|DEC|Diversified Energy Company plc Ordinary Shares|N|
        |N|100|N||DEC|DEC|N\r\nY|DECA|Denali Capital Acquisition Corp. - Class A Ordinary
        Shares|Q|G|N|100|N|D||DECA|N\r\nY|DECAU|Denali Capital Acquisition Corp. -
        Unit|Q|G|N|100|N|D||DECAU|N\r\nY|DECAW|Denali Capital Acquisition Corp. -
        Warrant|Q|G|N|100|N|D||DECAW|N\r\nY|DECK|Deckers Outdoor Corporation Common
        Stock|N| |N|100|N||DECK|DECK|N\r\nY|DECP|SHL Telemedicine Ltd PGIM US Large-Cap
        Buffer 12 ETF - December|Z| |Y|100|N||DECP|DECP|N\r\nY|DECT|AIM ETF Products
        Trust AllianzIM U.S. Large Cap Buffer10 Dec ETF|P| |Y|100|N||DECT|DECT|N\r\nY|DECW|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer20 Dec ETF|P| |Y|100|N||DECW|DECW|N\r\nY|DECZ|TrueShares
        Structured Outcome (December) ETF|Z| |Y|100|N||DECZ|DECZ|N\r\nY|DEED|First
        Trust TCW Securitized Plus ETF|P| |Y|100|N||DEED|DEED|N\r\nY|DEEF|Xtrackers
        FTSE Developed ex US Multifactor ETF|P| |Y|100|N||DEEF|DEEF|N\r\nY|DEEP|Roundhill
        Acquirers Deep Value ETF|P| |Y|100|N||DEEP|DEEP|N\r\nY|DEFI|Tidal Commodities
        Trust I Hashdex Bitcoin ETF|P| |Y|100|N||DEFI|DEFI|N\r\nY|DEHP|Dimensional
        ETF Trust Dimensional Emerging Markets High Profitability ETF|P| |Y|100|N||DEHP|DEHP|N\r\nY|DEI|Douglas
        Emmett, Inc. Common Stock|N| |N|100|N||DEI|DEI|N\r\nY|DELL|Dell Technologies
        Inc. Class C Common Stock |N| |N|100|N||DELL|DELL|N\r\nY|DEM|WisdomTree Emerging
        Markets High Dividend Fund|P| |Y|100|N||DEM|DEM|N\r\nY|DEMZ|Democratic Large
        Cap Core ETF|Q|G|Y|100|N|N||DEMZ|N\r\nY|DENN|Denny's Corporation - Common
        Stock|Q|S|N|100|N|N||DENN|N\r\nY|DEO|Diageo plc Common Stock|N| |N|100|N||DEO|DEO|N\r\nY|DERM|Journey
        Medical Corporation - Common Stock|Q|S|N|100|N|N||DERM|N\r\nY|DES|WisdomTree
        U.S. SmallCap Dividend Fund|P| |Y|100|N||DES|DES|N\r\nY|DESK|VanEck ETF Trust
        VanEck Office and Commercial REIT ETF|P| |Y|100|N||DESK|DESK|N\r\nY|DESP|Despegar.com,
        Corp. Ordinary Shares|N| |N|100|N||DESP|DESP|N\r\nY|DEUS|Xtrackers Russell
        US Multifactor ETF|P| |Y|100|N||DEUS|DEUS|N\r\nY|DEW|WisdomTree Global High
        Dividend Fund|P| |Y|100|N||DEW|DEW|N\r\nY|DFAC|Dimensional ETF Trust Dimensional
        U.S. Core Equity 2 ETF|P| |Y|100|N||DFAC|DFAC|N\r\nY|DFAE|Dimensional Emerging
        Core Equity Market ETF|P| |Y|100|N||DFAE|DFAE|N\r\nY|DFAI|Dimensional International
        Core Equity Market ETF|P| |Y|100|N||DFAI|DFAI|N\r\nY|DFAR|Dimensional ETF
        Trust Dimensional US Real Estate ETF|P| |Y|100|N||DFAR|DFAR|N\r\nY|DFAS|Dimensional
        U.S. Small Cap ETF|P| |Y|100|N||DFAS|DFAS|N\r\nY|DFAT|Dimensional U.S. Targeted
        Value ETF|P| |Y|100|N||DFAT|DFAT|N\r\nY|DFAU|Dimensional US Core Equity Market
        ETF|P| |Y|100|N||DFAU|DFAU|N\r\nY|DFAW|Dimensional ETF Trust Dimensional World
        Equity ETF|P| |Y|100|N||DFAW|DFAW|N\r\nY|DFAX|Dimensional World ex U.S. Core
        Equity 2 ETF|P| |Y|100|N||DFAX|DFAX|N\r\nY|DFCA|Dimensional ETF Trust Dimensional
        California Municipal Bond ETF|P| |Y|100|N||DFCA|DFCA|N\r\nY|DFCF|Dimensional
        ETF Trust Dimensional Core Fixed Income ETF|P| |Y|100|N||DFCF|DFCF|N\r\nY|DFE|WisdomTree
        Europe SmallCap Dividend Fund|P| |Y|100|N||DFE|DFE|N\r\nY|DFEB|FT Vest U.S.
        Equity Deep Buffer ETF - February|Z| |Y|100|N||DFEB|DFEB|N\r\nY|DFEM|Dimensional
        ETF Trust Dimensional Emerging Markets Core Equity 2 ETF|P| |Y|100|N||DFEM|DFEM|N\r\nY|DFEN|Direxion
        Daily Aerospace & Defense Bull 3X Shares|P| |Y|100|N||DFEN|DFEN|N\r\nY|DFEV|Dimensional
        ETF Trust Dimensional Emerging Markets Value ETF|P| |Y|100|N||DFEV|DFEV|N\r\nY|DFGP|Dimensional
        Global Core Plus Fixed Income ETF|Q|G|Y|100|N|N||DFGP|N\r\nY|DFGR|Dimensional
        ETF Trust Dimensional Global Real Estate ETF|P| |Y|100|N||DFGR|DFGR|N\r\nY|DFGX|Dimensional
        Global ex US Core Fixed Income ETF|Q|G|Y|100|N|N||DFGX|N\r\nY|DFH|Dream Finders
        Homes, Inc. Class A Common Stock|N| |N|100|N||DFH|DFH|N\r\nY|DFHY|TrimTabs
        ETF Trust Donoghue Forlines Tactical High Yield ETF|Z| |Y|100|N||DFHY|DFHY|N\r\nY|DFIC|Dimensional
        ETF Trust Dimensional International Core Equity 2 ETF|Z| |Y|100|N||DFIC|DFIC|N\r\nY|DFIN|Donnelley
        Financial Solutions, Inc. Common Stock |N| |N|100|N||DFIN|DFIN|N\r\nY|DFIP|Dimensional
        ETF Trust Dimensional Inflation-Protected Securities ETF|P| |Y|100|N||DFIP|DFIP|N\r\nY|DFIS|Dimensional
        ETF Trust Dimensional International Small Cap ETF|Z| |Y|100|N||DFIS|DFIS|N\r\nY|DFIV|Dimensional
        International Value ETF|P| |Y|100|N||DFIV|DFIV|N\r\nY|DFJ|WisdomTree Japan
        SmallCap Fund|P| |Y|100|N||DFJ|DFJ|N\r\nY|DFLI|Dragonfly Energy Holdings Corp
        - Common Stock|Q|S|N|100|N|D||DFLI|N\r\nY|DFLIW|Dragonfly Energy Holdings
        Corp - Warrant|Q|S|N|100|N|N||DFLIW|N\r\nY|DFLV|Dimensional ETF Trust Dimensional
        US Large Cap Value ETF|P| |Y|100|N||DFLV|DFLV|N\r\nY|DFND|Siren DIVCON Dividend
        Defender ETF|Z| |Y|100|N||DFND|DFND|N\r\nY|DFNL|Davis Fundamental ETF Trust
        Davis Select Financial ETF|Z| |Y|100|N||DFNL|DFNL|N\r\nY|DFNM|Dimensional
        ETF Trust Dimensional National Municipal Bond ETF|P| |Y|100|N||DFNM|DFNM|N\r\nY|DFNV|TrimTabs
        ETF Trust Donoghue Forlines Risk Managed Innovation ETF|Z| |Y|100|N||DFNV|DFNV|N\r\nY|DFP|Flaherty
        & Crumrine Dynamic Preferred and Income Fund Inc. Common Stock|N| |N|100|N||DFP|DFP|N\r\nY|DFRA|Donoghue
        Forlines Yield Enhanced Real Asset ETF|Z| |Y|100|N||DFRA|DFRA|N\r\nY|DFS|Discover
        Financial Services Common Stock|N| |N|100|N||DFS|DFS|N\r\nY|DFSB|Dimensional
        ETF Trust Dimensional Global Sustainability Fixed Income ETF|P| |Y|100|N||DFSB|DFSB|N\r\nY|DFSD|Dimensional
        ETF Trust Dimensional Short-Duration Fixed Income ETF|P| |Y|100|N||DFSD|DFSD|N\r\nY|DFSE|Dimensional
        ETF Trust Dimensional Emerging Markets Sustainability Core 1 ETF|P| |Y|100|N||DFSE|DFSE|N\r\nY|DFSI|Dimensional
        ETF Trust Dimensional International Sustainability Core 1 ETF|P| |Y|100|N||DFSI|DFSI|N\r\nY|DFSU|Dimensional
        ETF Trust Dimensional US Sustainability Core 1 ETF|P| |Y|100|N||DFSU|DFSU|N\r\nY|DFSV|Dimensional
        ETF Trust Dimensional US Small Cap Value ETF|P| |Y|100|N||DFSV|DFSV|N\r\nY|DFUS|Dimensional
        U.S. Equity ETF|P| |Y|100|N||DFUS|DFUS|N\r\nY|DFUV|Dimensional ETF Trust Dimensional
        US Marketwide Value ETF|P| |Y|100|N||DFUV|DFUV|N\r\nY|DFVE|DoubleLine ETF
        Trust DoubleLine Fortune 500 Equal Weight ETF|P| |Y|100|N||DFVE|DFVE|N\r\nY|DFVX|Dimensional
        ETF Trust Dimensional US Large Cap Vector ETF|P| |Y|100|N||DFVX|DFVX|N\r\nY|DG|Dollar
        General Corporation Common Stock|N| |N|100|N||DG|DG|N\r\nY|DGCB|Dimensional
        Global Credit ETF|Q|G|Y|100|N|N||DGCB|N\r\nY|DGHI|Digihost Technology Inc.
        - Common Subordinate Voting Shares|Q|S|N|100|N|E||DGHI|N\r\nY|DGICA|Donegal
        Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||DGICA|N\r\nY|DGICB|Donegal
        Group, Inc. - Class B Common Stock|Q|Q|N|100|N|N||DGICB|N\r\nY|DGII|Digi International
        Inc. - Common Stock|Q|Q|N|100|N|N||DGII|N\r\nY|DGIN|VanEck ETF Trust VanEck
        Digital India ETF|P| |Y|100|N||DGIN|DGIN|N\r\nY|DGLY|Digital Ally, Inc. -
        Common Stock|Q|S|N|100|N|D||DGLY|N\r\nY|DGP|DB Gold Double Long ETN due February
        15, 2038|P| |N|100|N||DGP|DGP|N\r\nY|DGRE|WisdomTree Emerging Markets Quality
        Dividend Growth Fund|Q|G|Y|100|N|N||DGRE|N\r\nY|DGRO|iShares Core Dividend
        Growth ETF|P| |Y|100|N||DGRO|DGRO|N\r\nY|DGRS|WisdomTree U.S. SmallCap Quality
        Dividend Growth Fund|Q|G|Y|100|N|N||DGRS|N\r\nY|DGRW|WisdomTree U.S. Quality
        Dividend Growth Fund|Q|G|Y|100|N|N||DGRW|N\r\nY|DGS|WisdomTree Emerging Market
        SmallCap Fund|P| |Y|100|N||DGS|DGS|N\r\nY|DGT|SPDR Global Dow ETF (based on
        The Global Dow)|P| |Y|100|N||DGT|DGT|N\r\nY|DGX|Quest Diagnostics Incorporated
        Common Stock|N| |N|100|N||DGX|DGX|N\r\nY|DGZ|DB Gold Short ETN due February
        15, 2038|P| |N|100|N||DGZ|DGZ|N\r\nY|DH|Definitive Healthcare Corp. - Class
        A Common Stock|Q|Q|N|100|N|N||DH|N\r\nY|DHAI|DIH Holding US, Inc. - Class
        A Common Stock|Q|G|N|100|N|N||DHAI|N\r\nY|DHAIW|DIH Holding US, Inc. - Warrant|Q|S|N|100|N|N||DHAIW|N\r\nY|DHC|Diversified
        Healthcare Trust  - Common Shares of Beneficial Interest|Q|Q|N|100|N|N||DHC|N\r\nY|DHCNI|Diversified
        Healthcare Trust  - 5.625% Senior Notes due 2042|Q|Q|N|100|N|N||DHCNI|N\r\nY|DHCNL|Diversified
        Healthcare Trust  - 6.25% Senior Notes Due 2046|Q|Q|N|100|N|N||DHCNL|N\r\nY|DHF|BNY
        Mellon High Yield Strategies Fund Common Stock|N| |N|100|N||DHF|DHF|N\r\nY|DHI|D.R.
        Horton, Inc. Common Stock|N| |N|100|N||DHI|DHI|N\r\nY|DHIL|Diamond Hill Investment
        Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||DHIL|N\r\nY|DHR|Danaher
        Corporation Common Stock|N| |N|100|N||DHR|DHR|N\r\nY|DHS|WisdomTree U.S. High
        Dividend Fund|P| |Y|100|N||DHS|DHS|N\r\nY|DHT|DHT Holdings, Inc.|N| |N|100|N||DHT|DHT|N\r\nY|DHX|DHI
        Group, Inc. Common Stock|N| |N|100|N||DHX|DHX|N\r\nY|DHY|Credit Suisse High
        Yield Bond Fund Common Stock|A| |N|100|N||DHY|DHY|N\r\nY|DIA|SPDR Dow Jones
        Industrial Average ETF|P| |Y|100|N||DIA|DIA|N\r\nY|DIAL|Columbia Diversified
        Fixed Income Allocation ETF|P| |Y|100|N||DIAL|DIAL|N\r\nY|DIAX|Nuveen Dow
        30SM Dynamic Overwrite Fund Common Shares of Beneficial Interest|N| |N|100|N||DIAX|DIAX|N\r\nY|DIBS|1stdibs.com,
        Inc. - Common Stock|Q|G|N|100|N|N||DIBS|N\r\nY|DIEM|Franklin Emerging Market
        Core Dividend Tilt Index ETF|P| |Y|100|N||DIEM|DIEM|N\r\nY|DIG|ProShares Ultra
        Energy|P| |Y|100|N||DIG|DIG|N\r\nY|DIHP|Dimensional ETF Trust Dimensional
        International High Profitability ETF|Z| |Y|100|N||DIHP|DIHP|N\r\nY|DIM|WisdomTree
        International MidCap Dividend Fund|P| |Y|100|N||DIM|DIM|N\r\nY|DIN|Dine Brands
        Global, Inc. Common Stock|N| |N|100|N||DIN|DIN|N\r\nY|DINO|HF Sinclair Corporation
        Common Stock|N| |N|100|N||DINO|DINO|N\r\nY|DINT|Davis Fundamental ETF Trust
        Davis Select International ETF|Z| |Y|100|N||DINT|DINT|N\r\nY|DIOD|Diodes Incorporated
        - Common Stock|Q|Q|N|100|N|N||DIOD|N\r\nY|DIS|Walt Disney Company (The) Common
        Stock|N| |N|100|N||DIS|DIS|N\r\nY|DISO|Tidal ETF Trust II YieldMax DIS Option
        Income Strategy ETF|P| |Y|100|N||DISO|DISO|N\r\nY|DIST|Distoken Acquisition
        Corporation - Ordinary Shares|Q|G|N|100|N|E||DIST|N\r\nY|DISTR|Distoken Acquisition
        Corporation - Right|Q|G|N|100|N|E||DISTR|N\r\nY|DISTW|Distoken Acquisition
        Corporation - Warrant|Q|G|N|100|N|E||DISTW|N\r\nY|DISV|Dimensional ETF Trust
        Dimensional International Small Cap Value ETF|Z| |Y|100|N||DISV|DISV|N\r\nY|DIT|AMCON
        Distributing Company Common Stock|A| |N|10|N||DIT|DIT|N\r\nY|DIV|Global X
        Super Dividend ETF|P| |Y|100|N||DIV|DIV|N\r\nY|DIVB|iShares Core Dividend
        ETF|Z| |Y|100|N||DIVB|DIVB|N\r\nY|DIVD|Altrius Global Dividend ETF|Q|G|Y|100|N|N||DIVD|N\r\nY|DIVG|Invesco
        Exchange-Traded Fund Trust II Invesco S&P 500 High Dividend Growers ETF|P|
        |Y|100|N||DIVG|DIVG|N\r\nY|DIVI|Franklin International Core Dividend Tilt
        Index ETF|P| |Y|100|N||DIVI|DIVI|N\r\nY|DIVL|Madison ETFs Trust Madison Dividend
        Value ETF|P| |Y|100|N||DIVL|DIVL|N\r\nY|DIVO|Amplify CWP Enhanced Dividend
        Income ETF|P| |Y|100|N||DIVO|DIVO|N\r\nY|DIVP|The Advisors? Inner Circle Fund
        II Cullen Enhanced Equity Income ETF|P| |Y|100|N||DIVP|DIVP|N\r\nY|DIVS|SmartETFs
        Dividend Builder ETF|P| |Y|100|N||DIVS|DIVS|N\r\nY|DIVY|Sound Equity Dividend
        Income ETF|N| |Y|100|N||DIVY|DIVY|N\r\nY|DIVZ|Opal Dividend Income ETF|P|
        |Y|100|N||DIVZ|DIVZ|N\r\nY|DJAN|FT Vest U.S. Equity Deep Buffer ETF - January|Z|
        |Y|100|N||DJAN|DJAN|N\r\nY|DJCB|ETRACS Bloomberg Commodity Index Total Return
        ETN Series B due October 31, 2039|P| |Y|100|N||DJCB|DJCB|N\r\nY|DJCO|Daily
        Journal Corp. (S.C.) - Common Stock|Q|S|N|100|N|N||DJCO|N\r\nY|DJD|Invesco
        Dow Jones Industrial Average Dividend ETF|P| |Y|100|N||DJD|DJD|N\r\nY|DJIA|Global
        X Funds Global X Dow 30 Covered Call ETF|P| |Y|100|N||DJIA|DJIA|N\r\nY|DJP|iPath
        Bloomberg Commodity Index Total Return ETN|P| |N|100|N||DJP|DJP|N\r\nY|DJT|Trump
        Media & Technology Group Corp. - Common Stock|Q|G|N|100|N|N||DJT|N\r\nY|DJTWW|Trump
        Media & Technology Group Corp. - Warrants|Q|G|N|100|N|N||DJTWW|N\r\nY|DJUL|FT
        Vest U.S. Equity Deep Buffer ETF - July|Z| |Y|100|N||DJUL|DJUL|N\r\nY|DJUN|FT
        Vest U.S. Equity Deep Buffer ETF - June|Z| |Y|100|N||DJUN|DJUN|N\r\nY|DK|Delek
        US Holdings, Inc. Common Stock|N| |N|100|N||DK|DK|N\r\nY|DKL|Delek Logistics
        Partners, L.P. Common Units representing Limited Partner Interests|N| |N|100|N||DKL|DKL|N\r\nY|DKNG|DraftKings
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||DKNG|N\r\nY|DKS|Dick's Sporting
        Goods Inc Common Stock|N| |N|100|N||DKS|DKS|N\r\nY|DLA|Delta Apparel, Inc.
        Common Stock|A| |N|100|N||DLA|DLA|N\r\nY|DLB|Dolby Laboratories Common Stock|N|
        |N|100|N||DLB|DLB|N\r\nY|DLHC|DLH Holdings Corp. - Common Stock|Q|S|N|100|N|N||DLHC|N\r\nY|DLN|WisdomTree
        U.S. LargeCap Dividend Fund|P| |Y|100|N||DLN|DLN|N\r\nY|DLNG|Dynagas LNG Partners
        LP Common Units|N| |N|100|N||DLNG|DLNG|N\r\nY|DLNG$A|Dynagas LNG Partners
        LP 9.00% Series A Cumulative Redeemable Preferred Units|N| |N|100|N||DLNGpA|DLNG-A|N\r\nY|DLNG$B|Dynagas
        LNG Partners LP 8.75% Series B Fixed to Floating Rate Cumulative Redeemable
        Perpetual Preferred Units, liquidation preference $25.00 per Uni|N| |N|100|N||DLNGpB|DLNG-B|N\r\nY|DLO|DLocal
        Limited - Class A Common Shares|Q|Q|N|100|N|N||DLO|N\r\nY|DLPN|Dolphin Entertainment,
        Inc. - Common Stock|Q|S|N|100|N|N||DLPN|N\r\nY|DLR|Digital Realty Trust, Inc.
        Common Stock|N| |N|100|N||DLR|DLR|N\r\nY|DLR$J|Digital Realty Trust, Inc.
        5.250% Series J Cumulative Redeemable Preferred Stock|N| |N|100|N||DLRpJ|DLR-J|N\r\nY|DLR$K|Digital
        Realty Trust, Inc. 5.850% Series K Cumulative Redeemable Preferred Stock,
        par value $0.01 per share|N| |N|100|N||DLRpK|DLR-K|N\r\nY|DLR$L|Digital Realty
        Trust, Inc. 5.200% Series L Cumulative Redeemable Preferred Stock|N| |N|100|N||DLRpL|DLR-L|N\r\nY|DLS|WisdomTree
        International SmallCap Fund|P| |Y|100|N||DLS|DLS|N\r\nY|DLTH|Duluth Holdings
        Inc. - Class B Common Stock|Q|Q|N|100|N|N||DLTH|N\r\nY|DLTR|Dollar Tree, Inc.
        - Common Stock|Q|Q|N|100|N|N||DLTR|N\r\nY|DLX|Deluxe Corporation Common Stock|N|
        |N|100|N||DLX|DLX|N\r\nY|DLY|DoubleLine Yield Opportunities Fund Common Shares
        of Beneficial Interest|N| |N|100|N||DLY|DLY|N\r\nY|DM|Desktop Metal, Inc.
        Class A Common Stock|N| |N|100|N||DM|DM|N\r\nY|DMA|Destra Multi-Alternative
        Fund Common Stock|N| |N|100|N||DMA|DMA|N\r\nY|DMAC|DiaMedica Therapeutics
        Inc. - Common Stock|Q|S|N|100|N|N||DMAC|N\r\nY|DMAR|FT Vest U.S. Equity Deep
        Buffer ETF - March|Z| |Y|100|N||DMAR|DMAR|N\r\nY|DMAT|Global X Disruptive
        Materials ETF|Q|G|Y|100|N|N||DMAT|N\r\nY|DMAY|FT Vest U.S. Equity Deep Buffer
        ETF - May|Z| |Y|100|N||DMAY|DMAY|N\r\nY|DMB|BNY Mellon Municipal Bond Infrastructure
        Fund, Inc. Common Stock|N| |N|100|N||DMB|DMB|N\r\nY|DMBS|DoubleLine ETF Trust
        DoubleLine Mortgage ETF|P| |Y|100|N||DMBS|DMBS|N\r\nY|DMCY|Democracy International
        Fund|P| |Y|100|N||DMCY|DMCY|N\r\nY|DMDV|AAM S&P Developed Markets High Dividend
        Value ETF|P| |Y|100|N||DMDV|DMDV|N\r\nY|DMF|BNY Mellon Municipal Income Inc.
        Common Stock|A| |N|100|N||DMF|DMF|N\r\nY|DMLP|Dorchester Minerals, L.P. -
        Common Units Representing Limited Partnership Interests|Q|Q|N|100|N|N||DMLP|N\r\nY|DMO|Western
        Asset Mortgage Opportunity Fund Inc. Common Stock|N| |N|100|N||DMO|DMO|N\r\nY|DMRC|Digimarc
        Corporation - Common Stock|Q|Q|N|100|N|N||DMRC|N\r\nY|DMXF|iShares ESG Advanced
        MSCI EAFE ETF|Q|G|Y|100|N|N||DMXF|N\r\nY|DMYY|dMY Squared Technology Group,
        Inc. Class A Common Stock|A| |N|100|N||DMYY|DMYY|N\r\nY|DMYY.U|dMY Squared
        Technology Group, Inc. Units, each consisting of one share of Class A common
        stock and one-half of one redeemable warrant|A| |N|100|N||DMYY.U|DMYY=|N\r\nY|DMYY.W|dMY
        Squared Technology Group, Inc. Redeemable Warrants, each whole warrant exercisable
        for one share of Class A common stock at an exercise price of $11.50 per share|A|
        |N|100|N||DMYY.WS|DMYY+|N\r\nY|DNA|Ginkgo Bioworks Holdings, Inc. Class A
        Common Stock|N| |N|100|N||DNA|DNA|N\r\nY|DNA.W|Ginkgo Bioworks Holdings, Inc.
        Warrant|N| |N|100|N||DNA.WS|DNA+|N\r\nY|DNB|Dun & Bradstreet Holdings, Inc.
        Common Stock|N| |N|100|N||DNB|DNB|N\r\nY|DNL|WisdomTree Global ex-US Quality
        Dividend Growth Fund|P| |Y|100|N||DNL|DNL|N\r\nY|DNLI|Denali Therapeutics
        Inc. - Common Stock|Q|Q|N|100|N|N||DNLI|N\r\nY|DNMR|Danimer Scientific, Inc.
        Common Stock|N| |N|100|N||DNMR|DNMR|N\r\nY|DNN|Denison Mines Corp Ordinary
        Shares (Canada)|A| |N|100|N||DNN|DNN|N\r\nY|DNOV|FT Vest U.S. Equity Deep
        Buffer ETF - November|Z| |Y|100|N||DNOV|DNOV|N\r\nY|DNOW|DNOW Inc. Common
        Stock|N| |N|100|N||DNOW|DNOW|N\r\nY|DNP|DNP Select Income Fund, Inc. Common
        Stock|N| |N|100|N||DNP|DNP|N\r\nY|DNTH|Dianthus Therapeutics, Inc. - Common
        Stock|Q|S|N|100|N|N||DNTH|N\r\nY|DNUT|Krispy Kreme, Inc. - Common Stock|Q|Q|N|100|N|N||DNUT|N\r\nY|DO|Diamond
        Offshore Drilling, Inc. Common Stock|N| |N|100|N||DO|DO|N\r\nY|DOC|Healthpeak
        Properties, Inc. Common Stock|N| |N|100|N||DOC|DOC|N\r\nY|DOCN|DigitalOcean
        Holdings, Inc. Common Stock|N| |N|100|N||DOCN|DOCN|N\r\nY|DOCS|Doximity, Inc.
        Class A Common Stock|N| |N|100|N||DOCS|DOCS|N\r\nY|DOCT|FT Vest U.S. Equity
        Deep Buffer ETF - October|Z| |Y|100|N||DOCT|DOCT|N\r\nY|DOCU|DocuSign, Inc.
        - Common Stock|Q|Q|N|100|N|N||DOCU|N\r\nY|DOG|ProShares Short Dow30|P| |Y|100|N||DOG|DOG|N\r\nY|DOGG|FT
        Vest DJIA Dogs 10 Target Income ETF|Z| |Y|100|N||DOGG|DOGG|N\r\nY|DOGZ|Dogness
        (International) Corporation - Class A Common Stock|Q|S|N|100|N|N||DOGZ|N\r\nY|DOL|WisdomTree
        International LargeCap Dividend Fund|P| |Y|100|N||DOL|DOL|N\r\nY|DOLE|Dole
        plc Ordinary Shares|N| |N|100|N||DOLE|DOLE|N\r\nY|DOMA|Doma Holdings, Inc.
        Common Stock|N| |N|100|N||DOMA|DOMA|N\r\nY|DOMH|Dominari Holdings Inc. - Common
        Stock|Q|S|N|100|N|N||DOMH|N\r\nY|DOMO|Domo, Inc. - Class B Common Stock|Q|G|N|100|N|N||DOMO|N\r\nY|DON|WisdomTree
        U.S. MidCap Dividend Fund|P| |Y|100|N||DON|DON|N\r\nY|DOOO|BRP Inc. - Common
        Subordinate Voting Shares|Q|Q|N|100|N|N||DOOO|N\r\nY|DORM|Dorman Products,
        Inc. - Common Stock|Q|Q|N|100|N|N||DORM|N\r\nY|DOUG|Douglas Elliman Inc. Common
        Stock|N| |N|100|N||DOUG|DOUG|N\r\nY|DOV|Dover Corporation Common Stock|N|
        |N|100|N||DOV|DOV|N\r\nY|DOW|Dow Inc. Common Stock |N| |N|100|N||DOW|DOW|N\r\nY|DOX|Amdocs
        Limited - Ordinary Shares|Q|Q|N|100|N|N||DOX|N\r\nY|DOYU|DouYu International
        Holdings Limited - American Depositary Shares|Q|Q|N|100|N|N||DOYU|N\r\nY|DPCS|DP
        Cap Acquisition Corp I - Class A Ordinary Shares|Q|S|N|100|N|N||DPCS|N\r\nY|DPCSU|DP
        Cap Acquisition Corp I - Unit|Q|S|N|100|N|N||DPCSU|N\r\nY|DPCSW|DP Cap Acquisition
        Corp I - Warrants|Q|S|N|100|N|N||DPCSW|N\r\nY|DPG|Duff & Phelps Utility and
        Infrastructure Fund Inc.|N| |N|100|N||DPG|DPG|N\r\nY|DPRO|Draganfly Inc. -
        Common Shares|Q|S|N|100|N|D||DPRO|N\r\nY|DPSI|DecisionPoint Systems, Inc.
        Common Stock|A| |N|100|N||DPSI|DPSI|N\r\nY|DPST|Direxion Daily Regional Banks
        Bull 3X Shares|P| |Y|100|N||DPST|DPST|N\r\nY|DPZ|Domino's Pizza Inc Common
        Stock|N| |N|100|N||DPZ|DPZ|N\r\nY|DQ|DAQO New Energy Corp. American Depositary
        Shares, each representing five ordinary shares|N| |N|100|N||DQ|DQ|N\r\nY|DRCT|Direct
        Digital Holdings, Inc. - Class A Common Stock|Q|S|N|100|N|E||DRCT|N\r\nY|DRD|DRDGOLD
        Limited American Depositary Shares|N| |N|100|N||DRD|DRD|N\r\nY|DRH|Diamondrock
        Hospitality Company Common Stock|N| |N|100|N||DRH|DRH|N\r\nY|DRH$A|Diamondrock
        Hospitality Company 8.250% Series A Cumulative Redeemable Preferred Stock|N|
        |N|100|N||DRHpA|DRH-A|N\r\nY|DRI|Darden Restaurants, Inc. Common Stock|N|
        |N|100|N||DRI|DRI|N\r\nY|DRIO|DarioHealth Corp. - Common Stock|Q|S|N|100|N|N||DRIO|N\r\nY|DRIP|Direxion
        Daily S&P Oil & Gas Exp. & Prod. Bear 2X Shares|P| |Y|100|N||DRIP|DRIP|N\r\nY|DRIV|Global
        X Autonomous & Electric Vehicles ETF|Q|G|Y|100|N|N||DRIV|N\r\nY|DRLL|EA Series
        Trust Strive U.S. Energy ETF|N| |Y|100|N||DRLL|DRLL|N\r\nY|DRMA|Dermata Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||DRMA|N\r\nY|DRMAW|Dermata Therapeutics,
        Inc. - Warrant|Q|S|N|100|N|N||DRMAW|N\r\nY|DRN|Direxion Daily Real Estate
        Bull 3X Shares|P| |Y|100|N||DRN|DRN|N\r\nY|DRQ|Dril-Quip, Inc. Common Stock|N|
        |N|100|N||DRQ|DRQ|N\r\nY|DRRX|DURECT Corporation - Common Stock|Q|S|N|100|N|N||DRRX|N\r\nY|DRS|Leonardo
        DRS, Inc. - Common Stock|Q|Q|N|100|N|N||DRS|N\r\nY|DRSK|Aptus Defined Risk
        ETF |Z| |Y|100|N||DRSK|DRSK|N\r\nY|DRTS|Alpha Tau Medical Ltd. - Ordinary
        Shares|Q|S|N|100|N|N||DRTS|N\r\nY|DRTSW|Alpha Tau Medical Ltd. - Warrant|Q|S|N|100|N|N||DRTSW|N\r\nY|DRUG|Bright
        Minds Biosciences Inc. - common stock|Q|S|N|100|N|N||DRUG|N\r\nY|DRUP|GraniteShares
        Nasdaq Select Disruptors ETF|P| |Y|100|N||DRUP|DRUP|N\r\nY|DRV|Direxion Daily
        Real Estate Bear 3X Shares|P| |Y|100|N||DRV|DRV|N\r\nY|DRVN|Driven Brands
        Holdings Inc. - Common Stock|Q|Q|N|100|N|N||DRVN|N\r\nY|DSCF|Discipline Fund
        ETF|Z| |Y|100|N||DSCF|DSCF|N\r\nY|DSEP|FT Vest U.S. Equity Deep Buffer ETF
        - September|Z| |Y|100|N||DSEP|DSEP|N\r\nY|DSGN|Design Therapeutics, Inc. -
        Common Stock|Q|Q|N|100|N|N||DSGN|N\r\nY|DSGR|Distribution Solutions Group,
        Inc. - Common Stock|Q|Q|N|100|N|N||DSGR|N\r\nY|DSGX|The Descartes Systems
        Group Inc. - Common Stock|Q|Q|N|100|N|N||DSGX|N\r\nY|DSI|iShares MSCI KLD
        400 Social ETF|P| |Y|100|N||DSI|DSI|N\r\nY|DSL|DoubleLine Income Solutions
        Fund Common Shares of Beneficial Interests|N| |N|100|N||DSL|DSL|N\r\nY|DSM|BNY
        Mellon Strategic Municipal Bond Fund, Inc. Common Stock|N| |N|100|N||DSM|DSM|N\r\nY|DSMC|ETF
        Series Solutions Distillate Small/Mid Cash Flow ETF|N| |Y|100|N||DSMC|DSMC|N\r\nY|DSP|Viant
        Technology Inc. - common stock|Q|Q|N|100|N|D||DSP|N\r\nY|DSS|DSS, Inc. Common
        Stock|A| |N|100|N||DSS|DSS|N\r\nY|DSTL|Distillate U.S. Fundamental Stability
        & Value ETF|P| |Y|100|N||DSTL|DSTL|N\r\nY|DSTX|Distillate International Fundamental
        Stability & Value ETF|N| |Y|100|N||DSTX|DSTX|N\r\nY|DSU|Blackrock Debt Strategies
        Fund, Inc. Common Stock|N| |N|100|N||DSU|DSU|N\r\nY|DSWL|Deswell Industries,
        Inc. - Common Shares|Q|G|N|100|N|N||DSWL|N\r\nY|DSX|Diana Shipping inc. common
        stock|N| |N|100|N||DSX|DSX|N\r\nY|DSX$B|Diana Shipping Inc. Perpetual Preferred
        Shares Series B (Marshall Islands)|N| |N|100|N||DSXpB|DSX-B|N\r\nY|DSX.W|Diana
        Shipping inc. Warrants|N| |N|100|N||DSX.WS|DSX+|N\r\nY|DSY|Big Tree Cloud
        Holdings Limited - Ordinary Shares|Q|G|N|100|N|N||DSY|N\r\nY|DSYWW|Big Tree
        Cloud Holdings Limited - Warrants|Q|S|N|100|N|N||DSYWW|N\r\nY|DT|Dynatrace,
        Inc. Common Stock|N| |N|100|N||DT|DT|N\r\nY|DTB|DTE Energy Company 2020 Series
        G 4.375% Junior Subordinated Debentures due 2080|N| |N|100|N||DTB|DTB|N\r\nY|DTC|Solo
        Brands, Inc. Class A Common Stock|N| |N|100|N||DTC|DTC|N\r\nY|DTCK|Davis Commodities
        Limited - Ordinary Shares|Q|S|N|100|N|N||DTCK|N\r\nY|DTCR|Global X Data Center
        & Digital Infrastructure ETF|Q|G|Y|100|N|N||DTCR|N\r\nY|DTD|WisdomTree U.S.
        Total Dividend Fund|P| |Y|100|N||DTD|DTD|N\r\nY|DTE|DTE Energy Company Common
        Stock|N| |N|100|N||DTE|DTE|N\r\nY|DTEC|ALPS ETF Trust ALPS Disruptive Technologies
        ETF|P| |Y|100|N||DTEC|DTEC|N\r\nY|DTF|DTF Tax-Free Income 2028 Term Fund Inc.
        Common Stock|N| |N|100|N||DTF|DTF|N\r\nY|DTG|DTE Energy Company 2021 Series
        E 4.375% Junior Subordinated Debentures|N| |N|100|N||DTG|DTG|N\r\nY|DTH|WisdomTree
        International High Dividend Fund|P| |Y|100|N||DTH|DTH|N\r\nY|DTI|Drilling
        Tools International Corporation  - Common Stock|Q|S|N|100|N|N||DTI|N\r\nY|DTIL|Precision
        BioSciences, Inc. - Common Stock|Q|S|N|100|N|N||DTIL|N\r\nY|DTM|DT Midstream,
        Inc. Common Stock |N| |N|100|N||DTM|DTM|N\r\nY|DTRE|First Trust Alerian Disruptive
        Technology Real Estate ETF|P| |Y|100|N||DTRE|DTRE|N\r\nY|DTSS|Datasea Inc.
        - Common Stock|Q|S|N|100|N|D||DTSS|N\r\nY|DTST|Data Storage Corporation -
        Common Stock|Q|S|N|100|N|N||DTST|N\r\nY|DTSTW|Data Storage Corporation - Warrant|Q|S|N|100|N|N||DTSTW|N\r\nY|DTW|DTE
        Energy Company 2017 Series E 5.25% Junior Subordinated Debentures due 2077|N|
        |N|100|N||DTW|DTW|N\r\nY|DUBS|ETF Series Solutions Aptus Large Cap Enhanced
        Yield ETF|Z| |Y|100|N||DUBS|DUBS|N\r\nY|DUET|DUET Acquisition Corp. - Class
        A Common Stock|Q|G|N|100|N|D||DUET|N\r\nY|DUETU|DUET Acquisition Corp. - Unit|Q|G|N|100|N|D||DUETU|N\r\nY|DUETW|DUET
        Acquisition Corp. - Warrant|Q|G|N|100|N|D||DUETW|N\r\nY|DUG|ProShares UltraShort
        Energy|P| |Y|100|N||DUG|DUG|N\r\nY|DUHP|Dimensional ETF Trust Dimensional
        US High Profitability ETF|P| |Y|100|N||DUHP|DUHP|N\r\nY|DUK|Duke Energy Corporation
        (Holding Company) Common Stock|N| |N|100|N||DUK|DUK|N\r\nY|DUK$A|Duke Energy
        Corporation Depositary Shares, each representing a 1/1,000th interest in a
        share of 5.75% Series A Cumulative Redeemable Perpetual Preferred Stock|N|
        |N|100|N||DUKpA|DUK-A|N\r\nY|DUKB|Duke Energy Corporation 5.625% Junior Subordinated
        Debentures due 2078|N| |N|100|N||DUKB|DUKB|N\r\nY|DULL|Bank Of Montreal MicroSectors
        Gold -3X Inverse Leveraged ETNs due January 29, 2043|P| |Y|100|N||DULL|DULL|N\r\nY|DUO|Fangdd
        Network Group Ltd. - American Depositary Shares|Q|S|N|100|N|D||DUO|N\r\nY|DUOL|Duolingo,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||DUOL|N\r\nY|DUOT|Duos Technologies
        Group, Inc. - Common Stock|Q|S|N|100|N|N||DUOT|N\r\nY|DURA|VanEck Durable
        High Dividend ETF|Z| |Y|100|N||DURA|DURA|N\r\nY|DUSA|Davis Fundamental ETF
        Trust Davis Select U.S. Equity ETF|Z| |Y|100|N||DUSA|DUSA|N\r\nY|DUSB|Dimensional
        ETF Trust Dimensional Ultrashort Fixed Income ETF|P| |Y|100|N||DUSB|DUSB|N\r\nY|DUSL|Direxion
        Daily Industrials Bull 3X Shares|P| |Y|100|N||DUSL|DUSL|N\r\nY|DUST|Direxion
        Daily Gold Miners Index Bear 2X Shares|P| |Y|100|N||DUST|DUST|N\r\nY|DV|DoubleVerify
        Holdings, Inc. Common Stock|N| |N|100|N||DV|DV|N\r\nY|DVA|DaVita Inc. Common
        Stock|N| |N|100|N||DVA|DVA|N\r\nY|DVAL|BrandywineGLOBAL-Dynamic US Large Cap
        Value ETF|Q|G|Y|100|N|N||DVAL|N\r\nY|DVAX|Dynavax Technologies Corporation
        - Common Stock|Q|Q|N|100|N|N||DVAX|N\r\nY|DVDN|ETF Opportunities Trust Kingsbarn
        Dividend Opportunity ETF|P| |Y|100|N||DVDN|DVDN|N\r\nY|DVLU|First Trust Dorsey
        Wright Momentum & Value ETF|Q|G|Y|100|N|N||DVLU|N\r\nY|DVN|Devon Energy Corporation
        Common Stock|N| |N|100|N||DVN|DVN|N\r\nY|DVND|Touchstone ETF Trust Touchstone
        Dividend Select ETF|P| |Y|100|N||DVND|DVND|N\r\nY|DVOL|First Trust Dorsey
        Wright Momentum & Low Volatility ETF|Q|G|Y|100|N|N||DVOL|N\r\nY|DVY|iShares
        Select Dividend ETF|Q|G|Y|100|N|N||DVY|N\r\nY|DVYA|iShares Asia / Pacific
        Dividend 30 Index Fund Exchange Traded Fund|P| |Y|100|N||DVYA|DVYA|N\r\nY|DVYE|iShares
        Emerging Markets Dividend Index Fund Exchange Traded Fund|P| |Y|100|N||DVYE|DVYE|N\r\nY|DWAS|Invesco
        Dorsey Wright SmallCap Momentum ETF|Q|G|Y|100|N|N||DWAS|N\r\nY|DWAT|Arrow
        Investments Trust Arrow DWA Tactical ETF|Z| |Y|100|N||DWAT|DWAT|N\r\nY|DWAW|AdvisorShares
        Dorsey Wright FSM All Cap World ETF|Q|G|Y|100|N|N||DWAW|N\r\nY|DWCR|Arrow
        Investments Trust Arrow DWA Country Rotation ETF|Z| |Y|100|N||DWCR|DWCR|N\r\nY|DWLD|Davis
        Fundamental ETF Trust Davis Select Worldwide ETF|Z| |Y|100|N||DWLD|DWLD|N\r\nY|DWM|WisdomTree
        International Equity Fund|P| |Y|100|N||DWM|DWM|N\r\nY|DWMF|WisdomTree International
        Multifactor Fund|P| |Y|100|N||DWMF|DWMF|N\r\nY|DWSH|AdvisorShares Dorsey Wright
        Short ETF|Q|G|Y|100|N|N||DWSH|N\r\nY|DWSN|Dawson Geophysical Company - Common
        Stock|Q|Q|N|100|N|N||DWSN|N\r\nY|DWUS|AdvisorShares Dorsey Wright FSM US Core
        ETF|Q|G|Y|100|N|N||DWUS|N\r\nY|DWX|SPDR S&P International Dividend ETF|P|
        |Y|100|N||DWX|DWX|N\r\nY|DX|Dynex Capital, Inc. Common Stock|N| |N|100|N||DX|DX|N\r\nY|DX$C|Dynex
        Capital, Inc. 6.900% Series C Fixed-to-Floating Rate Cumulative Redeemable
        Preferred Stock|N| |N|100|N||DXpC|DX-C|N\r\nY|DXC|DXC Technology Company Common
        Stock |N| |N|100|N||DXC|DXC|N\r\nY|DXCM|DexCom, Inc. - Common Stock|Q|Q|N|100|N|N||DXCM|N\r\nY|DXD|ProShares
        UltraShort Dow30|P| |Y|100|N||DXD|DXD|N\r\nY|DXF|Dunxin Financial Holdings
        Limited American Depositary Shares|A| |N|100|N||DXF|DXF|N\r\nY|DXJ|WisdomTree
        Japan Hedged Equity Fund|P| |Y|100|N||DXJ|DXJ|N\r\nY|DXJS|WisdomTree Japan
        Hedged SmallCap Equity Fund|Q|G|Y|100|N|N||DXJS|N\r\nY|DXLG|Destination XL
        Group, Inc. - Common Stock|Q|G|N|100|N|N||DXLG|N\r\nY|DXPE|DXP Enterprises,
        Inc. - Common Stock|Q|Q|N|100|N|N||DXPE|N\r\nY|DXR|Daxor Corporation - Closed
        End Fund|Q|S|N|100|N|N||DXR|N\r\nY|DXYN|The Dixie Group, Inc. - Common Stock|Q|S|N|100|N|D||DXYN|N\r\nY|DXYZ|Destiny
        Tech100 Inc. Common Stock|N| |N|100|N||DXYZ|DXYZ|N\r\nY|DY|Dycom Industries,
        Inc. Common Stock|N| |N|100|N||DY|DY|N\r\nY|DYAI|Dyadic International, Inc.
        - Common Stock|Q|S|N|100|N|N||DYAI|N\r\nY|DYCQ|DT Cloud Acquisition Corporation
        - Ordinary shares|Q|G|N|100|N|N||DYCQ|N\r\nY|DYCQR|DT Cloud Acquisition Corporation
        - Right|Q|G|N|100|N|N||DYCQR|N\r\nY|DYCQU|DT Cloud Acquisition Corporation
        - Unit|Q|G|N|100|N|N||DYCQU|N\r\nY|DYFI|IDX Dynamic Fixed Income ETF|Q|G|Y|100|N|N||DYFI|N\r\nY|DYLD|LeaderShares
        Dynamic Yield ETF|P| |Y|100|N||DYLD|DYLD|N\r\nY|DYLG|Global X Funds Global
        X Dow 30 Covered Call & Growth ETF|P| |Y|100|N||DYLG|DYLG|N\r\nY|DYN|Dyne
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||DYN|N\r\nY|DYNF|BlackRock
        U.S. Equity Factor Rotation ETF|P| |Y|100|N||DYNF|DYNF|N\r\nY|DYNI|IDX Dynamic
        Innovation ETF|Q|G|Y|100|N|N||DYNI|N\r\nY|DYNT|Dynatronics Corporation - Common
        Stock|Q|S|N|100|N|D||DYNT|N\r\nY|DYTA|SGI Dynamic Tactical ETF|Q|G|Y|100|N|N||DYTA|N\r\nY|DZSI|DZS
        Inc. - Common Stock|Q|S|N|100|N|E||DZSI|N\r\nY|DZZ|DB Gold Double Short ETN
        due February 15, 2038|P| |N|100|N||DZZ|DZZ|N\r\nY|E|ENI S.p.A. Common Stock|N|
        |N|100|N||E|E|N\r\nY|EA|Electronic Arts Inc. - Common Stock|Q|Q|N|100|N|N||EA|N\r\nY|EAD|Allspring
        Income Opportunities Fund Common Shares|A| |N|100|N||EAD|EAD|N\r\nY|EAF|GrafTech
        International Ltd. Common Stock|N| |N|100|N||EAF|EAF|N\r\nY|EAFG|Pacer Funds
        Trust Pacer Developed Markets Cash Cows Growth Leaders ETF|P| |Y|100|N||EAFG|EAFG|N\r\nY|EAGG|iShares
        ESG Aware U.S. Aggregate Bond ETF|P| |Y|100|N||EAGG|EAGG|N\r\nY|EAGL|The 2023
        ETF Series Trust Eagle Capital Select Equity ETF|P| |Y|100|N||EAGL|EAGL|N\r\nY|EAI|Entergy
        Arkansas, LLC First Mortgage Bonds, 4.875% Series Due September 1, 2066|N|
        |N|100|N||EAI|EAI|N\r\nY|EALT|Innovator ETFs Trust Innovator U.S. Equity 5
        to 15 Buffer ETF - Quarterly|Z| |Y|100|N||EALT|EALT|N\r\nY|EAOA|iShares ESG
        Aware Aggressive Allocation ETF|Z| |Y|100|N||EAOA|EAOA|N\r\nY|EAOK|iShares
        ESG Aware Conservative Allocation ETF|Z| |Y|100|N||EAOK|EAOK|N\r\nY|EAOM|iShares
        ESG Aware Moderate Allocation ETF|Z| |Y|100|N||EAOM|EAOM|N\r\nY|EAOR|iShares
        ESG Aware Growth Allocation ETF|Z| |Y|100|N||EAOR|EAOR|N\r\nY|EAPR|Innovator
        Emerging Markets Power Buffer ETF April|P| |Y|100|N||EAPR|EAPR|N\r\nY|EARN|Ellington
        Credit Company Common Shares of Beneficial Interest|N| |N|100|N||EARN|EARN|N\r\nY|EASG|Xtrackers
        MSCI EAFE ESG Leaders Equity ETF|P| |Y|100|N||EASG|EASG|N\r\nY|EAST|Eastside
        Distilling, Inc. - Common Stock|Q|S|N|100|N|D||EAST|N\r\nY|EAT|Brinker International,
        Inc. Common Stock|N| |N|100|N||EAT|EAT|N\r\nY|EATV|Advisors Series Trust VegTech
        Plant-based Innovation & Climate ETF|P| |Y|100|N||EATV|EATV|N\r\nY|EATZ|AdvisorShares
        Restaurant ETF|P| |Y|100|N||EATZ|EATZ|N\r\nY|EB|Eventbrite, Inc. Class A Common
        Stock|N| |N|100|N||EB|EB|N\r\nY|EBAY|eBay Inc. - Common Stock|Q|Q|N|100|N|N||EBAY|N\r\nY|EBC|Eastern
        Bankshares, Inc. - Common Stock|Q|Q|N|100|N|N||EBC|N\r\nY|EBF|Ennis, Inc.
        Common Stock|N| |N|100|N||EBF|EBF|N\r\nY|EBIZ|Global X E-commerce ETF|Q|G|Y|100|N|N||EBIZ|N\r\nY|EBLU|Ecofin
        Global Water ESG Fund|P| |Y|100|N||EBLU|EBLU|N\r\nY|EBMT|Eagle Bancorp Montana,
        Inc. - Common Stock|Q|G|N|100|N|N||EBMT|N\r\nY|EBND|SPDR Bloomberg Emerging
        Markets Local Bond ETF|P| |Y|100|N||EBND|EBND|N\r\nY|EBON|Ebang International
        Holdings Inc. - Class A Ordinary Shares|Q|Q|N|100|N|N||EBON|N\r\nY|EBR|Centrais
        Electricas Brasileiras S A American Depositary Shares (Each representing one
        Common Share)|N| |N|100|N||EBR|EBR|N\r\nY|EBR.B|Centrais Electricas Brasileiras
        S.A.- Eletrobr?!s American Depositary Shares (Each representing one Preferred
        Share)|N| |N|100|N||EBR.B|EBR.B|N\r\nY|EBS|Emergent Biosolutions, Inc. Common
        Stock|N| |N|100|N||EBS|EBS|N\r\nY|EBTC|Enterprise Bancorp Inc - Common Stock|Q|Q|N|100|N|N||EBTC|N\r\nY|EC|Ecopetrol
        S.A. American Depositary Shares|N| |N|100|N||EC|EC|N\r\nY|ECAT|BlackRock ESG
        Capital Allocation Term Trust Common Shares of Beneficial Interest|N| |N|100|N||ECAT|ECAT|N\r\nY|ECBK|ECB
        Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||ECBK|N\r\nY|ECC|Eagle Point Credit
        Company Inc. Common Stock|N| |N|100|N||ECC|ECC|N\r\nY|ECC$D|Eagle Point Credit
        Company Inc. 6.75% Series D Preferred Stock|N| |N|100|N||ECCpD|ECC-D|N\r\nY|ECCC|Eagle
        Point Credit Company Inc. 6.50% Series C Term Preferred Stock due 2031|N|
        |N|100|N||ECCC|ECCC|N\r\nY|ECCF|Eagle Point Credit Company Inc. 8.00% Series
        F Term Preferred Stock due 2029|N| |N|100|N||ECCF|ECCF|N\r\nY|ECCV|Eagle Point
        Credit Company Inc. 5.375% Notes due 2029|N| |N|100|N||ECCV|ECCV|N\r\nY|ECCW|Eagle
        Point Credit Company Inc. 6.75% Notes due 2031|N| |N|100|N||ECCW|ECCW|N\r\nY|ECCX|Eagle
        Point Credit Company Inc. 6.6875% Notes due 2028|N| |N|100|N||ECCX|ECCX|N\r\nY|ECDA|ECD
        Automotive Design, Inc. - Common Stock|Q|G|N|100|N|D||ECDA|N\r\nY|ECDAW|ECD
        Automotive Design, Inc. - Warrant|Q|S|N|100|N|N||ECDAW|N\r\nY|ECF|Ellsworth
        Growth and Income Fund Ltd.|A| |N|100|N||ECF|ECF|N\r\nY|ECF$A|Ellsworth Growth
        and Income Fund Ltd. 5.25% Series A Cumulative Preferred Shares (Liquidation
        Preference $25.00 per share)|A| |N|100|N||ECFpA|ECF-A|N\r\nY|ECH|iShares Inc.
        iShares MSCI Chile ETF|Z| |Y|100|N||ECH|ECH|N\r\nY|ECL|Ecolab Inc. Common
        Stock|N| |N|100|N||ECL|ECL|N\r\nY|ECLN|First Trust EIP Carbon Impact ETF|P|
        |Y|100|N||ECLN|ECLN|N\r\nY|ECML|EA Series Trust Euclidean Fundamental Value
        ETF|P| |Y|100|N||ECML|ECML|N\r\nY|ECNS|iShares MSCI China Small-Cap ETF|P|
        |Y|100|N||ECNS|ECNS|N\r\nY|ECO|Okeanis Eco Tankers Corp. Common Stock|N| |N|100|N||ECO|ECO|N\r\nY|ECON|Columbia
        Emerging Markets Consumer ETF|P| |Y|100|N||ECON|ECON|N\r\nY|ECOR|electroCore,
        Inc. - Common Stock|Q|S|N|100|N|N||ECOR|N\r\nY|ECOW|Pacer Emerging Markets
        Cash Cows 100 ETF|Q|G|Y|100|N|N||ECOW|N\r\nY|ECPG|Encore Capital Group Inc
        - Common Stock|Q|Q|N|100|N|N||ECPG|N\r\nY|ECVT|Ecovyst Inc. Common Stock|N|
        |N|100|N||ECVT|ECVT|N\r\nY|ECX|ECARX Holdings Inc. - Class A Ordinary shares|Q|G|N|100|N|N||ECX|N\r\nY|ECXWW|ECARX
        Holdings Inc. - Warrants|Q|S|N|100|N|N||ECXWW|N\r\nY|ED|Consolidated Edison,
        Inc. Common Stock|N| |N|100|N||ED|ED|N\r\nY|EDAP|EDAP TMS S.A. - American
        Depositary Shares, each representing One Ordinary Share|Q|G|N|100|N|N||EDAP|N\r\nY|EDBL|Edible
        Garden AG Incorporated - Common Stock|Q|S|N|100|N|D||EDBL|N\r\nY|EDBLW|Edible
        Garden AG Incorporated - Warrant|Q|S|N|100|N|D||EDBLW|N\r\nY|EDC|Direxion
        Emerging Markets Bull 3X Shares|P| |Y|100|N||EDC|EDC|N\r\nY|EDD|Morgan Stanley
        Emerging Markets Domestic Debt Fund, Inc. Common Stock|N| |N|100|N||EDD|EDD|N\r\nY|EDEN|iShares
        Inc iShares MSCI Denmark ETF|Z| |Y|100|N||EDEN|EDEN|N\r\nY|EDF|Virtus Stone
        Harbor Emerging Markets Income Fund Common Shares of Beneficial Interest|N|
        |N|100|N||EDF|EDF|N\r\nY|EDIT|Editas Medicine, Inc. - Common Stock|Q|Q|N|100|N|N||EDIT|N\r\nY|EDIV|SPDR
        S&P Emerging Markets Dividend ETF|P| |Y|100|N||EDIV|EDIV|N\r\nY|EDN|Empresa
        Distribuidora Y Comercializadora Norte S.A. (Edenor) American Depositary Shares|N|
        |N|100|N||EDN|EDN|N\r\nY|EDOC|Global X Telemedicine & Digital Health ETF|Q|G|Y|100|N|N||EDOC|N\r\nY|EDOG|ALPS
        Emerging Sector Dividend Dogs ETF|P| |Y|100|N||EDOG|EDOG|N\r\nY|EDOW|First
        Trust Dow 30 Equal Weight ETF|P| |Y|100|N||EDOW|EDOW|N\r\nY|EDR|Endeavor Group
        Holdings, Inc. Class A Common Stock|N| |N|100|N||EDR|EDR|N\r\nY|EDRY|EuroDry
        Ltd. - Common Shares|Q|S|N|100|N|N||EDRY|N\r\nY|EDSA|Edesa Biotech, Inc. -
        Common Shares|Q|S|N|100|N|N||EDSA|N\r\nY|EDTK|Skillful Craftsman Education
        Technology Limited - Ordinary Share|Q|S|N|100|N|N||EDTK|N\r\nY|EDU|New Oriental
        Education & Technology Group, Inc. Sponsored ADR representing 10 Ordinary
        Share (Cayman Islands)|N| |N|100|N||EDU|EDU|N\r\nY|EDUC|Educational Development
        Corporation - Common Stock|Q|G|N|100|N|D||EDUC|N\r\nY|EDV|Vanguard Extended
        Duration Treasury ETF|P| |Y|100|N||EDV|EDV|N\r\nY|EDZ|Direxion Emerging Markets
        Bear 3X Shares|P| |Y|100|N||EDZ|EDZ|N\r\nY|EE|Excelerate Energy, Inc. Class
        A Common Stock|N| |N|100|N||EE|EE|N\r\nY|EEA|The European Equity Fund, Inc.
        Common Stock|N| |N|100|N||EEA|EEA|N\r\nY|EEFT|Euronet Worldwide, Inc. - Common
        Stock|Q|Q|N|100|N|N||EEFT|N\r\nY|EEIQ|EpicQuest Education Group International
        Limited - Common Stock|Q|S|N|100|N|N||EEIQ|N\r\nY|EELV|Invesco S&P Emerging
        Markets Low Volatility ETF|P| |Y|100|N||EELV|EELV|N\r\nY|EEM|iShares MSCI
        Emerging Index Fund|P| |Y|100|N||EEM|EEM|N\r\nY|EEMA|iShares MSCI Emerging
        Markets Asia ETF|Q|G|Y|100|N|N||EEMA|N\r\nY|EEMD|AAM S&P Emerging Markets
        High Dividend Value ETF|P| |Y|100|N||EEMD|EEMD|N\r\nY|EEMO|Invesco S&P Emerging
        Markets Momentum ETF|P| |Y|100|N||EEMO|EEMO|N\r\nY|EEMS|Ishares MSCI Emerging
        Markets Small Cap Index Fund|P| |Y|100|N||EEMS|EEMS|N\r\nY|EEMV|iShares MSCI
        Emerging Markets Min Vol Factor ETF|Z| |Y|100|N||EEMV|EEMV|N\r\nY|EEMX|SPDR
        MSCI Emerging Markets Fuel Reserves Free ETF|P| |Y|100|N||EEMX|EEMX|N\r\nY|EES|WisdomTree
        U.S. SmallCap Fund|P| |Y|100|N||EES|EES|N\r\nY|EET|ProShares Ultra MSCI Emerging
        Markets|P| |Y|100|N||EET|EET|N\r\nY|EETH|ProShares Trust ProShares Ether Strategy
        ETF|P| |Y|100|N||EETH|EETH|N\r\nY|EEV|ProShares UltraShort MSCI Emerging Markets|P|
        |Y|100|N||EEV|EEV|N\r\nY|EEX|Emerald Holding, Inc. Common Stock|N| |N|100|N||EEX|EEX|N\r\nY|EFA|iShares
        MSCI EAFE ETF|P| |Y|100|N||EFA|EFA|N\r\nY|EFAD|ProShares Trust ProShares MSCI
        EAFE Dividend Growers ETF|Z| |Y|100|N||EFAD|EFAD|N\r\nY|EFAS|Global X MSCI
        SuperDividend EAFE ETF|Q|G|Y|100|N|N||EFAS|N\r\nY|EFAV|iShares MSCI EAFE Min
        Vol Factor ETF|Z| |Y|100|N||EFAV|EFAV|N\r\nY|EFAX|SPDR MSCI EAFE Fossil Fuel
        Reserves Free ETF|P| |Y|100|N||EFAX|EFAX|N\r\nY|EFC|Ellington Financial Inc.
        Common Stock |N| |N|100|N||EFC|EFC|N\r\nY|EFC$A|Ellington Financial Inc. 6.750%
        Series A Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|N| |N|100|N||EFCpA|EFC-A|N\r\nY|EFC$B|Ellington
        Financial Inc. 6.250% Series B Fixed-Rate Reset Cumulative Redeemable Preferred
        Stock|N| |N|100|N||EFCpB|EFC-B|N\r\nY|EFC$C|Ellington Financial Inc. 8.625%
        Series C Fixed-Rate Reset Cumulative Redeemable Preferred Stock|N| |N|100|N||EFCpC|EFC-C|N\r\nY|EFC$D|Ellington
        Financial Inc. 7.00% Series D Cumulative Perpetual Redeemable Preferred Stock|N|
        |N|100|N||EFCpD|EFC-D|N\r\nY|EFC$E|Ellington Financial Inc. 8.250% Series
        E Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|N| |N|100|N||EFCpE|EFC-E|N\r\nY|EFG|iShares
        MSCI EAFE Growth ETF|Z| |Y|100|N||EFG|EFG|N\r\nY|EFIV|SPDR S&P 500 ESG ETF|P|
        |Y|100|N||EFIV|EFIV|N\r\nY|EFIX|First Trust Exchange-Traded Fund VIII First
        Trust TCW Emerging Markets Debt ETF|P| |Y|100|N||EFIX|EFIX|N\r\nY|EFNL|iShares
        Inc iShares MSCI Finland ETF|Z| |Y|100|N||EFNL|EFNL|N\r\nY|EFO|ProShares Ultra
        MSCI EAFE|P| |Y|100|N||EFO|EFO|N\r\nY|EFOI|Energy Focus, Inc. - Common Stock|Q|S|N|100|N|N||EFOI|N\r\nY|EFR|Eaton
        Vance Senior Floating-Rate Fund Common Shares of Beneficial Interest|N| |N|100|N||EFR|EFR|N\r\nY|EFRA|iShares
        Environmental Infrastructure and Industrials ETF|Q|G|Y|100|N|N||EFRA|N\r\nY|EFSC|Enterprise
        Financial Services Corporation - Common Stock|Q|Q|N|100|N|N||EFSC|N\r\nY|EFSCP|Enterprise
        Financial Services Corporation - Depositary Shares Each Representing a 1/40th
        Interest in a Share of 5% Fixed Rate Non-Cumulative Perpetual Preferred Stock,
        Series A|Q|Q|N|100|N|N||EFSCP|N\r\nY|EFSH|1847 Holdings LLC Common Shares|A|
        |N|100|N||EFSH|EFSH|N\r\nY|EFT|Eaton Vance Floating Rate Income Trust Common
        Shares of Beneficial Interest|N| |N|100|N||EFT|EFT|N\r\nY|EFTR|eFFECTOR Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|D||EFTR|N\r\nY|EFTRW|eFFECTOR Therapeutics,
        Inc. - Warrant|Q|S|N|100|N|D||EFTRW|N\r\nY|EFU|ProShares UltraShort MSCI EAFE|P|
        |Y|100|N||EFU|EFU|N\r\nY|EFUT|VanEck ETF Trust VanEck Ethereum Strategy ETF|Z|
        |Y|100|N||EFUT|EFUT|N\r\nY|EFV|iShares MSCI EAFE Value ETF|Z| |Y|100|N||EFV|EFV|N\r\nY|EFX|Equifax,
        Inc. Common Stock|N| |N|100|N||EFX|EFX|N\r\nY|EFXT|Enerflex Ltd Common Shares|N|
        |N|100|N||EFXT|EFXT|N\r\nY|EFZ|ProShares Short MSCI EAFE|P| |Y|100|N||EFZ|EFZ|N\r\nY|EG|Everest
        Group, Ltd. Common Stock|N| |N|100|N||EG|EG|N\r\nY|EGAN|eGain Corporation
        - Common Stock|Q|S|N|100|N|N||EGAN|N\r\nY|EGBN|Eagle Bancorp, Inc. - Common
        Stock|Q|S|N|100|N|N||EGBN|N\r\nY|EGF|Blackrock Enhanced Government Fund, Inc.
        Common Stock|N| |N|100|N||EGF|EGF|N\r\nY|EGHT|8x8 Inc - Common stock|Q|Q|N|100|N|N||EGHT|N\r\nY|EGIO|Edgio,
        Inc. - Common Stock|Q|S|N|100|N|E||EGIO|N\r\nY|EGO|Eldorado Gold Corporation
        Ordinary Shares|N| |N|100|N||EGO|EGO|N\r\nY|EGP|EastGroup Properties, Inc.
        Common Stock|N| |N|100|N||EGP|EGP|N\r\nY|EGRX|Eagle Pharmaceuticals, Inc.
        - Common Stock|Q|G|N|100|N|E||EGRX|N\r\nY|EGUS|iShares Trust iShares ESG Aware
        MSCI USA Growth ETF|Z| |Y|100|N||EGUS|EGUS|N\r\nY|EGY|VAALCO Energy, Inc.
        \ Common Stock|N| |N|100|N||EGY|EGY|N\r\nY|EH|EHang Holdings Limited - ADS|Q|G|N|100|N|N||EH|N\r\nY|EHAB|Enhabit,
        Inc. Common Stock|N| |N|100|N||EHAB|EHAB|N\r\nY|EHC|Encompass Health Corporation
        Common Stock|N| |N|100|N||EHC|EHC|N\r\nY|EHI|Western Asset Global High Income
        Fund Inc Common Stock|N| |N|100|N||EHI|EHI|N\r\nY|EHLS|Even Herd Long Short
        ETF|Q|G|Y|100|N|N||EHLS|N\r\nY|EHTH|eHealth, Inc. - Common Stock|Q|Q|N|100|N|N||EHTH|N\r\nY|EIC|Eagle
        Point Income Company Inc. Common Stock|N| |N|100|N||EIC|EIC|N\r\nY|EICA|Eagle
        Point Income Company Inc. 5.00% Series A Term Preferred Stock due 2026|N|
        |N|100|N||EICA|EICA|N\r\nY|EICB|Eagle Point Income Company Inc. 7.75% Series
        B Term Preferred Stock Due 2028|N| |N|100|N||EICB|EICB|N\r\nY|EICC|Eagle Point
        Income Company Inc. 8.00% Series C Term Preferred Stock due 2029|N| |N|100|N||EICC|EICC|N\r\nY|EIDO|iShares
        MSCI Indonesia ETF|P| |Y|100|N||EIDO|EIDO|N\r\nY|EIG|Employers Holdings Inc
        Common Stock|N| |N|100|N||EIG|EIG|N\r\nY|EIM|Eaton Vance Municipal Bond Fund
        Common Shares of Beneficial Interest, $.01 par value|A| |N|100|N||EIM|EIM|N\r\nY|EINC|VanEck
        Energy Income ETF|P| |Y|100|N||EINC|EINC|N\r\nY|EIPI|First Trust Exchange-Traded
        Fund VIII FT Energy Income Partners Enhanced Income ETF|P| |Y|100|N||EIPI|EIPI|N\r\nY|EIPX|First
        Trust Exchange-Traded Fund IV FT Energy Income Partners Strategy ETF|P| |Y|100|N||EIPX|EIPX|N\r\nY|EIRL|iShares
        Trust iShares MSCI Ireland ETF|P| |Y|100|N||EIRL|EIRL|N\r\nY|EIS|iShares Inc
        iShares MSCI Israel ETF|P| |Y|100|N||EIS|EIS|N\r\nY|EIX|Edison International
        Common Stock|N| |N|100|N||EIX|EIX|N\r\nY|EJAN|Innovator Emerging Markets Power
        Buffer ETF January|P| |Y|100|N||EJAN|EJAN|N\r\nY|EJH|E-Home Household Service
        Holdings Limited - Ordinary shares|Q|S|N|100|N|N||EJH|N\r\nY|EJUL|Innovator
        Emerging Markets Power Buffer ETF July|P| |Y|100|N||EJUL|EJUL|N\r\nY|EKG|First
        Trust Nasdaq Lux Digital Health Solutions ETF|Q|G|Y|100|N|N||EKG|N\r\nY|EKSO|Ekso
        Bionics Holdings, Inc. - Common Stock|Q|S|N|100|N|N||EKSO|N\r\nY|EL|Estee
        Lauder Companies, Inc. (The) Common Stock|N| |N|100|N||EL|EL|N\r\nY|ELA|Envela
        Corporation Common Stock|A| |N|100|N||ELA|ELA|N\r\nY|ELAB|Elevai Labs, Inc.
        - Common Stock|Q|S|N|100|N|D||ELAB|N\r\nY|ELAN|Elanco Animal Health Incorporated
        Common Stock|N| |N|100|N||ELAN|ELAN|N\r\nY|ELBM|Electra Battery Materials
        Corporation - Common Stock|Q|S|N|100|N|D||ELBM|N\r\nY|ELC|Entergy Louisiana,
        Inc. Collateral Trust Mortgage Bonds, 4.875 % Series due September 1, 2066|N|
        |N|100|N||ELC|ELC|N\r\nY|ELD|WisdomTree Emerging Markets Local Debt Fund|P|
        |Y|100|N||ELD|ELD|N\r\nY|ELDN|Eledon Pharmaceuticals, Inc. - Common Stock|Q|S|N|100|N|N||ELDN|N\r\nY|ELEV|Elevation
        Oncology, Inc. - Common stock|Q|Q|N|100|N|N||ELEV|N\r\nY|ELF|e.l.f. Beauty,
        Inc. Common Stock|N| |N|100|N||ELF|ELF|N\r\nY|ELLO|Ellomay Capital Ltd Ordinary
        Shares (Israel)|A| |N|100|N||ELLO|ELLO|N\r\nY|ELMD|Electromed, Inc. Common
        Stock|A| |N|100|N||ELMD|ELMD|N\r\nY|ELME|Elme Communities Common Stock|N|
        |N|100|N||ELME|ELME|N\r\nY|ELP|Companhia Paranaense de Energia (COPEL) American
        Depositary Shares (each representing one Unit consisting one Common Share
        and four non-voting Class B Preferred Shares)|N| |N|100|N||ELP|ELP|N\r\nY|ELPC|Companhia
        Paranaense de Energia (COPEL) American Depositary Shares (each representing
        four (4) Common Shares)|N| |N|100|N||ELPC|ELPC|N\r\nY|ELQD|iShares ESG Advanced
        Investment Grade Corporate Bond ETF|P| |Y|100|N||ELQD|ELQD|N\r\nY|ELS|Equity
        Lifestyle Properties, Inc. Common Stock|N| |N|100|N||ELS|ELS|N\r\nY|ELSE|Electro-Sensors,
        Inc. - Common Stock|Q|S|N|100|N|N||ELSE|N\r\nY|ELTK|Eltek Ltd. - Ordinary
        Shares|Q|S|N|100|N|N||ELTK|N\r\nY|ELTX|Elicio Therapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||ELTX|N\r\nY|ELUT|Elutia, Inc. - Class A Common Stock|Q|S|N|100|N|N||ELUT|N\r\nY|ELV|Elevance
        Health, Inc. Common Stock|N| |N|100|N||ELV|ELV|N\r\nY|ELVA|Electrovaya Inc.
        - Common Shares|Q|S|N|100|N|N||ELVA|N\r\nY|ELVN|Enliven Therapeutics, Inc.
        \ - Common Stock|Q|Q|N|100|N|N||ELVN|N\r\nY|ELWS|Earlyworks Co., Ltd. - American
        Depositary Shares|Q|S|N|100|N|N||ELWS|N\r\nY|ELYM|Eliem Therapeutics, Inc
        - Common Stock|Q|G|N|100|N|N||ELYM|N\r\nY|EM|Smart Share Global Limited -
        American Depositary Shares|Q|S|N|100|N|N||EM|N\r\nY|EMB|iShares J.P. Morgan
        USD Emerging Markets Bond ETF|Q|G|Y|100|N|N||EMB|N\r\nY|EMBC|Embecta Corp.
        - Common Stock|Q|Q|N|100|N|N||EMBC|N\r\nY|EMBD|Global X Emerging Markets Bond
        ETF|P| |Y|100|N||EMBD|EMBD|N\r\nY|EMC|Global X Funds Global X Emerging Markets
        Great Consumer ETF|P| |Y|100|N||EMC|EMC|N\r\nY|EMCB|WisdomTree Emerging Markets
        Corporate Bond Fund|Q|G|Y|100|N|N||EMCB|N\r\nY|EMCC|Global X Funds Global
        X MSCI Emerging Markets Covered Call ETF|P| |Y|100|N||EMCC|EMCC|N\r\nY|EMCG|Embrace
        Change Acquisition Corp - Ordinary Shares|Q|G|N|100|N|H||EMCG|N\r\nY|EMCGR|Embrace
        Change Acquisition Corp - Rights|Q|G|N|100|N|E||EMCGR|N\r\nY|EMCGU|Embrace
        Change Acquisition Corp - Units|Q|G|N|100|N|E||EMCGU|N\r\nY|EMCGW|Embrace
        Change Acquisition Corp - Warrants|Q|G|N|100|N|E||EMCGW|N\r\nY|EMCR|Xtrackers
        Emerging Markets Carbon Reduction and Climate Improvers ETF|P| |Y|100|N||EMCR|EMCR|N\r\nY|EMD|Western
        Asset Emerging Markets Debt Fund Inc Common Stock|N| |N|100|N||EMD|EMD|N\r\nY|EMDM|First
        Trust Exchange-Traded Fund II First Trust Bloomberg Emerging Market Democracies
        ETF|P| |Y|100|N||EMDM|EMDM|N\r\nY|EMDV|ProShares MSCI Emerging Markets Dividend
        Growers ETF|Z| |Y|100|N||EMDV|EMDV|N\r\nY|EME|EMCOR Group, Inc. Common Stock|N|
        |N|100|N||EME|EME|N\r\nY|EMF|Templeton Emerging Markets Fund Common Stock|N|
        |N|100|N||EMF|EMF|N\r\nY|EMFQ|Amplify Emerging Markets FinTech ETF|P| |Y|100|N||EMFQ|EMFQ|N\r\nY|EMGF|iShares
        Emerging Markets Equity Factor ETF|Z| |Y|100|N||EMGF|EMGF|N\r\nY|EMHC|SPDR
        Bloomberg Emerging Markets USD Bond ETF|P| |Y|100|N||EMHC|EMHC|N\r\nY|EMHY|iShares
        J.P. Morgan EM High Yield Bond ETF|Z| |Y|100|N||EMHY|EMHY|N\r\nY|EMIF|iShares
        Emerging Markets Infrastructure ETF|Q|G|Y|100|N|N||EMIF|N\r\nY|EMKR|EMCORE
        Corporation - Common Stock|Q|S|N|100|N|N||EMKR|N\r\nY|EML|Eastern Company
        (The) - Common Stock|Q|G|N|100|N|N||EML|N\r\nY|EMLC|VanEck J. P. Morgan EM
        Local Currency Bond ET|P| |Y|100|N||EMLC|EMLC|N\r\nY|EMLD|FTAC Emerald Acquisition
        Corp. - Class A Common Stock|Q|G|N|100|N|N||EMLD|N\r\nY|EMLDU|FTAC Emerald
        Acquisition Corp. - Unit|Q|G|N|100|N|N||EMLDU|N\r\nY|EMLDW|FTAC Emerald Acquisition
        Corp. - Warrant|Q|G|N|100|N|N||EMLDW|N\r\nY|EMLP|First Trust North American
        Energy Infrastructure Fund|P| |Y|100|N||EMLP|EMLP|N\r\nY|EMM|Global X Funds
        Global X Emerging Markets ex-China ETF|P| |Y|100|N||EMM|EMM|N\r\nY|EMMF|WisdomTree
        Emerging Markets Multifactor Fund|P| |Y|100|N||EMMF|EMMF|N\r\nY|EMN|Eastman
        Chemical Company Common Stock|N| |N|100|N||EMN|EMN|N\r\nY|EMNT|PIMCO Enhanced
        Short Maturity Active ESG Exchange-Traded Fund|P| |Y|100|N||EMNT|EMNT|N\r\nY|EMO|ClearBridge
        Energy Midstream Opportunity Fund Inc. Common Stock|N| |N|100|N||EMO|EMO|N\r\nY|EMOT|First
        Trust Exchange-Traded Fund VI First Trust S&P 500 Economic Moat ETF|P| |Y|100|N||EMOT|EMOT|N\r\nY|EMP|Entergy
        Mississippi, LLC First Mortgage Bonds, 4.90% Series Due October 1, 2066|N|
        |N|100|N||EMP|EMP|N\r\nY|EMQQ|Emerging Markets Internet and Ecommerce ETF
        (The)|P| |Y|100|N||EMQQ|EMQQ|N\r\nY|EMR|Emerson Electric Company Common Stock|N|
        |N|100|N||EMR|EMR|N\r\nY|EMSF|Matthews International Funds Matthews Emerging
        Markets Sustainable Future Active ETF|P| |Y|100|N||EMSF|EMSF|N\r\nY|EMSG|Xtrackers
        MSCI Emerging Markets ESG Leaders Equity ETF|P| |Y|100|N||EMSG|EMSG|N\r\nY|EMTL|SPDR
        DoubleLine Emerging Markets Fixed Income ETF|Z| |Y|100|N||EMTL|EMTL|N\r\nY|EMTY|ProShares
        Decline of the Retail Store ETF|P| |Y|100|N||EMTY|EMTY|N\r\nY|EMX|EMX Royalty
        Corporation Common Shares (Canada)|A| |N|100|N||EMX|EMX|N\r\nY|EMXC|iShares
        MSCI Emerging Markets ex China ETF|Q|G|Y|100|N|N||EMXC|N\r\nY|EMXF|iShares
        ESG Advanced MSCI EM ETF|Q|G|Y|100|N|N||EMXF|N\r\nY|ENB|Enbridge Inc Common
        Stock|N| |N|100|N||ENB|ENB|N\r\nY|ENFN|Enfusion, Inc. Class A Common Stock|N|
        |N|100|N||ENFN|ENFN|N\r\nY|ENFR|Alerian Energy Infrastructure ETF|P| |Y|100|N||ENFR|ENFR|N\r\nY|ENG|ENGlobal
        Corporation - Common Stock|Q|S|N|100|N|D||ENG|N\r\nY|ENGN|enGene Holdings
        Inc. - Common Stock|Q|S|N|100|N|N||ENGN|N\r\nY|ENGNW|enGene Holdings Inc.
        - Warrants|Q|S|N|100|N|N||ENGNW|N\r\nY|ENIC|Enel Chile S.A. American Depositary
        Shares (Each representing 50 shares of Common Stock)|N| |N|100|N||ENIC|ENIC|N\r\nY|ENJ|Entergy
        New Orleans, LLC First Mortgage Bonds, 5.0% Series due December 1, 2052|N|
        |N|100|N||ENJ|ENJ|N\r\nY|ENLC|EnLink Midstream, LLC Common Units representing
        Limited Partner Interests|N| |N|100|N||ENLC|ENLC|N\r\nY|ENLT|Enlight Renewable
        Energy Ltd. - Ordinary Shares|Q|Q|N|100|N|N||ENLT|N\r\nY|ENLV|Enlivex Therapeutics
        Ltd. - Ordinary Shares|Q|S|N|100|N|N||ENLV|N\r\nY|ENO|Entergy New Orleans,
        LLC First Mortgage Bonds, 5.50% Series due April 1, 2066|N| |N|100|N||ENO|ENO|N\r\nY|ENOR|iShares
        Inc iShares MSCI Norway ETF|Z| |Y|100|N||ENOR|ENOR|N\r\nY|ENOV|Enovis Corporation
        Common Stock|N| |N|100|N||ENOV|ENOV|N\r\nY|ENPH|Enphase Energy, Inc. - Common
        Stock|Q|G|N|100|N|N||ENPH|N\r\nY|ENR|Energizer Holdings, Inc. Common Stock|N|
        |N|100|N||ENR|ENR|N\r\nY|ENS|EnerSys Common Stock|N| |N|100|N||ENS|ENS|N\r\nY|ENSC|Ensysce
        Biosciences, Inc. - Common Stock|Q|S|N|100|N|D||ENSC|N\r\nY|ENSG|The Ensign
        Group, Inc. - Common Stock|Q|Q|N|100|N|N||ENSG|N\r\nY|ENSV|Enservco Corporation
        Common Stock|A| |N|100|N||ENSV|ENSV|N\r\nY|ENTA|Enanta Pharmaceuticals, Inc.
        - Common Stock|Q|Q|N|100|N|N||ENTA|N\r\nY|ENTG|Entegris, Inc. - Common Stock|Q|Q|N|100|N|N||ENTG|N\r\nY|ENTO|Entero
        Therapeutics Inc. - Common Stock|Q|S|N|100|N|N||ENTO|N\r\nY|ENTR|ERShares
        Entrepreneurs ETF|Q|G|Y|100|N|N||ENTR|N\r\nY|ENTX|Entera Bio Ltd. - Ordinary
        Shares|Q|S|N|100|N|N||ENTX|N\r\nY|ENV|Envestnet, Inc Common Stock|N| |N|100|N||ENV|ENV|N\r\nY|ENVA|Enova
        International, Inc. Common Stock|N| |N|100|N||ENVA|ENVA|N\r\nY|ENVB|Enveric
        Biosciences, Inc.  - Common Stock|Q|S|N|100|N|D||ENVB|N\r\nY|ENVX|Enovix Corporation
        - Common Stock|Q|Q|N|100|N|N||ENVX|N\r\nY|ENX|Eaton Vance New York Municipal
        Bond Fund Common Shares of Beneficial Interest, $.01 par value|A| |N|100|N||ENX|ENX|N\r\nY|ENZ|Enzo
        Biochem, Inc. Common Stock ($0.01 Par Value)|N| |N|100|N||ENZ|ENZ|N\r\nY|ENZL|iShares
        MSCI New Zealand ETF|Q|G|Y|100|N|N||ENZL|N\r\nY|EOCT|Innovator Emerging Markets
        Power Buffer ETF - October|P| |Y|100|N||EOCT|EOCT|N\r\nY|EOD|Allspring Global
        Dividend Opportunity Fund Common Shares of Beneficial Interest|N| |N|100|N||EOD|EOD|N\r\nY|EOG|EOG
        Resources, Inc. Common Stock|N| |N|100|N||EOG|EOG|N\r\nY|EOI|Eaton Vance Enhance
        Equity Income Fund Eaton Vance Enhanced Equity Income Fund Shares of Beneficial
        Interest|N| |N|100|N||EOI|EOI|N\r\nY|EOLS|Evolus, Inc. - Common Stock|Q|G|N|100|N|N||EOLS|N\r\nY|EOS|Eaton
        Vance Enhance Equity Income Fund II Common Stock|N| |N|100|N||EOS|EOS|N\r\nY|EOSE|Eos
        Energy Enterprises, Inc. - Common Stock|Q|S|N|100|N|D||EOSE|N\r\nY|EOSEW|Eos
        Energy Enterprises, Inc. - Warrant|Q|S|N|100|N|N||EOSEW|N\r\nY|EOT|Eaton Vance
        Municipal Income Trust EATON VANCE NATIONAL MUNICIPAL OPPORTUNITIES TRUST|N|
        |N|100|N||EOT|EOT|N\r\nY|EP|Empire Petroleum Corporation Common Stock|A| |N|100|N||EP|EP|N\r\nY|EP$C|El
        Paso Corporation Preferred Stock|N| |N|100|N||EPpC|EP-C|N\r\nY|EPAC|Enerpac
        Tool Group Corp. Common Stock|N| |N|100|N||EPAC|EPAC|N\r\nY|EPAM|EPAM Systems,
        Inc. Common Stock|N| |N|100|N||EPAM|EPAM|N\r\nY|EPC|Edgewell Personal Care
        Company Common Stock|N| |N|100|N||EPC|EPC|N\r\nY|EPD|Enterprise Products Partners
        L.P. Common Stock|N| |N|100|N||EPD|EPD|N\r\nY|EPHE|iShares MSCI Philippines
        ETF|P| |Y|100|N||EPHE|EPHE|N\r\nY|EPI|WisdomTree India Earnings Fund|P| |Y|100|N||EPI|EPI|N\r\nY|EPIX|ESSA
        Pharma Inc. - Common Stock|Q|S|N|100|N|N||EPIX|N\r\nY|EPM|Evolution Petroleum
        Corporation, Inc. Common Stock|A| |N|100|N||EPM|EPM|N\r\nY|EPOL|iShares Trust
        iShares MSCI Poland ETF|P| |Y|100|N||EPOL|EPOL|N\r\nY|EPOW|Sunrise New Energy
        Co., Ltd - Class A Ordinary Shares|Q|S|N|100|N|D||EPOW|N\r\nY|EPP|iShares
        MSCI Pacific Ex-Japan Index Fund|P| |Y|100|N||EPP|EPP|N\r\nY|EPR|EPR Properties
        Common Stock|N| |N|100|N||EPR|EPR|N\r\nY|EPR$C|EPR Properties 5.75% Series
        C Cumulative Convertible Preferred Shares|N| |N|100|N||EPRpC|EPR-C|N\r\nY|EPR$E|EPR
        Properties Series E Cumulative Conv Pfd Shs Ser E|N| |N|100|N||EPRpE|EPR-E|N\r\nY|EPR$G|EPR
        Properties 5.750% Series G Cumulative Redeemable Preferred Shares|N| |N|100|N||EPRpG|EPR-G|N\r\nY|EPRF|Innovator
        S&P Investment Grade Preferred ETF|Z| |Y|100|N||EPRF|EPRF|N\r\nY|EPRT|Essential
        Properties Realty Trust, Inc. Common Stock|N| |N|100|N||EPRT|EPRT|N\r\nY|EPRX|Eupraxia
        Pharmaceuticals Inc. - Common Stock|Q|S|N|100|N|N||EPRX|N\r\nY|EPS|WisdomTree
        U.S. LargeCap Fund|P| |Y|100|N||EPS|EPS|N\r\nY|EPSN|Epsilon Energy Ltd. -
        Common Shares|Q|G|N|100|N|N||EPSN|N\r\nY|EPU|iShares MSCI Peru and Global
        Exposure ETF|P| |Y|100|N||EPU|EPU|N\r\nY|EPV|ProShares UltraShort FTSE Europe
        ETF|P| |Y|100|N||EPV|EPV|N\r\nY|EQ|Equillium, Inc. - Common Stock|Q|S|N|100|N|N||EQ|N\r\nY|EQAL|Invesco
        Russell 1000 Equal Weight ETF|P| |Y|100|N||EQAL|EQAL|N\r\nY|EQBK|Equity Bancshares,
        Inc. Class A Common Stock|N| |N|100|N||EQBK|EQBK|N\r\nY|EQC|Equity Commonwealth
        Common Shares of Beneficial Interest|N| |N|100|N||EQC|EQC|N\r\nY|EQC$D|Equity
        Commonwealth 6.50% Pfd Conv Shs Ser D|N| |N|100|N||EQCpD|EQC-D|N\r\nY|EQH|Equitable
        Holdings, Inc. Common Stock|N| |N|100|N||EQH|EQH|N\r\nY|EQH$A|Equitable Holdings,
        Inc. Depositary Shares|N| |N|100|N||EQHpA|EQH-A|N\r\nY|EQH$C|Equitable Holdings,
        Inc. Depositary Shares, each representing a 1/1,000th interest in a share
        of Fixed Rate Noncumulative Perpetual Preferred Stock, Series C|N| |N|100|N||EQHpC|EQH-C|N\r\nY|EQIN|Columbia
        U.S. Equity Income ETF|P| |Y|100|N||EQIN|EQIN|N\r\nY|EQIX|Equinix, Inc. -
        Common Stock|Q|Q|N|100|N|N||EQIX|N\r\nY|EQL|ALPS Equal Sector Weight ETF|P|
        |Y|100|N||EQL|EQL|N\r\nY|EQLS|Simplify Exchange Traded Funds Simplify Market
        Neutral Equity Long/Short ETF|P| |Y|100|N||EQLS|EQLS|N\r\nY|EQNR|Equinor ASA|N|
        |N|100|N||EQNR|EQNR|N\r\nY|EQR|Equity Residential Common Shares of Beneficial
        Interest|N| |N|100|N||EQR|EQR|N\r\nY|EQRR|ProShares Equities for Rising Rates
        ETF|Q|G|Y|100|N|N||EQRR|N\r\nY|EQS|Equus Total Return, Inc. Common Stock|N|
        |N|100|N||EQS|EQS|N\r\nY|EQT|EQT Corporation Common Stock|N| |N|100|N||EQT|EQT|N\r\nY|EQTY|Valued
        Advisers Trust Kovitz Core Equity ETF|P| |Y|100|N||EQTY|EQTY|N\r\nY|EQUL|IQ
        Engender Equality ETF|P| |Y|100|N||EQUL|EQUL|N\r\nY|EQWL|Invesco S&P 100 Equal
        Weight ETF|P| |Y|100|N||EQWL|EQWL|N\r\nY|EQX|Equinox Gold Corp. Common Shares|A|
        |N|100|N||EQX|EQX|N\r\nY|ERAS|Erasca, Inc. - Common Stock|Q|Q|N|100|N|N||ERAS|N\r\nY|ERC|Allspring
        Multi-Sector Income Fund Common Stock|A| |N|100|N||ERC|ERC|N\r\nY|ERET|iShares
        Environmentally Aware Real Estate ETF|Q|G|Y|100|N|N||ERET|N\r\nY|ERH|Allspring
        Utilities and High Income Fund Common Shares|A| |N|100|N||ERH|ERH|N\r\nY|ERIC|Ericsson
        - American Depositary Shares each representing 1 underlying Class B share|Q|Q|N|100|N|N||ERIC|N\r\nY|ERIE|Erie
        Indemnity Company - Class A Common Stock|Q|Q|N|100|N|N||ERIE|N\r\nY|ERII|Energy
        Recovery, Inc. - Common Stock|Q|Q|N|100|N|N||ERII|N\r\nY|ERJ|Embraer S.A.
        Common Stock|N| |N|100|N||ERJ|ERJ|N\r\nY|ERNA|Eterna Therapeutics Inc. - Common
        Stock|Q|S|N|100|N|D||ERNA|N\r\nY|ERNZ|TrueShares Active Yield ETF|Q|G|Y|100|N|N||ERNZ|N\r\nY|ERO|Ero
        Copper Corp. Common Shares|N| |N|100|N||ERO|ERO|N\r\nY|ERTH|Invesco MSCI Sustainable
        Future ETF|P| |Y|100|N||ERTH|ERTH|N\r\nY|ERX|Direxion Energy Bull 2X Shares|P|
        |Y|100|N||ERX|ERX|N\r\nY|ERY|Direxion Daily Energy Bear 2X Shares|P| |Y|100|N||ERY|ERY|N\r\nY|ES|Eversource
        Energy (D/B/A) Common Stock|N| |N|100|N||ES|ES|N\r\nY|ESAB|ESAB Corporation
        Common Stock|N| |N|100|N||ESAB|ESAB|N\r\nY|ESBA|Empire State Realty OP, L.P.
        Series ES Operating Partnership Units Representing Limited Partnership Interests|P|
        |N|100|N||ESBA|ESBA|N\r\nY|ESCA|Escalade, Incorporated - Common Stock|Q|G|N|100|N|N||ESCA|N\r\nY|ESE|ESCO
        Technologies Inc. Common Stock|N| |N|100|N||ESE|ESE|N\r\nY|ESEA|Euroseas Ltd.
        - Common Stock|Q|S|N|100|N|N||ESEA|N\r\nY|ESG|FlexShares STOXX US ESG Select
        Index Fund|Z| |Y|100|N||ESG|ESG|N\r\nY|ESGA|American Century Sustainable Equity
        ETF|P| |Y|100|N||ESGA|ESGA|N\r\nY|ESGB|IQ MacKay ESG Core Plus Bond ETF|P|
        |Y|100|N||ESGB|ESGB|N\r\nY|ESGD|iShares ESG Aware MSCI EAFE ETF|Q|G|Y|100|N|N||ESGD|N\r\nY|ESGE|iShares
        ESG Aware MSCI EM ETF|Q|G|Y|100|N|N||ESGE|N\r\nY|ESGG|FlexShares STOXX Global
        ESG Select Index Fund|Z| |Y|100|N||ESGG|ESGG|N\r\nY|ESGL|ESGL Holdings Limited
        - Class A Ordinary Shares|Q|S|N|100|N|N||ESGL|N\r\nY|ESGLW|ESGL Holdings Limited
        - Warrants|Q|S|N|100|N|N||ESGLW|N\r\nY|ESGR|Enstar Group Limited - Ordinary
        Shares|Q|Q|N|100|N|N||ESGR|N\r\nY|ESGRO|Enstar Group Limited - Depository
        Shares 7.00% Perpetual Non-Cumulative Preference Shares, Series E|Q|Q|N|100|N|N||ESGRO|N\r\nY|ESGRP|Enstar
        Group Limited - Depositary Shares Each Representing 1/1000th of an interest
        in Preference Shares|Q|Q|N|100|N|N||ESGRP|N\r\nY|ESGU|iShares ESG Aware MSCI
        USA ETF|Q|G|Y|100|N|N||ESGU|N\r\nY|ESGV|Vanguard ESG U.S. Stock ETF|Z| |Y|100|N||ESGV|ESGV|N\r\nY|ESGY|American
        Century Sustainable Growth ETF|P| |Y|100|N||ESGY|ESGY|N\r\nY|ESHA|ESH Acquisition
        Corp. - Class A Common Stock|Q|G|N|100|N|N||ESHA|N\r\nY|ESHAR|ESH Acquisition
        Corp. - Right|Q|G|N|100|N|N||ESHAR|N\r\nY|ESI|Element Solutions Inc. Common
        Stock|N| |N|100|N||ESI|ESI|N\r\nY|ESIX|SSGA Active Trust SPDR S&P SmallCap
        600 ESG ETF|P| |Y|100|N||ESIX|ESIX|N\r\nY|ESLA|Estrella Immunopharma, Inc.
        - Common Stock|Q|S|N|100|N|N||ESLA|N\r\nY|ESLAW|Estrella Immunopharma, Inc.
        - Warrant|Q|S|N|100|N|N||ESLAW|N\r\nY|ESLT|Elbit Systems Ltd. - Ordinary Shares|Q|Q|N|100|N|N||ESLT|N\r\nY|ESML|iShares
        ESG Aware MSCI USA Small-Cap ETF|Z| |Y|100|N||ESML|ESML|N\r\nY|ESMV|iShares
        ESG MSCI USA Min Vol Factor ETF|Q|G|Y|100|N|N||ESMV|N\r\nY|ESNT|Essent Group
        Ltd. Common Shares|N| |N|100|N||ESNT|ESNT|N\r\nY|ESOA|Energy Services of America
        Corporation - Common Stock|Q|S|N|100|N|N||ESOA|N\r\nY|ESP|Espey Mfg. & Electronics
        Corp. Common Stock|A| |N|100|N||ESP|ESP|N\r\nY|ESPO|VanEck Video Gaming and
        eSports ETF|Q|G|Y|100|N|N||ESPO|N\r\nY|ESPR|Esperion Therapeutics, Inc. -
        Common Stock|Q|G|N|100|N|N||ESPR|N\r\nY|ESQ|Esquire Financial Holdings, Inc.
        - Common Stock|Q|S|N|100|N|N||ESQ|N\r\nY|ESRT|Empire State Realty Trust, Inc.
        Class A Common Stock|N| |N|100|N||ESRT|ESRT|N\r\nY|ESS|Essex Property Trust,
        Inc. Common Stock|N| |N|100|N||ESS|ESS|N\r\nY|ESSA|ESSA Bancorp, Inc. - common
        stock|Q|Q|N|100|N|N||ESSA|N\r\nY|ESTA|Establishment Labs Holdings Inc. - Common
        Shares|Q|S|N|100|N|N||ESTA|N\r\nY|ESTC|Elastic N.V. Ordinary Shares|N| |N|100|N||ESTC|ESTC|N\r\nY|ESUS|ETRACS
        2x Leveraged MSCI US ESG Focus TR ETN|P| |Y|100|N||ESUS|ESUS|N\r\nY|ET|Energy
        Transfer LP Common Units |N| |N|100|N||ET|ET|N\r\nY|ET$I|Energy Transfer L.P.
        Series I Fixed Rate Perpetual Preferred Units|N| |N|100|N||ETpI|ET-I|N\r\nY|ETB|Eaton
        Vance Tax-Managed Buy-Write Income Fund Eaton Vance Tax-Managed Buy-Write
        Income Fund Common Shares of Beneficial Interest|N| |N|100|N||ETB|ETB|N\r\nY|ETD|Ethan
        Allen Interiors Inc. Common Stock|N| |N|100|N||ETD|ETD|N\r\nY|ETEC|iShares
        Breakthrough Environmental Solutions ETF|Q|G|Y|100|N|N||ETEC|N\r\nY|ETG|Eaton
        Vance Tax-Advantaged Global Dividend Income Fund Common Shares of Beneficial
        Interest|N| |N|100|N||ETG|ETG|N\r\nY|ETHD|ProShares Trust ProShares UltraShort
        Ether ETF|P| |Y|100|N||ETHD|ETHD|N\r\nY|ETHO|Amplify ETF Trust Amplify Etho
        Climate Leadership U.S. ETF|P| |Y|100|N||ETHO|ETHO|N\r\nY|ETHT|ProShares Trust
        ProShares Ultra Ether ETF|P| |Y|100|N||ETHT|ETHT|N\r\nY|ETHU|Volatility Shares
        Trust 2x Ether ETF|Z| |Y|100|N||ETHU|ETHU|N\r\nY|ETI$|Entergy Texas Inc 5.375%
        Series A Preferred Stock, Cumulative, No Par Value|N| |N|100|N||ETIp|ETI-|N\r\nY|ETJ|Eaton
        Vance Risk-Managed Diversified Equity Income Fund Common Shares of Beneficial
        Interest|N| |N|100|N||ETJ|ETJ|N\r\nY|ETN|Eaton Corporation, PLC Ordinary Shares|N|
        |N|100|N||ETN|ETN|N\r\nY|ETNB|89bio, Inc. - Common Stock|Q|G|N|100|N|N||ETNB|N\r\nY|ETO|Eaton
        Vance Tax-Advantage Global Dividend Opp Common Stock|N| |N|100|N||ETO|ETO|N\r\nY|ETON|Eton
        Pharmaceuticals, Inc. - Common Stock|Q|G|N|100|N|N||ETON|N\r\nY|ETR|Entergy
        Corporation Common Stock|N| |N|100|N||ETR|ETR|N\r\nY|ETRN|Equitrans Midstream
        Corporation Common Stock |N| |N|100|N||ETRN|ETRN|N\r\nY|ETSY|Etsy, Inc. -
        Common Stock|Q|Q|N|100|N|N||ETSY|N\r\nY|ETV|Eaton Vance Corporation Eaton
        Vance Tax-Managed Buy-Write Opportunities Fund Common Shares of Beneficial
        Interest|N| |N|100|N||ETV|ETV|N\r\nY|ETW|Eaton Vance Corporation Eaton Vance
        Tax-Managed Global Buy-Write Opportunites Fund Common Shares of Beneficial
        Interest|N| |N|100|N||ETW|ETW|N\r\nY|ETWO|E2open Parent Holdings, Inc.Class
        A Common Stock|N| |N|100|N||ETWO|ETWO|N\r\nY|ETWO.W|E2open Parent Holdings,
        Inc. Warrants|N| |N|100|N||ETWO.WS|ETWO+|N\r\nY|ETX|Eaton Vance Municipal
        Income 2028 Term Trust Common Shares of Beneficial Interest|N| |N|100|N||ETX|ETX|N\r\nY|ETY|Eaton
        Vance Tax-Managed Diversified Equity Income Fund Common Shares of Beneficial
        Interest,|N| |N|100|N||ETY|ETY|N\r\nY|EU|enCore Energy Corp. - Common Stock|Q|S|N|100|N|N||EU|N\r\nY|EUDA|Euda
        Health Holdings Limited - Ordinary Shares|Q|S|N|100|N|N||EUDA|N\r\nY|EUDAW|Euda
        Health Holdings Limited - Warrant|Q|S|N|100|N|N||EUDAW|N\r\nY|EUDG|WisdomTree
        Europe Quality Dividend Growth Fund|P| |Y|100|N||EUDG|EUDG|N\r\nY|EUDV|ProShares
        MSCI Europe Dividend Growers ETF|Z| |Y|100|N||EUDV|EUDV|N\r\nY|EUFN|iShares
        MSCI Europe Financials ETF|Q|G|Y|100|N|N||EUFN|N\r\nY|EUM|ProShares Short
        MSCI Emerging Markets|P| |Y|100|N||EUM|EUM|N\r\nY|EUO|ProShares UltraShort
        Euro|P| |Y|100|N||EUO|EUO|N\r\nY|EURL|Direxion Daily FTSE Europe Bull 3x Shares|P|
        |Y|100|N||EURL|EURL|N\r\nY|EURN|Euronav NV Ordinary Shares|N| |N|100|N||EURN|EURN|N\r\nY|EUSA|iShares
        MSCI USA Equal Weighted ETF|P| |Y|100|N||EUSA|EUSA|N\r\nY|EUSB|iShares ESG
        Advanced Total USD Bond Market ETF|P| |Y|100|N||EUSB|EUSB|N\r\nY|EUSC|WisdomTree
        Europe Hedged SmallCap Equity Fund|P| |Y|100|N||EUSC|EUSC|N\r\nY|EV|NEOS ETF
        Trust Mast Global Battery Recycling & Production ETF|P| |Y|100|N||EV|EV|N\r\nY|EVA|Enviva
        Inc. Common Stock|N| |N|100|N||EVA|EVA|N\r\nY|EVAV|Direxion Shares ETF Trust
        Direxion Daily Electric and Autonomous Vehicles Bull 2X Shares|P| |Y|100|N||EVAV|EVAV|N\r\nY|EVAX|Evaxion
        Biotech A/S - American Depositary Share|Q|S|N|100|N|D||EVAX|N\r\nY|EVBG|Everbridge,
        Inc. - Common Stock|Q|G|N|100|N|N||EVBG|N\r\nY|EVBN|Evans Bancorp, Inc. Common
        Stock|A| |N|100|N||EVBN|EVBN|N\r\nY|EVC|Entravision Communications Corporation
        Common Stock|N| |N|100|N||EVC|EVC|N\r\nY|EVCM|EverCommerce Inc. - Common Stock|Q|Q|N|100|N|D||EVCM|N\r\nY|EVE|EVe
        Mobility Acquisition Corp Class A Ordinary Shares|A| |N|100|N||EVE|EVE|N\r\nY|EVE.U|EVe
        Mobility Acquisition Corp Units, each consisting of one Class A ordinary share
        and one-half of one redeemable warrant(|A| |N|100|N||EVE.U|EVE=|N\r\nY|EVE.W|EVe
        Mobility Acquisition Corp Redeemable warrants, each whole warrant exercisable
        for one Class A ordinary share at an exercise price of $11.50|A| |N|100|N||EVE.WS|EVE+|N\r\nY|EVER|EverQuote,
        Inc. - Class A Common Stock|Q|G|N|100|N|N||EVER|N\r\nY|EVEX|Eve Holding, Inc.
        Common Stock|N| |N|100|N||EVEX|EVEX|N\r\nY|EVEX.W|Eve Holding, Inc. Warrants,
        each exercisable for one share of Common Stock at an exercise price of $11.50
        per share|N| |N|100|N||EVEX.WS|EVEX+|N\r\nY|EVF|Eaton Vance Senior Income
        Trust Common Stock|N| |N|100|N||EVF|EVF|N\r\nY|EVG|Eaton Vance Short Diversified
        Income Fund Eaton Vance Short Duration Diversified Income Fund Common Shares
        of Beneficial Interest|N| |N|100|N||EVG|EVG|N\r\nY|EVGN|Evogene Ltd. - Ordinary
        Shares|Q|S|N|100|N|D||EVGN|N\r\nY|EVGO|EVgo Inc. - Common Stock|Q|Q|N|100|N|N||EVGO|N\r\nY|EVGOW|EVgo
        Inc. - Warrants, each whole warrant exercisable for one share of Class A Common
        Stock at an exercise price of $11.50|Q|Q|N|100|N|N||EVGOW|N\r\nY|EVGR|Evergreen
        Corporation - Class A Ordinary Share|Q|G|N|100|N|N||EVGR|N\r\nY|EVGRU|Evergreen
        Corporation - Unit|Q|G|N|100|N|N||EVGRU|N\r\nY|EVGRW|Evergreen Corporation
        - Warrant|Q|G|N|100|N|N||EVGRW|N\r\nY|EVH|Evolent Health, Inc Class A Common
        Stock|N| |N|100|N||EVH|EVH|N\r\nY|EVHY|Morgan Stanley ETF Trust Eaton Vance
        High Yield ETF|P| |Y|100|N||EVHY|EVHY|N\r\nY|EVI|EVI Industries, Inc.  Common
        Stock|A| |N|100|N||EVI|EVI|N\r\nY|EVIM|Morgan Stanley ETF Trust Eaton Vance
        Intermediate Municipal Income ETF|P| |Y|100|N||EVIM|EVIM|N\r\nY|EVLN|Morgan
        Stanley ETF Trust Eaton Vance Floating-Rate ETF|P| |Y|100|N||EVLN|EVLN|N\r\nY|EVLV|Evolv
        Technologies Holdings, Inc. - Class A Common Stock|Q|S|N|100|N|N||EVLV|N\r\nY|EVLVW|Evolv
        Technologies Holdings, Inc. - Warrant|Q|S|N|100|N|N||EVLVW|N\r\nY|EVM|Eaton
        Vance California Municipal Bond Fund Common Shares of Beneficial Interest,
        $.01 par value|A| |N|100|N||EVM|EVM|N\r\nY|EVMT|Invesco Electric Vehicle Metals
        Commodity Strategy No K-1 ETF|Q|G|Y|100|N|N||EVMT|N\r\nY|EVN|Eaton Vance Municipal
        Income Trust Common Stock|N| |N|100|N||EVN|EVN|N\r\nY|EVNT|AltShares Event-Driven
        ETF|P| |Y|100|N||EVNT|EVNT|N\r\nY|EVO|Evotec SE - American Depositary Shares
        each representing 1/2 of one ordinary share|Q|Q|N|100|N|E||EVO|N\r\nY|EVOK|Evoke
        Pharma, Inc. - Common Stock|Q|S|N|100|N|D||EVOK|N\r\nY|EVR|Evercore Inc. Class
        A Common Stock|N| |N|100|N||EVR|EVR|N\r\nY|EVRG|Evergy, Inc. - Common Stock|Q|Q|N|100|N|N||EVRG|N\r\nY|EVRI|Everi
        Holdings Inc. Common Stock|N| |N|100|N||EVRI|EVRI|N\r\nY|EVSB|Morgan Stanley
        ETF Trust Eaton Vance Ultra-Short Income ETF|P| |Y|100|N||EVSB|EVSB|N\r\nY|EVSD|Eaton
        Vance Short Duration Income ETF|Q|G|Y|100|N|N||EVSD|N\r\nY|EVSM|Morgan Stanley
        ETF Trust Eaton Vance Short Duration Municipal Income ETF|P| |Y|100|N||EVSM|EVSM|N\r\nY|EVT|Eaton
        Vance Tax Advantaged Dividend Income Fund Common Shares of Beneficial Interest|N|
        |N|100|N||EVT|EVT|N\r\nY|EVTC|Evertec, Inc. Common Stock|N| |N|100|N||EVTC|EVTC|N\r\nY|EVTL|Vertical
        Aerospace Ltd. Ordinary Shares|N| |N|100|N||EVTL|EVTL|N\r\nY|EVTL.W|Vertical
        Aerospace Ltd. Warrants, each whole warrant exercisable for one ordinary share
        at an exercise price of $11.50 per share|N| |N|100|N||EVTL.WS|EVTL+|N\r\nY|EVTR|Morgan
        Stanley ETF Trust Eaton Vance Total Return Bond ETF|N| |Y|100|N||EVTR|EVTR|N\r\nY|EVTV|Envirotech
        Vehicles, Inc. - Common stock|Q|S|N|100|N|N||EVTV|N\r\nY|EVUS|iShares Trust
        iShares ESG Aware MSCI USA Value ETF|Z| |Y|100|N||EVUS|EVUS|N\r\nY|EVV|Eaton
        Vance Limited Duration Income Fund Common Shares of Beneficial Interest|A|
        |N|100|N||EVV|EVV|N\r\nY|EVX|VanEck Environmental Services ETF|P| |Y|100|N||EVX|EVX|N\r\nY|EW|Edwards
        Lifesciences Corporation Common Stock|N| |N|100|N||EW|EW|N\r\nY|EWA|iShares
        MSCI Australia Index Fund|P| |Y|100|N||EWA|EWA|N\r\nY|EWBC|East West Bancorp,
        Inc. - Common Stock|Q|Q|N|100|N|N||EWBC|N\r\nY|EWC|iShares MSCI Canada Index
        Fund|P| |Y|100|N||EWC|EWC|N\r\nY|EWCZ|European Wax Center, Inc. - Class A
        Common Stock|Q|Q|N|100|N|N||EWCZ|N\r\nY|EWD|iShares Inc iShares MSCI Sweden
        ETF|P| |Y|100|N||EWD|EWD|N\r\nY|EWG|iShares MSCI Germany Index Fund|P| |Y|100|N||EWG|EWG|N\r\nY|EWH|iShares
        MSCI Hong Kong Index Fund|P| |Y|100|N||EWH|EWH|N\r\nY|EWI|iShares Inc iShares
        MSCI Italy ETF|P| |Y|100|N||EWI|EWI|N\r\nY|EWJ|iShares MSCI Japan Index Fund|P|
        |Y|100|N||EWJ|EWJ|N\r\nY|EWJV|iShares MSCI Japan Value ETF|Q|G|Y|100|N|N||EWJV|N\r\nY|EWK|iShares
        Inc iShares MSCI Belgium ETF|P| |Y|100|N||EWK|EWK|N\r\nY|EWL|iShares Inc iShares
        MSCI Switzerland ETF|P| |Y|100|N||EWL|EWL|N\r\nY|EWM|iShares MSCI Malaysia
        Index Fund|P| |Y|100|N||EWM|EWM|N\r\nY|EWN|iShares MSCI Netherlands Index
        Fund|P| |Y|100|N||EWN|EWN|N\r\nY|EWO|iShares Inc iShares MSCI Austria ETF|P|
        |Y|100|N||EWO|EWO|N\r\nY|EWP|iShares Inc iShares MSCI Spain ETF|P| |Y|100|N||EWP|EWP|N\r\nY|EWQ|iShares
        MSCI France Index Fund|P| |Y|100|N||EWQ|EWQ|N\r\nY|EWS|iShares Inc iShares
        MSCI Singapore ETF|P| |Y|100|N||EWS|EWS|N\r\nY|EWT|iShares Inc iShares MSCI
        Taiwan ETF|P| |Y|100|N||EWT|EWT|N\r\nY|EWTX|Edgewise Therapeutics, Inc. -
        Common Stock|Q|Q|N|100|N|N||EWTX|N\r\nY|EWU|iShares MSCI United Kingdom ETF|P|
        |Y|100|N||EWU|EWU|N\r\nY|EWUS|Ishares MSCI United Kingdom Small Cap ETF|Z|
        |Y|100|N||EWUS|EWUS|N\r\nY|EWV|ProShares UltraShort MSCI Japan|P| |Y|100|N||EWV|EWV|N\r\nY|EWW|iShares
        Inc iShares MSCI Mexico ETF|P| |Y|100|N||EWW|EWW|N\r\nY|EWX|SPDR S&P Emerging
        Markets Small Cap ETF|P| |Y|100|N||EWX|EWX|N\r\nY|EWY|iShares Inc iShares
        MSCI South Korea ETF|P| |Y|100|N||EWY|EWY|N\r\nY|EWZ|iShares Inc iShares MSCI
        Brazil ETF|P| |Y|100|N||EWZ|EWZ|N\r\nY|EWZS|iShares MSCI Brazil Small-Cap
        ETF|Q|G|Y|100|N|N||EWZS|N\r\nY|EXAI|Exscientia Plc - American Depositary Shares|Q|Q|N|100|N|N||EXAI|N\r\nY|EXAS|Exact
        Sciences Corporation - Common Stock|Q|S|N|100|N|N||EXAS|N\r\nY|EXC|Exelon
        Corporation - Common Stock|Q|Q|N|100|N|N||EXC|N\r\nY|EXEL|Exelixis, Inc. -
        Common Stock|Q|Q|N|100|N|N||EXEL|N\r\nY|EXFY|Expensify, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||EXFY|N\r\nY|EXG|Eaton Vance Tax-Managed Global Diversified
        Equity Income Fund Common Shares of Beneficial Interest|N| |N|100|N||EXG|EXG|N\r\nY|EXI|iShares
        Global Industrials ETF|P| |Y|100|N||EXI|EXI|N\r\nY|EXK|Endeavour Silver Corporation
        Ordinary Shares (Canada)|N| |N|100|N||EXK|EXK|N\r\nY|EXLS|ExlService Holdings,
        Inc. - Common Stock|Q|Q|N|100|N|N||EXLS|N\r\nY|EXP|Eagle Materials Inc Common
        Stock|N| |N|100|N||EXP|EXP|N\r\nY|EXPD|Expeditors International of Washington,
        Inc. Common Stock|N| |N|100|N||EXPD|EXPD|N\r\nY|EXPE|Expedia Group, Inc. -
        Common Stock|Q|Q|N|100|N|N||EXPE|N\r\nY|EXPI|eXp World Holdings, Inc. - Common
        Stock|Q|G|N|100|N|N||EXPI|N\r\nY|EXPO|Exponent, Inc. - Common Stock|Q|Q|N|100|N|N||EXPO|N\r\nY|EXR|Extra
        Space Storage Inc Common Stock|N| |N|100|N||EXR|EXR|N\r\nY|EXTO|Almacenes
        Exito S.A. American Depositary Share, each representing eight (8) Common Shares|N|
        |N|100|N||EXTO|EXTO|N\r\nY|EXTR|Extreme Networks, Inc. - Common Stock|Q|Q|N|100|N|N||EXTR|N\r\nY|EYE|National
        Vision Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||EYE|N\r\nY|EYEG|AB Corporate
        Bond ETF|Q|G|Y|100|N|N||EYEG|N\r\nY|EYEN|Eyenovia, Inc. - Common Stock|Q|S|N|100|N|N||EYEN|N\r\nY|EYLD|Cambria
        ETF Trust Cambria Emerging Shareholder Yield ETF|Z| |Y|100|N||EYLD|EYLD|N\r\nY|EYPT|EyePoint
        Pharmaceuticals, Inc. - Common Stock|Q|G|N|100|N|N||EYPT|N\r\nY|EZA|iShares
        MSCI South Africa Index Fund|P| |Y|100|N||EZA|EZA|N\r\nY|EZBC|Franklin Templeton
        Digital Holdings Trust Shares of Franklin Bitcoin ETF|Z| |Y|100|N||EZBC|EZBC|N\r\nY|EZFL|EzFill
        Holdings, Inc. - Common Stock|Q|S|N|100|N|D||EZFL|N\r\nY|EZGO|EZGO Technologies
        Ltd. - Ordinary Shares|Q|S|N|100|N|N||EZGO|N\r\nY|EZJ|ProShares Ultra MSCI
        Japan|P| |Y|100|N||EZJ|EZJ|N\r\nY|EZM|WisdomTree U.S. MidCap Fund|P| |Y|100|N||EZM|EZM|N\r\nY|EZPW|EZCORP,
        Inc. - Class A Non-Voting Common Stock|Q|Q|N|100|N|N||EZPW|N\r\nY|EZU|iShares
        MSCI Eurozone ETF|Z| |Y|100|N||EZU|EZU|N\r\nY|F|Ford Motor Company Common
        Stock|N| |N|100|N||F|F|N\r\nY|F$B|Ford Motor Company 6.20% Notes due June
        1, 2059|N| |N|100|N||FpB|F-B|N\r\nY|F$C|Ford Motor Company 6% Notes due December
        1, 2059|N| |N|100|N||FpC|F-C|N\r\nY|F$D|Ford Motor Company 6.500% Notes due
        August 15, 2062|N| |N|100|N||FpD|F-D|N\r\nY|FA|First Advantage Corporation
        - Common Stock|Q|Q|N|100|N|N||FA|N\r\nY|FAAR|First Trust Alternative Absolute
        Return Strategy ETF|Q|G|Y|100|N|N||FAAR|N\r\nY|FAAS|DigiAsia Corp. - Ordinary
        Shares|Q|S|N|100|N|N||FAAS|N\r\nY|FAASW|DigiAsia Corp. - Warrant|Q|S|N|100|N|N||FAASW|N\r\nY|FAB|First
        Trust Multi Cap Value AlphaDEX Fund|Q|G|Y|100|N|N||FAB|N\r\nY|FAD|First Trust
        Multi Cap Growth AlphaDEX Fund|Q|G|Y|100|N|N||FAD|N\r\nY|FAF|First American
        Corporation (New) Common Stock|N| |N|100|N||FAF|FAF|N\r\nY|FAIL|Cambria ETF
        Trust Cambria Global Tail Risk ETF|Z| |Y|100|N||FAIL|FAIL|N\r\nY|FALN|iShares
        Fallen Angels USD Bond ETF|Q|G|Y|100|N|N||FALN|N\r\nY|FAM|First Trust/abrdn
        Global Opportunity Income Fund Common Shares of Beneficial Interest|N| |N|100|N||FAM|FAM|N\r\nY|FAMI|Farmmi,
        INC. - Ordinary Shares|Q|S|N|100|N|D||FAMI|N\r\nY|FAN|First Trust Global Wind
        Energy ETF|P| |Y|100|N||FAN|FAN|N\r\nY|FANG|Diamondback Energy, Inc. - Common
        Stock|Q|Q|N|100|N|N||FANG|N\r\nY|FANH|Fanhua Inc. - American depositary shares,
        each representing 20 ordinary shares|Q|Q|N|100|N|N||FANH|N\r\nY|FAPR|FT Vest
        U.S. Equity Buffer ETF - April|Z| |Y|100|N||FAPR|FAPR|N\r\nY|FARM|Farmer Brothers
        Company - Common Stock|Q|Q|N|100|N|N||FARM|N\r\nY|FARO|FARO Technologies,
        Inc. - Common Stock|Q|Q|N|100|N|N||FARO|N\r\nY|FAS|Direxion Financial Bull
        3X Shares|P| |Y|100|N||FAS|FAS|N\r\nY|FAST|Fastenal Company - Common Stock|Q|Q|N|100|N|N||FAST|N\r\nY|FAT|FAT
        Brands Inc. - Common Stock|Q|S|N|100|N|N||FAT|N\r\nY|FATBB|FAT Brands Inc.
        - Class B Common Stock|Q|S|N|100|N|N||FATBB|N\r\nY|FATBP|FAT Brands Inc. -
        8.25% Series B Cumulative Preferred Stock|Q|S|N|100|N|N||FATBP|N\r\nY|FATBW|FAT
        Brands Inc. - Warrant|Q|S|N|100|N|N||FATBW|N\r\nY|FATE|Fate Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||FATE|N\r\nY|FAUG|FT Vest U.S. Equity Buffer
        ETF - August|Z| |Y|100|N||FAUG|FAUG|N\r\nY|FAX|abrdn Asia-Pacific Income Fund,
        Inc. Common Stock|A| |N|100|N||FAX|FAX|N\r\nY|FAZ|Direxion Financial Bear
        3X Shares|P| |Y|100|N||FAZ|FAZ|N\r\nY|FBCG|Fidelity Blue Chip Growth ETF|Z|
        |Y|100|N||FBCG|FBCG|N\r\nY|FBCV|Fidelity Blue Chip Value ETF|Z| |Y|100|N||FBCV|FBCV|N\r\nY|FBIN|Fortune
        Brands Innovations, Inc. Common Stock|N| |N|100|N||FBIN|FBIN|N\r\nY|FBIO|Fortress
        Biotech, Inc. - Common Stock|Q|S|N|100|N|N||FBIO|N\r\nY|FBIOP|Fortress Biotech,
        Inc. - 9.375% Series A Cumulative Redeemable Perpetual Preferred Stock|Q|S|N|100|N|N||FBIOP|N\r\nY|FBIZ|First
        Business Financial Services, Inc. - Common Stock|Q|Q|N|100|N|N||FBIZ|N\r\nY|FBK|FB
        Financial Corporation Common Stock|N| |N|100|N||FBK|FBK|N\r\nY|FBL|GraniteShares
        2x Long META Daily ETF|Q|G|Y|100|N|N||FBL|N\r\nY|FBLG|FibroBiologics, Inc.
        - Common Stock|Q|G|N|100|N|N||FBLG|N\r\nY|FBMS|First Bancshares, Inc.|N| |N|100|N||FBMS|FBMS|N\r\nY|FBNC|First
        Bancorp - Common Stock|Q|Q|N|100|N|N||FBNC|N\r\nY|FBND|Fidelity Total Bond
        ETF|P| |Y|100|N||FBND|FBND|N\r\nY|FBOT|Fidelity Disruptive Automation ETF|Q|G|Y|100|N|N||FBOT|N\r\nY|FBP|First
        BanCorp. New Common Stock|N| |N|100|N||FBP|FBP|N\r\nY|FBRT|Franklin BSP Realty
        Trust, Inc. Common Stock|N| |N|100|N||FBRT|FBRT|N\r\nY|FBRT$E|Franklin BSP
        Realty Trust, Inc. 7.50% Series E Cumulative Redeemable Preferred Stock|N|
        |N|100|N||FBRTpE|FBRT-E|N\r\nY|FBRX|Forte Biosciences, Inc.  - Common Stock|Q|S|N|100|N|D||FBRX|N\r\nY|FBT|First
        Trust Amex Biotech Index Fund|P| |Y|100|N||FBT|FBT|N\r\nY|FBTC|Fidelity Wise
        Origin Bitcoin Fund Common Shares of Beneficial Interest|Z| |Y|100|N||FBTC|FBTC|N\r\nY|FBUF|Fidelity
        Dynamic Buffered Equity ETF Fidelity Dynamic Buffered Equity ETF|Z| |Y|100|N||FBUF|FBUF|N\r\nY|FBY|Tidal
        ETF Trust II YieldMax META Option Income Strategy ETF|P| |Y|100|N||FBY|FBY|N\r\nY|FBYD|Falcon's
        Beyond Global, Inc. - Class A Common Stock|Q|G|N|100|N|N||FBYD|N\r\nY|FBYDW|Falcon's
        Beyond Global, Inc. - Warrants|Q|S|N|100|N|N||FBYDW|N\r\nY|FBZ|First Trust
        Brazil AlphaDEX Fund|Q|G|Y|100|N|N||FBZ|N\r\nY|FC|Franklin Covey Company Common
        Stock|N| |N|100|N||FC|FC|N\r\nY|FCA|First Trust China AlphaDEX Fund|Q|G|Y|100|N|N||FCA|N\r\nY|FCAL|First
        Trust California Municipal High income ETF|Q|G|Y|100|N|N||FCAL|N\r\nY|FCAP|First
        Capital, Inc. - Common Stock|Q|S|N|100|N|N||FCAP|N\r\nY|FCBC|First Community
        Bankshares, Inc. - Common Stock|Q|Q|N|100|N|N||FCBC|N\r\nY|FCCO|First Community
        Corporation - Common Stock|Q|S|N|100|N|N||FCCO|N\r\nY|FCEF|First Trust Income
        Opportunities ETF|Q|G|Y|100|N|N||FCEF|N\r\nY|FCEL|FuelCell Energy, Inc. -
        Common Stock|Q|G|N|100|N|D||FCEL|N\r\nY|FCF|First Commonwealth Financial Corporation
        Common Stock|N| |N|100|N||FCF|FCF|N\r\nY|FCFS|FirstCash Holdings, Inc. - Common
        Stock|Q|Q|N|100|N|N||FCFS|N\r\nY|FCFY|First Trust Exchange-Traded Fund First
        Trust S&P 500 Diversified Free Cash Flow ETF|P| |Y|100|N||FCFY|FCFY|N\r\nY|FCG|First
        Trust Natural Gas ETF|P| |Y|100|N||FCG|FCG|N\r\nY|FCLD|Fidelity Cloud Computing
        ETF|Z| |Y|100|N||FCLD|FCLD|N\r\nY|FCN|FTI Consulting, Inc. Common Stock|N|
        |N|100|N||FCN|FCN|N\r\nY|FCNCA|First Citizens BancShares, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||FCNCA|N\r\nY|FCNCO|First Citizens BancShares, Inc. -
        5.625% Non-Cumulative Perpetual Preferred Stock, Series C|Q|Q|N|100|N|N||FCNCO|N\r\nY|FCNCP|First
        Citizens BancShares, Inc. - Depositary Shares Each Representing a 1/40th Interest
        in a Share of 5.375% Non-Cumulative Perpetual Preferred Stock, Series A|Q|Q|N|100|N|N||FCNCP|N\r\nY|FCO|abrdn
        Global Income Fund, Inc. Common Stock|A| |N|100|N||FCO|FCO|N\r\nY|FCOM|Fidelity
        MSCI Communication Services Index ETF|P| |Y|100|N||FCOM|FCOM|N\r\nY|FCOR|Fidelity
        Corporate Bond ETF|P| |Y|100|N||FCOR|FCOR|N\r\nY|FCPI|Fidelity Stocks for
        Inflation ETF |Z| |Y|100|N||FCPI|FCPI|N\r\nY|FCPT|Four Corners Property Trust,
        Inc. Common Stock|N| |N|100|N||FCPT|FCPT|N\r\nY|FCRX|Crescent Capital BDC,
        Inc. 5.00% Notes due 2026|N| |N|100|N||FCRX|FCRX|N\r\nY|FCSH|Federated Hermes
        ETF Trust Federated Hermes Short Duration Corporate ETF|P| |Y|100|N||FCSH|FCSH|N\r\nY|FCT|First
        Trust Senior Floating Rate Income Fund II Common Shares of Beneficial Interest|N|
        |N|100|N||FCT|FCT|N\r\nY|FCTR|First Trust Lunt U.S. Factor Rotation ETF|Z|
        |Y|100|N||FCTR|FCTR|N\r\nY|FCUS|Tidal ETF Trust II Pinnacle Focused Opportunities
        ETF|P| |Y|100|N||FCUS|FCUS|N\r\nY|FCUV|Focus Universal Inc. - Common Stock|Q|G|N|100|N|D||FCUV|N\r\nY|FCVT|First
        Trust SSI Strategic Convertible Securities ETF|Q|G|Y|100|N|N||FCVT|N\r\nY|FCX|Freeport-McMoRan,
        Inc. Common Stock|N| |N|100|N||FCX|FCX|N\r\nY|FDAT|Return Stacked Bonds &
        Managed Futures ETF Tactical Advantage ETF|P| |Y|100|N||FDAT|FDAT|N\r\nY|FDBC|Fidelity
        D & D Bancorp, Inc. - Common Stock|Q|G|N|100|N|N||FDBC|N\r\nY|FDCE|Affinity
        World Leaders Equity ETF Foundations Dynamic Core ETF|Z| |Y|100|N||FDCE|FDCE|N\r\nY|FDCF|Fidelity
        Disruptive Communications ETF|Q|G|Y|100|N|N||FDCF|N\r\nY|FDD|First Trust Dow
        Jones STOXX Select Dividend 30 Index Fund|P| |Y|100|N||FDD|FDD|N\r\nY|FDEC|FT
        Vest U.S. Equity Buffer ETF - December|Z| |Y|100|N||FDEC|FDEC|N\r\nY|FDEM|Fidelity
        Emerging Markets Multifactor ETF|Z| |Y|100|N||FDEM|FDEM|N\r\nY|FDEV|Fidelity
        Emerging Markets Multifactor ETF|Z| |Y|100|N||FDEV|FDEV|N\r\nY|FDFF|Fidelity
        Disruptive Finance ETF|Q|G|Y|100|N|N||FDFF|N\r\nY|FDG|American Century Focused
        Dynamic Growth ETF|P| |Y|100|N||FDG|FDG|N\r\nY|FDGR|Affinity World Leaders
        Equity ETF Foundations Dynamic Growth ETF|Z| |Y|100|N||FDGR|FDGR|N\r\nY|FDHT|Fidelity
        Digital Health ETF|Z| |Y|100|N||FDHT|FDHT|N\r\nY|FDHY|Fidelity High Yield
        Factor ETF|P| |Y|100|N||FDHY|FDHY|N\r\nY|FDIF|Fidelity Disruptors ETF|Q|G|Y|100|N|N||FDIF|N\r\nY|FDIG|Fidelity
        Crypto Industry and Digital Payments ETF|Q|G|Y|100|N|N||FDIG|N\r\nY|FDIS|Fidelity
        MSCI Consumer Discretionary Index ETF|P| |Y|100|N||FDIS|FDIS|N\r\nY|FDIV|MarketDesk
        Focused U.S. Dividend ETF|Q|G|Y|100|N|N||FDIV|N\r\nY|FDL|First Trust Morningstar
        ETF|P| |Y|100|N||FDL|FDL|N\r\nY|FDLO|Fidelity Low Volatility Factor ETF|P|
        |Y|100|N||FDLO|FDLO|N\r\nY|FDLS|Northern Lights Fund Trust IV Inspire Fidelis
        Multi Factor ETF|P| |Y|100|N||FDLS|FDLS|N\r\nY|FDM|First Trust DJ Select MicroCap
        ETF|P| |Y|100|N||FDM|FDM|N\r\nY|FDMO|Fidelity Momentum Factor ETF|P| |Y|100|N||FDMO|FDMO|N\r\nY|FDMT|4D
        Molecular Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||FDMT|N\r\nY|FDN|First
        Trust DJ Internet Index Fund|P| |Y|100|N||FDN|FDN|N\r\nY|FDND|First Trust
        Exchange-Traded Fund IV FT Vest Dow Jones Internet & Target Income ETF|Z|
        |Y|100|N||FDND|FDND|N\r\nY|FDNI|First Trust Dow Jones International Internet
        ETF|Q|G|Y|100|N|N||FDNI|N\r\nY|FDP|Fresh Del Monte Produce, Inc. Common Stock|N|
        |N|100|N||FDP|FDP|N\r\nY|FDRR|Fidelity Dividend ETF for Rising Rates|P| |Y|100|N||FDRR|FDRR|N\r\nY|FDRV|Fidelity
        Electric Vehicles and Future Transportation ETF|Z| |Y|100|N||FDRV|FDRV|N\r\nY|FDS|FactSet
        Research Systems Inc. Common Stock|N| |N|100|N||FDS|FDS|N\r\nY|FDT|First Trust
        Developed Markets Ex-US AlphaDEX Fund|Q|G|Y|100|N|N||FDT|N\r\nY|FDTB|Affinity
        World Leaders Equity ETF Foundations Dynamic Income ETF|Z| |Y|100|N||FDTB|FDTB|N\r\nY|FDTS|First
        Trust Developed Markets ex-US Small Cap AlphaDEX Fund|Q|G|Y|100|N|N||FDTS|N\r\nY|FDTX|Fidelity
        Disruptive Technology ETF|Q|G|Y|100|N|N||FDTX|N\r\nY|FDUS|Fidus Investment
        Corporation - Closed End Fund|Q|Q|N|100|N|N||FDUS|N\r\nY|FDV|Federated Hermes
        ETF Trust Federated Hermes U.S. Strategic Dividend ETF|P| |Y|100|N||FDV|FDV|N\r\nY|FDVL|Affinity
        World Leaders Equity ETF Foundations Dynamic Value ETF|Z| |Y|100|N||FDVL|FDVL|N\r\nY|FDVV|Fidelity
        High Dividend ETF|P| |Y|100|N||FDVV|FDVV|N\r\nY|FDWM|Fidelity Women's Leadership
        ETF|P| |Y|100|N||FDWM|FDWM|N\r\nY|FDX|FedEx Corporation Common Stock|N| |N|100|N||FDX|FDX|N\r\nY|FE|FirstEnergy
        Corp. Common Stock|N| |N|100|N||FE|FE|N\r\nY|FEAM|5E Advanced Materials, Inc.
        - Common Stock|Q|Q|N|100|N|N||FEAM|N\r\nY|FEBO|Fenbo Holdings Limited - Ordinary
        Shares|Q|S|N|100|N|N||FEBO|N\r\nY|FEBP|PGIM US Large-Cap Buffer 12 ETF - January
        PGIM US Large-Cap Buffer 12 ETF - February|Z| |Y|100|N||FEBP|FEBP|N\r\nY|FEBT|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer10 Feb ETF|P| |Y|100|N||FEBT|FEBT|N\r\nY|FEBW|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer20 Feb ETF|P| |Y|100|N||FEBW|FEBW|N\r\nY|FEBZ|TrueShares
        Structured Outcome (February) ETF|Z| |Y|100|N||FEBZ|FEBZ|N\r\nY|FEDL|ETRACS
        2x Leveraged IFED Invest with the Fed TR Index ETN|P| |Y|100|N||FEDL|FEDL|N\r\nY|FEDM|FlexShares
        ESG & Climate Developed Markets ex-US Core Index Fund|P| |Y|100|N||FEDM|FEDM|N\r\nY|FEDU|Four
        Seasons Education (Cayman) Inc. American Depositary Shares, each ADS representing
        10 ordinary shares|N| |N|100|N||FEDU|FEDU|N\r\nY|FEIG|FlexShares ESG & Climate
        Investment Grade Corporate Core Index Fund|P| |Y|100|N||FEIG|FEIG|N\r\nY|FEIM|Frequency
        Electronics, Inc. - Common Stock|Q|G|N|100|N|N||FEIM|N\r\nY|FELC|Fidelity
        Covington Trust Fidelity Enhanced Large Cap Core ETF|P| |Y|100|N||FELC|FELC|N\r\nY|FELE|Franklin
        Electric Co., Inc. - Common Stock|Q|Q|N|100|N|N||FELE|N\r\nY|FELG|Fidelity
        Covington Trust Fidelity Enhanced Large Cap Growth ETF|P| |Y|100|N||FELG|FELG|N\r\nY|FELV|Fidelity
        Covington Trust Fidelity Enhanced Large Cap Value ETF|P| |Y|100|N||FELV|FELV|N\r\nY|FEM|First
        Trust Emerging Markets AlphaDEX Fund|Q|G|Y|100|N|N||FEM|N\r\nY|FEMB|First
        Trust Emerging Markets Local Currency Bond ETF|Q|G|Y|100|N|N||FEMB|N\r\nY|FEMS|First
        Trust Emerging Markets Small Cap AlphaDEX Fund|Q|G|Y|100|N|N||FEMS|N\r\nY|FEMY|Femasys
        Inc. - Common Stock|Q|S|N|100|N|N||FEMY|N\r\nY|FENC|Fennec Pharmaceuticals
        Inc. - Common Stock|Q|S|N|100|N|N||FENC|N\r\nY|FENG|Phoenix New Media Limited
        American Depositary Shares, each representing 48 Class A ordinary shares.|N|
        |N|100|N||FENG|FENG|N\r\nY|FENI|Fidelity Covington Trust Fidelity Enhanced
        International ETF|P| |Y|100|N||FENI|FENI|N\r\nY|FENY|Fidelity MSCI Energy
        Index ETF|P| |Y|100|N||FENY|FENY|N\r\nY|FEP|First Trust Europe AlphaDEX Fund|Q|G|Y|100|N|N||FEP|N\r\nY|FEPI|REX
        FANG & Innovation Equity Premium Income ETF|Q|G|Y|100|N|N||FEPI|N\r\nY|FER|Ferrovial
        SE - Ordinary Shares|Q|Q|N|100|N|N||FER|N\r\nY|FERG|Ferguson plc Ordinary
        Shares|N| |N|100|N||FERG|FERG|N\r\nY|FESM|Fidelity Covington Trust Fidelity
        Enhanced Small Cap ETF|P| |Y|100|N||FESM|FESM|N\r\nY|FET|Forum Energy Technologies,
        Inc. Common Stock|N| |N|100|N||FET|FET|N\r\nY|FEUS|FlexShares ESG & Climate
        US Large Cap Core Index Fund|P| |Y|100|N||FEUS|FEUS|N\r\nY|FEUZ|First Trust
        Eurozone AlphaDEX ETF|Q|G|Y|100|N|N||FEUZ|N\r\nY|FEX|First Trust Large Cap
        Core AlphaDEX Fund|Q|G|Y|100|N|N||FEX|N\r\nY|FEXD|Fintech Ecosystem Development
        Corp. - Class A Common Stock|Q|S|N|100|N|E||FEXD|N\r\nY|FEXDR|Fintech Ecosystem
        Development Corp. - Right|Q|S|N|100|N|E||FEXDR|N\r\nY|FEXDU|Fintech Ecosystem
        Development Corp. - Units|Q|S|N|100|N|E||FEXDU|N\r\nY|FEXDW|Fintech Ecosystem
        Development Corp. - Warrant|Q|S|N|100|N|E||FEXDW|N\r\nY|FEZ|SPDR DJ Euro STOXX
        50 Etf|P| |Y|100|N||FEZ|FEZ|N\r\nY|FF|FutureFuel Corp.  Common shares|N| |N|100|N||FF|FF|N\r\nY|FFA|First
        Trust Enhanced Equity Income Fund|N| |N|100|N||FFA|FFA|N\r\nY|FFBC|First Financial
        Bancorp. - Common Stock|Q|Q|N|100|N|N||FFBC|N\r\nY|FFC|Flaherty & Crumrine
        Preferred and Income Securities Fund Incorporated|N| |N|100|N||FFC|FFC|N\r\nY|FFEB|FT
        Vest U.S. Equity Buffer ETF - February|Z| |Y|100|N||FFEB|FFEB|N\r\nY|FFIC|Flushing
        Financial Corporation - Common Stock|Q|Q|N|100|N|N||FFIC|N\r\nY|FFIE|Faraday
        Future Intelligent Electric Inc. - Common Stock|Q|S|N|100|N|H||FFIE|N\r\nY|FFIEW|Faraday
        Future Intelligent Electric Inc. - Warrant|Q|S|N|100|N|E||FFIEW|N\r\nY|FFIN|First
        Financial Bankshares, Inc. - Common Stock|Q|Q|N|100|N|N||FFIN|N\r\nY|FFIU|UVA
        Unconstrained Medium-Term Fixed Income ETF|P| |Y|100|N||FFIU|FFIU|N\r\nY|FFIV|F5,
        Inc. - Common Stock|Q|Q|N|100|N|N||FFIV|N\r\nY|FFLC|Fidelity Fundamental Large
        Cap Core ETF|Z| |Y|100|N||FFLC|FFLC|N\r\nY|FFLG|Fidelity Fundamental Large
        Cap Growth ETF|Z| |Y|100|N||FFLG|FFLG|N\r\nY|FFLS|Northern Lights Fund Trust
        II The Future Fund Long/Short ETF|P| |Y|100|N||FFLS|FFLS|N\r\nY|FFLV|Fidelity
        Covington Trust Fidelity Fundamental Large Cap Value ETF|Z| |Y|100|N||FFLV|FFLV|N\r\nY|FFND|The
        Future Fund Active ETF|P| |Y|100|N||FFND|FFND|N\r\nY|FFNW|First Financial
        Northwest, Inc. - Common Stock|Q|Q|N|100|N|N||FFNW|N\r\nY|FFOG|Franklin Templeton
        ETF Trust Franklin Focused Growth ETF|Z| |Y|100|N||FFOG|FFOG|N\r\nY|FFSM|Fidelity
        Fundamental Small-Mid Cap ETF|Z| |Y|100|N||FFSM|FFSM|N\r\nY|FFTY|Innovator
        IBD 50 ETF|P| |Y|100|N||FFTY|FFTY|N\r\nY|FFWM|First Foundation Inc. Common
        Stock|N| |N|100|N||FFWM|FFWM|N\r\nY|FG|F&G Annuities & Life, Inc. Common Stock|N|
        |N|100|N||FG|FG|N\r\nY|FGB|First Trust Specialty Finance and Financial Opportunities
        Fund|N| |N|100|N||FGB|FGB|N\r\nY|FGBI|First Guaranty Bancshares, Inc. - Common
        Stock|Q|G|N|100|N|N||FGBI|N\r\nY|FGBIP|First Guaranty Bancshares, Inc. - 6.75%
        Series A Fixed-Rate Non-Cumulative Perpetual Preferred Stock|Q|G|N|100|N|N||FGBIP|N\r\nY|FGD|First
        Trust DJ Global Select Dividend|P| |Y|100|N||FGD|FGD|N\r\nY|FGDL|Franklin
        Templeton Holdings Trust Franklin Responsibly Sourced Gold ETF|P| |Y|100|N||FGDL|FGDL|N\r\nY|FGEN|FibroGen,
        Inc - Common Stock|Q|Q|N|100|N|N||FGEN|N\r\nY|FGF|Fundamental Global Inc.
        - Common Stock|Q|G|N|100|N|N||FGF|N\r\nY|FGFPP|Fundamental Global Inc. - 8.00%
        Cumulative Series A Preferred Stock|Q|G|N|100|N|N||FGFPP|N\r\nY|FGI|FGI Industries
        Ltd. - Ordinary Shares|Q|S|N|100|N|N||FGI|N\r\nY|FGIWW|FGI Industries Ltd.
        - warrant|Q|S|N|100|N|N||FGIWW|N\r\nY|FGM|First Trust Germany AlphaDEX Fund|Q|G|Y|100|N|N||FGM|N\r\nY|FGN|F&G
        Annuities & Life, Inc. 7.950% Senior Notes due 2053|N| |N|100|N||FGN|FGN|N\r\nY|FHB|First
        Hawaiian, Inc. - Common Stock|Q|Q|N|100|N|N||FHB|N\r\nY|FHEQ|Fidelity Dynamic
        Buffered Equity ETF Fidelity Hedged Equity ETF|Z| |Y|100|N||FHEQ|FHEQ|N\r\nY|FHI|Federated
        Hermes, Inc. Common Stock|N| |N|100|N||FHI|FHI|N\r\nY|FHLC|Fidelity MSCI Health
        Care Index ETF|P| |Y|100|N||FHLC|FHLC|N\r\nY|FHN|First Horizon Corporation
        Common Stock|N| |N|100|N||FHN|FHN|N\r\nY|FHN$B|First Horizon Corporation Depositary
        Shares, each representing a 1/400th interest in a share of Non-Cumulative
        Perpetual Preferred Stock, Series B|N| |N|100|N||FHNpB|FHN-B|N\r\nY|FHN$C|First
        Horizon Corporation Depositary Shares, each representing a 1/400th interest
        in a share of Non-Cumulative Perpetual Preferred Stock, Series C|N| |N|100|N||FHNpC|FHN-C|N\r\nY|FHN$E|First
        Horizon Corporation Depositary Shares, each representing a 1/4,000th interest
        in a share of Non-Cumulative Perpetual Preferred Stock, Series E|N| |N|100|N||FHNpE|FHN-E|N\r\nY|FHN$F|First
        Horizon Corporation Depositary Shares, each representing 1/4000th Interest
        in a Share of Non-Cumulative Perpetual Preferred Stock, Series F|N| |N|100|N||FHNpF|FHN-F|N\r\nY|FHTX|Foghorn
        Therapeutics Inc. - Common Stock|Q|G|N|100|N|N||FHTX|N\r\nY|FHYS|Federated
        Hermes ETF Trust Federated Hermes Short Duration High Yield ETF|P| |Y|100|N||FHYS|FHYS|N\r\nY|FI|Fiserv,
        Inc. Common Stock|N| |N|100|N||FI|FI|N\r\nY|FIAC|Focus Impact Acquisition
        Corp. - Class A Common Stock|Q|G|N|100|N|N||FIAC|N\r\nY|FIACU|Focus Impact
        Acquisition Corp. - Unit|Q|G|N|100|N|N||FIACU|N\r\nY|FIACW|Focus Impact Acquisition
        Corp. - Warrant|Q|G|N|100|N|N||FIACW|N\r\nY|FIAX|Tidal ETF Trust II Nicholas
        Fixed Income Alternative ETF|P| |Y|100|N||FIAX|FIAX|N\r\nY|FIBK|First Interstate
        BancSystem, Inc. - Common Stock|Q|Q|N|100|N|N||FIBK|N\r\nY|FIBR|iShares U.S.
        Fixed Income Balanced Risk Systematic ETF|Z| |Y|100|N||FIBR|FIBR|N\r\nY|FICO|Fair
        Isaac Corproation Common Stock|N| |N|100|N||FICO|FICO|N\r\nY|FICS|First Trust
        International Developed Capital Strength ETF|Q|G|Y|100|N|N||FICS|N\r\nY|FID|First
        Trust S&P International Dividend Aristocrats ETF|Q|G|Y|100|N|N||FID|N\r\nY|FIDI|Fidelity
        International High Dividend ETF|P| |Y|100|N||FIDI|FIDI|N\r\nY|FIDU|Fidelity
        MSCI Industrials Index ETF|P| |Y|100|N||FIDU|FIDU|N\r\nY|FIG|Simplify Exchange
        Traded Funds Simplify Macro Strategy ETF|P| |Y|100|N||FIG|FIG|N\r\nY|FIGB|Fidelity
        Investment Grade Bond ETF|P| |Y|100|N||FIGB|FIGB|N\r\nY|FIGS|FIGS, Inc. Class
        A Common Stock|N| |N|100|N||FIGS|FIGS|N\r\nY|FIHL|Fidelis Insurance Holdings
        Limited Common Shares|N| |N|100|N||FIHL|FIHL|N\r\nY|FIIG|First Trust Exchange-Traded
        Fund IV First Trust Intermediate Duration Investment Grade Corporate ETF|P|
        |Y|100|N||FIIG|FIIG|N\r\nY|FILL|iShares MSCI Global Energy Producers Fund|P|
        |Y|100|N||FILL|FILL|N\r\nY|FINE|Themes European Luxury ETF|Q|G|Y|100|N|N||FINE|N\r\nY|FINS|Angel
        Oak Financial Strategies Income Term Trust Common Shares of Beneficial Interest|N|
        |N|100|N||FINS|FINS|N\r\nY|FINV|FinVolution Group American Depositary Shares|N|
        |N|100|N||FINV|FINV|N\r\nY|FINW|FinWise Bancorp - Common Stock|Q|G|N|100|N|N||FINW|N\r\nY|FINX|Global
        X FinTech ETF|Q|G|Y|100|N|N||FINX|N\r\nY|FIP|FTAI Infrastructure Inc. - Common
        Stock|Q|Q|N|100|N|N||FIP|N\r\nY|FIS|Fidelity National Information Services,
        Inc. Common Stock|N| |N|100|N||FIS|FIS|N\r\nY|FISI|Financial Institutions,
        Inc. - Common Stock|Q|Q|N|100|N|N||FISI|N\r\nY|FISK|Empire State Realty OP,
        L.P. Series 250 Operating Partnership Units Representing Limited Partnership
        Interests|P| |N|100|N||FISK|FISK|N\r\nY|FISR|SPDR SSGA Fixed Income Sector
        Rotation ETF|P| |Y|100|N||FISR|FISR|N\r\nY|FITB|Fifth Third Bancorp - Common
        Stock|Q|Q|N|100|N|N||FITB|N\r\nY|FITBI|Fifth Third Bancorp - Depositary Share
        repstg 1/1000th Ownership Interest Perp Pfd Series I|Q|Q|N|100|N|N||FITBI|N\r\nY|FITBO|Fifth
        Third Bancorp - Depositary Shares each representing a 1/1000th ownership interest
        in a share of Non-Cumulative Perpetual Preferred Stock, Series K|Q|Q|N|100|N|N||FITBO|N\r\nY|FITBP|Fifth
        Third Bancorp - Depositary Shares each representing 1/40th share of Fifth
        Third 6.00% Non-Cumulative Perpetual Class B Preferred Stock, Series A|Q|Q|N|100|N|N||FITBP|N\r\nY|FITE|SPDR
        S&P Kensho Future Security ETF |P| |Y|100|N||FITE|FITE|N\r\nY|FIVA|Fidelity
        International Value Factor ETF|P| |Y|100|N||FIVA|FIVA|N\r\nY|FIVE|Five Below,
        Inc. - Common Stock|Q|Q|N|100|N|N||FIVE|N\r\nY|FIVG|Defiance Next Gen Connectivity
        ETF|P| |Y|100|N||FIVG|FIVG|N\r\nY|FIVN|Five9, Inc. - Common Stock|Q|G|N|100|N|N||FIVN|N\r\nY|FIW|First
        Trust Water ETF|P| |Y|100|N||FIW|FIW|N\r\nY|FIX|Comfort Systems USA, Inc.
        Common Stock|N| |N|100|N||FIX|FIX|N\r\nY|FIXD|First Trust TCW Opportunistic
        Fixed Income ETF|Q|G|Y|100|N|N||FIXD|N\r\nY|FIXT|Procure Disaster Recovery
        Strategy ETF|Q|G|Y|100|N|N||FIXT|N\r\nY|FIZZ|National Beverage Corp. - Common
        Stock|Q|Q|N|100|N|N||FIZZ|N\r\nY|FJAN|FT Vest U.S. Equity Buffer ETF - January|Z|
        |Y|100|N||FJAN|FJAN|N\r\nY|FJP|First Trust Japan AlphaDEX Fund|Q|G|Y|100|N|N||FJP|N\r\nY|FJUL|FT
        Vest U.S. Equity Buffer ETF - July|Z| |Y|100|N||FJUL|FJUL|N\r\nY|FJUN|FT Vest
        U.S. Equity Buffer ETF - June|Z| |Y|100|N||FJUN|FJUN|N\r\nY|FKU|First Trust
        United Kingdom AlphaDEX Fund|Q|G|Y|100|N|N||FKU|N\r\nY|FKWL|Franklin Wireless
        Corp. - common stock|Q|S|N|100|N|N||FKWL|N\r\nY|FL|Foot Locker, Inc.|N| |N|100|N||FL|FL|N\r\nY|FLAO|AIM
        ETF Products Trust AllianzIM U.S. Equity 6 Month Floor5 Apr/Oct ETF|P| |Y|100|N||FLAO|FLAO|N\r\nY|FLAU|Franklin
        FTSE Australia ETF|P| |Y|100|N||FLAU|FLAU|N\r\nY|FLAX|Franklin FTSE Asia ex
        Japan ETF|P| |Y|100|N||FLAX|FLAX|N\r\nY|FLBL|Franklin Senior Loan ETF|Z| |Y|100|N||FLBL|FLBL|N\r\nY|FLBR|Franklin
        FTSE Brazil ETF|P| |Y|100|N||FLBR|FLBR|N\r\nY|FLC|Flaherty & Crumrine Total
        Return Fund Inc Common Stock|N| |N|100|N||FLC|FLC|N\r\nY|FLCA|Franklin FTSE
        Canada ETF|P| |Y|100|N||FLCA|FLCA|N\r\nY|FLCB|Franklin U.S. Core Bond ETF|P|
        |Y|100|N||FLCB|FLCB|N\r\nY|FLCH|Franklin FTSE China ETF|P| |Y|100|N||FLCH|FLCH|N\r\nY|FLCO|Franklin
        Investment Grade Corporate ETF|P| |Y|100|N||FLCO|FLCO|N\r\nY|FLDB|Fidelity
        Low Duration Bond ETF|Q|G|Y|100|N|N||FLDB|N\r\nY|FLDR|Fidelity Low Duration
        Bond Factor ETF|Z| |Y|100|N||FLDR|FLDR|N\r\nY|FLDZ|RiverNorth Patriot ETF|Z|
        |Y|100|N||FLDZ|FLDZ|N\r\nY|FLEE|Franklin FTSE Europe ETF|P| |Y|100|N||FLEE|FLEE|N\r\nY|FLEU|Franklin
        FTSE Eurozone ETF|P| |Y|100|N||FLEU|FLEU|N\r\nY|FLEX|Flex Ltd. - Ordinary
        Shares|Q|Q|N|100|N|N||FLEX|N\r\nY|FLGB|Franklin FTSE United Kingdom ETF|P|
        |Y|100|N||FLGB|FLGB|N\r\nY|FLGC|Flora Growth Corp. - Common Stock|Q|S|N|100|N|N||FLGC|N\r\nY|FLGR|Franklin
        FTSE Germany ETF|P| |Y|100|N||FLGR|FLGR|N\r\nY|FLGT|Fulgent Genetics, Inc.
        - Common Stock|Q|G|N|100|N|N||FLGT|N\r\nY|FLGV|Franklin U.S. Treasury Bond
        ETF|P| |Y|100|N||FLGV|FLGV|N\r\nY|FLHK|Franklin FTSE Hong Kong ETF|P| |Y|100|N||FLHK|FLHK|N\r\nY|FLHY|Franklin
        High Yield Corporate ETF|Z| |Y|100|N||FLHY|FLHY|N\r\nY|FLIA|Franklin International
        Aggregate Bond ETF|Z| |Y|100|N||FLIA|FLIA|N\r\nY|FLIC|The First of Long Island
        Corporation - Common Stock|Q|S|N|100|N|N||FLIC|N\r\nY|FLIN|Franklin FTSE India
        ETF|P| |Y|100|N||FLIN|FLIN|N\r\nY|FLJH|Franklin FTSE Japan Hedged ETF|P| |Y|100|N||FLJH|FLJH|N\r\nY|FLJJ|AIM
        ETF Products Trust AllianzIM U.S. Equity 6 Month Floor5 Jan/Jul ETF|P| |Y|100|N||FLJJ|FLJJ|N\r\nY|FLJP|Franklin
        FTSE Japan ETF|P| |Y|100|N||FLJP|FLJP|N\r\nY|FLKR|Franklin FTSE South Korea
        ETF|P| |Y|100|N||FLKR|FLKR|N\r\nY|FLL|Full House Resorts, Inc. - Common Stock|Q|S|N|100|N|N||FLL|N\r\nY|FLLA|Franklin
        FTSE Latin America ETF|P| |Y|100|N||FLLA|FLLA|N\r\nY|FLMB|Franklin Municipal
        Green Bond ETF|P| |Y|100|N||FLMB|FLMB|N\r\nY|FLMI|Franklin Dynamic Municipal
        Bond ETF|P| |Y|100|N||FLMI|FLMI|N\r\nY|FLMX|Franklin FTSE Mexico ETF|P| |Y|100|N||FLMX|FLMX|N\r\nY|FLN|First
        Trust Latin America AlphaDEX Fund|Q|G|Y|100|N|N||FLN|N\r\nY|FLNC|Fluence Energy,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||FLNC|N\r\nY|FLNG|FLEX LNG Ltd.
        Ordinary Shares|N| |N|100|N||FLNG|FLNG|N\r\nY|FLNT|Fluent, Inc. - Common Stock|Q|S|N|100|N|N||FLNT|N\r\nY|FLO|Flowers
        Foods, Inc. Common Stock|N| |N|100|N||FLO|FLO|N\r\nY|FLOT|iShares Floating
        Rate Bond ETF|Z| |Y|100|N||FLOT|FLOT|N\r\nY|FLOW|Global X Funds Global X U.S.
        Cash Flow Kings 100 ETF|P| |Y|100|N||FLOW|FLOW|N\r\nY|FLQL|Franklin U.S. Large
        Cap Multifactor Index ETF|Z| |Y|100|N||FLQL|FLQL|N\r\nY|FLQM|Franklin U.S.
        Mid Cap Multifactor Index ETF|Z| |Y|100|N||FLQM|FLQM|N\r\nY|FLQS|Franklin
        U.S. Small Cap Multifactor Index ETF|Z| |Y|100|N||FLQS|FLQS|N\r\nY|FLR|Fluor
        Corporation Common Stock|N| |N|100|N||FLR|FLR|N\r\nY|FLRG|Fidelity U.S. Multifactor
        ETF|P| |Y|100|N||FLRG|FLRG|N\r\nY|FLRN|SPDR Bloomberg Investment Grade Floating
        Rate ETF|P| |Y|100|N||FLRN|FLRN|N\r\nY|FLRT|Pacer Funds Pacer Pacific Asset
        Floating Rate High Income ETF|P| |Y|100|N||FLRT|FLRT|N\r\nY|FLS|Flowserve
        Corporation Common Stock|N| |N|100|N||FLS|FLS|N\r\nY|FLSA|Franklin FTSE Saudi
        Arabia ETF|P| |Y|100|N||FLSA|FLSA|N\r\nY|FLSP|Franklin Systematic Style Premia
        ETF|P| |Y|100|N||FLSP|FLSP|N\r\nY|FLSW|Franklin FTSE Switzerland ETF|P| |Y|100|N||FLSW|FLSW|N\r\nY|FLTB|Fidelity
        Limited Term Bond ETF|P| |Y|100|N||FLTB|FLTB|N\r\nY|FLTR|VanEck ETF Trust
        VanEck IG Floating Rate ETF|P| |Y|100|N||FLTR|FLTR|N\r\nY|FLTW|Franklin FTSE
        Taiwan ETF|P| |Y|100|N||FLTW|FLTW|N\r\nY|FLUD|Franklin Ultra Short Bond ETF|P|
        |Y|100|N||FLUD|FLUD|N\r\nY|FLUT|Flutter Entertainment plc Ordinary Shares|N|
        |N|100|N||FLUT|FLUT|N\r\nY|FLUX|Flux Power Holdings, Inc. - Common Stock|Q|S|N|100|N|N||FLUX|N\r\nY|FLV|American
        Century Focused Large Cap Value ETF|P| |Y|100|N||FLV|FLV|N\r\nY|FLWS|1-800-FLOWERS.COM,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||FLWS|N\r\nY|FLXR|Engine No. 1 ETF
        Trust TCW Flexible Income ETF|N| |Y|100|N||FLXR|FLXR|N\r\nY|FLXS|Flexsteel
        Industries, Inc. - Common Stock|Q|Q|N|100|N|N||FLXS|N\r\nY|FLYD|Bank of Montreal
        MicroSectors Travel -3x Inverse Leveraged ETN|P| |Y|100|N||FLYD|FLYD|N\r\nY|FLYE|Fly-E
        Group, Inc. - Common Stock|Q|S|N|100|N|N||FLYE|N\r\nY|FLYU|Bank of Montreal
        MicroSectors Travel 3x Leveraged ETN|P| |Y|100|N||FLYU|FLYU|N\r\nY|FLYW|Flywire
        Corporation - Voting Common Stock|Q|Q|N|100|N|N||FLYW|N\r\nY|FLYX|flyExclusive,
        Inc. Class A Common Stock|A| |N|100|N||FLYX|FLYX|N\r\nY|FLYX.W|flyExclusive,
        Inc. Redeemable warrants, each whole warrant exercisable for one Class A common
        stock at an exercise price of $11.50 per share|A| |N|100|N||FLYX.WS|FLYX+|N\r\nY|FM|iShares
        Frontier and Select EM ETF|P| |Y|100|N||FM|FM|N\r\nY|FMAG|Fidelity Magellan
        ETF|Z| |Y|100|N||FMAG|FMAG|N\r\nY|FMAO|Farmers & Merchants Bancorp, Inc. -
        Common Stock|Q|S|N|100|N|N||FMAO|N\r\nY|FMAR|FT Vest U.S. Equity Buffer ETF
        - March|Z| |Y|100|N||FMAR|FMAR|N\r\nY|FMAT|Fidelity MSCI Materials Index ETF|P|
        |Y|100|N||FMAT|FMAT|N\r\nY|FMAY|FT Vest U.S. Equity Buffer ETF - May|Z| |Y|100|N||FMAY|FMAY|N\r\nY|FMB|First
        Trust Managed Municipal ETF|Q|G|Y|100|N|N||FMB|N\r\nY|FMBH|First Mid Bancshares,
        Inc. - Common Stock|Q|G|N|100|N|N||FMBH|N\r\nY|FMC|FMC Corporation Common
        Stock|N| |N|100|N||FMC|FMC|N\r\nY|FMCX|Northern Lights Fund Trust IV FMC Excelsior
        Focus Equity ETF|P| |Y|100|N||FMCX|FMCX|N\r\nY|FMDE|Fidelity Covington Trust
        Fidelity Enhanced Mid Cap ETF|P| |Y|100|N||FMDE|FMDE|N\r\nY|FMED|Fidelity
        Disruptive Medicine ETF|Q|G|Y|100|N|N||FMED|N\r\nY|FMET|Fidelity Metaverse
        ETF|Q|G|Y|100|N|N||FMET|N\r\nY|FMF|First Trust Managed Futures Strategy Fund|P|
        |Y|100|N||FMF|FMF|N\r\nY|FMHI|First Trust Municipal High Income ETF|Q|G|Y|100|N|N||FMHI|N\r\nY|FMN|Federated
        Hermes Premier Municipal Income Fund|N| |N|100|N||FMN|FMN|N\r\nY|FMNB|Farmers
        National Banc Corp. - Common Stock|Q|S|N|100|N|N||FMNB|N\r\nY|FMNY|First Trust
        New York Municipal High Income ETF|P| |Y|100|N||FMNY|FMNY|N\r\nY|FMQQ|FMQQ
        The Next Frontier Internet & Ecommerce ETF|P| |Y|100|N||FMQQ|FMQQ|N\r\nY|FMS|Fresenius
        Medical Care AG American Depositary Shares (Each representing 1/2 of an Ordinary
        Share)|N| |N|100|N||FMS|FMS|N\r\nY|FMST|Foremost Lithium Resource & Technology
        Ltd. - Common stock|Q|S|N|100|N|N||FMST|N\r\nY|FMSTW|Foremost Lithium Resource
        & Technology Ltd. - Warrant|Q|S|N|100|N|N||FMSTW|N\r\nY|FMX|Fomento Economico
        Mexicano S.A.B. de C.V. Common Stock|N| |N|100|N||FMX|FMX|N\r\nY|FMY|First
        Trust Motgage Income Fund Common Shares of Beneficial Interest|N| |N|100|N||FMY|FMY|N\r\nY|FN|Fabrinet
        Ordinary Shares|N| |N|100|N||FN|FN|N\r\nY|FNA|Paragon 28, Inc. Common Stock|N|
        |N|100|N||FNA|FNA|N\r\nY|FNB|F.N.B. Corporation Common Stock|N| |N|100|N||FNB|FNB|N\r\nY|FNCB|FNCB
        Bancorp Inc. - Common Stock|Q|S|N|100|N|N||FNCB|N\r\nY|FNCL|Fidelity MSCI
        Financials Index ETF|P| |Y|100|N||FNCL|FNCL|N\r\nY|FND|Floor & Decor Holdings,
        Inc. Common Stock|N| |N|100|N||FND|FND|N\r\nY|FNDA|Schwab Fundamental U.S.
        Small Company ETF|P| |Y|100|N||FNDA|FNDA|N\r\nY|FNDB|Schwab Fundamental U.S.
        Broad Market ETF|P| |Y|100|N||FNDB|FNDB|N\r\nY|FNDC|Schwab Fundamental International
        Small Equity ETF|P| |Y|100|N||FNDC|FNDC|N\r\nY|FNDE|Schwab Fundamental Emerging
        Markets Equity ETF|P| |Y|100|N||FNDE|FNDE|N\r\nY|FNDF|Schwab Fundamental International
        Equity ETF|P| |Y|100|N||FNDF|FNDF|N\r\nY|FNDX|Schwab Fundamental U.S. Large
        Company ETF|P| |Y|100|N||FNDX|FNDX|N\r\nY|FNF|FNF Group of Fidelity National
        Financial, Inc. Common Stock|N| |N|100|N||FNF|FNF|N\r\nY|FNGD|MicroSectors
        FANG  Index -3X Inverse Leveraged ETNs due January 8, 2038|P| |N|100|N||FNGD|FNGD|N\r\nY|FNGG|Direxion
        Daily NYSE FANG+ Bull 2X Shares|P| |Y|100|N||FNGG|FNGG|N\r\nY|FNGO|MicroSectors
        FANG  Index 2X Leveraged ETNs due January 8, 2038|P| |N|100|N||FNGO|FNGO|N\r\nY|FNGR|FingerMotion,
        Inc. - common stock|Q|S|N|100|N|N||FNGR|N\r\nY|FNGS|MicroSectors FANG  ETNs
        due January 8, 2038|P| |Y|100|N||FNGS|FNGS|N\r\nY|FNGU|MicroSectors FANG  Index
        3X Leveraged ETNs due January 8, 2038|P| |N|100|N||FNGU|FNGU|N\r\nY|FNK|First
        Trust Mid Cap Value AlphaDEX Fund|Q|G|Y|100|N|N||FNK|N\r\nY|FNKO|Funko, Inc.
        - Class A Common Stock|Q|Q|N|100|N|N||FNKO|N\r\nY|FNLC|First Bancorp, Inc
        (ME) - Common Stock|Q|Q|N|100|N|N||FNLC|N\r\nY|FNOV|FT Vest U.S. Equity Buffer
        ETF - November|Z| |Y|100|N||FNOV|FNOV|N\r\nY|FNV|Franco-Nevada Corporation|N|
        |N|100|N||FNV|FNV|N\r\nY|FNVT|Finnovate Acquisition Corp. - Class A Ordinary
        Shares|Q|G|N|100|N|D||FNVT|N\r\nY|FNVTU|Finnovate Acquisition Corp. - Units|Q|G|N|100|N|N||FNVTU|N\r\nY|FNVTW|Finnovate
        Acquisition Corp. - Warrants|Q|G|N|100|N|N||FNVTW|N\r\nY|FNWB|First Northwest
        Bancorp - Common Stock|Q|G|N|100|N|N||FNWB|N\r\nY|FNWD|Finward Bancorp - common
        stock|Q|S|N|100|N|N||FNWD|N\r\nY|FNX|First Trust Mid Cap Core AlphaDEX Fund|Q|G|Y|100|N|N||FNX|N\r\nY|FNY|First
        Trust Mid Cap Growth AlphaDEX Fund|Q|G|Y|100|N|N||FNY|N\r\nY|FOA|Finance of
        America Companies Inc. Class A Common Stock|N| |N|100|N||FOA|FOA|N\r\nY|FOA.W|Finance
        of America Companies Inc. Warrants, each whole warrant exercisable for one
        Class A Common Stock at an exercise price of $11.50|N| |N|100|N||FOA.WS|FOA+|N\r\nY|FOCT|FT
        Vest U.S. Equity Buffer ETF - October|Z| |Y|100|N||FOCT|FOCT|N\r\nY|FOF|Cohen
        & Steers Closed-End Opportunity Fund, Inc. Common Stock|N| |N|100|N||FOF|FOF|N\r\nY|FOLD|Amicus
        Therapeutics, Inc. - Common Stock|Q|G|N|100|N|N||FOLD|N\r\nY|FONR|Fonar Corporation
        - Common Stock|Q|S|N|100|N|N||FONR|N\r\nY|FOR|Forestar Group Inc Common Stock
        |N| |N|100|N||FOR|FOR|N\r\nY|FORA|Forian Inc. - Common Stock|Q|S|N|100|N|N||FORA|N\r\nY|FORD|Forward
        Industries, Inc. - Common Stock|Q|S|N|100|N|D||FORD|N\r\nY|FORH|Formidable
        ETF|P| |Y|100|N||FORH|FORH|N\r\nY|FORL|Four Leaf Acquisition Corporation -
        Class A Common Stock|Q|S|N|100|N|N||FORL|N\r\nY|FORLU|Four Leaf Acquisition
        Corporation - Unit|Q|S|N|100|N|N||FORLU|N\r\nY|FORLW|Four Leaf Acquisition
        Corporation - Warrants|Q|S|N|100|N|N||FORLW|N\r\nY|FORM|FormFactor, Inc. -
        Common Stock|Q|Q|N|100|N|N||FORM|N\r\nY|FORR|Forrester Research, Inc. - Common
        Stock|Q|Q|N|100|N|N||FORR|N\r\nY|FORTY|Formula Systems (1985) Ltd. - American
        Depositary Shares|Q|Q|N|100|N|N||FORTY|N\r\nY|FOSL|Fossil Group, Inc. - Common
        Stock|Q|Q|N|100|N|N||FOSL|N\r\nY|FOSLL|Fossil Group, Inc. - 7% Senior Notes
        due 2026|Q|Q|N|100|N|N||FOSLL|N\r\nY|FOUR|Shift4 Payments, Inc. Class A Common
        Stock|N| |N|100|N||FOUR|FOUR|N\r\nY|FOVL|iShares Focused Value Factor ETF|P|
        |Y|100|N||FOVL|FOVL|N\r\nY|FOX|Fox Corporation - Class B Common Stock|Q|Q|N|100|N|N||FOX|N\r\nY|FOXA|Fox
        Corporation - Class A Common Stock|Q|Q|N|100|N|N||FOXA|N\r\nY|FOXF|Fox Factory
        Holding Corp. - Common Stock|Q|Q|N|100|N|N||FOXF|N\r\nY|FOXO|FOXO Technologies
        Inc. Class A Common Stock|A| |N|100|N||FOXO|FOXO|N\r\nY|FPA|First Trust Asia
        Pacific Ex-Japan AlphaDEX Fund|Q|G|Y|100|N|N||FPA|N\r\nY|FPAG|Investment Managers
        Series Trust III FPA Global Equity ETF|Z| |Y|100|N||FPAG|FPAG|N\r\nY|FPAY|FlexShopper,
        Inc. - Common Stock|Q|S|N|100|N|N||FPAY|N\r\nY|FPE|First Trust Preferred Securities
        and Income ETF ETF|P| |Y|100|N||FPE|FPE|N\r\nY|FPEI|First Trust Institutional
        Preferred Securities and Income ETF|P| |Y|100|N||FPEI|FPEI|N\r\nY|FPF|First
        Trust Intermediate Duration Preferred & Income Fund Common Shares of Beneficial
        Interest|N| |N|100|N||FPF|FPF|N\r\nY|FPFD|Fidelity Preferred Securities &
        Income ETF|Z| |Y|100|N||FPFD|FPFD|N\r\nY|FPH|Five Point Holdings, LLC Class
        A Common Shares|N| |N|100|N||FPH|FPH|N\r\nY|FPI|Farmland Partners Inc. Common
        Stock|N| |N|100|N||FPI|FPI|N\r\nY|FPRO|Fidelity Real Estate Investment ETF|Z|
        |Y|100|N||FPRO|FPRO|N\r\nY|FPX|First Trust US Equity Opportunities ETF|P|
        |Y|100|N||FPX|FPX|N\r\nY|FPXE|First Trust IPOX Europe Equity Opportunities
        ETF|Q|G|Y|100|N|N||FPXE|N\r\nY|FPXI|First Trust International Equity Opportunities
        ETF|Q|G|Y|100|N|N||FPXI|N\r\nY|FQAL|Fidelity Quality Factor ETF|P| |Y|100|N||FQAL|FQAL|N\r\nY|FR|First
        Industrial Realty Trust, Inc. Common Stock|N| |N|100|N||FR|FR|N\r\nY|FRA|Blackrock
        Floating Rate Income Strategies Fund Inc  Common Stock|N| |N|100|N||FRA|FRA|N\r\nY|FRAF|Franklin
        Financial Services Corporation - Common Stock|Q|S|N|100|N|N||FRAF|N\r\nY|FRBA|First
        Bank  - Common Stock|Q|G|N|100|N|N||FRBA|N\r\nY|FRD|Friedman Industries Inc.
        Common Stock|A| |N|100|N||FRD|FRD|N\r\nY|FRDM|Freedom 100 Emerging Markets
        ETF|Z| |Y|100|N||FRDM|FRDM|N\r\nY|FREE|Whole Earth Brands, Inc. - Class A
        Common Stock|Q|S|N|100|N|N||FREE|N\r\nY|FREEW|Whole Earth Brands, Inc. - Warrant|Q|S|N|100|N|N||FREEW|N\r\nY|FREL|Fidelity
        MSCI Real Estate Index ETF|P| |Y|100|N||FREL|FREL|N\r\nY|FRES|Fresh2 Group
        Limited - American Depositary Shares|Q|S|N|100|N|H||FRES|N\r\nY|FREY|FREYR
        Battery, Inc. Common Stock|N| |N|100|N||FREY|FREY|N\r\nY|FREY.W|FREYR Battery
        Warrants each whole warrant exercisable to purchase one Common Stock at an
        exercise price of $11.50 per share|N| |N|100|N||FREY.WS|FREY+|N\r\nY|FRGE|Forge
        Global Holdings, Inc. Common Stock|N| |N|100|N||FRGE|FRGE|N\r\nY|FRGT|Freight
        Technologies, Inc. - Ordinary Shares|Q|S|N|100|N|D||FRGT|N\r\nY|FRHC|Freedom
        Holding Corp. - Common Stock|Q|S|N|100|N|N||FRHC|N\r\nY|FRI|First Trust S&P
        REIT Index Fund|P| |Y|100|N||FRI|FRI|N\r\nY|FRLA|Fortune Rise Acquisition
        Corporation - Class A Common Stock|Q|S|N|100|N|D||FRLA|N\r\nY|FRLAU|Fortune
        Rise Acquisition Corporation - Units|Q|S|N|100|N|D||FRLAU|N\r\nY|FRLAW|Fortune
        Rise Acquisition Corporation - Warrant|Q|S|N|100|N|D||FRLAW|N\r\nY|FRME|First
        Merchants Corporation - Common Stock|Q|Q|N|100|N|N||FRME|N\r\nY|FRMEP|First
        Merchants Corporation - Depository Shares, each representing a 1/100th interest
        in a share of 7.50% Non-Cumulative Perpetual Preferred Stock, A|Q|Q|N|100|N|N||FRMEP|N\r\nY|FRNW|Fidelity
        Clean Energy ETF|Z| |Y|100|N||FRNW|FRNW|N\r\nY|FRO|Frontline Plc Ordinary
        Shares|N| |N|100|N||FRO|FRO|N\r\nY|FROG|JFrog Ltd. - Ordinary shares|Q|Q|N|100|N|N||FROG|N\r\nY|FRPH|FRP
        Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||FRPH|N\r\nY|FRPT|Freshpet, Inc.
        - Common Stock|Q|G|N|100|N|N||FRPT|N\r\nY|FRSH|Freshworks Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||FRSH|N\r\nY|FRST|Primis Financial Corp. - Common Stock|Q|G|N|100|N|E||FRST|N\r\nY|FRSX|Foresight
        Autonomous Holdings Ltd. - American Depositary Shares|Q|S|N|100|N|N||FRSX|N\r\nY|FRT|Federal
        Realty Investment Trust Common Stock|N| |N|100|N||FRT|FRT|N\r\nY|FRT$C|Federal
        Realty Investment Trust Depositary Shares, each representing a 1/1000th interest
        in a 5.000% Series C Cumulative Redeemable Preferred Share|N| |N|100|N||FRTpC|FRT-C|N\r\nY|FRTY|Alger
        Mid Cap 40 ETF|P| |Y|100|N||FRTY|FRTY|N\r\nY|FRZA|Forza X1, Inc. - Common
        Stock|Q|S|N|100|N|D||FRZA|N\r\nY|FSBC|Five Star Bancorp - Common Stock|Q|Q|N|100|N|N||FSBC|N\r\nY|FSBD|Fidelity
        Merrimack Street Trust Fidelity Sustainable Core Plus Bond ETF|P| |Y|100|N||FSBD|FSBD|N\r\nY|FSBW|FS
        Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||FSBW|N\r\nY|FSCO|FS Credit Opportunities
        Corp. Common Stock|N| |N|100|N||FSCO|FSCO|N\r\nY|FSCS|First Trust SMID Capital
        Strength ETF|Q|G|Y|100|N|N||FSCS|N\r\nY|FSD|First Trust High Income Long Short
        Fund Common Shares of Beneficial Interest|N| |N|100|N||FSD|FSD|N\r\nY|FSEA|First
        Seacoast Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||FSEA|N\r\nY|FSEC|Fidelity
        Investment Grade Securitized ETF|P| |Y|100|N||FSEC|FSEC|N\r\nY|FSEP|FT Vest
        U.S. Equity Buffer ETF - September|Z| |Y|100|N||FSEP|FSEP|N\r\nY|FSFG|First
        Savings Financial Group, Inc. - Common Stock|Q|S|N|100|N|N||FSFG|N\r\nY|FSHPU|Flag
        Ship Acquisition Corp. - Unit|Q|G|N|100|N|N||FSHPU|N\r\nY|FSI|Flexible Solutions
        International Inc. Common Stock (CDA)|A| |N|100|N||FSI|FSI|N\r\nY|FSIG|First
        Trust Limited Duration Investment Grade Corporate ETF|P| |Y|100|N||FSIG|FSIG|N\r\nY|FSK|FS
        KKR Capital Corp. Common Stock|N| |N|100|N||FSK|FSK|N\r\nY|FSLD|Fidelity Merrimack
        Street Trust Fidelity Sustainable Low Duration Bond ETF|P| |Y|100|N||FSLD|FSLD|N\r\nY|FSLR|First
        Solar, Inc. - Common Stock|Q|Q|N|100|N|N||FSLR|N\r\nY|FSLY|Fastly, Inc. Class
        A Common Stock|N| |N|100|N||FSLY|FSLY|N\r\nY|FSM|Fortuna Mining Corp. Common
        Shares|N| |N|100|N||FSM|FSM|N\r\nY|FSMB|First Trust Short Duration Managed
        Municipal ETF|P| |Y|100|N||FSMB|FSMB|N\r\nY|FSMD|Fidelity Small-Mid Multifactor
        ETF|P| |Y|100|N||FSMD|FSMD|N\r\nY|FSP|Franklin Street Properties Corp. Common
        Stock|A| |N|100|N||FSP|FSP|N\r\nY|FSS|Federal Signal Corporation Common Stock|N|
        |N|100|N||FSS|FSS|N\r\nY|FSST|Fidelity Sustainable U.S. Equity ETF|P| |Y|100|N||FSST|FSST|N\r\nY|FSTA|Fidelity
        MSCI COnsumer Staples Index ETF|P| |Y|100|N||FSTA|FSTA|N\r\nY|FSTR|L.B. Foster
        Company - Common Stock|Q|Q|N|100|N|N||FSTR|N\r\nY|FSV|FirstService Corporation
        - Common Shares|Q|Q|N|100|N|N||FSV|N\r\nY|FSYD|Fidelity Covington Trust Fidelity
        Sustainable High Yield ETF|P| |Y|100|N||FSYD|FSYD|N\r\nY|FSZ|First Trust Switzerland
        AlphaDEX Fund|Q|G|Y|100|N|N||FSZ|N\r\nY|FT|Franklin Universal Trust Common
        Stock|N| |N|100|N||FT|FT|N\r\nY|FTA|First Trust Large Cap Value AlphaDEX Fund|Q|G|Y|100|N|N||FTA|N\r\nY|FTAG|First
        Trust Indxx Global Agriculture ETF|Q|G|Y|100|N|N||FTAG|N\r\nY|FTAI|FTAI Aviation
        Ltd. - Common Stock|Q|Q|N|100|N|N||FTAI|N\r\nY|FTAIM|FTAI Aviation Ltd. -
        9.500% Fixed-Rate Reset Series D Cumulative Perpetual Redeemable Preferred
        Shares|Q|Q|N|100|N|N||FTAIM|N\r\nY|FTAIN|FTAI Aviation Ltd. - 8.25% Fixed-Rate
        Reset Series C Cumulative Perpetual Redeemable Preferred Shares|Q|Q|N|100|N|N||FTAIN|N\r\nY|FTAIO|FTAI
        Aviation Ltd. - 8.00% Fixed-to-Floating Rate Series B Cumulative Perpetual
        Redeemable Preferred Shares|Q|Q|N|100|N|N||FTAIO|N\r\nY|FTAIP|FTAI Aviation
        Ltd. - 8.25% Fixed-to-Floating Rate Series A Cumulative Perpetual Redeemable
        Preferred Shares|Q|Q|N|100|N|N||FTAIP|N\r\nY|FTBD|Fidelity Merrimack Street
        Trust Fidelity Tactical Bond ETF|P| |Y|100|N||FTBD|FTBD|N\r\nY|FTC|First Trust
        Large Cap Growth AlphaDEX Fund|Q|G|Y|100|N|N||FTC|N\r\nY|FTCB|First Trust
        Exchange-Traded Fund IV First Trust Core Investment Grade ETF|P| |Y|100|N||FTCB|FTCB|N\r\nY|FTCI|FTC
        Solar, Inc. - Common Stock|Q|S|N|100|N|D||FTCI|N\r\nY|FTCS|First Trust Capital
        Strength ETF|Q|G|Y|100|N|N||FTCS|N\r\nY|FTDR|Frontdoor, Inc. - Common Stock|Q|Q|N|100|N|N||FTDR|N\r\nY|FTDS|First
        Trust Dividend Strength ETF|Q|G|Y|100|N|N||FTDS|N\r\nY|FTEC|Fidelity MSCI
        Information Technology Index ETF|P| |Y|100|N||FTEC|FTEC|N\r\nY|FTEK|Fuel Tech,
        Inc. - Common Stock|Q|S|N|100|N|N||FTEK|N\r\nY|FTEL|Fitell Corporation - Ordinary
        Shares|Q|S|N|100|N|N||FTEL|N\r\nY|FTF|Franklin Limited Duration Income Trust
        Common Shares of Beneficial Interest|A| |N|100|N||FTF|FTF|N\r\nY|FTFT|Future
        FinTech Group Inc. - Common Stock|Q|S|N|100|N|D||FTFT|N\r\nY|FTGC|First Trust
        Global Tactical Commodity Strategy Fund|Q|G|Y|100|N|N||FTGC|N\r\nY|FTGS|First
        Trust Growth Strength ETF|Q|G|Y|100|N|N||FTGS|N\r\nY|FTHF|First Trust Exchange-Traded
        Fund II First Trust Emerging Markets Human Flourishing ETF|P| |Y|100|N||FTHF|FTHF|N\r\nY|FTHI|First
        Trust BuyWrite Income ETF|Q|G|Y|100|N|N||FTHI|N\r\nY|FTHM|Fathom Holdings
        Inc. - Common Stock|Q|S|N|100|N|N||FTHM|N\r\nY|FTHY|First Trust High Yield
        Opportunities 2027 Term Fund Common Stock|N| |N|100|N||FTHY|FTHY|N\r\nY|FTI|TechnipFMC
        plc Ordinary Share|N| |N|100|N||FTI|FTI|N\r\nY|FTIF|First Trust Exchange-Traded
        Fund First Trust Bloomberg Inflation Sensitive Equity ETF|P| |Y|100|N||FTIF|FTIF|N\r\nY|FTII|FutureTech
        II Acquisition Corp. - Class A Common Stock|Q|G|N|100|N|D||FTII|N\r\nY|FTIIU|FutureTech
        II Acquisition Corp. - Unit|Q|G|N|100|N|D||FTIIU|N\r\nY|FTIIW|FutureTech II
        Acquisition Corp. - Warrant|Q|G|N|100|N|D||FTIIW|N\r\nY|FTK|Flotek Industries,
        Inc. Common Stock|N| |N|100|N||FTK|FTK|N\r\nY|FTLF|FitLife Brands, Inc. -
        Common Stock|Q|S|N|100|N|N||FTLF|N\r\nY|FTLS|First Trust Long/Short Equity|P|
        |Y|100|N||FTLS|FTLS|N\r\nY|FTNT|Fortinet, Inc. - Common Stock|Q|Q|N|100|N|N||FTNT|N\r\nY|FTQI|First
        Trust Nasdaq BuyWrite Income ETF|Q|G|Y|100|N|N||FTQI|N\r\nY|FTRB|Federated
        Hermes ETF Trust Federated Hermes Total Return Bond ETF|P| |Y|100|N||FTRB|FTRB|N\r\nY|FTRE|Fortrea
        Holdings Inc. - Common Stock|Q|Q|N|100|N|N||FTRE|N\r\nY|FTRI|First Trust Indxx
        Global Natural Resources Income ETF|Q|G|Y|100|N|N||FTRI|N\r\nY|FTS|Fortis
        Inc. Common Shares|N| |N|100|N||FTS|FTS|N\r\nY|FTSD|Franklin Short Duration
        U.S. Government ETF|P| |Y|100|N||FTSD|FTSD|N\r\nY|FTSL|First Trust Senior
        Loan Fund|Q|G|Y|100|N|N||FTSL|N\r\nY|FTSM|First Trust Enhanced Short Maturity
        ETF|Q|G|Y|100|N|N||FTSM|N\r\nY|FTV|Fortive Corporation Common Stock |N| |N|100|N||FTV|FTV|N\r\nY|FTWO|EA
        Series Trust Strive FAANG 2.0 ETF|N| |Y|100|N||FTWO|FTWO|N\r\nY|FTXG|First
        Trust Nasdaq Food & Beverage ETF|Q|G|Y|100|N|N||FTXG|N\r\nY|FTXH|First Trust
        Nasdaq Pharmaceuticals ETF|Q|G|Y|100|N|N||FTXH|N\r\nY|FTXL|First Trust Nasdaq
        Semiconductor ETF|Q|G|Y|100|N|N||FTXL|N\r\nY|FTXN|First Trust Nasdaq Oil &
        Gas ETF|Q|G|Y|100|N|N||FTXN|N\r\nY|FTXO|First Trust Nasdaq Bank ETF|Q|G|Y|100|N|N||FTXO|N\r\nY|FTXR|First
        Trust Nasdaq Transportation ETF|Q|G|Y|100|N|N||FTXR|N\r\nY|FUBO|fuboTV Inc.
        Common Stock|N| |N|100|N||FUBO|FUBO|N\r\nY|FUFU|BitFuFu Inc. - Class A Ordinary
        Shares|Q|S|N|100|N|N||FUFU|N\r\nY|FUFUW|BitFuFu Inc. - Warrant|Q|S|N|100|N|N||FUFUW|N\r\nY|FUL|H.
        B. Fuller Company Common Stock|N| |N|100|N||FUL|FUL|N\r\nY|FULC|Fulcrum Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||FULC|N\r\nY|FULT|Fulton Financial Corporation
        - Common Stock|Q|Q|N|100|N|N||FULT|N\r\nY|FULTP|Fulton Financial Corporation
        - Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed
        Rate Non-Cumulative Perpetual Preferred Stock, Series A|Q|Q|N|100|N|N||FULTP|N\r\nY|FUMB|First
        Trust Ultra Short Duration Municipal ETF|P| |Y|100|N||FUMB|FUMB|N\r\nY|FUN|Cedar
        Fair, L.P. Common Stock|N| |N|100|N||FUN|FUN|N\r\nY|FUNC|First United Corporation
        - Common Stock|Q|Q|N|100|N|N||FUNC|N\r\nY|FUND|Sprott Focus Trust, Inc. -
        Closed End Fund|Q|Q|N|100|N|N||FUND|N\r\nY|FUNL|CornerCap Fundametrics Large-Cap
        ETF|Z| |Y|100|N||FUNL|FUNL|N\r\nY|FURY|Fury Gold Mines Limited Common Shares|A|
        |N|100|N||FURY|FURY|N\r\nY|FUSB|First US Bancshares, Inc. - Common Stock|Q|S|N|100|N|N||FUSB|N\r\nY|FUSI|American
        Century ETF Trust American Century Multisector Floating Income ETF|P| |Y|100|N||FUSI|FUSI|N\r\nY|FUTU|Futu
        Holdings Limited - American Depositary Shares|Q|G|N|100|N|N||FUTU|N\r\nY|FUTY|Fidelity
        MSCI Utilities Index ETF|P| |Y|100|N||FUTY|FUTY|N\r\nY|FV|First Trust Dorsey
        Wright Focus 5 ETF|Q|G|Y|100|N|N||FV|N\r\nY|FVAL|Fidelity Value Factor ETF|P|
        |Y|100|N||FVAL|FVAL|N\r\nY|FVC|First Trust Dorsey Wright Dynamic Focus 5 ETF|Q|G|Y|100|N|N||FVC|N\r\nY|FVCB|FVCBankcorp,
        Inc. - Common Stock|Q|S|N|100|N|N||FVCB|N\r\nY|FVD|First Trust VL Dividend|P|
        |Y|100|N||FVD|FVD|N\r\nY|FVRR|Fiverr International Ltd. Ordinary Shares, no
        par value|N| |N|100|N||FVRR|FVRR|N\r\nY|FWD|AB Active ETFs, Inc. AB Disruptors
        ETF|P| |Y|100|N||FWD|FWD|N\r\nY|FWONA|Liberty Media Corporation - Series A
        Liberty Formula One Common Stock|Q|Q|N|100|N|N||FWONA|N\r\nY|FWONK|Liberty
        Media Corporation - Series C Liberty Formula One Common Stock|Q|Q|N|100|N|N||FWONK|N\r\nY|FWRD|Forward
        Air Corporation - Common Stock|Q|Q|N|100|N|N||FWRD|N\r\nY|FWRG|First Watch
        Restaurant Group, Inc. - Common Stock|Q|Q|N|100|N|N||FWRG|N\r\nY|FXA|Invesco
        CurrencyShares Australian Dollar Trust|P| |Y|100|N||FXA|FXA|N\r\nY|FXB|Invesco
        CurrencyShares British Pound Sterling Trust|P| |Y|100|N||FXB|FXB|N\r\nY|FXC|Invesco
        CurrencyShares Canadian Dollar Trust|P| |Y|100|N||FXC|FXC|N\r\nY|FXD|First
        Trust Cons. Discret. AlphaDEX|P| |Y|100|N||FXD|FXD|N\r\nY|FXE|Invesco CurrencyShares
        Euro Currency Trust|P| |Y|100|N||FXE|FXE|N\r\nY|FXED|Sound Enhanced Fixed
        Income ETF|N| |Y|100|N||FXED|FXED|N\r\nY|FXF|Invesco CurrencyShares Swiss
        Franc Trust|P| |Y|100|N||FXF|FXF|N\r\nY|FXG|First Trust Cons. Staples AlphaDEX|P|
        |Y|100|N||FXG|FXG|N\r\nY|FXH|First Trust Health Care AlphaDEX|P| |Y|100|N||FXH|FXH|N\r\nY|FXI|iShares
        China Large-Cap ETF|P| |Y|100|N||FXI|FXI|N\r\nY|FXL|First Trust Technology
        AlphaDEX|P| |Y|100|N||FXL|FXL|N\r\nY|FXN|First Trust Energy AlphaDEX Fund|P|
        |Y|100|N||FXN|FXN|N\r\nY|FXNC|First National Corporation - Common Stock|Q|S|N|100|N|N||FXNC|N\r\nY|FXO|First
        Trust Financials AlphaDEX|P| |Y|100|N||FXO|FXO|N\r\nY|FXP|ProShares Ultrashort
        FTSE China 50|P| |Y|100|N||FXP|FXP|N\r\nY|FXR|First Trust Industrials AlphaDEX|P|
        |Y|100|N||FXR|FXR|N\r\nY|FXU|First Trust Utilities AlphaDEX Fund|P| |Y|100|N||FXU|FXU|N\r\nY|FXY|Invesco
        CurrencyShares Japanese Yen Trust|P| |Y|100|N||FXY|FXY|N\r\nY|FXZ|First Trust
        Materials AlphaDEX Fund|P| |Y|100|N||FXZ|FXZ|N\r\nY|FYBR|Frontier Communications
        Parent, Inc. - Common Stock|Q|Q|N|100|N|N||FYBR|N\r\nY|FYC|First Trust Small
        Cap Growth AlphaDEX Fund|Q|G|Y|100|N|N||FYC|N\r\nY|FYEE|Fidelity Dynamic Buffered
        Equity ETF Fidelity Yield Enhanced Equity ETF|Z| |Y|100|N||FYEE|FYEE|N\r\nY|FYLD|Cambria
        Foreign Shareholder Yield ETF|Z| |Y|100|N||FYLD|FYLD|N\r\nY|FYLG|Global X
        Funds Global X Financials Covered Call & Growth ETF|P| |Y|100|N||FYLG|FYLG|N\r\nY|FYT|First
        Trust Small Cap Value AlphaDEX Fund|Q|G|Y|100|N|N||FYT|N\r\nY|FYX|First Trust
        Small Cap Core AlphaDEX Fund|Q|G|Y|100|N|N||FYX|N\r\nY|G|Genpact Limited Common
        Stock|N| |N|100|N||G|G|N\r\nY|GAA|Cambria Global Asset Allocation ETF|Z| |Y|100|N||GAA|GAA|N\r\nY|GAB|Gabelli
        Equity Trust, Inc. (The) Common Stock|N| |N|100|N||GAB|GAB|N\r\nY|GAB$G|Gabelli
        Equity Trust, Inc. (The) Series G Cumulative Preferred Stock|N| |N|100|N||GABpG|GAB-G|N\r\nY|GAB$H|Gabelli
        Equity Trust, Inc. (The) Pfd Ser H|N| |N|100|N||GABpH|GAB-H|N\r\nY|GAB$K|Gabelli
        Equity Trust, Inc. (The) 5.00% Series K Cumulative Preferred Stock|N| |N|100|N||GABpK|GAB-K|N\r\nY|GABC|German
        American Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||GABC|N\r\nY|GABF|Gabelli
        ETFs Trust Gabelli Financial Services Opportunities ETF|P| |Y|100|N||GABF|GABF|N\r\nY|GAIA|Gaia,
        Inc. - Class A Common Stock|Q|G|N|100|N|N||GAIA|N\r\nY|GAIN|Gladstone Investment
        Corporation - Business Development Company|Q|Q|N|100|N|N||GAIN|N\r\nY|GAINL|Gladstone
        Investment Corporation - 8.00% Notes due 2028|Q|Q|N|100|N|N||GAINL|N\r\nY|GAINN|Gladstone
        Investment Corporation - 5.00% Notes Due 2026|Q|Q|N|100|N|N||GAINN|N\r\nY|GAINZ|Gladstone
        Investment Corporation - 4.875% Notes due 2028|Q|Q|N|100|N|N||GAINZ|N\r\nY|GAL|SPDR
        SSgA Global Allocation ETF|P| |Y|100|N||GAL|GAL|N\r\nY|GALT|Galectin Therapeutics
        Inc. - Common Stock|Q|S|N|100|N|N||GALT|N\r\nY|GAM|General American Investors,
        Inc. Common Stock|N| |N|100|N||GAM|GAM|N\r\nY|GAM$B|General American Investors
        Company, Inc. Cumulative Preferred Stock|N| |N|100|N||GAMpB|GAM-B|N\r\nY|GAMB|Gambling.com
        Group Limited - Ordinary Shares|Q|G|N|100|N|N||GAMB|N\r\nY|GAMC|Golden Arrow
        Merger Corp. - Class A Common Stock|Q|S|N|100|N|D||GAMC|N\r\nY|GAMCU|Golden
        Arrow Merger Corp. - Unit|Q|S|N|100|N|D||GAMCU|N\r\nY|GAMCW|Golden Arrow Merger
        Corp. - Warrant|Q|S|N|100|N|D||GAMCW|N\r\nY|GAME|GameSquare Holdings, Inc.
        - Common stock|Q|S|N|100|N|N||GAME|N\r\nY|GAMR|Amplify ETF Trust Amplify Video
        Game Tech ETF|P| |Y|100|N||GAMR|GAMR|N\r\nY|GAN|GAN Limited - Ordinary Shares|Q|S|N|100|N|N||GAN|N\r\nY|GANX|Gain
        Therapeutics, Inc. - Common Stock|Q|G|N|100|N|N||GANX|N\r\nY|GAPR|FT Vest
        U.S. Equity Moderate Buffer ETF - April|Z| |Y|100|N||GAPR|GAPR|N\r\nY|GAQ|Generation
        Asia I Acquisition Limited - Class A Ordinary Shares|Q|G|N|100|N|N||GAQ|N\r\nY|GARP|iShares
        MSCI USA Quality GARP ETF|Z| |Y|100|N||GARP|GARP|N\r\nY|GASS|StealthGas, Inc.
        - common stock|Q|Q|N|100|N|N||GASS|N\r\nY|GAST|Gabelli Automation ETF|P| |Y|100|N||GAST|GAST|N\r\nY|GATE|Marblegate
        Acquisition Corp. - Class A Common Stock|Q|S|N|100|N|N||GATE|N\r\nY|GATEU|Marblegate
        Acquisition Corp. - Unit|Q|S|N|100|N|N||GATEU|N\r\nY|GATEW|Marblegate Acquisition
        Corp. - Warrant|Q|S|N|100|N|N||GATEW|N\r\nY|GATO|Gatos Silver, Inc. Common
        Stock|N| |N|100|N||GATO|GATO|N\r\nY|GATX|GATX Corporation Common Stock|N|
        |N|100|N||GATX|GATX|N\r\nY|GAU|Galiano Gold Inc.|A| |N|100|N||GAU|GAU|N\r\nY|GAUG|FT
        Vest U.S. Equity Moderate Buffer ETF - August|Z| |Y|100|N||GAUG|GAUG|N\r\nY|GAUZ|Gauzy
        Ltd. - Ordinary Shares|Q|G|N|100|N|N||GAUZ|N\r\nY|GB|Global Blue Group Holding
        AG Ordinary Shares|N| |N|100|N||GB|GB|N\r\nY|GB.W|Global Blue Group Holding
        AG Warrants exercisable for one Ordinary Share of Global Blue Group Holding
        AG at a price of $11.50 per share|N| |N|100|N||GB.WS|GB+|N\r\nY|GBAB|Guggenheim
        Taxable Municipal Bond & Investment Grade Debt Trust Common Shares of Beneficial
        Interest|N| |N|100|N||GBAB|GBAB|N\r\nY|GBBK|Global Blockchain Acquisition
        Corp. - Common Stock|Q|G|N|100|N|D||GBBK|N\r\nY|GBBKR|Global Blockchain Acquisition
        Corp. - Right|Q|G|N|100|N|N||GBBKR|N\r\nY|GBBKW|Global Blockchain Acquisition
        Corp. - Warrant|Q|G|N|100|N|N||GBBKW|N\r\nY|GBCI|Glacier Bancorp, Inc. Common
        Stock|N| |N|100|N||GBCI|GBCI|N\r\nY|GBDC|Golub Capital BDC, Inc. - Closed
        End Fund|Q|Q|N|100|N|N||GBDC|N\r\nY|GBF|iShares Government/Credit Bond ETF|P|
        |Y|100|N||GBF|GBF|N\r\nY|GBIL|Goldman Sachs Access Treasury 0-1 Year ETF|P|
        |Y|100|N||GBIL|GBIL|N\r\nY|GBIO|Generation Bio Co. - Common stock|Q|Q|N|100|N|N||GBIO|N\r\nY|GBLD|Invesco
        MSCI Green Building ETF|P| |Y|100|N||GBLD|GBLD|N\r\nY|GBLI|Global Indemnity
        Group, LLC Class A Common Stock (DE)|N| |N|100|N||GBLI|GBLI|N\r\nY|GBNY|Generations
        Bancorp NY, Inc. - Common Stock|Q|S|N|100|N|N||GBNY|N\r\nY|GBR|New Concept
        Energy, Inc Common Stock|A| |N|100|N||GBR|GBR|N\r\nY|GBTC|Grayscale Bitcoin
        Trust (BTC) Common Units of fractional undivided beneficial interest|P| |Y|100|N||GBTC|GBTC|N\r\nY|GBTG|Global
        Business Travel Group, Inc. Class A Common Stock|N| |N|100|N||GBTG|GBTG|N\r\nY|GBUY|Goldman
        Sachs Future Consumer Equity ETF|P| |Y|100|N||GBUY|GBUY|N\r\nY|GBX|Greenbrier
        Companies, Inc. (The) Common Stock|N| |N|100|N||GBX|GBX|N\r\nY|GCAD|Gabelli
        Commercial Aerospace and Defense ETF|P| |Y|100|N||GCAD|GCAD|N\r\nY|GCBC|Greene
        County Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||GCBC|N\r\nY|GCC|WisdomTree
        EnhancedContinuous Commodity Index Fund|P| |Y|100|N||GCC|GCC|N\r\nY|GCI|Gannett
        Co., Inc. Common Stock|N| |N|100|N||GCI|GCI|N\r\nY|GCLN|Goldman Sachs ETF
        Trust Goldman Sachs Bloomberg Clean Energy Equity ETF|Z| |Y|100|N||GCLN|GCLN|N\r\nY|GCMG|GCM
        Grosvenor Inc. - Class A Common Stock|Q|G|N|100|N|N||GCMG|N\r\nY|GCMGW|GCM
        Grosvenor Inc. - Warrant|Q|G|N|100|N|N||GCMGW|N\r\nY|GCO|Genesco Inc. Common
        Stock|N| |N|100|N||GCO|GCO|N\r\nY|GCOR|Goldman Sachs ETF Trust Goldman Sachs
        Access U.S. Aggregate Bond ETF|P| |Y|100|N||GCOR|GCOR|N\r\nY|GCOW|Pacer Global
        Cash Cows Dividend ETF|Z| |Y|100|N||GCOW|GCOW|N\r\nY|GCT|GigaCloud Technology
        Inc - Class A Ordinary Shares|Q|G|N|100|N|N||GCT|N\r\nY|GCTK|GlucoTrack, Inc.
        - Common Stock|Q|S|N|100|N|D||GCTK|N\r\nY|GCTS|GCT Semiconductor Holding,
        Inc. Common Stock|N| |N|100|N||GCTS|GCTS|N\r\nY|GCTS.W|GCT Semiconductor Holding,
        Inc. Warrants, each whole warrant exercisable for one share of Common Stock
        at an exercise price of $11.50|N| |N|100|N||GCTS.WS|GCTS+|N\r\nY|GCV|Gabelli
        Convertible and Income Securities Fund, Inc. (The) Common Stock|N| |N|100|N||GCV|GCV|N\r\nY|GD|General
        Dynamics Corporation Common Stock|N| |N|100|N||GD|GD|N\r\nY|GDC|GD Culture
        Group Limited - Common Stock|Q|S|N|100|N|N||GDC|N\r\nY|GDDY|GoDaddy Inc. Class
        A Common Stock|N| |N|100|N||GDDY|GDDY|N\r\nY|GDE|WisdomTree Trust WisdomTree
        Efficient Gold Plus Equity Strategy Fund|Z| |Y|100|N||GDE|GDE|N\r\nY|GDEC|FT
        Vest U.S. Equity Moderate Buffer ETF - December|Z| |Y|100|N||GDEC|GDEC|N\r\nY|GDEF|Goldman
        Sachs ETF Trust Goldman Sachs Defensive Equity ETF|P| |Y|100|N||GDEF|GDEF|N\r\nY|GDEN|Golden
        Entertainment, Inc. - Common Stock|Q|G|N|100|N|N||GDEN|N\r\nY|GDEV|GDEV Inc.
        - Ordinary Shares|Q|G|N|100|N|N||GDEV|N\r\nY|GDEVW|GDEV Inc. - Warrant|Q|G|N|100|N|N||GDEVW|N\r\nY|GDHG|Golden
        Heaven Group Holdings Ltd.  - Class A Ordinary Shares|Q|S|N|100|N|D||GDHG|N\r\nY|GDIV|Harbor
        ETF Trust Harbor Dividend Growth Leaders ETF|N| |Y|100|N||GDIV|GDIV|N\r\nY|GDL|GDL
        Fund, The Common Shares of Beneficial Interest|N| |N|100|N||GDL|GDL|N\r\nY|GDL$C|The
        GDL Fund Series C Cumulative Puttable and Callable Preferred Shares|N| |N|100|N||GDLpC|GDL-C|N\r\nY|GDMA|GadsdenA
        DynamicA Multi-AssetA ETF|Z| |Y|100|N||GDMA|GDMA|N\r\nY|GDMN|WisdomTree Trust
        WisdomTree Efficient Gold Plus Gold Miners Strategy Fund|Z| |Y|100|N||GDMN|GDMN|N\r\nY|GDO|Western
        Asset Global Corporate Defined Opportunity Fund Inc.|N| |N|100|N||GDO|GDO|N\r\nY|GDOC|Goldman
        Sachs Future Health Care Equity ETF|P| |Y|100|N||GDOC|GDOC|N\r\nY|GDOT|Green
        Dot Corporation Class A Common Stock, $0.001 par value|N| |N|100|N||GDOT|GDOT|N\r\nY|GDRX|GoodRx
        Holdings, Inc. - Class A Common Stock|Q|Q|N|100|N|N||GDRX|N\r\nY|GDS|GDS Holdings
        Limited - American Depositary Shares|Q|G|N|100|N|N||GDS|N\r\nY|GDST|Goldenstone
        Acquisition Limited - Common Stock|Q|S|N|100|N|N||GDST|N\r\nY|GDSTR|Goldenstone
        Acquisition Limited - Rights|Q|S|N|100|N|N||GDSTR|N\r\nY|GDSTU|Goldenstone
        Acquisition Limited - Units|Q|S|N|100|N|N||GDSTU|N\r\nY|GDSTW|Goldenstone
        Acquisition Limited - Warrants|Q|S|N|100|N|N||GDSTW|N\r\nY|GDTC|CytoMed Therapeutics
        Limited - Ordinary Shares|Q|S|N|100|N|N||GDTC|N\r\nY|GDV|Gabelli Dividend
        & Income Trust Common Shares of Beneficial Interest|N| |N|100|N||GDV|GDV|N\r\nY|GDV$H|The
        Gabelli Dividend & Income Trust 5.375% Series H Cumulative Preferred Shares|N|
        |N|100|N||GDVpH|GDV-H|N\r\nY|GDV$K|The Gabelli Dividend & Income Trust 4.250%
        Series K Cumulative Preferred Shares|N| |N|100|N||GDVpK|GDV-K|N\r\nY|GDVD|Copper
        Place Global Dividend Growth ETF|P| |Y|100|N||GDVD|GDVD|N\r\nY|GDX|VanEck
        Gold Miners ETF |P| |Y|100|N||GDX|GDX|N\r\nY|GDXD|MicroSectors Gold Miners
        -3X Inverse Leveraged ETNs|P| |Y|100|N||GDXD|GDXD|N\r\nY|GDXJ|VanEck Junior
        Gold Miners ETF|P| |Y|100|N||GDXJ|GDXJ|N\r\nY|GDXU|MicroSectors Gold Miners
        3X Leveraged ETN|P| |Y|100|N||GDXU|GDXU|N\r\nY|GDXY|Tidal Trust II YieldMax
        Gold Miners Option Income Strategy ETF|P| |Y|100|N||GDXY|GDXY|N\r\nY|GDYN|Grid
        Dynamics Holdings, Inc. - Class A Common Stock|Q|S|N|100|N|N||GDYN|N\r\nY|GE|GE
        Aerospace Common Stock|N| |N|100|N||GE|GE|N\r\nY|GECC|Great Elm Capital Corp.
        - Closed End Fund|Q|G|N|100|N|N||GECC|N\r\nY|GECCI|Great Elm Capital Corp.
        - 8.50% NOTES DUE 2029|Q|G|N|100|N|N||GECCI|N\r\nY|GECCM|Great Elm Capital
        Corp. - 6.75% Notes Due 2025|Q|G|N|100|N|N||GECCM|N\r\nY|GECCO|Great Elm Capital
        Corp. - 5.875% Notes due 2026|Q|G|N|100|N|N||GECCO|N\r\nY|GECCZ|Great Elm
        Capital Corp. - 8.75% Notes due 2028|Q|G|N|100|N|N||GECCZ|N\r\nY|GEF|Greif
        Inc. Class A Common Stock|N| |N|100|N||GEF|GEF|N\r\nY|GEF.B|Greif, Inc. Corporation
        Class B Common Stock|N| |N|100|N||GEF.B|GEF.B|N\r\nY|GEG|Great Elm Group,
        Inc.  - Common Stock|Q|Q|N|100|N|N||GEG|N\r\nY|GEGGL|Great Elm Group, Inc.
        \ - 7.25% Notes due 2027|Q|G|N|100|N|N||GEGGL|N\r\nY|GEHC|GE HealthCare Technologies
        Inc. - Common Stock|Q|Q|N|100|N|N||GEHC|N\r\nY|GEL|Genesis Energy, L.P. Common
        Units|N| |N|100|N||GEL|GEL|N\r\nY|GEM|Goldman Sachs ActiveBeta Emerging Markets
        Equity ETF|P| |Y|100|N||GEM|GEM|N\r\nY|GEMD|Goldman Sachs ETF Trust Goldman
        Sachs Access Emerging Markets USD Bond ETF|Z| |Y|100|N||GEMD|GEMD|N\r\nY|GEN|Gen
        Digital Inc. - Common Stock|Q|Q|N|100|N|N||GEN|N\r\nY|GENC|Gencor Industries,
        Inc. Common Stock|A| |N|100|N||GENC|GENC|N\r\nY|GENE|Genetic Technologies
        Ltd - American Depositary Shares|Q|S|N|100|N|N||GENE|N\r\nY|GENI|Genius Sports
        Limited Ordinary Shares|N| |N|100|N||GENI|GENI|N\r\nY|GENK|GEN Restaurant
        Group, Inc. - Class A Common Stock|Q|G|N|100|N|N||GENK|N\r\nY|GENM|Spinnaker
        ETF Series Genter Capital Municipal Quality Intermediate ETF|P| |Y|100|N||GENM|GENM|N\r\nY|GENT|Spinnaker
        ETF Series Genter Capital Taxable Quality Intermediate ETF|P| |Y|100|N||GENT|GENT|N\r\nY|GEO|Geo
        Group Inc (The) REIT|N| |N|100|N||GEO|GEO|N\r\nY|GEOS|Geospace Technologies
        Corporation - Common Stock|Q|Q|N|100|N|N||GEOS|N\r\nY|GERM|Amplify ETF Trust
        Amplify Treatments, Testing and Advancements ETF|P| |Y|100|N||GERM|GERM|N\r\nY|GERN|Geron
        Corporation - Common Stock|Q|Q|N|100|N|N||GERN|N\r\nY|GES|Guess?, Inc. Common
        Stock|N| |N|100|N||GES|GES|N\r\nY|GETR|Getaround, Inc. Common Stock|N| |N|100|N||GETR|GETR|N\r\nY|GETY|Getty
        Images Holdings, Inc. Class A Common Stock|N| |N|100|N||GETY|GETY|N\r\nY|GEV|GE
        Vernova Inc. Common Stock|N| |N|100|N||GEV|GEV|N\r\nY|GEVO|Gevo, Inc. - Common
        Stock|Q|S|N|100|N|D||GEVO|N\r\nY|GF|New Germany Fund, Inc. (The) Common Stock|N|
        |N|100|N||GF|GF|N\r\nY|GFAI|Guardforce AI Co., Limited - Ordinary Shares|Q|S|N|100|N|N||GFAI|N\r\nY|GFAIW|Guardforce
        AI Co., Limited - Warrant|Q|S|N|100|N|N||GFAIW|N\r\nY|GFEB|FT Vest U.S. Equity
        Moderate Buffer ETF - February|Z| |Y|100|N||GFEB|GFEB|N\r\nY|GFF|Griffon Corporation
        Common Stock|N| |N|100|N||GFF|GFF|N\r\nY|GFGF|Guru Favorite Stocks ETF|Q|G|Y|100|N|N||GFGF|N\r\nY|GFI|Gold
        Fields Limited American Depositary Shares|N| |N|100|N||GFI|GFI|N\r\nY|GFL|GFL
        Environmental Inc. Subordinate voting shares, no par value|N| |N|100|N||GFL|GFL|N\r\nY|GFOF|ETF
        Series Solutions Grayscale Future of Finance ETF|P| |Y|100|N||GFOF|GFOF|N\r\nY|GFR|Greenfire
        Resources Ltd. Common Shares|N| |N|100|N||GFR|GFR|N\r\nY|GFS|GlobalFoundries
        Inc. - Ordinary Share|Q|Q|N|100|N|N||GFS|N\r\nY|GGAL|Grupo Financiero Galicia
        S.A. - American Depositary Shares, Class B Shares underlying|Q|S|N|100|N|N||GGAL|N\r\nY|GGB|Gerdau
        S.A. Common Stock|N| |N|100|N||GGB|GGB|N\r\nY|GGG|Graco Inc. Common Stock|N|
        |N|100|N||GGG|GGG|N\r\nY|GGLL|Direxion Daily GOOGL Bull 2X Shares|Q|G|Y|100|N|N||GGLL|N\r\nY|GGLS|Direxion
        Daily GOOGL Bear 1X Shares|Q|G|Y|100|N|N||GGLS|N\r\nY|GGM|Northern Lights
        Fund Trust II GGM Macro Alignment ETF|P| |Y|100|N||GGM|GGM|N\r\nY|GGME|Invesco
        Next Gen Media and Gaming ETF|P| |Y|100|N||GGME|GGME|N\r\nY|GGN|GAMCO Global
        Gold, Natural Resources & Income Trust|A| |N|100|N||GGN|GGN|N\r\nY|GGN$B|GAMCO
        Global Gold, Natural Reources & Income Trust 5.00% Series B Cumulative 25.00
        Liquidation Preference|A| |N|100|N||GGNpB|GGN-B|N\r\nY|GGR|Gogoro Inc. - Ordinary
        Shares|Q|Q|N|100|N|N||GGR|N\r\nY|GGROW|Gogoro Inc. - Warrant|Q|Q|N|100|N|N||GGROW|N\r\nY|GGRW|Gabelli
        Growth Innovators ETF|P| |Y|100|N||GGRW|GGRW|N\r\nY|GGT|Gabelli Multi-Media
        Trust, Inc. (The) Common Stock|N| |N|100|N||GGT|GGT|N\r\nY|GGT$E|Gabelli Multi-Media
        Trust Inc. (The) 5.125% Series E Cumulative Preferred Stock|N| |N|100|N||GGTpE|GGT-E|N\r\nY|GGT$G|Gabelli
        Multi-Media Trust Inc. (The) 5.125% Series G Cumulative Preferred Shares|N|
        |N|100|N||GGTpG|GGT-G|N\r\nY|GGT.V|Gabelli Multi-Media Trust Inc. (The) Rights
        (expiring July 22, 2024) Rights when issued|N| |N|100|N||GGTrw|GGT^#|N\r\nY|GGUS|Goldman
        Sachs ETF Trust Goldman Sachs MarketBeta Russell 1000 Growth Equity ETF|P|
        |Y|100|N||GGUS|GGUS|N\r\nY|GGZ|Gabelli Global Small and Mid Cap Value Trust
        (The) Common Shares of Beneficial Interest|N| |N|100|N||GGZ|GGZ|N\r\nY|GH|Guardant
        Health, Inc. - Common Stock|Q|Q|N|100|N|N||GH|N\r\nY|GHC|Graham Holdings Company
        Common Stock|N| |N|100|N||GHC|GHC|N\r\nY|GHEE|Collaborative Investment Series
        Trust Goose Hollow Enhanced Equity ETF|Z| |Y|100|N||GHEE|GHEE|N\r\nY|GHG|GreenTree
        Hospitality Group Ltd. American depositary shares, each representing one Class
        A ordinary share|N| |N|100|N||GHG|GHG|N\r\nY|GHI|Greystone Housing Impact
        Investors LP Beneficial Unit Certificates representing assignments of limited
        partnership interests|N| |N|100|N||GHI|GHI|N\r\nY|GHIX|Gores Holdings IX,
        Inc. - Class A Common Stock|Q|G|N|100|N|N||GHIX|N\r\nY|GHIXU|Gores Holdings
        IX, Inc. - Unit|Q|G|N|100|N|N||GHIXU|N\r\nY|GHIXW|Gores Holdings IX, Inc.
        - Warrant|Q|G|N|100|N|N||GHIXW|N\r\nY|GHLD|Guild Holdings Company Class A
        Common Stock|N| |N|100|N||GHLD|GHLD|N\r\nY|GHM|Graham Corporation Common Stock|N|
        |N|100|N||GHM|GHM|N\r\nY|GHMS|Collaborative Investment Series Trust Goose
        Hollow Multi-Strategy Income ETF|Z| |Y|100|N||GHMS|GHMS|N\r\nY|GHRS|GH Research
        PLC - Ordinary Shares|Q|G|N|100|N|N||GHRS|N\r\nY|GHSI|Guardion Health Sciences,
        Inc. - Common Stock|Q|S|N|100|N|N||GHSI|N\r\nY|GHTA|Goose Hollow Tactical
        Allocation ETF|Z| |Y|100|N||GHTA|GHTA|N\r\nY|GHY|PGIM Global High Yield Fund,
        Inc.|N| |N|100|N||GHY|GHY|N\r\nY|GHYB|Goldman Sachs Access High Yield Corporate
        Bond ETF|P| |Y|100|N||GHYB|GHYB|N\r\nY|GHYG|iShares US & Intl High Yield Corp
        Bond ETF|Z| |Y|100|N||GHYG|GHYG|N\r\nY|GIB|CGI Inc. Common Stock|N| |N|100|N||GIB|GIB|N\r\nY|GIC|Global
        Industrial Company Common Stock|N| |N|100|N||GIC|GIC|N\r\nY|GIFI|Gulf Island
        Fabrication, Inc. - Common Stock|Q|Q|N|100|N|N||GIFI|N\r\nY|GIGB|Goldman Sachs
        Access Investment Grade Corporate Bond ETF|P| |Y|100|N||GIGB|GIGB|N\r\nY|GIGM|GigaMedia
        Limited - Ordinary Shares|Q|S|N|100|N|N||GIGM|N\r\nY|GII|SPDR S&P Global Infrastructure
        ETF|P| |Y|100|N||GII|GII|N\r\nY|GIII|G-III Apparel Group, LTD. - Common Stock|Q|Q|N|100|N|N||GIII|N\r\nY|GIL|Gildan
        Activewear, Inc. Class A Sub. Vot. Common Stock|N| |N|100|N||GIL|GIL|N\r\nY|GILD|Gilead
        Sciences, Inc. - Common Stock|Q|Q|N|100|N|N||GILD|N\r\nY|GILT|Gilat Satellite
        Networks Ltd. - Ordinary Shares|Q|Q|N|100|N|N||GILT|N\r\nY|GINN|Goldman Sachs
        Innovate Equity ETF|P| |Y|100|N||GINN|GINN|N\r\nY|GINX|SGI Enhanced Global
        Income ETF|Q|G|Y|100|N|N||GINX|N\r\nY|GIPR|Generation Income Properties Inc.
        - Common stock|Q|S|N|100|N|N||GIPR|N\r\nY|GIPRW|Generation Income Properties
        Inc. - Warrant|Q|S|N|100|N|N||GIPRW|N\r\nY|GIS|General Mills, Inc. Common
        Stock|N| |N|100|N||GIS|GIS|N\r\nY|GJAN|FT Vest U.S. Equity Moderate Buffer
        ETF - January|Z| |Y|100|N||GJAN|GJAN|N\r\nY|GJH|Synthetic Fixed-Income Securities
        Inc 6.375% (STRATS) Cl A-1|N| |N|100|N||GJH|GJH|N\r\nY|GJO|Synthetic Fixed-Income
        Securities, Inc. on behalf of STRATS(SM) Trust for Wal-Mart Stores, Inc. Securities,
        Series 2004-5|N| |N|100|N||GJO|GJO|N\r\nY|GJP|Synthetic Fixed-Income Securities,
        Inc. on behalf of STRATS (SM) Trust for Dominion Resources, Inc. Securities,
        Series 2005-6, Floating Rate Structured Repackaged Asset-Backed Trust Securities
        (STRATS) Certificates|N| |N|100|N||GJP|GJP|N\r\nY|GJR|Synthetic Fixed-Income
        Securities, Inc. STRATS Trust for Procter&Gamble Securities, Series 2006-1|N|
        |N|100|N||GJR|GJR|N\r\nY|GJS|Goldman Sachs Group Securities STRATS Trust for
        Goldman Sachs Group Securities, Series 2006-2|N| |N|100|N||GJS|GJS|N\r\nY|GJT|Synthetic
        Fixed-Income Securities, Inc. Floating Rate Structured Repackaged Asset-Backed
        Trust Securities Certificates, Series 2006-3|N| |N|100|N||GJT|GJT|N\r\nY|GJUL|FT
        Vest U.S. Equity Moderate Buffer ETF - July|Z| |Y|100|N||GJUL|GJUL|N\r\nY|GJUN|FT
        Vest U.S. Equity Moderate Buffer ETF - June|Z| |Y|100|N||GJUN|GJUN|N\r\nY|GK|AdvisorShares
        Gerber Kawasaki ETF|P| |Y|100|N||GK|GK|N\r\nY|GKOS|Glaukos Corporation Common
        Stock|N| |N|100|N||GKOS|GKOS|N\r\nY|GL|Globe Life Inc. Common Stock|N| |N|100|N||GL|GL|N\r\nY|GL$D|Globe
        Life Inc. 4.25% Junior Subordinated Debentures due 2061|N| |N|100|N||GLpD|GL-D|N\r\nY|GLAC|Global
        Lights Acquisition Corp - Ordinary Shares|Q|G|N|100|N|N||GLAC|N\r\nY|GLACR|Global
        Lights Acquisition Corp - Rights|Q|G|N|100|N|N||GLACR|N\r\nY|GLACU|Global
        Lights Acquisition Corp - Unit|Q|G|N|100|N|N||GLACU|N\r\nY|GLAD|Gladstone
        Capital Corporation - Closed End Fund|Q|Q|N|100|N|N||GLAD|N\r\nY|GLADZ|Gladstone
        Capital Corporation - 7.75% Notes due 2028|Q|Q|N|100|N|N||GLADZ|N\r\nY|GLBE|Global-E
        Online Ltd. - ordinary shares|Q|Q|N|100|N|N||GLBE|N\r\nY|GLBS|Globus Maritime
        Limited - Common Stock|Q|S|N|100|N|N||GLBS|N\r\nY|GLBZ|Glen Burnie Bancorp
        - Common Stock|Q|S|N|100|N|N||GLBZ|N\r\nY|GLD|SPDR Gold Trust|P| |Y|100|N||GLD|GLD|N\r\nY|GLDD|Great
        Lakes Dredge & Dock Corporation - Common Stock|Q|Q|N|100|N|N||GLDD|N\r\nY|GLDG|GoldMining
        Inc. Common Shares|A| |N|100|N||GLDG|GLDG|N\r\nY|GLDI|ETRACS Gold Shares Covered
        Call ETNs due February 2, 2033|Q|G|N|100|N|N||GLDI|N\r\nY|GLDM|SPDR Gold MiniShares
        Trust|P| |Y|100|N||GLDM|GLDM|N\r\nY|GLIN|VanEck India Growth Leaders ETF|P|
        |Y|100|N||GLIN|GLIN|N\r\nY|GLL|ProShares UltraShort Gold|P| |Y|100|N||GLL|GLL|N\r\nY|GLLI|Globalink
        Investment Inc. - Common Stock|Q|S|N|100|N|N||GLLI|N\r\nY|GLLIR|Globalink
        Investment Inc. - Rights|Q|S|N|100|N|N||GLLIR|N\r\nY|GLLIU|Globalink Investment
        Inc. - Units|Q|S|N|100|N|N||GLLIU|N\r\nY|GLLIW|Globalink Investment Inc. -
        Warrants|Q|S|N|100|N|N||GLLIW|N\r\nY|GLMD|Galmed Pharmaceuticals Ltd. - Ordinary
        Shares|Q|S|N|100|N|D||GLMD|N\r\nY|GLNG|Golar LNG Limited - Common Shares|Q|Q|N|100|N|N||GLNG|N\r\nY|GLO|Clough
        Global Opportunities Fund Common Stock|A| |N|100|N||GLO|GLO|N\r\nY|GLOB|Globant
        S.A. Common Shares|N| |N|100|N||GLOB|GLOB|N\r\nY|GLOF|iShares Global Equity
        Factor ETF|P| |Y|100|N||GLOF|GLOF|N\r\nY|GLOP$A|GasLog Partners LP 8.625%
        Series A Cumulative Redeemable Perpetual Fixed to Floating Rate Preference
        Units|N| |N|100|N||GLOPpA|GLOP-A|N\r\nY|GLOP$B|GasLog Partners LP 8.200% Series
        B Cumulative Redeemable Perpetual Fixed to Floating Rate Preference Units|N|
        |N|100|N||GLOPpB|GLOP-B|N\r\nY|GLOP$C|GasLog Partners LP 8.500% Series C Cumulative
        Redeemable Perpetual Fixed to Floating Rate Preference Units|N| |N|100|N||GLOPpC|GLOP-C|N\r\nY|GLOV|Goldman
        Sachs ETF Trust Goldman Sachs ActiveBeta World Low Vol Plus Equity ETF|Z|
        |Y|100|N||GLOV|GLOV|N\r\nY|GLOW|VictoryShares WestEnd Global Equity ETF|Q|G|Y|100|N|N||GLOW|N\r\nY|GLP|Global
        Partners LP Common Units representing Limited Partner Interests|N| |N|100|N||GLP|GLP|N\r\nY|GLP$B|Global
        Partners LP 9.50% Series B Fixed Rate Cumulative Redeemable Perpetual Preferred
        Units representing limited partner interests|N| |N|100|N||GLPpB|GLP-B|N\r\nY|GLPG|Galapagos
        NV - American Depositary Shares|Q|Q|N|100|N|N||GLPG|N\r\nY|GLPI|Gaming and
        Leisure Properties, Inc. - Common Stock|Q|Q|N|100|N|N||GLPI|N\r\nY|GLQ|Clough
        Global Equity Fund Clough Global Equity Fund Common Shares of Beneficial Interest|A|
        |N|100|N||GLQ|GLQ|N\r\nY|GLRE|Greenlight Reinsurance, Ltd. - Class A Ordinary
        Shares|Q|Q|N|100|N|N||GLRE|N\r\nY|GLRY|Northern Lights Fund Trust IV Inspire
        Momentum ETF|P| |Y|100|N||GLRY|GLRY|N\r\nY|GLSI|Greenwich LifeSciences, Inc.
        - Common stock|Q|S|N|100|N|N||GLSI|N\r\nY|GLST|Global Star Acquisition, Inc.
        - Class A Common Stock|Q|G|N|100|N|N||GLST|N\r\nY|GLSTR|Global Star Acquisition,
        Inc. - Right|Q|G|N|100|N|N||GLSTR|N\r\nY|GLSTU|Global Star Acquisition, Inc.
        - Unit|Q|G|N|100|N|N||GLSTU|N\r\nY|GLSTW|Global Star Acquisition, Inc. - Warrants|Q|G|N|100|N|N||GLSTW|N\r\nY|GLT|Glatfelter
        Corporation Common Stock|N| |N|100|N||GLT|GLT|N\r\nY|GLTO|Galecto, Inc. -
        Common Stock|Q|S|N|100|N|D||GLTO|N\r\nY|GLTR|abrdn Physical Precious Metals
        Basket Shares ETF|P| |Y|100|N||GLTR|GLTR|N\r\nY|GLU|Gabelli Global Utility
        Common Shares of Beneficial Ownership|A| |N|100|N||GLU|GLU|N\r\nY|GLU$A|The
        Gabelli Global Utility and Income Trust Series A Cumulative Puttable and Callable
        Preferred Shares|A| |N|100|N||GLUpA|GLU-A|N\r\nY|GLU$B|The Gabelli Global
        Utility and Income Trust Series B Cumulative Puttable and Callable Preferred
        Shares|A| |N|100|N||GLUpB|GLU-B|N\r\nY|GLUE|Monte Rosa Therapeutics, Inc.
        - Common Stock|Q|Q|N|100|N|N||GLUE|N\r\nY|GLV|Clough Global Dividend and Income
        Fund Common Shares of beneficial interest|A| |N|100|N||GLV|GLV|N\r\nY|GLW|Corning
        Incorporated Common Stock|N| |N|100|N||GLW|GLW|N\r\nY|GLYC|GlycoMimetics,
        Inc. - Common Stock|Q|G|N|100|N|N||GLYC|N\r\nY|GM|General Motors Company Common
        Stock|N| |N|100|N||GM|GM|N\r\nY|GMAB|Genmab A/S - American Depositary Shares|Q|Q|N|100|N|N||GMAB|N\r\nY|GMAR|FT
        Vest U.S. Equity Moderate Buffer ETF - March|Z| |Y|100|N||GMAR|GMAR|N\r\nY|GMAY|FT
        Vest U.S. Equity Moderate Buffer ETF - May|Z| |Y|100|N||GMAY|GMAY|N\r\nY|GME|GameStop
        Corporation Common Stock|N| |N|100|N||GME|GME|N\r\nY|GMED|Globus Medical,
        Inc. Class A Common Stock|N| |N|100|N||GMED|GMED|N\r\nY|GMET|VanEck Green
        Metals ETF|P| |Y|100|N||GMET|GMET|N\r\nY|GMF|SPDR S&P Emerging Asia Pacific
        ETF|P| |Y|100|N||GMF|GMF|N\r\nY|GMGI|Golden Matrix Group, Inc. - Common Stock|Q|S|N|100|N|N||GMGI|N\r\nY|GMM|Global
        Mofy Metaverse Limited - Ordinary Shares|Q|S|N|100|N|N||GMM|N\r\nY|GMOM|Cambria
        Global Momentum ETF|Z| |Y|100|N||GMOM|GMOM|N\r\nY|GMRE|Global Medical REIT
        Inc. Common Stock|N| |N|100|N||GMRE|GMRE|N\r\nY|GMRE$A|Global Medical REIT
        Inc. Series A Cumulative Redeemable Preferred Stock|N| |N|100|N||GMREpA|GMRE-A|N\r\nY|GMS|GMS
        Inc. Common Stock|N| |N|100|N||GMS|GMS|N\r\nY|GMUN|Goldman Sachs ETF Trust
        Goldman Sachs Community Municipal Bond ETF|P| |Y|100|N||GMUN|GMUN|N\r\nY|GNE|Genie
        Energy Ltd. Class B Common Stock Stock|N| |N|100|N||GNE|GNE|N\r\nY|GNFT|GENFIT
        S.A. - American Depositary Shares|Q|Q|N|100|N|N||GNFT|N\r\nY|GNK|Genco Shipping
        & Trading Limited Ordinary Shares New (Marshall Islands)|N| |N|100|N||GNK|GNK|N\r\nY|GNL|Global
        Net Lease, Inc. Common Stock|N| |N|100|N||GNL|GNL|N\r\nY|GNL$A|Global Net
        Lease, Inc. 7.25% Series A Cumulative Redeemable Preferred Stock, $0.01 par
        value per share|N| |N|100|N||GNLpA|GNL-A|N\r\nY|GNL$B|Global Net Lease, Inc.
        6.875% Series B Cumulative Redeemable Perpetual Preferred Stock|N| |N|100|N||GNLpB|GNL-B|N\r\nY|GNL$D|Global
        Net Lease, Inc. 7.50% Series D Cumulative Redeemable Perpetual Preferred Stock|N|
        |N|100|N||GNLpD|GNL-D|N\r\nY|GNL$E|Global Net Lease, Inc. 7.375% Series E
        Cumulative Redeemable Perpetual Preferred Stock|N| |N|100|N||GNLpE|GNL-E|N\r\nY|GNLN|Greenlane
        Holdings, Inc. - Class A Common Stock|Q|S|N|100|N|H||GNLN|N\r\nY|GNLX|Genelux
        Corporation - Common Stock|Q|S|N|100|N|N||GNLX|N\r\nY|GNMA|iShares GNMA Bond
        ETF|Q|G|Y|100|N|N||GNMA|N\r\nY|GNOM|Global X Genomics & Biotechnology ETF|Q|G|Y|100|N|N||GNOM|N\r\nY|GNOV|FT
        Vest U.S. Equity Moderate Buffer ETF - November|Z| |Y|100|N||GNOV|GNOV|N\r\nY|GNPX|Genprex,
        Inc. - Common Stock|Q|S|N|100|N|N||GNPX|N\r\nY|GNR|SPDR S&P Global Natural
        Resources ETF|P| |Y|100|N||GNR|GNR|N\r\nY|GNRC|Generac Holdlings Inc. Common
        Stock|N| |N|100|N||GNRC|GNRC|N\r\nY|GNS|Genius Group Limited Ordinary Shares|A|
        |N|100|N||GNS|GNS|N\r\nY|GNSS|Genasys Inc. - Common Stock|Q|S|N|100|N|N||GNSS|N\r\nY|GNT|GAMCO
        Natural Resources, Gold & Income Trust|N| |N|100|N||GNT|GNT|N\r\nY|GNT$A|GAMCO
        Natural Resources, Gold & Income Tust  5.20% Series A Cumulative Preferred
        Shares (Liquidation Preference $25.00 per share)|N| |N|100|N||GNTpA|GNT-A|N\r\nY|GNTA|Genenta
        Science S.p.A. - American Depositary Shares|Q|S|N|100|N|N||GNTA|N\r\nY|GNTX|Gentex
        Corporation - Common Stock|Q|Q|N|100|N|N||GNTX|N\r\nY|GNTY|Guaranty Bancshares,
        Inc. Common Stock|N| |N|100|N||GNTY|GNTY|N\r\nY|GNW|Genworth Financial Inc
        Common Stock|N| |N|100|N||GNW|GNW|N\r\nY|GO|Grocery Outlet Holding Corp. -
        Common Stock|Q|Q|N|100|N|N||GO|N\r\nY|GOAU|US Global GO Gold and Precious
        Metal Miners ETF|P| |Y|100|N||GOAU|GOAU|N\r\nY|GOCO|GoHealth, Inc. - Class
        A Common Stock|Q|S|N|100|N|N||GOCO|N\r\nY|GOCT|FT Vest U.S. Equity Moderate
        Buffer ETF - October|Z| |Y|100|N||GOCT|GOCT|N\r\nY|GODN|Golden Star Acquisition
        Corporation - Ordinary Shares|Q|G|N|100|N|N||GODN|N\r\nY|GODNR|Golden Star
        Acquisition Corporation - Rights|Q|G|N|100|N|N||GODNR|N\r\nY|GODNU|Golden
        Star Acquisition Corporation - Unit|Q|G|N|100|N|N||GODNU|N\r\nY|GOEV|Canoo
        Inc.  - Class A Common Stock|Q|S|N|100|N|N||GOEV|N\r\nY|GOEVW|Canoo Inc.  -
        Warrant|Q|S|N|100|N|N||GOEVW|N\r\nY|GOEX|Global X Gold Explorers ETF|P| |Y|100|N||GOEX|GOEX|N\r\nY|GOF|Guggenheim
        Strategic Opportunities Fund Common Shares of Beneficial Interest|N| |N|100|N||GOF|GOF|N\r\nY|GOGL|Golden
        Ocean Group Limited - Common Stock|Q|Q|N|100|N|N||GOGL|N\r\nY|GOGO|Gogo Inc.
        - Common Stock|Q|Q|N|100|N|N||GOGO|N\r\nY|GOLD|Barrick Gold Corporation Common
        Stock (BC)|N| |N|100|N||GOLD|GOLD|N\r\nY|GOLF|Acushnet Holdings Corp. Common
        Stock|N| |N|100|N||GOLF|GOLF|N\r\nY|GOLY|Strategy Shares Gold-Hedged Bond
        ETF|Z| |Y|100|N||GOLY|GOLY|N\r\nY|GOOD|Gladstone Commercial Corporation -
        Real Estate Investment Trust|Q|Q|N|100|N|N||GOOD|N\r\nY|GOODN|Gladstone Commercial
        Corporation - 6.625% Series E Cumulative Redeemable Preferred Stock|Q|Q|N|100|N|N||GOODN|N\r\nY|GOODO|Gladstone
        Commercial Corporation - 6.00% Series G Cumulative Redeemable Preferred Stock,
        par value $0.001 per share|Q|Q|N|100|N|N||GOODO|N\r\nY|GOOG|Alphabet Inc.
        - Class C Capital Stock|Q|Q|N|100|N|N||GOOG|N\r\nY|GOOGL|Alphabet Inc. - Class
        A Common Stock|Q|Q|N|100|N|N||GOOGL|N\r\nY|GOOP|NEOS ETF Trust Kurv Yield
        Premium Strategy Google (GOOGL) ETF|Z| |Y|100|N||GOOP|GOOP|N\r\nY|GOOS|Canada
        Goose Holdings Inc. Subordinate Voting Shares|N| |N|100|N||GOOS|GOOS|N\r\nY|GOOX|ETF
        Opportunities Trust T-Rex 2X Long Alphabet Daily Target ETF|Z| |Y|100|N||GOOX|GOOX|N\r\nY|GOOY|Tidal
        ETF Trust II YieldMax GOOGL Option Income Strategy ETF|P| |Y|100|N||GOOY|GOOY|N\r\nY|GORO|Gold
        Resource Corporation Common Stock|A| |N|100|N||GORO|GORO|N\r\nY|GORV|Lazydays
        Holdings, Inc. - Common Stock|Q|S|N|100|N|N||GORV|N\r\nY|GOSS|Gossamer Bio,
        Inc. - Common Stock|Q|Q|N|100|N|D||GOSS|N\r\nY|GOTU|Gaotu Techedu Inc. American
        Depositary Shares|N| |N|100|N||GOTU|GOTU|N\r\nY|GOVI|Invesco Equal Weight
        0-30 Year Treasury ETF|Q|G|Y|100|N|N||GOVI|N\r\nY|GOVT|iShares U.S. Treasury
        Bond ETF|Z| |Y|100|N||GOVT|GOVT|N\r\nY|GOVX|GeoVax Labs, Inc. - Common Stock|Q|S|N|100|N|D||GOVX|N\r\nY|GOVXW|GeoVax
        Labs, Inc. - Warrants|Q|S|N|100|N|D||GOVXW|N\r\nY|GOVZ|iShares 25  Year Treasury
        STRIPS Bond ETF|Z| |Y|100|N||GOVZ|GOVZ|N\r\nY|GP|GreenPower Motor Company
        Inc. - Common Shares|Q|S|N|100|N|N||GP|N\r\nY|GPAC|Global Partner Acquisition
        Corp II - Class A Ordinary Share|Q|S|N|100|N|D||GPAC|N\r\nY|GPACU|Global Partner
        Acquisition Corp II - Unit|Q|S|N|100|N|D||GPACU|N\r\nY|GPACW|Global Partner
        Acquisition Corp II - Warrant|Q|S|N|100|N|D||GPACW|N\r\nY|GPAK|Gamer Pakistan
        Inc. - Common Stock|Q|S|N|100|N|H||GPAK|N\r\nY|GPATU|GP-Act III Acquisition
        Corp. - Units|Q|G|N|100|N|N||GPATU|N\r\nY|GPC|Genuine Parts Company Common
        Stock|N| |N|100|N||GPC|GPC|N\r\nY|GPCR|Structure Therapeutics Inc. - American
        Depositary Shares|Q|G|N|100|N|N||GPCR|N\r\nY|GPI|Group 1 Automotive, Inc.
        Common Stock|N| |N|100|N||GPI|GPI|N\r\nY|GPIQ|Goldman Sachs Nasdaq-100 Core
        Premium Income ETF|Q|G|Y|100|N|N||GPIQ|N\r\nY|GPIX|Goldman Sachs S&P 500 Core
        Premium Income ETF|Q|G|Y|100|N|N||GPIX|N\r\nY|GPJA|Georgia Power Company Series
        2017A 5.00% Junior Subordinated Notes due October 1, 2077|N| |N|100|N||GPJA|GPJA|N\r\nY|GPK|Graphic
        Packaging Holding Company|N| |N|100|N||GPK|GPK|N\r\nY|GPMT|Granite Point Mortgage
        Trust Inc. Common Stock|N| |N|100|N||GPMT|GPMT|N\r\nY|GPMT$A|Granite Point
        Mortgage Trust Inc. 7.00% Series A Fixed-to-Floating Rate Cumulative Redeemable
        Preferred Stock|N| |N|100|N||GPMTpA|GPMT-A|N\r\nY|GPN|Global Payments Inc.
        Common Stock|N| |N|100|N||GPN|GPN|N\r\nY|GPOR|Gulfport Energy Corporation
        Common Shares|N| |N|100|N||GPOR|GPOR|N\r\nY|GPOW|Goldman Sachs ETF Trust Goldman
        Sachs North American Pipelines & Power Equity ETF|Z| |Y|100|N||GPOW|GPOW|N\r\nY|GPRE|Green
        Plains, Inc. - Common Stock|Q|Q|N|100|N|N||GPRE|N\r\nY|GPRK|Geopark Ltd Common
        Shares|N| |N|100|N||GPRK|GPRK|N\r\nY|GPRO|GoPro, Inc. - Class A Common Stock|Q|Q|N|100|N|N||GPRO|N\r\nY|GPS|Gap,
        Inc. (The) Common Stock|N| |N|100|N||GPS|GPS|N\r\nY|GQI|Natixis ETF Trust
        Natixis Gateway Quality Income ETF|P| |Y|100|N||GQI|GQI|N\r\nY|GQRE|FlexShares
        Global Quality Real Estate Index Fund|P| |Y|100|N||GQRE|GQRE|N\r\nY|GRAB|Grab
        Holdings Limited - Class A Ordinary Shares|Q|Q|N|100|N|N||GRAB|N\r\nY|GRABW|Grab
        Holdings Limited - Warrant|Q|Q|N|100|N|N||GRABW|N\r\nY|GRAF.U|Graf Global
        Corp. Units, each consisting of one Class A ordinary share and one-half of
        one redeemable warrant|A| |N|100|N||GRAF.U|GRAF=|N\r\nY|GRAL|GRAIL, Inc. -
        Common Stock|Q|Q|N|100|N|N||GRAL|N\r\nY|GRBK|Green Brick Partners, Inc. Common
        Stock|N| |N|100|N||GRBK|GRBK|N\r\nY|GRBK$A|Green Brick Partners, Inc. Depositary
        Shares (each representing a 1/1000th fractional interest in a share of 5.75%
        Series A Cumulative Perpetual Preferred Stock)|N| |N|100|N||GRBKpA|GRBK-A|N\r\nY|GRC|Gorman-Rupp
        Company (The) Common Stock|N| |N|100|N||GRC|GRC|N\r\nY|GRDI|GRIID Infrastructure
        Inc. - Common Stock|Q|G|N|100|N|D||GRDI|N\r\nY|GRDIW|GRIID Infrastructure
        Inc. - Warrant|Q|G|N|100|N|N||GRDIW|N\r\nY|GREE|Greenidge Generation Holdings
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||GREE|N\r\nY|GREEL|Greenidge Generation
        Holdings Inc. - 8.50% Senior Notes due 2026|Q|Q|N|100|N|N||GREEL|N\r\nY|GREI|Goldman
        Sachs Future Real Estate and Infrastructure Equity ETF|P| |Y|100|N||GREI|GREI|N\r\nY|GREK|Global
        X MSCI Greece ETF|P| |Y|100|N||GREK|GREK|N\r\nY|GRF|Eagle Capital Growth Fund,
        Inc. Common Stock|A| |N|100|N||GRF|GRF|N\r\nY|GRFS|Grifols, S.A. - American
        Depositary Shares|Q|Q|N|100|N|N||GRFS|N\r\nY|GRFX|Graphex Group Limited American
        Depositary Shares, each American Depositary Share representing 20 Ordinary
        Shares|A| |N|100|N||GRFX|GRFX|N\r\nY|GRI|GRI Bio, Inc. - Common Stock|Q|S|N|100|N|D||GRI|N\r\nY|GRID|First
        Trust NASDAQ Clean Edge Smart Grid Infrastructure Index Fund|Q|G|Y|100|N|N||GRID|N\r\nY|GRIN|Grindrod
        Shipping Holdings Ltd. - Ordinary Shares|Q|Q|N|100|N|N||GRIN|N\r\nY|GRMN|Garmin
        Ltd. Common Stock (Switzerland)|N| |N|100|N||GRMN|GRMN|N\r\nY|GRN|iPath Series
        B Carbon Exchange-Traded Notes|P| |N|100|N||GRN|GRN|N\r\nY|GRNB|VanEck Green
        Bond ETF|P| |Y|100|N||GRNB|GRNB|N\r\nY|GRND|Grindr Inc. Common Stock|N| |N|100|N||GRND|GRND|N\r\nY|GRND.W|Grindr
        Inc. Warrants, each exercisable for one share of Common Stock at an exercise
        price of $11.50 per share|N| |N|100|N||GRND.WS|GRND+|N\r\nY|GRNQ|Greenpro
        Capital Corp. - Common Stock|Q|S|N|100|N|N||GRNQ|N\r\nY|GRNT|Granite Ridge
        Resources, Inc. Common Stock|N| |N|100|N||GRNT|GRNT|N\r\nY|GROM|Grom Social
        Enterprises Inc. - Common Stock|Q|S|N|100|N|D||GROM|N\r\nY|GROMW|Grom Social
        Enterprises Inc. - Warrants|Q|S|N|100|N|N||GROMW|N\r\nY|GROV|Grove Collaborative
        Holdings, Inc. Class A Common Stock|N| |N|100|N||GROV|GROV|N\r\nY|GROW|U.S.
        Global Investors, Inc. - Class A Common Stock|Q|S|N|100|N|N||GROW|N\r\nY|GROY|Gold
        Royalty Corp. Common Shares|A| |N|100|N||GROY|GROY|N\r\nY|GROY.W|Gold Royalty
        Corp. Warrants|A| |N|100|N||GROY.WS|GROY+|N\r\nY|GRP.U|Granite Real Estate
        Inc. Stapled Units, each consisting of one unit of Granite Real Estate Trust
        and one common share of Granite REIT Inc.|N| |N|100|N||GRP.U|GRP=|N\r\nY|GRPM|Invesco
        S&P MidCap 400? GARP ETF|P| |Y|100|N||GRPM|GRPM|N\r\nY|GRPN|Groupon, Inc.
        - Common Stock|Q|Q|N|100|N|N||GRPN|N\r\nY|GRPZ|Invesco Exchange-Traded Fund
        Trust II Invesco S&P SmallCap 600 GARP ETF|P| |Y|100|N||GRPZ|GRPZ|N\r\nY|GRRR|Gorilla
        Technology Group Inc. - Ordinary shares|Q|S|N|100|N|N||GRRR|N\r\nY|GRRRW|Gorilla
        Technology Group Inc. - Warrant|Q|S|N|100|N|N||GRRRW|N\r\nY|GRTS|Gritstone
        bio, Inc. - Common Stock|Q|Q|N|100|N|N||GRTS|N\r\nY|GRVY|GRAVITY Co., Ltd.
        - American depositary shares, each representing one common share.|Q|G|N|100|N|N||GRVY|N\r\nY|GRW|Engine
        No. 1 ETF Trust TCW Compounders ETF|N| |Y|100|N||GRW|GRW|N\r\nY|GRWG|GrowGeneration
        Corp. - Common Stock|Q|S|N|100|N|N||GRWG|N\r\nY|GRX|The Gabelli Healthcare
        & Wellness Trust Common Shares of Beneficial Interest|N| |N|100|N||GRX|GRX|N\r\nY|GRYP|Gryphon
        Digital Mining, Inc - Common Stock|Q|S|N|100|N|N||GRYP|N\r\nY|GS|Goldman Sachs
        Group, Inc. (The) Common Stock|N| |N|100|N||GS|GS|N\r\nY|GS$A|Goldman Sachs
        Group, Inc. (The) Depositary Shares each representing 1/1000th Interest in
        a Share of Floating Rate Non-Cumulative Preferred Stock Series A|N| |N|100|N||GSpA|GS-A|N\r\nY|GS$C|Goldman
        Sachs Group, Inc. (The) Depositary Share repstg 1/1000th Preferred Series
        C|N| |N|100|N||GSpC|GS-C|N\r\nY|GS$D|Goldman Sachs Group, Inc. (The) Dep Shs
        repstg 1/1000 Pfd Ser D Fltg|N| |N|100|N||GSpD|GS-D|N\r\nY|GSAT|Globalstar,
        Inc. Common Stock|A| |N|100|N||GSAT|GSAT|N\r\nY|GSBC|Great Southern Bancorp,
        Inc. - Common Stock|Q|Q|N|100|N|N||GSBC|N\r\nY|GSBD|Goldman Sachs BDC, Inc.
        Common Stock|N| |N|100|N||GSBD|GSBD|N\r\nY|GSC|Goldman Sachs ETF Trust Goldman
        Sachs Small Cap Core Equity ETF|P| |Y|100|N||GSC|GSC|N\r\nY|GSEE|Goldman Sachs
        MarketBeta Emerging Markets Equity ETF|Z| |Y|100|N||GSEE|GSEE|N\r\nY|GSEP|FT
        Vest U.S. Equity Moderate Buffer ETF - September|Z| |Y|100|N||GSEP|GSEP|N\r\nY|GSEU|Goldman
        Sachs ActiveBeta Europe Equity ETF|P| |Y|100|N||GSEU|GSEU|N\r\nY|GSEW|Goldman
        Sachs Equal Weight U.S. Large Cap Equity ETF|Z| |Y|100|N||GSEW|GSEW|N\r\nY|GSFP|Goldman
        Sachs Future Planet Equity ETF|P| |Y|100|N||GSFP|GSFP|N\r\nY|GSG|iShares GSCI
        Commodity-Indexed Trust Fund|P| |Y|100|N||GSG|GSG|N\r\nY|GSHD|Goosehead Insurance,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||GSHD|N\r\nY|GSIB|Themes Global
        Systemically Important Banks ETF|Q|G|Y|100|N|N||GSIB|N\r\nY|GSID|Goldman Sachs
        MarketBeta International Equity ETF|Z| |Y|100|N||GSID|GSID|N\r\nY|GSIE|Goldman
        Sachs ActiveBeta International Equity ETF|P| |Y|100|N||GSIE|GSIE|N\r\nY|GSIG|Golden
        Sachs ETF Trust Goldman Sachs Access Investment Grade Corporate 1-5 Year Bond
        ETF|P| |Y|100|N||GSIG|GSIG|N\r\nY|GSIT|GSI Technology, Inc. - Common Stock|Q|Q|N|100|N|N||GSIT|N\r\nY|GSIW|Garden
        Stage Limited - Ordinary Shares|Q|S|N|100|N|N||GSIW|N\r\nY|GSJY|Goldman Sachs
        ActiveBeta Japan Equity ETF|P| |Y|100|N||GSJY|GSJY|N\r\nY|GSK|GSK plc American
        Depositary Shares (Each representing two Ordinary Shares)|N| |N|100|N||GSK|GSK|N\r\nY|GSL|Global
        Ship Lease Inc New Class A Common Shares|N| |N|100|N||GSL|GSL|N\r\nY|GSL$B|Global
        Ship Lease, Inc. Depository Shares Representing 1/100th Perpetual Preferred
        Series B% (Marshall Island)|N| |N|100|N||GSLpB|GSL-B|N\r\nY|GSLC|Goldman Sachs
        ActiveBeta U.S. Large Cap Equity ETF|P| |Y|100|N||GSLC|GSLC|N\r\nY|GSM|Ferroglobe
        PLC - Ordinary Shares|Q|S|N|100|N|N||GSM|N\r\nY|GSMGW|Cheer Holding, Inc.
        \ - Warrant|Q|S|N|100|N|N||GSMGW|N\r\nY|GSPY|Gotham Enhanced 500 ETF|P| |Y|100|N||GSPY|GSPY|N\r\nY|GSSC|GS
        ActiveBeta U.S. Small Cap Equity ETF|P| |Y|100|N||GSSC|GSSC|N\r\nY|GSST|Goldman
        Sachs Access Ultra Short Bond ETF|Z| |Y|100|N||GSST|GSST|N\r\nY|GSUN|Golden
        Sun Health Technology Group Limited - Class A Ordinary Shares|Q|S|N|100|N|N||GSUN|N\r\nY|GSUS|Goldman
        Sachs MarketBeta U.S. Equity ETF|Z| |Y|100|N||GSUS|GSUS|N\r\nY|GSY|Invesco
        Ultra Short Duration ETF|P| |Y|100|N||GSY|GSY|N\r\nY|GT|The Goodyear Tire
        & Rubber Company - Common Stock|Q|Q|N|100|N|N||GT|N\r\nY|GTAC|Global Technology
        Acquisition Corp. I - Class A Ordinary Shares|Q|S|N|100|N|N||GTAC|N\r\nY|GTACU|Global
        Technology Acquisition Corp. I - Unit|Q|S|N|100|N|N||GTACU|N\r\nY|GTACW|Global
        Technology Acquisition Corp. I - Warrant|Q|S|N|100|N|N||GTACW|N\r\nY|GTBP|GT
        Biopharma, Inc. - Common Stock|Q|S|N|100|N|N||GTBP|N\r\nY|GTE|Gran Tierra
        Energy Inc. Common Stock|A| |N|100|N||GTE|GTE|N\r\nY|GTEC|Greenland Technologies
        Holding Corporation - Ordinary Shares|Q|S|N|100|N|N||GTEC|N\r\nY|GTEK|Goldman
        Sachs Future Tech Leaders Equity ETF|P| |Y|100|N||GTEK|GTEK|N\r\nY|GTES|Gates
        Industrial Corporation plc Ordinary Shares|N| |N|100|N||GTES|GTES|N\r\nY|GTHX|G1
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||GTHX|N\r\nY|GTI|Graphjet
        Technology - Class A Ordinary Shares|Q|G|N|100|N|E||GTI|N\r\nY|GTIM|Good Times
        Restaurants Inc. - Common Stock|Q|S|N|100|N|N||GTIM|N\r\nY|GTIP|Goldman Sachs
        Access Inflation Protected USD Bond ETF|Z| |Y|100|N||GTIP|GTIP|N\r\nY|GTLB|GitLab
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||GTLB|N\r\nY|GTLS|Chart Industries,
        Inc. Common Stock|N| |N|100|N||GTLS|GTLS|N\r\nY|GTLS$B|Chart Industries, Inc.
        Depositary Shares, each Representing a 1/20th Interest in a Share of 6.75%
        Series B Mandatory Convertible Preferred Stock|N| |N|100|N||GTLSpB|GTLS-B|N\r\nY|GTN|Gray
        Television, Inc. Common Stock|N| |N|100|N||GTN|GTN|N\r\nY|GTN.A|Gray Television,
        Inc. CLass A Common Stock|N| |N|100|N||GTN.A|GTN.A|N\r\nY|GTO|Invesco Total
        Return Bond ETF|P| |Y|100|N||GTO|GTO|N\r\nY|GTR|WisdomTree Target Range Fund|Q|G|Y|100|N|N||GTR|N\r\nY|GTX|Garrett
        Motion Inc. - Common Stock|Q|Q|N|100|N|N||GTX|N\r\nY|GTY|Getty Realty Corporation
        Common Stock|N| |N|100|N||GTY|GTY|N\r\nY|GUG|Guggenheim Active Allocation
        Fund Common Shares of Beneficial Interest|N| |N|100|N||GUG|GUG|N\r\nY|GUNR|FlexShares
        Global Upstream Natural Resources Index Fund ETF|P| |Y|100|N||GUNR|GUNR|N\r\nY|GURE|Gulf
        Resources, Inc. - Common Stock|Q|Q|N|100|N|E||GURE|N\r\nY|GURU|Global X Guru
        Index ETF|P| |Y|100|N||GURU|GURU|N\r\nY|GUSA|Goldman Sachs ETF Trust II Goldman
        Sachs MarketBeta U.S. 1000 Equity ETF|P| |Y|100|N||GUSA|GUSA|N\r\nY|GUSH|Direxion
        Daily S&P Oil & Gas Exp. & Prod. Bull 2X Shares|P| |Y|100|N||GUSH|GUSH|N\r\nY|GUT|Gabelli
        Utility Trust (The) Common Stock|N| |N|100|N||GUT|GUT|N\r\nY|GUT$C|Gabelli
        Utility Trust (The) 5.375% Series C Cumulative Preferred Shares|N| |N|100|N||GUTpC|GUT-C|N\r\nY|GUTS|Fractyl
        Health, Inc. - Common Stock|Q|G|N|100|N|N||GUTS|N\r\nY|GV|Visionary Holdings
        Inc. - Common Shares|Q|S|N|100|N|N||GV|N\r\nY|GVA|Granite Construction Incorporated
        Common Stock|N| |N|100|N||GVA|GVA|N\r\nY|GVAL|Cambria Global Value ETF|Z|
        |Y|100|N||GVAL|GVAL|N\r\nY|GVH|Globavend Holdings Limited - Ord Shares|Q|S|N|100|N|N||GVH|N\r\nY|GVI|iShares
        Intermediate Government/Credit Bond ETF|Z| |Y|100|N||GVI|GVI|N\r\nY|GVIP|Goldman
        Sachs Hedge Industry VIP ETF|P| |Y|100|N||GVIP|GVIP|N\r\nY|GVLU|Tidal ETF
        Trust Gotham 1000 Value ETF|P| |Y|100|N||GVLU|GVLU|N\r\nY|GVP|GSE Systems,
        Inc. - Common Stock|Q|S|N|100|N|N||GVP|N\r\nY|GVUS|Goldman Sachs ETF Trust
        Goldman Sachs MarketBeta Russell 1000 Value Equity ETF|P| |Y|100|N||GVUS|GVUS|N\r\nY|GWAV|Greenwave
        Technology Solutions, Inc. - Common Stock|Q|S|N|100|N|N||GWAV|N\r\nY|GWH|ESS
        Tech, Inc. Common Stock|N| |N|100|N||GWH|GWH|N\r\nY|GWH.W|ESS Tech, Inc. Warrant|N|
        |N|100|N||GWH.WS|GWH+|N\r\nY|GWRE|Guidewire Software, Inc. Common Stock|N|
        |N|100|N||GWRE|GWRE|N\r\nY|GWRS|Global Water Resources, Inc. - common stock|Q|G|N|100|N|N||GWRS|N\r\nY|GWW|W.W.
        Grainger, Inc. Common Stock|N| |N|100|N||GWW|GWW|N\r\nY|GWX|SPDR S&P International
        SmallCap ETF|P| |Y|100|N||GWX|GWX|N\r\nY|GXAI|Gaxos.ai Inc. - Common Stock|Q|S|N|100|N|N||GXAI|N\r\nY|GXC|SPDR
        S&P China ETF|P| |Y|100|N||GXC|GXC|N\r\nY|GXG|Global X MSCI Colombia ETF|P|
        |Y|100|N||GXG|GXG|N\r\nY|GXO|GXO Logistics, Inc. Common Stock |N| |N|100|N||GXO|GXO|N\r\nY|GXTG|Global
        X Thematic Growth ETF|Q|G|Y|100|N|N||GXTG|N\r\nY|GXUS|Goldman Sachs ETF Trust
        II Goldman Sachs MarketBeta Total International Equity ETF|P| |Y|100|N||GXUS|GXUS|N\r\nY|GYLD|Arrow
        Dow Jones Global Yield ETF ETF|N| |Y|100|N||GYLD|GYLD|N\r\nY|GYRE|Gyre Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||GYRE|N\r\nY|GYRO|Gyrodyne , LLC - Common
        Stock|Q|S|N|100|N|N||GYRO|N\r\nY|H|Hyatt Hotels Corporation Class A Common
        Stock|N| |N|100|N||H|H|N\r\nY|HA|Hawaiian Holdings, Inc. - Common Stock|Q|Q|N|100|N|N||HA|N\r\nY|HACK|Amplify
        ETF Trust Amplify Cybersecurity ETF|P| |Y|100|N||HACK|HACK|N\r\nY|HAE|Haemonetics
        Corporation Common Stock|N| |N|100|N||HAE|HAE|N\r\nY|HAFC|Hanmi Financial
        Corporation - Common Stock|Q|Q|N|100|N|N||HAFC|N\r\nY|HAFN|Hafnia Limited
        Common Shares|N| |N|100|N||HAFN|HAFN|N\r\nY|HAIA|Healthcare AI Acquisition
        Corp. - Class A Ordinary Shares|Q|S|N|100|N|N||HAIA|N\r\nY|HAIAU|Healthcare
        AI Acquisition Corp. - Units|Q|S|N|100|N|N||HAIAU|N\r\nY|HAIAW|Healthcare
        AI Acquisition Corp. - Warrants|Q|S|N|100|N|N||HAIAW|N\r\nY|HAIL|SPDR S&P
        Kensho Smart Mobility ETF|P| |Y|100|N||HAIL|HAIL|N\r\nY|HAIN|The Hain Celestial
        Group, Inc. - Common Stock|Q|Q|N|100|N|N||HAIN|N\r\nY|HAL|Halliburton Company
        Common Stock|N| |N|100|N||HAL|HAL|N\r\nY|HALO|Halozyme Therapeutics, Inc.
        - Common Stock|Q|Q|N|100|N|N||HALO|N\r\nY|HAO|Haoxi Health Technology Limited
        - Class A Ord Share|Q|S|N|100|N|N||HAO|N\r\nY|HAP|VanEck Natural Resources
        ETF|P| |Y|100|N||HAP|HAP|N\r\nY|HAPI|Harbor Human Capital Factor US Large
        Cap ETF|P| |Y|100|N||HAPI|HAPI|N\r\nY|HAPR|SHL Telemedicine Ltd Innovator
        Premium Income 9 Buffer ETF - April|Z| |Y|100|N||HAPR|HAPR|N\r\nY|HAPS|Harbor
        Human Capital Factor US Small Cap ETF|P| |Y|100|N||HAPS|HAPS|N\r\nY|HAPY|Harbor
        Human Capital Factor Unconstrained ETF|P| |Y|100|N||HAPY|HAPY|N\r\nY|HARD|Simplify
        Exchange Traded Funds Simplify Commodities Strategy No K-1 ETF|P| |Y|100|N||HARD|HARD|N\r\nY|HART|IQ
        Healthy Hearts ETF|P| |Y|100|N||HART|HART|N\r\nY|HAS|Hasbro, Inc. - Common
        Stock|Q|Q|N|100|N|N||HAS|N\r\nY|HASI|Hannon Armstrong Sustainable Infrastructure
        Capital, Inc. Common Stock|N| |N|100|N||HASI|HASI|N\r\nY|HAUS|Tidal ETF Trust
        Residential REIT ETF|Z| |Y|100|N||HAUS|HAUS|N\r\nY|HAUZ|Xtrackers International
        Real Estate ETF|P| |Y|100|N||HAUZ|HAUZ|N\r\nY|HAWX|iShares Currency Hedged
        MSCI ACWI ex U.S. ETF|P| |Y|100|N||HAWX|HAWX|N\r\nY|HAYN|Haynes International,
        Inc. - Common Stock|Q|Q|N|100|N|N||HAYN|N\r\nY|HAYW|Hayward Holdings, Inc.
        Common Stock|N| |N|100|N||HAYW|HAYW|N\r\nY|HBAN|Huntington Bancshares Incorporated
        - Common Stock|Q|Q|N|100|N|N||HBAN|N\r\nY|HBANL|Huntington Bancshares Incorporated
        - Depositary Shares, Each Representing a 1/40th Interest in a Share of 6.875%
        Series J Non-Cumulative Perpetual Preferred Stock|Q|Q|N|100|N|N||HBANL|N\r\nY|HBANM|Huntington
        Bancshares Incorporated - Depositary Shares each representing a 1/1000th interest
        in a share of Huntington Series I Preferred Stock|Q|Q|N|100|N|N||HBANM|N\r\nY|HBANP|Huntington
        Bancshares Incorporated - Depositary Shares 4.500% Series H Non-Cumulative
        Perpetual Preferred Stock|Q|Q|N|100|N|N||HBANP|N\r\nY|HBB|Hamilton Beach Brands
        Holding Company Class A Common Stock |N| |N|100|N||HBB|HBB|N\r\nY|HBCP|Home
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||HBCP|N\r\nY|HBI|Hanesbrands Inc.
        Common Stock|N| |N|100|N||HBI|HBI|N\r\nY|HBIO|Harvard Bioscience, Inc. - Common
        Stock|Q|G|N|100|N|N||HBIO|N\r\nY|HBM|Hudbay Minerals Inc. Ordinary Shares
        (Canada)|N| |N|100|N||HBM|HBM|N\r\nY|HBNC|Horizon Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||HBNC|N\r\nY|HBT|HBT
        Financial, Inc. - Common Stock|Q|Q|N|100|N|N||HBT|N\r\nY|HCA|HCA Healthcare,
        Inc. Common Stock|N| |N|100|N||HCA|HCA|N\r\nY|HCAT|Health Catalyst, Inc -
        Common stock|Q|Q|N|100|N|N||HCAT|N\r\nY|HCC|Warrior Met Coal, Inc. Common
        Stock|N| |N|100|N||HCC|HCC|N\r\nY|HCI|HCI Group, Inc. Common Stock|N| |N|100|N||HCI|HCI|N\r\nY|HCKT|The
        Hackett Group, Inc. - Common Stock|Q|Q|N|100|N|N||HCKT|N\r\nY|HCM|HUTCHMED
        (China) Limited - American Depositary Shares|Q|Q|N|100|N|N||HCM|N\r\nY|HCMT|Direxion
        Shares ETF Trust Direxion HCM Tactical Enhanced US ETF|P| |Y|100|N||HCMT|HCMT|N\r\nY|HCOM|Hartford
        Schroders Commodity Strategy ETF|P| |Y|100|N||HCOM|HCOM|N\r\nY|HCOW|Amplify
        Cash Flow High Income ETF|Q|G|Y|100|N|N||HCOW|N\r\nY|HCP|HashiCorp, Inc. -
        Class A Common Stock|Q|Q|N|100|N|N||HCP|N\r\nY|HCRB|Hartford Core Bond ETF|Z|
        |Y|100|N||HCRB|HCRB|N\r\nY|HCSG|Healthcare Services Group, Inc. - Common Stock|Q|Q|N|100|N|N||HCSG|N\r\nY|HCTI|Healthcare
        Triangle, Inc. - Common Stock|Q|S|N|100|N|D||HCTI|N\r\nY|HCVI|Hennessy Capital
        Investment Corp. VI - Class A Common Stock|Q|G|N|100|N|N||HCVI|N\r\nY|HCVIU|Hennessy
        Capital Investment Corp. VI - Unit|Q|G|N|100|N|N||HCVIU|N\r\nY|HCVIW|Hennessy
        Capital Investment Corp. VI - Warrant|Q|G|N|100|N|N||HCVIW|N\r\nY|HCWB|HCW
        Biologics Inc. - Common Stock|Q|G|N|100|N|D||HCWB|N\r\nY|HCXY|Hercules Capital,
        Inc. 6.25% Notes due 2033|N| |N|100|N||HCXY|HCXY|N\r\nY|HD|Home Depot, Inc.
        (The) Common Stock|N| |N|100|N||HD|HD|N\r\nY|HDAW|Xtrackers MSCI All World
        ex US High Dividend Yield Equity ETF|P| |Y|100|N||HDAW|HDAW|N\r\nY|HDB|HDFC
        Bank Limited Common Stock|N| |N|100|N||HDB|HDB|N\r\nY|HDEF|Xtrackers MSCI
        EAFE High Dividend Yield Equity ETF|P| |Y|100|N||HDEF|HDEF|N\r\nY|HDG|ProShares
        Hedge Replication ETF|P| |Y|100|N||HDG|HDG|N\r\nY|HDGE|Ranger Equity Bear
        Bear ETF|P| |Y|100|N||HDGE|HDGE|N\r\nY|HDL|SUPER HI INTERNATIONAL HOLDING
        LTD. - American Depositary Shares|Q|G|N|100|N|N||HDL|N\r\nY|HDLB|ETRACS Monthly
        Pay 2xLeveraged US High Dividend Low Volatility ETN Series B due September
        30, 2044|P| |Y|100|N||HDLB|HDLB|N\r\nY|HDMV|First Trust Exchange-Traded Fund
        III First Trust Horizon Managed Volatility Developed International ETF|P|
        |Y|100|N||HDMV|HDMV|N\r\nY|HDRO|ETF Series Solutions Defiance Next Gen H2
        ETF|P| |Y|100|N||HDRO|HDRO|N\r\nY|HDSN|Hudson Technologies, Inc. - Common
        Stock|Q|S|N|100|N|N||HDSN|N\r\nY|HDUS|Lattice Strategies Trust Hartford Disciplined
        US Equity ETF|P| |Y|100|N||HDUS|HDUS|N\r\nY|HDV|iShares Core High Dividend
        ETF|P| |Y|100|N||HDV|HDV|N\r\nY|HE|Hawaiian Electric Industries, Inc. Common
        Stock|N| |N|100|N||HE|HE|N\r\nY|HEAR|Turtle Beach Corporation - Common Stock|Q|G|N|100|N|N||HEAR|N\r\nY|HEAT|Touchstone
        ETF Trust Touchstone Climate Transition ETF|Z| |Y|100|N||HEAT|HEAT|N\r\nY|HEDJ|WisdomTree
        Europe Hedged Equity Fund|P| |Y|100|N||HEDJ|HEDJ|N\r\nY|HEEM|iShares Currency
        Hedged MSCI Emerging Markets ETF|Z| |Y|100|N||HEEM|HEEM|N\r\nY|HEES|H&E Equipment
        Services, Inc. - Common Stock|Q|Q|N|100|N|N||HEES|N\r\nY|HEFA|iShares Currency
        Hedged MSCI EAFE ETF|Z| |Y|100|N||HEFA|HEFA|N\r\nY|HEGD|Swan Hedged Equity
        US Large Cap ETF|Z| |Y|100|N||HEGD|HEGD|N\r\nY|HEI|Heico Corporation Common
        Stock|N| |N|100|N||HEI|HEI|N\r\nY|HEI.A|Heico Corporation Common Stock|N|
        |N|100|N||HEI.A|HEI.A|N\r\nY|HELE|Helen of Troy Limited - Common Stock|Q|Q|N|100|N|N||HELE|N\r\nY|HELO|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Hedged Equity Laddered Overlay
        ETF|P| |Y|100|N||HELO|HELO|N\r\nY|HELX|Franklin Genomic Advancements ETF|Z|
        |Y|100|N||HELX|HELX|N\r\nY|HEPA|Hepion Pharmaceuticals, Inc. - Common Stock|Q|S|N|100|N|N||HEPA|N\r\nY|HEPS|D-Market
        Electronic Services & Trading - American Depositary Shares|Q|Q|N|100|N|N||HEPS|N\r\nY|HEQ|John
        Hancock Hedged Equity & Income Fund Common Shares of Beneficial Interest|N|
        |N|100|N||HEQ|HEQ|N\r\nY|HEQT|Simplify Hedged Equity ETF|P| |Y|100|N||HEQT|HEQT|N\r\nY|HERD|Pacer
        Cash Cows Fund of Funds ETF|Q|G|Y|100|N|N||HERD|N\r\nY|HERO|Global X Video
        Games & Esports ETF|Q|G|Y|100|N|N||HERO|N\r\nY|HES|Hess Corporation Common
        Stock|N| |N|100|N||HES|HES|N\r\nY|HESM|Hess Midstream LP Class A Share|N|
        |N|100|N||HESM|HESM|N\r\nY|HEWG|iShares Currency Hedged MSCI Germany ETF|Q|G|Y|100|N|N||HEWG|N\r\nY|HEWJ|iShares
        Currency Hedged MSCI Japan ETF|P| |Y|100|N||HEWJ|HEWJ|N\r\nY|HEZU|iShares
        Currency Hedged MSCI Eurozone ETF|P| |Y|100|N||HEZU|HEZU|N\r\nY|HF|Return
        Stacked Bonds & Managed Futures ETF DGA Absolute Return ETF|P| |Y|100|N||HF|HF|N\r\nY|HFBL|Home
        Federal Bancorp, Inc. of Louisiana - Common Stock|Q|S|N|100|N|N||HFBL|N\r\nY|HFFG|HF
        Foods Group Inc. - Common Stock|Q|S|N|100|N|N||HFFG|N\r\nY|HFGO|Hartford Large
        Cap Growth ETF|Z| |Y|100|N||HFGO|HFGO|N\r\nY|HFND|Tidal ETF Trust Unlimited
        HFND Multi-Strategy Return Tracker ETF|P| |Y|100|N||HFND|HFND|N\r\nY|HFRO|Highland
        Opportunities and Income Fund Common Shares of Beneficial Interest|N| |N|100|N||HFRO|HFRO|N\r\nY|HFRO$A|Highland
        Opportunities and Income Fund 5.375% Series A Cumulative Preferred Shares|N|
        |N|100|N||HFROpA|HFRO-A|N\r\nY|HFWA|Heritage Financial Corporation - Common
        Stock|Q|Q|N|100|N|N||HFWA|N\r\nY|HFXI|IQ FTSE International Equity Currency
        Neutral ETF|P| |Y|100|N||HFXI|HFXI|N\r\nY|HG|Hamilton Insurance Group, Ltd.
        Class B Common Shares|N| |N|100|N||HG|HG|N\r\nY|HGBL|Heritage Global Inc.
        - Common Stock|Q|S|N|100|N|N||HGBL|N\r\nY|HGER|Harbor Commodity All-Weather
        Strategy ETF|N| |Y|100|N||HGER|HGER|N\r\nY|HGLB|Highland Global Allocation
        Fund Common Stock|N| |N|100|N||HGLB|HGLB|N\r\nY|HGTY|Hagerty, Inc. Class A
        Common Stock|N| |N|100|N||HGTY|HGTY|N\r\nY|HGTY.W|Hagerty, Inc. Warrants,
        each whole warrant entitles the holder thereof to purchase one share of Class
        A common stock at a price of $11.50 per share|N| |N|100|N||HGTY.WS|HGTY+|N\r\nY|HGV|Hilton
        Grand Vacations Inc. Common Stock |N| |N|100|N||HGV|HGV|N\r\nY|HHGC|HHG Capital
        Corporation - Ordinary Shares|Q|S|N|100|N|N||HHGC|N\r\nY|HHGCR|HHG Capital
        Corporation - Rights|Q|S|N|100|N|N||HHGCR|N\r\nY|HHGCU|HHG Capital Corporation
        - Units|Q|S|N|100|N|N||HHGCU|N\r\nY|HHGCW|HHG Capital Corporation - Warrant|Q|S|N|100|N|N||HHGCW|N\r\nY|HHH|Howard
        Hughes Holdings Inc. Common Stock|N| |N|100|N||HHH|HHH|N\r\nY|HHS|Harte Hanks,
        Inc. - Common Stock|Q|G|N|100|N|N||HHS|N\r\nY|HI|Hillenbrand Inc Common Stock|N|
        |N|100|N||HI|HI|N\r\nY|HIBB|Hibbett, Inc. - Common Stock|Q|Q|N|100|N|N||HIBB|N\r\nY|HIBL|Direxion
        Daily S&P 500 High Beta Bull 3X Shares|P| |Y|100|N||HIBL|HIBL|N\r\nY|HIBS|Direxion
        Daily S&P 500 High Beta Bear 3X Shares|P| |Y|100|N||HIBS|HIBS|N\r\nY|HIDE|Alpha
        Architect High Inflation and Deflation ETF|Q|G|Y|100|N|N||HIDE|N\r\nY|HIDV|AB
        Active ETFs, Inc. AB US High Dividend ETF|P| |Y|100|N||HIDV|HIDV|N\r\nY|HIE|Miller/Howard
        High Income Equity Fund Common Shares of Beneficial Interest|N| |N|100|N||HIE|HIE|N\r\nY|HIFS|Hingham
        Institution for Savings - Common Stock|Q|G|N|100|N|N||HIFS|N\r\nY|HIG|Hartford
        Financial Services Group, Inc. (The) Common Stock|N| |N|100|N||HIG|HIG|N\r\nY|HIG$G|Hartford
        Financial Services Group, Inc. (The) Depositary Shares each representing a
        1/1,000th interest in a share of 6.000% Non-Cumulative Preferred Stock, Series
        G, $0.01 par value|N| |N|100|N||HIGpG|HIG-G|N\r\nY|HIGH|Simplify Exchange
        Traded Funds Simplify Enhanced Income ETF|P| |Y|100|N||HIGH|HIGH|N\r\nY|HIHO|Highway
        Holdings Limited - Common Stock|Q|S|N|100|N|N||HIHO|N\r\nY|HII|Huntington
        Ingalls Industries, Inc. Common Stock|N| |N|100|N||HII|HII|N\r\nY|HIMS|Hims
        & Hers Health, Inc. Class A Common Stock|N| |N|100|N||HIMS|HIMS|N\r\nY|HIMX|Himax
        Technologies, Inc. - American depositary shares, each of which represents
        two ordinary shares.|Q|Q|N|100|N|N||HIMX|N\r\nY|HIO|Western Asset High Income
        Opportunity Fund, Inc. Common Stock|N| |N|100|N||HIO|HIO|N\r\nY|HIPO|Hippo
        Holdings Inc. Common Stock|N| |N|100|N||HIPO|HIPO|N\r\nY|HIPO.W|Hippo Holdings
        Inc. Warrants|N| |N|100|N||HIPO.WS|HIPO+|N\r\nY|HIPS|GraniteShares HIPS US
        High Income ETF|P| |Y|100|N||HIPS|HIPS|N\r\nY|HISF|First Trust High Income
        Strategic Focus ETF|Q|G|Y|100|N|N||HISF|N\r\nY|HITI|High Tide Inc. - Common
        Shares|Q|S|N|100|N|N||HITI|N\r\nY|HIVE|HIVE Digital Technologies Ltd - Common
        Shares|Q|S|N|100|N|N||HIVE|N\r\nY|HIW|Highwoods Properties, Inc. Common Stock|N|
        |N|100|N||HIW|HIW|N\r\nY|HIX|Western Asset High Income Fund II Inc. Common
        Stock|N| |N|100|N||HIX|HIX|N\r\nY|HIYS|Invesco Actively Managed Exchange-Traded
        Fund Trus Invesco High Yield Select ETF|Z| |Y|100|N||HIYS|HIYS|N\r\nY|HJAN|Innovator
        ETFs Trust Innovator Premium Income 9 Buffer ETF - January|Z| |Y|100|N||HJAN|HJAN|N\r\nY|HJEN|Direxion
        Hydrogen ETF|P| |Y|100|N||HJEN|HJEN|N\r\nY|HKD|AMTD Digital Inc. American
        Depositary Shares (every five of which represent two Class A Ordinary Shares)|N|
        |N|100|N||HKD|HKD|N\r\nY|HKIT|Hitek Global Inc. - Class A Ordinary Share|Q|S|N|100|N|N||HKIT|N\r\nY|HKND|Humankind
        US Stock ETF|P| |Y|100|N||HKND|HKND|N\r\nY|HL|Hecla Mining Company Common
        Stock|N| |N|100|N||HL|HL|N\r\nY|HL$B|Hecla Mining Company Preferred Stock|N|
        |N|100|N||HLpB|HL-B|N\r\nY|HLAL|Wahed FTSE USA Shariah ETF|Q|G|Y|100|N|N||HLAL|N\r\nY|HLF|Herbalife
        Ltd. Common Shares|N| |N|100|N||HLF|HLF|N\r\nY|HLGE|Hartford Longevity Economy
        ETF|P| |Y|100|N||HLGE|HLGE|N\r\nY|HLI|Houlihan Lokey, Inc. Class A Common
        Stock|N| |N|100|N||HLI|HLI|N\r\nY|HLIO|Helios Technologies, Inc. Common Stock|N|
        |N|100|N||HLIO|HLIO|N\r\nY|HLIT|Harmonic Inc. - Common Stock|Q|Q|N|100|N|N||HLIT|N\r\nY|HLLY|Holley
        Inc. Common Stock|N| |N|100|N||HLLY|HLLY|N\r\nY|HLLY.W|Holley Inc. Warrants|N|
        |N|100|N||HLLY.WS|HLLY+|N\r\nY|HLMN|Hillman Solutions Corp. - Common Stock|Q|G|N|100|N|N||HLMN|N\r\nY|HLN|Haleon
        plc American Depositary Shares (Each representing two Ordinary Shares)|N|
        |N|100|N||HLN|HLN|N\r\nY|HLNE|Hamilton Lane Incorporated - Class A Common
        Stock|Q|Q|N|100|N|N||HLNE|N\r\nY|HLP|Hongli Group Inc. - Ordinary Shares|Q|S|N|100|N|N||HLP|N\r\nY|HLT|Hilton
        Worldwide Holdings Inc. Common Stock |N| |N|100|N||HLT|HLT|N\r\nY|HLVX|HilleVax,
        Inc. - Common Stock|Q|Q|N|100|N|N||HLVX|N\r\nY|HLX|Helix Energy Solutions
        Group, Inc. Common Stock|N| |N|100|N||HLX|HLX|N\r\nY|HLXB|Helix Acquisition
        Corp. II - Class A Ordinary Shares|Q|G|N|100|N|N||HLXB|N\r\nY|HMC|Honda Motor
        Company, Ltd. Common Stock|N| |N|100|N||HMC|HMC|N\r\nY|HMN|Horace Mann Educators
        Corporation Common Stock|N| |N|100|N||HMN|HMN|N\r\nY|HMNF|HMN Financial, Inc.
        - Common Stock|Q|G|N|100|N|N||HMNF|N\r\nY|HMOP|Hartford Municipal Opportunities
        ETF|P| |Y|100|N||HMOP|HMOP|N\r\nY|HMST|HomeStreet, Inc. - Common Stock|Q|Q|N|100|N|N||HMST|N\r\nY|HMY|Harmony
        Gold Mining Company Limited|N| |N|100|N||HMY|HMY|N\r\nY|HNDL|Strategy Shares
        Nasdaq 7HANDL Index ETF|Q|G|Y|100|N|N||HNDL|N\r\nY|HNI|HNI Corporation Common
        Stock|N| |N|100|N||HNI|HNI|N\r\nY|HNNA|Hennessy Advisors, Inc. - Common Stock|Q|G|N|100|N|N||HNNA|N\r\nY|HNNAZ|Hennessy
        Advisors, Inc. - 4.875% Notes due 2026|Q|G|N|100|N|N||HNNAZ|N\r\nY|HNRA|HNR
        Acquisition Corp Class A Common Stock|A| |N|100|N||HNRA|HNRA|N\r\nY|HNRA.W|HNR
        Acquisition Corp Warrants, each whole warrant exercisable for three quarters
        of one share of Common Stock at an exercise price of $11.50 per whole share|A|
        |N|100|N||HNRA.WS|HNRA+|N\r\nY|HNRG|Hallador Energy Company - Common Stock|Q|S|N|100|N|N||HNRG|N\r\nY|HNST|The
        Honest Company, Inc. - Common Stock|Q|Q|N|100|N|N||HNST|N\r\nY|HNVR|Hanover
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||HNVR|N\r\nY|HNW|Pioneer Diversified
        High Income Fund, Inc.|A| |N|100|N||HNW|HNW|N\r\nY|HOCT|Innovator ETFs Trust
        Innovator Premium Income 9 Buffer ETF - October|Z| |Y|100|N||HOCT|HOCT|N\r\nY|HODL|VanEck
        Bitcoin Trust Common Shares of Beneficial Interest|Z| |Y|100|N||HODL|HODL|N\r\nY|HOFT|Hooker
        Furnishings Corporation - Common Stock|Q|Q|N|100|N|N||HOFT|N\r\nY|HOFV|Hall
        of Fame Resort & Entertainment Company - Common Stock|Q|S|N|100|N|N||HOFV|N\r\nY|HOFVW|Hall
        of Fame Resort & Entertainment Company - Warrant|Q|S|N|100|N|N||HOFVW|N\r\nY|HOG|Harley-Davidson,
        Inc. Common Stock|N| |N|100|N||HOG|HOG|N\r\nY|HOLI|Hollysys Automation Technologies,
        Ltd. - Common Stock|Q|Q|N|100|N|N||HOLI|N\r\nY|HOLO|MicroCloud Hologram Inc.
        - Ordinary Shares|Q|S|N|100|N|N||HOLO|N\r\nY|HOLOW|MicroCloud Hologram Inc.
        - Warrant|Q|S|N|100|N|N||HOLOW|N\r\nY|HOLX|Hologic, Inc. - Common Stock|Q|Q|N|100|N|N||HOLX|N\r\nY|HOMB|Home
        BancShares, Inc. Common Stock|N| |N|100|N||HOMB|HOMB|N\r\nY|HOMZ|Hoya Capital
        Housing ETF|P| |Y|100|N||HOMZ|HOMZ|N\r\nY|HON|Honeywell International Inc.
        - Common Stock|Q|Q|N|100|N|N||HON|N\r\nY|HONE|HarborOne Bancorp, Inc. - Common
        Stock|Q|Q|N|100|N|N||HONE|N\r\nY|HOOD|Robinhood Markets, Inc. - Class A Common
        Stock|Q|Q|N|100|N|N||HOOD|N\r\nY|HOOK|HOOKIPA Pharma Inc. - Common Stock|Q|S|N|100|N|D||HOOK|N\r\nY|HOPE|Hope
        Bancorp, Inc. - Common Stock|Q|Q|N|100|N|N||HOPE|N\r\nY|HOTH|Hoth Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||HOTH|N\r\nY|HOUR|Hour Loop, Inc. - common
        stock|Q|S|N|100|N|N||HOUR|N\r\nY|HOUS|Anywhere Real Estate Inc. Common Stock,|N|
        |N|100|N||HOUS|HOUS|N\r\nY|HOV|Hovnanian Enterprises, Inc. Class A Common
        Stock|N| |N|100|N||HOV|HOV|N\r\nY|HOVNP|Hovnanian Enterprises Inc - Depositary
        Share representing 1/1000th of 7.625% Series A Preferred Stock|Q|G|N|100|N|N||HOVNP|N\r\nY|HOVR|New
        Horizon Aircraft Ltd. - Class A Ordinary Shares|Q|S|N|100|N|N||HOVR|N\r\nY|HOVRW|New
        Horizon Aircraft Ltd. - Warrant|Q|S|N|100|N|N||HOVRW|N\r\nY|HOWL|Werewolf
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||HOWL|N\r\nY|HP|Helmerich
        & Payne, Inc. Common Stock|N| |N|100|N||HP|HP|N\r\nY|HPCO|Hempacco Co., Inc.
        - Common Stock|Q|S|N|100|N|H||HPCO|N\r\nY|HPE|Hewlett Packard Enterprise Company
        Common Stock|N| |N|100|N||HPE|HPE|N\r\nY|HPF|John Hancock Pfd Income Fund
        II Pfd Income Fund II|N| |N|100|N||HPF|HPF|N\r\nY|HPH|Highest Performances
        Holdings Inc. - American Depository Shares|Q|G|N|100|N|N||HPH|N\r\nY|HPI|John
        Hancock Preferred Income Fund Common Shares of Beneficial Interest|N| |N|100|N||HPI|HPI|N\r\nY|HPK|HighPeak
        Energy, Inc. - Common Stock|Q|G|N|100|N|N||HPK|N\r\nY|HPKEW|HighPeak Energy,
        Inc. - Warrant|Q|G|N|100|N|N||HPKEW|N\r\nY|HPP|Hudson Pacific Properties,
        Inc. Common Stock|N| |N|100|N||HPP|HPP|N\r\nY|HPP$C|Hudson Pacific Properties,
        Inc. 4.750% Series C Cumulative Redeemable Preferred Stock|N| |N|100|N||HPPpC|HPP-C|N\r\nY|HPQ|HP
        Inc. Common Stock|N| |N|100|N||HPQ|HPQ|N\r\nY|HPS|John Hancock Preferred Income
        Fund III Preferred Income Fund III|N| |N|100|N||HPS|HPS|N\r\nY|HQGO|Hartford
        US Quality Growth ETF|Q|G|Y|100|N|N||HQGO|N\r\nY|HQH|abrdn Healthcare Investors
        Shares of Beneficial Interest|N| |N|100|N||HQH|HQH|N\r\nY|HQI|HireQuest, Inc.
        - Common Stock|Q|S|N|100|N|N||HQI|N\r\nY|HQL|abrdn Life Sciences Investors
        Shares of Beneficial Interest|N| |N|100|N||HQL|HQL|N\r\nY|HQY|HealthEquity,
        Inc. - Common Stock|Q|Q|N|100|N|N||HQY|N\r\nY|HR|Healthcare Realty Trust Incorporated
        Common Stock|N| |N|100|N||HR|HR|N\r\nY|HRB|H&R Block, Inc. Common Stock|N|
        |N|100|N||HRB|HRB|N\r\nY|HRI|Herc Holdings Inc. Common Stock |N| |N|100|N||HRI|HRI|N\r\nY|HRL|Hormel
        Foods Corporation Common Stock|N| |N|100|N||HRL|HRL|N\r\nY|HRMY|Harmony Biosciences
        Holdings, Inc. - Common Stock|Q|G|N|100|N|N||HRMY|N\r\nY|HROW|Harrow, Inc.
        - Common Stock|Q|G|N|100|N|N||HROW|N\r\nY|HROWL|Harrow, Inc. - 8.625% senior
        notes due 2026|Q|G|N|100|N|N||HROWL|N\r\nY|HROWM|Harrow, Inc. - 11.875% Senior
        Notes due 2027|Q|G|N|100|N|N||HROWM|N\r\nY|HRT|HireRight Holdings Corporation
        Common Stock|N| |N|100|N||HRT|HRT|N\r\nY|HRTG|Heritage Insurance Holdings,
        Inc. Common Stock|N| |N|100|N||HRTG|HRTG|N\r\nY|HRTS|Tema Obesity & Cardiometabolic
        ETF|Q|G|Y|100|N|N||HRTS|N\r\nY|HRTX|Heron Therapeutics, Inc.   - Common Stock|Q|S|N|100|N|N||HRTX|N\r\nY|HRYU|Hanryu
        Holdings, Inc. - Common Stock|Q|S|N|100|N|H||HRYU|N\r\nY|HRZN|Horizon Technology
        Finance Corporation - Common Stock|Q|Q|N|100|N|N||HRZN|N\r\nY|HSAI|Hesai Group
        - American Depositary Share, each ADS represents one Class B ordinary share|Q|Q|N|100|N|N||HSAI|N\r\nY|HSBC|HSBC
        Holdings, plc. Common Stock|N| |N|100|N||HSBC|HSBC|N\r\nY|HSCS|Heart Test
        Laboratories, Inc. - Common Stock|Q|S|N|100|N|N||HSCS|N\r\nY|HSCSW|Heart Test
        Laboratories, Inc. - Warrant|Q|S|N|100|N|N||HSCSW|N\r\nY|HSCZ|iShares Currency
        Hedged MSCI EAFE Small-Cap ETF|P| |Y|100|N||HSCZ|HSCZ|N\r\nY|HSDT|Helius Medical
        Technologies, Inc. - Class A Common Stock|Q|S|N|100|N|N||HSDT|N\r\nY|HSHP|Himalaya
        Shipping Ltd. Common Shares|N| |N|100|N||HSHP|HSHP|N\r\nY|HSIC|Henry Schein,
        Inc. - Common Stock|Q|Q|N|100|N|N||HSIC|N\r\nY|HSII|Heidrick & Struggles International,
        Inc. - Common Stock|Q|Q|N|100|N|N||HSII|N\r\nY|HSMV|First Trust Horizon Managed
        Volatility Small/Mid ETF|P| |Y|100|N||HSMV|HSMV|N\r\nY|HSON|Hudson Global,
        Inc. - Common Stock|Q|Q|N|100|N|N||HSON|N\r\nY|HSPO|Horizon Space Acquisition
        I Corp. - Ordinary Shares|Q|G|N|100|N|N||HSPO|N\r\nY|HSPOR|Horizon Space Acquisition
        I Corp. - Right|Q|G|N|100|N|N||HSPOR|N\r\nY|HSPOU|Horizon Space Acquisition
        I Corp. - Unit|Q|G|N|100|N|N||HSPOU|N\r\nY|HSPOW|Horizon Space Acquisition
        I Corp. - Warrant|Q|G|N|100|N|N||HSPOW|N\r\nY|HSRT|Hartford AAA CLO ETF|Z|
        |Y|100|N||HSRT|HSRT|N\r\nY|HST|Host Hotels & Resorts, Inc. - Common Stock|Q|Q|N|100|N|N||HST|N\r\nY|HSTM|HealthStream,
        Inc. - Common Stock|Q|Q|N|100|N|N||HSTM|N\r\nY|HSUN|Hartford Sustainable Income
        ETF|Z| |Y|100|N||HSUN|HSUN|N\r\nY|HSY|The Hershey Company Common Stock|N|
        |N|100|N||HSY|HSY|N\r\nY|HTAB|Hartford Schroders Tax-Aware Bond ETF|P| |Y|100|N||HTAB|HTAB|N\r\nY|HTBI|HomeTrust
        Bancshares, Inc. - Common Stock|Q|Q|N|100|N|N||HTBI|N\r\nY|HTBK|Heritage Commerce
        Corp - Common Stock|Q|Q|N|100|N|N||HTBK|N\r\nY|HTCR|Heartcore Enterprises,
        Inc. - Common Stock|Q|S|N|100|N|D||HTCR|N\r\nY|HTD|John Hancock Tax Advantaged
        Dividend Income Fund Common Shares of Beneficial Interest|N| |N|100|N||HTD|HTD|N\r\nY|HTEC|Robo
        Global Healthcare Technology and Innovation ETF|P| |Y|100|N||HTEC|HTEC|N\r\nY|HTFB|Horizon
        Technology Finance Corporation 4.875% Notes due 2026|N| |N|100|N||HTFB|HTFB|N\r\nY|HTFC|Horizon
        Technology Finance Corporation 6.25% Notes due 2027|N| |N|100|N||HTFC|HTFC|N\r\nY|HTGC|Hercules
        Capital, Inc. Common Stock|N| |N|100|N||HTGC|HTGC|N\r\nY|HTH|Hilltop Holdings
        Inc.|N| |N|100|N||HTH|HTH|N\r\nY|HTHT|H World Group Limited - American Depositary
        Shares|Q|Q|N|100|N|N||HTHT|N\r\nY|HTIA|Healthcare Trust, Inc. - 7.375% Series
        A Cumulative Redeemable Perpetual Preferred Stock|Q|G|N|100|N|N||HTIA|N\r\nY|HTIBP|Healthcare
        Trust, Inc. - 7.125% Series B Cumulative Redeemable Perpetual Preferred Stock|Q|G|N|100|N|N||HTIBP|N\r\nY|HTLD|Heartland
        Express, Inc. - Common Stock|Q|Q|N|100|N|N||HTLD|N\r\nY|HTLF|Heartland Financial
        USA, Inc. - Common Stock|Q|Q|N|100|N|N||HTLF|N\r\nY|HTLFP|Heartland Financial
        USA, Inc. - Depositary Shares, each representing a 1/400th ownership interest
        in a share of 7.00% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock,
        Series E|Q|Q|N|100|N|N||HTLFP|N\r\nY|HTOO|Fusion Fuel Green PLC - Ordinary
        Shares|Q|G|N|100|N|D||HTOO|N\r\nY|HTOOW|Fusion Fuel Green PLC - Warrant|Q|G|N|100|N|D||HTOOW|N\r\nY|HTRB|Hartford
        Total Return Bond ETF|P| |Y|100|N||HTRB|HTRB|N\r\nY|HTUS|Capitol Series Trust
        Hull Tactical US ETF|P| |Y|100|N||HTUS|HTUS|N\r\nY|HTZ|Hertz Global Holdings,
        Inc - Common Stock|Q|Q|N|100|N|N||HTZ|N\r\nY|HTZWW|Hertz Global Holdings,
        Inc - Warrant|Q|Q|N|100|N|N||HTZWW|N\r\nY|HUBB|Hubbell Inc Common Stock|N|
        |N|100|N||HUBB|HUBB|N\r\nY|HUBC|Hub Cyber Security Ltd. - Ordinary Shares|Q|G|N|100|N|H||HUBC|N\r\nY|HUBCW|Hub
        Cyber Security Ltd. - Warrant expiring 2/27/28|Q|S|N|100|N|E||HUBCW|N\r\nY|HUBCZ|Hub
        Cyber Security Ltd. - Warrant|Q|G|N|100|N|H||HUBCZ|N\r\nY|HUBG|Hub Group,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||HUBG|N\r\nY|HUBS|HubSpot, Inc.
        Common Stock|N| |N|100|N||HUBS|HUBS|N\r\nY|HUDA|Hudson Acquisition I Corp.
        - Common Stock|Q|G|N|100|N|H||HUDA|N\r\nY|HUDAR|Hudson Acquisition I Corp.
        - Right|Q|G|N|100|N|H||HUDAR|N\r\nY|HUDAU|Hudson Acquisition I Corp. - Unit|Q|G|N|100|N|H||HUDAU|N\r\nY|HUDI|Huadi
        International Group Co., Ltd. - Ordinary Shares|Q|S|N|100|N|N||HUDI|N\r\nY|HUGE|FSD
        Pharma Inc. - Class B Subordinate Voting Shares|Q|S|N|100|N|D||HUGE|N\r\nY|HUIZ|Huize
        Holding Limited - American Depositary Shares|Q|G|N|100|N|D||HUIZ|N\r\nY|HUM|Humana
        Inc. Common Stock|N| |N|100|N||HUM|HUM|N\r\nY|HUMA|Humacyte, Inc. - Common
        Stock|Q|Q|N|100|N|N||HUMA|N\r\nY|HUMAW|Humacyte, Inc. - Warrant|Q|Q|N|100|N|N||HUMAW|N\r\nY|HUN|Huntsman
        Corporation Common Stock|N| |N|100|N||HUN|HUN|N\r\nY|HURC|Hurco Companies,
        Inc. - Common Stock|Q|Q|N|100|N|N||HURC|N\r\nY|HURN|Huron Consulting Group
        Inc. - Common Stock|Q|Q|N|100|N|N||HURN|N\r\nY|HUSA|Houston American Energy
        Corporation Common Stock|A| |N|100|N||HUSA|HUSA|N\r\nY|HUSV|First Trust Exchange-Traded
        Fund III First Trust Horizon Managed Volatility Domestic ETF|P| |Y|100|N||HUSV|HUSV|N\r\nY|HUT|Hut
        8 Corp. - Common Stock|Q|Q|N|100|N|N||HUT|N\r\nY|HUYA|HUYA Inc. American depositary
        shares, each  representing one Class A ordinary share|N| |N|100|N||HUYA|HUYA|N\r\nY|HVT|Haverty
        Furniture Companies, Inc. Common Stock|N| |N|100|N||HVT|HVT|N\r\nY|HVT.A|Haverty
        Furniture Companies, Inc. Common Stock|N| |N|100|N||HVT.A|HVT.A|N\r\nY|HWBK|Hawthorn
        Bancshares, Inc. - Common Stock|Q|Q|N|100|N|N||HWBK|N\r\nY|HWC|Hancock Whitney
        Corporation - Common Stock|Q|Q|N|100|N|N||HWC|N\r\nY|HWCPZ|Hancock Whitney
        Corporation - 6.25% Subordinated Notes due 2060|Q|Q|N|100|N|N||HWCPZ|N\r\nY|HWH|HWH
        International Inc. - Common Stock|Q|G|N|100|N|D||HWH|N\r\nY|HWKN|Hawkins,
        Inc. - Common Stock|Q|Q|N|100|N|N||HWKN|N\r\nY|HWM|Howmet Aerospace Inc. Common
        Stock|N| |N|100|N||HWM|HWM|N\r\nY|HWM$|Howmet Aerospace Inc. $3.75 Preferred
        Stock|A| |N|100|N||HWMp|HWM-|N\r\nY|HXL|Hexcel Corporation Common Stock|N|
        |N|100|N||HXL|HXL|N\r\nY|HY|Hyster-Yale, Inc. Class A common stock|N| |N|100|N||HY|HY|N\r\nY|HYAC|Haymaker
        Acquisition Corp. 4 Class A Ordinary Shares|N| |N|100|N||HYAC|HYAC|N\r\nY|HYAC.U|Haymaker
        Acquisition Corp. 4 Units, each consisting one Class A Ordinary Share and
        one-half of one redeemable Warrant|N| |N|100|N||HYAC.U|HYAC=|N\r\nY|HYAC.W|Haymaker
        Acquisition Corp. 4 Warrants, each whole warrant exercisable for one Class
        A ordinary share at an exercise price of $11.50 per share|N| |N|100|N||HYAC.WS|HYAC+|N\r\nY|HYB|New
        America High Income Fund, Inc. (The) Common Stock|N| |N|100|N||HYB|HYB|N\r\nY|HYBB|iShares
        BB Rated Corporate Bond ETF|P| |Y|100|N||HYBB|HYBB|N\r\nY|HYBL|SPDR Series
        Trust SPDR Blackstone High Income ETF|Z| |Y|100|N||HYBL|HYBL|N\r\nY|HYD|VanEck
        ETF Trust VanEck High Yield Muni ETF|Z| |Y|100|N||HYD|HYD|N\r\nY|HYDB|iShares
        High Yield Systematic Bond ETF|Z| |Y|100|N||HYDB|HYDB|N\r\nY|HYDR|Global X
        Hydrogen ETF|Q|G|Y|100|N|N||HYDR|N\r\nY|HYDW|Xtrackers Low Beta High Yield
        Bond ETF|P| |Y|100|N||HYDW|HYDW|N\r\nY|HYEM|VanEck Emerging Markets High Yield
        Bond ETF|P| |Y|100|N||HYEM|HYEM|N\r\nY|HYFI|AB Active ETFs, Inc. AB High Yield
        ETF|P| |Y|100|N||HYFI|HYFI|N\r\nY|HYFM|Hydrofarm Holdings Group, Inc. - Common
        Stock|Q|Q|N|100|N|D||HYFM|N\r\nY|HYG|iShares iBoxx $ High Yield Corporate
        Bond ETF|P| |Y|100|N||HYG|HYG|N\r\nY|HYGH|iShares Interest Rate Hedged High
        Yield Bond ETF|P| |Y|100|N||HYGH|HYGH|N\r\nY|HYGI|iShares U.S. ETF Trust iShares
        Inflation Hedged High Yield Bond ETF|P| |Y|100|N||HYGI|HYGI|N\r\nY|HYGV|FlexShares
        High Yield Value-Scored Bond Index Fund|P| |Y|100|N||HYGV|HYGV|N\r\nY|HYGW|iShares
        Trust iShares High Yield Corporate Bond BuyWrite Strategy ETF|Z| |Y|100|N||HYGW|HYGW|N\r\nY|HYHG|ProShares
        High Yield Interest Rate Hedged|Z| |Y|100|N||HYHG|HYHG|N\r\nY|HYI|Western
        Asset High Yield Defined Opportunity Fund Inc. Common Stock|N| |N|100|N||HYI|HYI|N\r\nY|HYIN|WisdomTree
        Alternative Income Fund|Z| |Y|100|N||HYIN|HYIN|N\r\nY|HYKE|ETF Series Solutions
        Vest 2 Year Interest Rate Hedge ETF|Z| |Y|100|N||HYKE|HYKE|N\r\nY|HYLB|Xtrackers
        USD High Yield Corporate Bond ETF|P| |Y|100|N||HYLB|HYLB|N\r\nY|HYLG|Global
        X Funds Global X Health Care Covered Call & Growth ETF|P| |Y|100|N||HYLG|HYLG|N\r\nY|HYLN|Hyliion
        Holdings Corp. Class A Common Stock|N| |N|100|N||HYLN|HYLN|N\r\nY|HYLS|First
        Trust Tactical High Yield ETF|Q|G|Y|100|N|N||HYLS|N\r\nY|HYMB|SPDR Nuveen
        Bloomberg High Yield Municipal Bond ETF|P| |Y|100|N||HYMB|HYMB|N\r\nY|HYMC|Hycroft
        Mining Holding Corporation - Class A Common Stock|Q|S|N|100|N|N||HYMC|N\r\nY|HYMCL|Hycroft
        Mining Holding Corporation - Warrants|Q|S|N|100|N|N||HYMCL|N\r\nY|HYMCW|Hycroft
        Mining Holding Corporation - Warrant|Q|S|N|100|N|N||HYMCW|N\r\nY|HYMU|BlackRock
        High Yield Muni Income Bond ETF|Z| |Y|100|N||HYMU|HYMU|N\r\nY|HYPR|Hyperfine,
        Inc.  - Class A Common Stock|Q|G|N|100|N|D||HYPR|N\r\nY|HYRM|DBX ETF Trust
        Xtrackers Risk Managed USD High Yield Strategy ETF|P| |Y|100|N||HYRM|HYRM|N\r\nY|HYS|PIMCO
        0-5 Year High Yield Corporat Bond Index Exchange-Traded Fund|P| |Y|100|N||HYS|HYS|N\r\nY|HYSA|BondBloxx
        ETF Trust BondBloxx USD High Yield Bond Sector Rotation ETF|P| |Y|100|N||HYSA|HYSA|N\r\nY|HYT|Blackrock
        Corporate High Yield Fund, Inc. Common Stock|N| |N|100|N||HYT|HYT|N\r\nY|HYTR|CP
        High Yield Trend ETF|P| |Y|100|N||HYTR|HYTR|N\r\nY|HYUP|Xtrackers High Beta
        High Yield Bond ETF|P| |Y|100|N||HYUP|HYUP|N\r\nY|HYW|Hywin Holdings Ltd.
        - American Depositary Shares|Q|G|N|100|N|D||HYW|N\r\nY|HYXF|iShares ESG Advanced
        High Yield Corporate Bond ETF|Q|G|Y|100|N|N||HYXF|N\r\nY|HYXU|iShares International
        High Yield Bond ETF|Z| |Y|100|N||HYXU|HYXU|N\r\nY|HYZD|WisdomTree Interest
        Rate Hedged High Yield Bond Fund|Q|G|Y|100|N|N||HYZD|N\r\nY|HYZN|Hyzon Motors
        Inc. - Class A Common Stock|Q|Q|N|100|N|D||HYZN|N\r\nY|HYZNW|Hyzon Motors
        Inc. - Warrant|Q|Q|N|100|N|N||HYZNW|N\r\nY|HZO|MarineMax, Inc.  (FL) Common
        Stock|N| |N|100|N||HZO|HZO|N\r\nY|IAC|IAC Inc. - Common Stock|Q|Q|N|100|N|N||IAC|N\r\nY|IAE|Voya
        Asia Pacific High Dividend Equity Income Fund ING Asia Pacific High Dividend
        Equity Income Fund Common Shares of Beneficial Interest|N| |N|100|N||IAE|IAE|N\r\nY|IAF|abrdn
        Australia Equity Fund, Inc. Common Stock|A| |N|100|N||IAF|IAF|N\r\nY|IAG|Iamgold
        Corporation Ordinary Shares|N| |N|100|N||IAG|IAG|N\r\nY|IAGG|iShares International
        Aggregate Bond Fund|Z| |Y|100|N||IAGG|IAGG|N\r\nY|IAI|iShares U.S. Broker-Dealers
        & Securities Exchanges ETF|P| |Y|100|N||IAI|IAI|N\r\nY|IAK|iShares U.S. Insurance
        ETF|P| |Y|100|N||IAK|IAK|N\r\nY|IAPR|Innovator International Developed Power
        Buffer ETF  April|P| |Y|100|N||IAPR|IAPR|N\r\nY|IART|Integra LifeSciences
        Holdings Corporation - Common Stock|Q|Q|N|100|N|N||IART|N\r\nY|IAS|Integral
        Ad Science Holding Corp. - Common Stock|Q|Q|N|100|N|N||IAS|N\r\nY|IAT|iShares
        U.S. Regional Banks ETF|P| |Y|100|N||IAT|IAT|N\r\nY|IAU|iShares Gold Trust
        Shares of the iShares Gold Trust|P| |Y|100|N||IAU|IAU|N\r\nY|IAUF|iShares
        Gold Strategy ETF|Z| |Y|100|N||IAUF|IAUF|N\r\nY|IAUM|iShares Gold Trust Micro
        Shares|P| |Y|100|N||IAUM|IAUM|N\r\nY|IAUX|i-80 Gold Corp. Common Shares|A|
        |N|100|N||IAUX|IAUX|N\r\nY|IBAC|IB Acquisition Corp. - Common Stock|Q|G|N|100|N|N||IBAC|N\r\nY|IBACR|IB
        Acquisition Corp. - Right|Q|G|N|100|N|N||IBACR|N\r\nY|IBAT|iShares Energy
        Storage & Materials ETF|Q|G|Y|100|N|N||IBAT|N\r\nY|IBB|iShares Biotechnology
        ETF|Q|G|Y|100|N|N||IBB|N\r\nY|IBBQ|Invesco Nasdaq Biotechnology ETF|Q|G|Y|100|N|N||IBBQ|N\r\nY|IBCP|Independent
        Bank Corporation - Common Stock|Q|Q|N|100|N|N||IBCP|N\r\nY|IBD|Inspire Corporate
        Bond ETF|P| |Y|100|N||IBD|IBD|N\r\nY|IBDP|iShares iBonds Dec 2024 Term Corporate
        ETF|P| |Y|100|N||IBDP|IBDP|N\r\nY|IBDQ|iShares iBonds Dec 2025 Term Corporate
        ETF|P| |Y|100|N||IBDQ|IBDQ|N\r\nY|IBDR|iShares iBonds Dec 2026 Term Corporate
        ETF|P| |Y|100|N||IBDR|IBDR|N\r\nY|IBDS|iShares iBonds Dec 2027 Term Corporate
        ETF|P| |Y|100|N||IBDS|IBDS|N\r\nY|IBDT|iShares iBonds Dec 2028 Term Corporate
        ETF|P| |Y|100|N||IBDT|IBDT|N\r\nY|IBDU|iShares iBonds Dec 2029 Term Corporate
        ETF|P| |Y|100|N||IBDU|IBDU|N\r\nY|IBDV|iShares iBonds Dec 2030 Term Corporate
        ETF|P| |Y|100|N||IBDV|IBDV|N\r\nY|IBDW|iShares iBonds Dec 2031 Term Corporate
        ETF|P| |Y|100|N||IBDW|IBDW|N\r\nY|IBDX|iShares Trust iShares iBonds Dec 2032
        Term Corporate ETF|P| |Y|100|N||IBDX|IBDX|N\r\nY|IBDY|iShares Trust iShares
        iBonds Dec 2033 Term Corporate ETF|P| |Y|100|N||IBDY|IBDY|N\r\nY|IBDZ|iShares
        Trust iShares iBonds Dec 2034 Term Corporate ETF|P| |Y|100|N||IBDZ|IBDZ|N\r\nY|IBEX|IBEX
        Limited - Common Share|Q|G|N|100|N|N||IBEX|N\r\nY|IBGA|iShares iBonds Dec
        2044 Term Treasury ETF|Q|G|Y|100|N|N||IBGA|N\r\nY|IBGK|iShares iBonds Dec
        2054 Term Treasury ETF|Q|G|Y|100|N|N||IBGK|N\r\nY|IBHD|iShares iBonds 2024
        Term High Yield and Income ETF|Z| |Y|100|N||IBHD|IBHD|N\r\nY|IBHE|iShares
        iBonds 2025 Term High Yield and Income ETF|Z| |Y|100|N||IBHE|IBHE|N\r\nY|IBHF|iShares
        iBonds 2026 Term High Yield and Income ETF|Z| |Y|100|N||IBHF|IBHF|N\r\nY|IBHG|iShares
        iBonds 2027 Term High Yield and Income ETF|Z| |Y|100|N||IBHG|IBHG|N\r\nY|IBHH|iShares
        Trust iShares iBonds 2028 Term High Yield and Income ETF|Z| |Y|100|N||IBHH|IBHH|N\r\nY|IBHI|iShares
        Trust iShares iBonds 2029 Term High Yield and Income ETF|Z| |Y|100|N||IBHI|IBHI|N\r\nY|IBHJ|iShares
        Trust iShares iBonds 2030 Term High Yield and Income ETF|Z| |Y|100|N||IBHJ|IBHJ|N\r\nY|IBHK|iShares
        Trust iShares iBonds 2031 Term High Yield and Income ETF|Z| |Y|100|N||IBHK|IBHK|N\r\nY|IBIA|iShares
        Trust iShares iBonds Oct 2024 Term TIPS ETF|P| |Y|100|N||IBIA|IBIA|N\r\nY|IBIB|iShares
        Trust iShares iBonds Oct 2025 Term TIPS ETF|P| |Y|100|N||IBIB|IBIB|N\r\nY|IBIC|iShares
        Trust iShares iBonds Oct 2026 Term TIPS ETF|P| |Y|100|N||IBIC|IBIC|N\r\nY|IBID|iShares
        Trust iShares iBonds Oct 2027 Term TIPS ETF|P| |Y|100|N||IBID|IBID|N\r\nY|IBIE|iShares
        Trust iShares iBonds Oct 2028 Term TIPS ETF|P| |Y|100|N||IBIE|IBIE|N\r\nY|IBIF|iShares
        Trust iShares iBonds Oct 2029 Term TIPS ETF|P| |Y|100|N||IBIF|IBIF|N\r\nY|IBIG|iShares
        Trust iShares iBonds Oct 2030 Term TIPS ETF|P| |Y|100|N||IBIG|IBIG|N\r\nY|IBIH|iShares
        Trust iShares iBonds Oct 2031 Term TIPS ETF|P| |Y|100|N||IBIH|IBIH|N\r\nY|IBII|iShares
        Trust iShares iBonds Oct 2032 Term TIPS ETF|P| |Y|100|N||IBII|IBII|N\r\nY|IBIJ|iShares
        Trust iShares iBonds Oct 2033 Term TIPS ETF|P| |Y|100|N||IBIJ|IBIJ|N\r\nY|IBIK|iShares
        Trust iShares iBonds Oct 2034 Term TIPS ETF|P| |Y|100|N||IBIK|IBIK|N\r\nY|IBIO|iBio,
        Inc. Common Stock|A| |N|100|N||IBIO|IBIO|N\r\nY|IBIT|iShares Bitcoin Trust|Q|G|Y|100|N|N||IBIT|N\r\nY|IBKR|Interactive
        Brokers Group, Inc. - Class A Common Stock|Q|Q|N|100|N|N||IBKR|N\r\nY|IBLC|iShares
        Trust iShares Blockchain and Tech ETF|P| |Y|100|N||IBLC|IBLC|N\r\nY|IBM|International
        Business Machines Corporation Common Stock|N| |N|100|N||IBM|IBM|N\r\nY|IBMM|iShares
        iBonds Dec 2024 Term Muni Bond ETF|Z| |Y|100|N||IBMM|IBMM|N\r\nY|IBMN|iShares
        iBonds Dec 2025 Term Muni Bond ETF|Z| |Y|100|N||IBMN|IBMN|N\r\nY|IBMO|iShares
        iBonds Dec 2026 Term Muni Bond ETF|Z| |Y|100|N||IBMO|IBMO|N\r\nY|IBMP|iShares
        iBonds Dec 2027 Term Muni Bond ETF|Z| |Y|100|N||IBMP|IBMP|N\r\nY|IBMQ|iShares
        iBonds Dec 2028 Term Muni Bond ETF|Z| |Y|100|N||IBMQ|IBMQ|N\r\nY|IBMR|iShares
        Trust iShares iBonds Dec 2029 Term Muni Bond ETF|Z| |Y|100|N||IBMR|IBMR|N\r\nY|IBMS|iShares
        Trust iShares iBonds Dec 2030 Term Muni Bond ETF|Z| |Y|100|N||IBMS|IBMS|N\r\nY|IBN|ICICI
        Bank Limited Common Stock|N| |N|100|N||IBN|IBN|N\r\nY|IBND|SPDR Bloomberg
        International Corporate Bond ETF|P| |Y|100|N||IBND|IBND|N\r\nY|IBOC|International
        Bancshares Corporation - Common Stock|Q|Q|N|100|N|N||IBOC|N\r\nY|IBOT|VanEck
        Robotics ETF|Q|G|Y|100|N|N||IBOT|N\r\nY|IBP|Installed Building Products, Inc.
        Common Stock|N| |N|100|N||IBP|IBP|N\r\nY|IBRN|iShares Trust iShares Neuroscience
        and Healthcare ETF|P| |Y|100|N||IBRN|IBRN|N\r\nY|IBRX|ImmunityBio, Inc. -
        Common Stock|Q|Q|N|100|N|N||IBRX|N\r\nY|IBTA|Ibotta, Inc. Class A Common Stock|N|
        |N|100|N||IBTA|IBTA|N\r\nY|IBTE|iShares iBonds Dec 2024 Term Treasury ETF|Q|G|Y|100|N|N||IBTE|N\r\nY|IBTF|iShares
        iBonds Dec 2025 Term Treasury ETF|Q|G|Y|100|N|N||IBTF|N\r\nY|IBTG|iShares
        iBonds Dec 2026 Term Treasury ETF|Q|G|Y|100|N|N||IBTG|N\r\nY|IBTH|iShares
        iBonds Dec 2027 Term Treasury ETF|Q|G|Y|100|N|N||IBTH|N\r\nY|IBTI|iShares
        iBonds Dec 2028 Term Treasury ETF|Q|G|Y|100|N|N||IBTI|N\r\nY|IBTJ|iShares
        iBonds Dec 2029 Term Treasury ETF|Q|G|Y|100|N|N||IBTJ|N\r\nY|IBTK|iShares
        iBonds Dec 2030 Term Treasury ETF|Q|G|Y|100|N|N||IBTK|N\r\nY|IBTL|iShares
        iBonds Dec 2031 Term Treasury ETF|Q|G|Y|100|N|N||IBTL|N\r\nY|IBTM|iShares
        iBonds Dec 2032 Term Treasury ETF|Q|G|Y|100|N|N||IBTM|N\r\nY|IBTO|iShares
        iBonds Dec 2033 Term Treasury ETF|Q|G|Y|100|N|N||IBTO|N\r\nY|IBTP|iShares
        iBonds Dec 2034 Term Treasury ETF|Q|G|Y|100|N|N||IBTP|N\r\nY|IBTX|Independent
        Bank Group, Inc - Common Stock|Q|Q|N|100|N|N||IBTX|N\r\nY|IBUY|Amplify ETF
        Trust Amplify Online Retail ETF|P| |Y|100|N||IBUY|IBUY|N\r\nY|ICAD|icad inc.
        - Common Stock|Q|S|N|100|N|N||ICAD|N\r\nY|ICAP|Series Portfolios Trust InfraCap
        Equity Income Fund ETF|P| |Y|100|N||ICAP|ICAP|N\r\nY|ICCC|ImmuCell Corporation
        - Common Stock|Q|S|N|100|N|N||ICCC|N\r\nY|ICCH|ICC Holdings, Inc. - Common
        Stock|Q|S|N|100|N|N||ICCH|N\r\nY|ICCM|IceCure Medical Ltd. - Ordinary Shares|Q|S|N|100|N|N||ICCM|N\r\nY|ICCT|iCoreConnect
        Inc. - Common stock|Q|S|N|100|N|D||ICCT|N\r\nY|ICD|Independence Contract Drilling,
        Inc. Common Stock|N| |N|100|N||ICD|ICD|N\r\nY|ICE|Intercontinental Exchange
        Inc. Common Stock|N| |N|100|N||ICE|ICE|N\r\nY|ICF|iShares Cohen & Steers REIT
        ETF|Z| |Y|100|N||ICF|ICF|N\r\nY|ICFI|ICF International, Inc. - Common Stock|Q|Q|N|100|N|N||ICFI|N\r\nY|ICG|Intchains
        Group Limited - American Depositary Shares|Q|S|N|100|N|N||ICG|N\r\nY|ICHR|Ichor
        Holdings - Ordinary Shares|Q|Q|N|100|N|N||ICHR|N\r\nY|ICL|ICL Group Ltd. Ordinary
        Shares|N| |N|100|N||ICL|ICL|N\r\nY|ICLK|iClick Interactive Asia Group Limited
        - American Depositary Shares|Q|G|N|100|N|N||ICLK|N\r\nY|ICLN|iShares Global
        Clean Energy ETF|Q|G|Y|100|N|N||ICLN|N\r\nY|ICLO|Invesco Actively Managed
        Exchange-Traded Fund Trus Invesco AAA CLO Floating Rate Note ETF|Z| |Y|100|N||ICLO|ICLO|N\r\nY|ICLR|ICON
        plc - Ordinary Shares|Q|Q|N|100|N|N||ICLR|N\r\nY|ICMB|Investcorp Credit Management
        BDC, Inc. - Common Stock|Q|Q|N|100|N|N||ICMB|N\r\nY|ICOP|iShares Copper and
        Metals Mining ETF|Q|G|Y|100|N|N||ICOP|N\r\nY|ICOW|Pacer Developed Markets
        International Cash Cows 100 ETF|Z| |Y|100|N||ICOW|ICOW|N\r\nY|ICR$A|InPoint
        Commercial Real Estate Income, Inc. 6.75% Series A Cumulative Redeemable Preferred
        Stock|N| |N|100|N||ICRpA|ICR-A|N\r\nY|ICSH|BlackRock Ultra Short-Term Bond
        ETF|Z| |Y|100|N||ICSH|ICSH|N\r\nY|ICU|SeaStar Medical Holding Corporation
        - Common Stock|Q|S|N|100|N|D||ICU|N\r\nY|ICUCW|SeaStar Medical Holding Corporation
        - Warrant|Q|S|N|100|N|N||ICUCW|N\r\nY|ICUI|ICU Medical, Inc. - Common Stock|Q|Q|N|100|N|N||ICUI|N\r\nY|ICVT|iShares
        Convertible Bond ETF|Z| |Y|100|N||ICVT|ICVT|N\r\nY|IDA|IDACORP, Inc. Common
        Stock|N| |N|100|N||IDA|IDA|N\r\nY|IDAI|T Stamp Inc. - Class A Common Stock|Q|S|N|100|N|D||IDAI|N\r\nY|IDAT|iShares
        Future Cloud 5G and Tech ETF|P| |Y|100|N||IDAT|IDAT|N\r\nY|IDCC|InterDigital,
        Inc. - Common Stock|Q|Q|N|100|N|N||IDCC|N\r\nY|IDE|Voya Infrastructure, Industrials
        and Materials Fund Common Shares of Beneficial Interest|N| |N|100|N||IDE|IDE|N\r\nY|IDEC|Innovator
        ETFs Trust Innovator International Developed Power Buffer ETF  December|P|
        |Y|100|N||IDEC|IDEC|N\r\nY|IDEV|iShares Core MSCI International Developed
        Markets ETF|P| |Y|100|N||IDEV|IDEV|N\r\nY|IDEX|Ideanomics, Inc. - Common Stock|Q|S|N|100|N|E||IDEX|N\r\nY|IDGT|iShares
        U.S. Digital Infrastructure and Real Estate ETF|P| |Y|100|N||IDGT|IDGT|N\r\nY|IDHQ|Invesco
        S&P International Developed Quality ETF|P| |Y|100|N||IDHQ|IDHQ|N\r\nY|IDLV|Invesco
        S&P International Developed Low Volatility ETF|P| |Y|100|N||IDLV|IDLV|N\r\nY|IDMO|Invesco
        S&P International Developed Momentum ETF|P| |Y|100|N||IDMO|IDMO|N\r\nY|IDN|Intellicheck,
        Inc. - Common Stock|Q|G|N|100|N|N||IDN|N\r\nY|IDNA|iShares Genomics Immunology
        and Healthcare ETF|P| |Y|100|N||IDNA|IDNA|N\r\nY|IDOG|ALPS International Sector
        Dividend Dogs ETF|P| |Y|100|N||IDOG|IDOG|N\r\nY|IDR|Idaho Strategic Resources,
        Inc. Common Stock|A| |N|100|N||IDR|IDR|N\r\nY|IDRV|iShares Self-Driving EV
        and Tech ETF|P| |Y|100|N||IDRV|IDRV|N\r\nY|IDT|IDT Corporation Class B Common
        Stock|N| |N|100|N||IDT|IDT|N\r\nY|IDU|iShares U.S. Utilities ETF|P| |Y|100|N||IDU|IDU|N\r\nY|IDUB|Aptus
        International Enhanced Yield ETF|Z| |Y|100|N||IDUB|IDUB|N\r\nY|IDV|iShares
        International Select Dividend ETF|Z| |Y|100|N||IDV|IDV|N\r\nY|IDVO|Amplify
        CWP International Enhanced Dividend Income ETF|P| |Y|100|N||IDVO|IDVO|N\r\nY|IDX|VanEck
        Indonesia Index ETF|P| |Y|100|N||IDX|IDX|N\r\nY|IDXX|IDEXX Laboratories, Inc.
        - Common Stock|Q|Q|N|100|N|N||IDXX|N\r\nY|IDYA|IDEAYA Biosciences, Inc. -
        Common Stock|Q|Q|N|100|N|N||IDYA|N\r\nY|IE|Ivanhoe Electric Inc. Common Stock|A|
        |N|100|N||IE|IE|N\r\nY|IEDI|iShares U.S. Consumer Focused ETF|Z| |Y|100|N||IEDI|IEDI|N\r\nY|IEF|iShares
        7-10 Year Treasury Bond ETF|Q|G|Y|100|N|N||IEF|N\r\nY|IEFA|iShares Core MSCI
        EAFE ETF|Z| |Y|100|N||IEFA|IEFA|N\r\nY|IEI|iShares 3-7 Year Treasury Bond
        ETF|Q|G|Y|100|N|N||IEI|N\r\nY|IEMG|iShares Core MSCI Emerging Markets ETF|P|
        |Y|100|N||IEMG|IEMG|N\r\nY|IEO|iShares U.S. Oil & Gas Exploration & Production
        ETF|Z| |Y|100|N||IEO|IEO|N\r\nY|IEP|Icahn Enterprises L.P. - Depositary Units
        representing Limited Partner Interests|Q|Q|N|100|N|N||IEP|N\r\nY|IESC|IES
        Holdings, Inc. - Common Stock|Q|G|N|100|N|N||IESC|N\r\nY|IETC|iShares U.S.
        Tech Independence Focused ETF|Z| |Y|100|N||IETC|IETC|N\r\nY|IEUR|iShares Core
        MSCI Europe ETF|P| |Y|100|N||IEUR|IEUR|N\r\nY|IEUS|iShares MSCI Europe Small-Cap
        ETF|Q|G|Y|100|N|N||IEUS|N\r\nY|IEV|iShares Europe ETF|P| |Y|100|N||IEV|IEV|N\r\nY|IEX|IDEX
        Corporation Common Stock|N| |N|100|N||IEX|IEX|N\r\nY|IEZ|iShares U.S. Oil
        Equipment & Services ETF|P| |Y|100|N||IEZ|IEZ|N\r\nY|IFBD|Infobird Co., Ltd
        - Ordinary Shares|Q|S|N|100|N|E||IFBD|N\r\nY|IFEB|Innovator ETFs Trust Innovator
        International Developed Power Buffer ETF  February|P| |Y|100|N||IFEB|IFEB|N\r\nY|IFED|ETRACS
        IFED Invest with the Fed TR Index ETN|P| |Y|100|N||IFED|IFED|N\r\nY|IFF|International
        Flavors & Fragrances, Inc. Common Stock|N| |N|100|N||IFF|IFF|N\r\nY|IFGL|iShares
        International Developed Real Estate ETF|Q|G|Y|100|N|N||IFGL|N\r\nY|IFIN|InFinT
        Acquisition Corporation Class A Ordinary Shares|N| |N|100|N||IFIN|IFIN|N\r\nY|IFIN.U|InFinT
        Acquisition Corporation Units,each consisting of one Class A ordinary share
        and one-half of one redeemable warrant|N| |N|100|N||IFIN.U|IFIN=|N\r\nY|IFN|India
        Fund, Inc. (The) Common Stock|N| |N|100|N||IFN|IFN|N\r\nY|IFRA|iShares U.S.
        Infrastructure ETF|Z| |Y|100|N||IFRA|IFRA|N\r\nY|IFRX|InflaRx N.V. - Common
        Stock|Q|Q|N|100|N|N||IFRX|N\r\nY|IFS|Intercorp Financial Services Inc. Common
        Shares|N| |N|100|N||IFS|IFS|N\r\nY|IFV|First Trust Dorsey Wright International
        Focus 5 ETF|Q|G|Y|100|N|N||IFV|N\r\nY|IG|Principal Investment Grade Corporate
        Active ETF|P| |Y|100|N||IG|IG|N\r\nY|IGA|Voya Global Advantage and Premium
        Opportunity Fund Common Shares of Beneficial Interest|N| |N|100|N||IGA|IGA|N\r\nY|IGBH|iShares
        Interest Rate Hedged Long-Term Corporate Bond ETF|P| |Y|100|N||IGBH|IGBH|N\r\nY|IGC|IGC
        Pharma, Inc. Common Stock|A| |N|100|N||IGC|IGC|N\r\nY|IGD|Voya Global Equity
        Dividend and Premium Opportunity Fund|N| |N|100|N||IGD|IGD|N\r\nY|IGE|iShares
        North American Natural Resources ETF|Z| |Y|100|N||IGE|IGE|N\r\nY|IGEB|iShares
        Investment Grade Systematic Bond ETF|Z| |Y|100|N||IGEB|IGEB|N\r\nY|IGF|iShares
        Global Infrastructure ETF|Q|G|Y|100|N|N||IGF|N\r\nY|IGHG|ProShares Investment
        Grade-Interest Rate Hedged|Z| |Y|100|N||IGHG|IGHG|N\r\nY|IGI|Western Asset
        Investment Grade Defined Opportunity Trust Inc. Common Stock|N| |N|100|N||IGI|IGI|N\r\nY|IGIB|iShares
        5-10 Year Investment Grade Corporate Bond ETF|Q|G|Y|100|N|N||IGIB|N\r\nY|IGIC|International
        General Insurance Holdings Ltd. - Ordinary Shares|Q|S|N|100|N|N||IGIC|N\r\nY|IGLB|iShares
        10  Year Investment Grade Corporate Bond ETF|P| |Y|100|N||IGLB|IGLB|N\r\nY|IGLD|FT
        Vest Gold Strategy Target Income ETF|Z| |Y|100|N||IGLD|IGLD|N\r\nY|IGM|iShares
        Expanded Tech Sector ETF|P| |Y|100|N||IGM|IGM|N\r\nY|IGMS|IGM Biosciences,
        Inc. - Common Stock|Q|Q|N|100|N|N||IGMS|N\r\nY|IGOV|iShares International
        Treasury Bond ETF|Q|G|Y|100|N|N||IGOV|N\r\nY|IGPT|Invesco AI and Next Gen
        Software ETF|P| |Y|100|N||IGPT|IGPT|N\r\nY|IGR|CBRE Global Real Estate Income
        Fund Common Shares of Beneficial Interest|N| |N|100|N||IGR|IGR|N\r\nY|IGRO|iShares
        International Dividend Growth ETF|Z| |Y|100|N||IGRO|IGRO|N\r\nY|IGSB|iShares
        1-5 Year Investment Grade Corporate Bond ETF|Q|G|Y|100|N|N||IGSB|N\r\nY|IGT|International
        Game Technology Ordinary Shares|N| |N|100|N||IGT|IGT|N\r\nY|IGTA|Inception
        Growth Acquisition Limited - Common Stock|Q|S|N|100|N|N||IGTA|N\r\nY|IGTAR|Inception
        Growth Acquisition Limited - Rights|Q|S|N|100|N|N||IGTAR|N\r\nY|IGTAU|Inception
        Growth Acquisition Limited - Units|Q|S|N|100|N|N||IGTAU|N\r\nY|IGTAW|Inception
        Growth Acquisition Limited - Warrants|Q|S|N|100|N|N||IGTAW|N\r\nY|IGTR|Innovator
        ETFs Trust Innovator Gradient Tactical Rotation Strategy ETF|P| |Y|100|N||IGTR|IGTR|N\r\nY|IGV|iShares
        Expanded Tech-Software Sector ETF|Z| |Y|100|N||IGV|IGV|N\r\nY|IGZ|IGZ (Listing
        Market NYSE Arca Network B F) Common Stock|P| |N|100|Y||IGZ|IGZ|N\r\nY|IH|iHuman
        Inc. American depositary shares, each representing five Class A ordinary shares|N|
        |N|100|N||IH|IH|N\r\nY|IHAK|iShares Cybersecurity and Tech ETF|P| |Y|100|N||IHAK|IHAK|N\r\nY|IHD|Voya
        Emerging Markets High Income Dividend Equity Fund Common Shares|N| |N|100|N||IHD|IHD|N\r\nY|IHDG|WisdomTree
        International Hedged Quality Dividend Growth Fund|P| |Y|100|N||IHDG|IHDG|N\r\nY|IHE|iShares
        U.S. Pharmaceutical ETF|P| |Y|100|N||IHE|IHE|N\r\nY|IHF|iShares U.S. Health
        Care Providers ETF|P| |Y|100|N||IHF|IHF|N\r\nY|IHG|Intercontinental Hotels
        Group American Depositary Shares (Each representing one Ordinary Share)|N|
        |N|100|N||IHG|IHG|N\r\nY|IHI|iShares U.S. Medical Devices ETF|P| |Y|100|N||IHI|IHI|N\r\nY|IHRT|iHeartMedia,
        Inc. - Class A Common Stock|Q|Q|N|100|N|N||IHRT|N\r\nY|IHS|IHS Holding Limited
        Ordinary Shares|N| |N|100|N||IHS|IHS|N\r\nY|IHT|InnSuites Hospitality Trust
        Shares of Beneficial Interest|A| |N|100|N||IHT|IHT|N\r\nY|IHTA|Invesco High
        Income 2024 Target Term Fund Common Shares of Beneficial Interest, No par
        value per share|N| |N|100|N||IHTA|IHTA|N\r\nY|IHY|VanEck International High
        Yield Bond ETF|P| |Y|100|N||IHY|IHY|N\r\nY|IHYF|Invesco High Yield Bond Factor
        ETF|Q|G|Y|100|N|N||IHYF|N\r\nY|IIF|Morgan Stanley India Investment Fund, Inc.
        Common Stock|N| |N|100|N||IIF|IIF|N\r\nY|IIGD|Invesco Investment Grade Defensive
        ETF|P| |Y|100|N||IIGD|IIGD|N\r\nY|III|Information Services Group, Inc. - Common
        Stock|Q|G|N|100|N|N||III|N\r\nY|IIIN|Insteel Industries, Inc. Common Stock|N|
        |N|100|N||IIIN|IIIN|N\r\nY|IIIV|i3 Verticals, Inc. - Common Stock|Q|Q|N|100|N|N||IIIV|N\r\nY|IIM|Invesco
        Value Municipal Income Trust Common Stock|N| |N|100|N||IIM|IIM|N\r\nY|IINN|Inspira
        Technologies Oxy B.H.N. Ltd. - Ordinary Shares|Q|S|N|100|N|N||IINN|N\r\nY|IINNW|Inspira
        Technologies Oxy B.H.N. Ltd. - Warrant|Q|S|N|100|N|N||IINNW|N\r\nY|IIPR|Innovative
        Industrial Properties, Inc. Common Stock|N| |N|100|N||IIPR|IIPR|N\r\nY|IIPR$A|Innovative
        Industrial Properties, Inc. 9.00% Series A Cumulative Redeemable Preferred
        Stock|N| |N|100|N||IIPRpA|IIPR-A|N\r\nY|IJAN|Innovator International Developed
        Power Buffer ETF January|P| |Y|100|N||IJAN|IJAN|N\r\nY|IJH|iShares Core S&P
        Mid-Cap ETF|P| |Y|100|N||IJH|IJH|N\r\nY|IJJ|iShares S&P Mid-Cap 400 Value
        ETF|P| |Y|100|N||IJJ|IJJ|N\r\nY|IJK|iShares S&P Mid-Cap 400 Growth ETF|P|
        |Y|100|N||IJK|IJK|N\r\nY|IJR|iShares Core S&P Small-Cap ETF|P| |Y|100|N||IJR|IJR|N\r\nY|IJS|iShares
        S&P SmallCap 600 Value ETF|P| |Y|100|N||IJS|IJS|N\r\nY|IJT|iShares S&P SmallCap
        600 Growth ETF|Q|G|Y|100|N|N||IJT|N\r\nY|IJUL|Innovator International Developed
        Power Buffer ETF  July|P| |Y|100|N||IJUL|IJUL|N\r\nY|IJUN|SHL Telemedicine
        Ltd Innovator International Developed Power Buffer ETF  June|P| |Y|100|N||IJUN|IJUN|N\r\nY|IKNA|Ikena
        Oncology, Inc. - Common Stock|Q|G|N|100|N|N||IKNA|N\r\nY|IKT|Inhibikase Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||IKT|N\r\nY|ILAG|Intelligent Living Application
        Group Inc. - Ordinary Shares|Q|S|N|100|N|D||ILAG|N\r\nY|ILCB|iShares Morningstar
        Large-Cap ETF|P| |Y|100|N||ILCB|ILCB|N\r\nY|ILCG|iShares Morningstar Large-Cap
        Growth ETF|P| |Y|100|N||ILCG|ILCG|N\r\nY|ILCV|iShares Morningstar Large-Cap
        \ Value ETF|P| |Y|100|N||ILCV|ILCV|N\r\nY|ILDR|First Trust Innovation Leaders
        ETF|P| |Y|100|N||ILDR|ILDR|N\r\nY|ILF|iShares Latin America 40 ETF|P| |Y|100|N||ILF|ILF|N\r\nY|ILIT|iShares
        Lithium Miners and Producers ETF|Q|G|Y|100|N|N||ILIT|N\r\nY|ILMN|Illumina,
        Inc. - Common Stock|Q|Q|N|100|N|N||ILMN|N\r\nY|ILPT|Industrial Logistics Properties
        Trust - Common Shares of Beneficial Interest|Q|Q|N|100|N|N||ILPT|N\r\nY|ILTB|iShares
        Core 10  Year USD Bond ETF|P| |Y|100|N||ILTB|ILTB|N\r\nY|IMAB|I-MAB - American
        Depositary Shares|Q|G|N|100|N|N||IMAB|N\r\nY|IMAQ|International Media Acquisition
        Corp. - Class A Common Stock|Q|S|N|100|N|N||IMAQ|N\r\nY|IMAQR|International
        Media Acquisition Corp. - Rights|Q|S|N|100|N|N||IMAQR|N\r\nY|IMAQU|International
        Media Acquisition Corp. - Unit|Q|S|N|100|N|N||IMAQU|N\r\nY|IMAQW|International
        Media Acquisition Corp. - Warrants|Q|S|N|100|N|N||IMAQW|N\r\nY|IMAR|Innovator
        ETFs Trust Innovator International Developed Power Buffer ETF  March|P| |Y|100|N||IMAR|IMAR|N\r\nY|IMAX|Imax
        Corporation Common Stock|N| |N|100|N||IMAX|IMAX|N\r\nY|IMAY|SHL Telemedicine
        Ltd Innovator International Developed Power Buffer ETF - May|P| |Y|100|N||IMAY|IMAY|N\r\nY|IMCB|iShares
        Morningstar Mid-Cap ETF|P| |Y|100|N||IMCB|IMCB|N\r\nY|IMCC|IM Cannabis Corp.
        - Common Shares|Q|S|N|100|N|D||IMCC|N\r\nY|IMCG|iShares Morningstar Mid-Cap
        Growth ETF|P| |Y|100|N||IMCG|IMCG|N\r\nY|IMCR|Immunocore Holdings plc - American
        Depositary Shares|Q|Q|N|100|N|N||IMCR|N\r\nY|IMCV|iShares Morningstar Mid-Cap
        Value ETF|Q|G|Y|100|N|N||IMCV|N\r\nY|IMFL|Invesco International Developed
        Dynamic Multifactor ETF|Z| |Y|100|N||IMFL|IMFL|N\r\nY|IMKTA|Ingles Markets,
        Incorporated - Class A Common Stock|Q|Q|N|100|N|N||IMKTA|N\r\nY|IMMP|Immutep
        Limited - American Depositary Shares|Q|G|N|100|N|N||IMMP|N\r\nY|IMMR|Immersion
        Corporation - Common Stock|Q|Q|N|100|N|N||IMMR|N\r\nY|IMMX|Immix Biopharma,
        Inc. - Common Stock|Q|S|N|100|N|N||IMMX|N\r\nY|IMNM|Immunome, Inc. - Common
        Stock|Q|S|N|100|N|N||IMNM|N\r\nY|IMNN|Imunon, Inc. - Common Stock|Q|S|N|100|N|N||IMNN|N\r\nY|IMO|Imperial
        Oil Limited Common Stock|A| |N|100|N||IMO|IMO|N\r\nY|IMOM|Alpha Architect
        International Quantitative Momentum ETF|Q|G|Y|100|N|N||IMOM|N\r\nY|IMOS|ChipMOS
        TECHNOLOGIES INC. - American Depositary Shares|Q|Q|N|100|N|N||IMOS|N\r\nY|IMPP|Imperial
        Petroleum Inc. - Common Shares|Q|S|N|100|N|N||IMPP|N\r\nY|IMPPP|Imperial Petroleum
        Inc. - 8.75% Series A Cumulative Redeemable Perpetual Preferred Shares|Q|S|N|100|N|N||IMPPP|N\r\nY|IMRN|Immuron
        Limited - American Depositary Shares|Q|S|N|100|N|N||IMRN|N\r\nY|IMRX|Immuneering
        Corporation - Class A Common Stock|Q|G|N|100|N|N||IMRX|N\r\nY|IMSI|Invesco
        Actively Managed Exchange-Traded Fund Trus Invesco Municipal Strategic Income
        ETF|Z| |Y|100|N||IMSI|IMSI|N\r\nY|IMTB|iShares Core 5-10 Year USD Bond ETF|P|
        |Y|100|N||IMTB|IMTB|N\r\nY|IMTE|Integrated Media Technology Limited - Ordinary
        Shares|Q|S|N|100|N|E||IMTE|N\r\nY|IMTM|iShares MSCI Intl Momentum Factor ETF|P|
        |Y|100|N||IMTM|IMTM|N\r\nY|IMTX|Immatics N.V. - Ordinary Shares|Q|S|N|100|N|N||IMTX|N\r\nY|IMTXW|Immatics
        N.V. - Warrants|Q|S|N|100|N|N||IMTXW|N\r\nY|IMUX|Immunic, Inc.  - Common Stock|Q|Q|N|100|N|N||IMUX|N\r\nY|IMVT|Immunovant,
        Inc.  - Common Stock|Q|Q|N|100|N|N||IMVT|N\r\nY|IMXI|International Money Express,
        Inc. - Common Stock|Q|S|N|100|N|N||IMXI|N\r\nY|INAB|IN8bio, Inc. - Common
        Stock|Q|G|N|100|N|N||INAB|N\r\nY|INAQ|Insight Acquisition Corp. - Class A
        Common Stock|Q|G|N|100|N|N||INAQ|N\r\nY|INAQU|Insight Acquisition Corp. -
        Unit|Q|G|N|100|N|N||INAQU|N\r\nY|INAQW|Insight Acquisition Corp. - Warrant|Q|S|N|100|N|N||INAQW|N\r\nY|INAV|Collaborative
        Investment Series Trust Mohr Industry Nav ETF|Z| |Y|100|N||INAV|INAV|N\r\nY|INBK|First
        Internet Bancorp - Common Stock|Q|Q|N|100|N|N||INBK|N\r\nY|INBKZ|First Internet
        Bancorp - Fixed-to-Floating Rate Subordinated Notes Due 2029|Q|Q|N|100|N|N||INBKZ|N\r\nY|INBS|Intelligent
        Bio Solutions Inc.  - Common Stock|Q|S|N|100|N|N||INBS|N\r\nY|INBX|Inhibrx
        Biosciences, Inc. - Common Stock|Q|Q|N|100|N|N||INBX|N\r\nY|INC|VanEck ETF
        Trust VanEck Dynamic High Income ETF|P| |Y|100|N||INC|INC|N\r\nY|INCE|Franklin
        Income Equity Focus ETF|P| |Y|100|N||INCE|INCE|N\r\nY|INCM|Franklin Templeton
        ETF Trust Franklin Income Focus ETF|P| |Y|100|N||INCM|INCM|N\r\nY|INCO|Columbia
        India Consumer ETF|P| |Y|100|N||INCO|INCO|N\r\nY|INCR|Intercure Ltd. - ordinary
        shares|Q|G|N|100|N|N||INCR|N\r\nY|INCY|Incyte Corporation - Common Stock|Q|Q|N|100|N|N||INCY|N\r\nY|INDA|Ishares
        MSCI India ETF|Z| |Y|100|N||INDA|INDA|N\r\nY|INDB|Independent Bank Corp. -
        Common Stock|Q|Q|N|100|N|N||INDB|N\r\nY|INDE|Matthews International Funds
        Matthews India Active ETF|P| |Y|100|N||INDE|INDE|N\r\nY|INDF|Nifty India Financials
        ETF|P| |Y|100|N||INDF|INDF|N\r\nY|INDH|WisdomTree India Hedged Equity Fund|Q|G|Y|100|N|N||INDH|N\r\nY|INDI|indie
        Semiconductor, Inc. - Class A Common Stock|Q|S|N|100|N|N||INDI|N\r\nY|INDL|Direxion
        Daily MSCI India Bull 2X Shares|P| |Y|100|N||INDL|INDL|N\r\nY|INDO|Indonesia
        Energy Corporation Limited Ordinary Shares|A| |N|100|N||INDO|INDO|N\r\nY|INDP|Indaptus
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|N||INDP|N\r\nY|INDS|Pacer Industrial
        Real Estate ETF|P| |Y|100|N||INDS|INDS|N\r\nY|INDV|Indivior PLC - Ordinary
        Shares|Q|Q|N|100|N|N||INDV|N\r\nY|INDY|iShares India 50 ETF|Q|G|Y|100|N|N||INDY|N\r\nY|INEQ|Columbia
        International Equity Income ETF|P| |Y|100|N||INEQ|INEQ|N\r\nY|INFA|Informatica
        Inc. Class A Common Stock|N| |N|100|N||INFA|INFA|N\r\nY|INFL|Horizon Kinetics
        Inflation Beneficiaries ETF|P| |Y|100|N||INFL|INFL|N\r\nY|INFN|Infinera Corporation
        - Common Stock|Q|Q|N|100|N|N||INFN|N\r\nY|INFR|ClearBridge Sustainable Infrastructure
        ETF|Q|G|Y|100|N|N||INFR|N\r\nY|INFU|InfuSystems Holdings, Inc. Common Stock|A|
        |N|100|N||INFU|INFU|N\r\nY|INFY|Infosys Limited American Depositary Shares|N|
        |N|100|N||INFY|INFY|N\r\nY|ING|ING Group, N.V. Common Stock|N| |N|100|N||ING|ING|N\r\nY|INGN|Inogen,
        Inc - Common Stock|Q|Q|N|100|N|N||INGN|N\r\nY|INGR|Ingredion Incorporated
        Common Stock|N| |N|100|N||INGR|INGR|N\r\nY|INHD|Inno Holdings Inc. - Common
        Stock|Q|S|N|100|N|D||INHD|N\r\nY|INKM|SPDR SSgA Income Allocation ETF|P| |Y|100|N||INKM|INKM|N\r\nY|INKT|MiNK
        Therapeutics, Inc. - Common Stock|Q|S|N|100|N|D||INKT|N\r\nY|INLX|Intellinetics,
        Inc. Common Stock|A| |N|100|N||INLX|INLX|N\r\nY|INM|InMed Pharmaceuticals
        Inc. - Common Shares|Q|S|N|100|N|D||INM|N\r\nY|INMB|INmune Bio Inc. - Common
        stock|Q|S|N|100|N|N||INMB|N\r\nY|INMD|InMode Ltd.  - Ordinary Shares|Q|Q|N|100|N|N||INMD|N\r\nY|INMU|BlackRock
        Intermediate Muni Income Bond ETF|P| |Y|100|N||INMU|INMU|N\r\nY|INN|Summit
        Hotel Properties, Inc. Common Stock|N| |N|100|N||INN|INN|N\r\nY|INN$E|Summit
        Hotel Properties, Inc. 6.250% Series E Cumulative Redeemable Preferred Stock|N|
        |N|100|N||INNpE|INN-E|N\r\nY|INN$F|Summit Hotel Properties, Inc. 5.875% Series
        F Cumulative Redeemable Preferred Stock, $0.01 par value per share|N| |N|100|N||INNpF|INN-F|N\r\nY|INNO|Harbor
        ETF Trust Harbor Disruptive Innovation ETF|P| |Y|100|N||INNO|INNO|N\r\nY|INNV|InnovAge
        Holding Corp. - Common Stock|Q|Q|N|100|N|N||INNV|N\r\nY|INO|Inovio Pharmaceuticals,
        Inc. - Common Stock|Q|S|N|100|N|N||INO|N\r\nY|INOD|Innodata Inc. - Common
        Stock|Q|G|N|100|N|N||INOD|N\r\nY|INOV|Innovator ETFs Trust Innovator International
        Developed Power Buffer ETF  November|P| |Y|100|N||INOV|INOV|N\r\nY|INQQ|Exchange
        Traded Concepts Trust India Internet & Ecommerce ETF|P| |Y|100|N||INQQ|INQQ|N\r\nY|INRO|BlackRock
        U.S. Industry Rotation ETF|Q|G|Y|100|N|N||INRO|N\r\nY|INSE|Inspired Entertainment,
        Inc. - Common Stock|Q|S|N|100|N|N||INSE|N\r\nY|INSG|Inseego Corp. - Common
        Stock|Q|Q|N|100|N|N||INSG|N\r\nY|INSI|Insight Select Income Fund|N| |N|100|N||INSI|INSI|N\r\nY|INSM|Insmed
        Incorporated - Common Stock|Q|Q|N|100|N|N||INSM|N\r\nY|INSP|Inspire Medical
        Systems, Inc. Common Stock|N| |N|100|N||INSP|INSP|N\r\nY|INST|Instructure
        Holdings, Inc. Common Stock|N| |N|100|N||INST|INST|N\r\nY|INSW|International
        Seaways, Inc. Common Stock |N| |N|100|N||INSW|INSW|N\r\nY|INTA|Intapp, Inc.
        - Common Stock|Q|Q|N|100|N|N||INTA|N\r\nY|INTC|Intel Corporation - Common
        Stock|Q|Q|N|100|N|N||INTC|N\r\nY|INTE|Integral Acquisition Corporation 1 -
        Class A Common Stock|Q|S|N|100|N|N||INTE|N\r\nY|INTEU|Integral Acquisition
        Corporation 1 - Unit|Q|S|N|100|N|N||INTEU|N\r\nY|INTEW|Integral Acquisition
        Corporation 1 - Warrant|Q|S|N|100|N|N||INTEW|N\r\nY|INTF|iShares International
        Equity Factor ETF|P| |Y|100|N||INTF|INTF|N\r\nY|INTG|The Intergroup Corporation
        - Common Stock|Q|S|N|100|N|N||INTG|N\r\nY|INTJ|Intelligent Group Limited -
        Ordinary Shares|Q|S|N|100|N|N||INTJ|N\r\nY|INTL|Northern Lights Fund Trust
        IV Main International ETF|Z| |Y|100|N||INTL|INTL|N\r\nY|INTR|Inter & Co. Inc.
        - Class A Common Shares|Q|Q|N|100|N|N||INTR|N\r\nY|INTS|Intensity Therapeutics,
        Inc. - Common Stock|Q|S|N|100|N|N||INTS|N\r\nY|INTT|inTest Corporation Common
        Stock|A| |N|100|N||INTT|INTT|N\r\nY|INTU|Intuit Inc. - Common Stock|Q|Q|N|100|N|N||INTU|N\r\nY|INTZ|Intrusion
        Inc. - Common Stock|Q|S|N|100|N|N||INTZ|N\r\nY|INUV|Inuvo, Inc.|A| |N|100|N||INUV|INUV|N\r\nY|INVA|Innoviva,
        Inc. - Common Stock|Q|Q|N|100|N|N||INVA|N\r\nY|INVE|Identiv, Inc. - Common
        Stock|Q|S|N|100|N|N||INVE|N\r\nY|INVH|Invitation Homes Inc. Common Stock|N|
        |N|100|N||INVH|INVH|N\r\nY|INVO|INVO BioScience, Inc. - Common Stock|Q|S|N|100|N|D||INVO|N\r\nY|INVZ|Innoviz
        Technologies Ltd. - Ordinary shares|Q|S|N|100|N|N||INVZ|N\r\nY|INVZW|Innoviz
        Technologies Ltd. - Warrant|Q|S|N|100|N|N||INVZW|N\r\nY|INZY|Inozyme Pharma,
        Inc. - Common Stock|Q|Q|N|100|N|N||INZY|N\r\nY|IOBT|IO Biotech, Inc. - Common
        Stock|Q|Q|N|100|N|N||IOBT|N\r\nY|IOCT|Innovator International Developed Power
        Buffer ETF - October|P| |Y|100|N||IOCT|IOCT|N\r\nY|ION|ProShares Trust ProShares
        S&P Global Core Battery Metals ETF|P| |Y|100|N||ION|ION|N\r\nY|IONM|Assure
        Holdings Corp. - Common Stock|Q|S|N|100|N|D||IONM|N\r\nY|IONQ|IonQ, Inc. Common
        Stock|N| |N|100|N||IONQ|IONQ|N\r\nY|IONQ.W|IonQ, Inc. Redeemable warrants,
        each whole warrant exercisable for one share of Common Stock, each at an exercise
        price of $11.50 per share|N| |N|100|N||IONQ.WS|IONQ+|N\r\nY|IONR|ioneer Ltd
        - American Depositary Shares|Q|S|N|100|N|N||IONR|N\r\nY|IONS|Ionis Pharmaceuticals,
        Inc. - Common Stock|Q|Q|N|100|N|N||IONS|N\r\nY|IOO|iShares Global 100 ETF|P|
        |Y|100|N||IOO|IOO|N\r\nY|IOPP|Simplify Exchange Traded Funds Simplify Tara
        India Opportunities ETF|P| |Y|100|N||IOPP|IOPP|N\r\nY|IOR|Income Opportunity
        Realty Investors, Inc. Common Stock|A| |N|100|N||IOR|IOR|N\r\nY|IOSP|Innospec
        Inc. - Common Stock|Q|Q|N|100|N|N||IOSP|N\r\nY|IOT|Samsara Inc. Class A Common
        Stock|N| |N|100|N||IOT|IOT|N\r\nY|IOVA|Iovance Biotherapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||IOVA|N\r\nY|IP|International Paper Company Common Stock|N|
        |N|100|N||IP|IP|N\r\nY|IPA|ImmunoPrecise Antibodies Ltd. - Common Stock|Q|G|N|100|N|N||IPA|N\r\nY|IPAC|iShares
        Core MSCI Pacific ETF|P| |Y|100|N||IPAC|IPAC|N\r\nY|IPAR|Inter Parfums, Inc.
        - Common Stock|Q|Q|N|100|N|N||IPAR|N\r\nY|IPAY|Amplify ETF Trust Amplify Mobile
        Payments ETF|P| |Y|100|N||IPAY|IPAY|N\r\nY|IPB|Merrill Lynch & Co., Inc. 6.0518%
        Index Plus Trust Certificates Series 2003-1|N| |Y|100|N||IPB|IPB|N\r\nY|IPDN|Professional
        Diversity Network, Inc. - Common Stock|Q|S|N|100|N|D||IPDN|N\r\nY|IPDP|Listed
        Funds Trust Dividend Performers ETF|Z| |Y|100|N||IPDP|IPDP|N\r\nY|IPG|Interpublic
        Group of Companies, Inc. (The) Common Stock|N| |N|100|N||IPG|IPG|N\r\nY|IPGP|IPG
        Photonics Corporation - Common Stock|Q|Q|N|100|N|N||IPGP|N\r\nY|IPHA|Innate
        Pharma S.A. - American Depositary Shares|Q|Q|N|100|N|N||IPHA|N\r\nY|IPI|Intrepid
        Potash, Inc Common Stock|N| |N|100|N||IPI|IPI|N\r\nY|IPKW|Invesco International
        BuyBack Achievers ETF|Q|G|Y|100|N|N||IPKW|N\r\nY|IPO|Renaissance IPO ETF|P|
        |Y|100|N||IPO|IPO|N\r\nY|IPOS|Renaissance Capital Greenwich Fund|P| |Y|100|N||IPOS|IPOS|N\r\nY|IPPP|Listed
        Funds Trust Preferred-Plus ETF|Z| |Y|100|N||IPPP|IPPP|N\r\nY|IPSC|Century
        Therapeutics, Inc. - Common Stock|Q|Q|N|100|N|N||IPSC|N\r\nY|IPW|iPower Inc.
        - Common Stock|Q|S|N|100|N|N||IPW|N\r\nY|IPWR|Ideal Power Inc. - Common Stock|Q|S|N|100|N|N||IPWR|N\r\nY|IPX|IperionX
        Limited - American Depositary Share|Q|S|N|100|N|N||IPX|N\r\nY|IPXX|Inflection
        Point Acquisition Corp. II - Class A Ordinary Shares|Q|G|N|100|N|N||IPXX|N\r\nY|IPXXU|Inflection
        Point Acquisition Corp. II - Unit|Q|G|N|100|N|N||IPXXU|N\r\nY|IPXXW|Inflection
        Point Acquisition Corp. II - Warrant|Q|G|N|100|N|N||IPXXW|N\r\nY|IQ|iQIYI,
        Inc. - American Depositary Shares|Q|Q|N|100|N|N||IQ|N\r\nY|IQDE|FlexShares
        International Quality Dividend Defensive Index Fund|P| |Y|100|N||IQDE|IQDE|N\r\nY|IQDF|FlexShares
        International Quality Dividend Index Fund|P| |Y|100|N||IQDF|IQDF|N\r\nY|IQDG|WisdomTree
        International Quality Dividend Growth Fund|Z| |Y|100|N||IQDG|IQDG|N\r\nY|IQDY|FlexShares
        International Quality Dividend Dynamic Index Fund|P| |Y|100|N||IQDY|IQDY|N\r\nY|IQHI|IQ
        MacKay Municipal Insured ETF IQ MacKay ESG High Income ETF|P| |Y|100|N||IQHI|IQHI|N\r\nY|IQI|Invesco
        Quality Municipal Income Trust Common Stock|N| |N|100|N||IQI|IQI|N\r\nY|IQIN|IQ
        500 International ETF|P| |Y|100|N||IQIN|IQIN|N\r\nY|IQLT|iShares MSCI Intl
        Quality Factor ETF|P| |Y|100|N||IQLT|IQLT|N\r\nY|IQM|Franklin Intelligent
        Machines ETF|Z| |Y|100|N||IQM|IQM|N\r\nY|IQQQ|ProShares Nasdaq-100 High Income
        ETF|Q|G|Y|100|N|N||IQQQ|N\r\nY|IQRA|IQ MacKay Municipal Insured ETF IQ CBRE
        Real Assets ETF|P| |Y|100|N||IQRA|IQRA|N\r\nY|IQSI|IQ Candriam International
        Equity ETF|P| |Y|100|N||IQSI|IQSI|N\r\nY|IQSM|IQ Candriam U.S. Mid Cap Equity
        ETF|P| |Y|100|N||IQSM|IQSM|N\r\nY|IQSU|IQ Candriam U.S. Large Cap Equity ETF|P|
        |Y|100|N||IQSU|IQSU|N\r\nY|IQV|IQVIA Holdings, Inc. Common Stock|N| |N|100|N||IQV|IQV|N\r\nY|IR|Ingersoll
        Rand Inc. Common Stock|N| |N|100|N||IR|IR|N\r\nY|IRAA|Iris Acquisition Corp
        - Class A Common Stock|Q|S|N|100|N|D||IRAA|N\r\nY|IRAAU|Iris Acquisition Corp
        - Units|Q|S|N|100|N|D||IRAAU|N\r\nY|IRAAW|Iris Acquisition Corp - Warrant|Q|S|N|100|N|D||IRAAW|N\r\nY|IRBO|iShares
        Robotics and Artificial Intelligence Multisector ETF|P| |Y|100|N||IRBO|IRBO|N\r\nY|IRBT|iRobot
        Corporation - Common Stock|Q|Q|N|100|N|N||IRBT|N\r\nY|IRDM|Iridium Communications
        Inc - Common Stock|Q|Q|N|100|N|N||IRDM|N\r\nY|IREN|Iris Energy Limited - Ordinary
        Shares|Q|Q|N|100|N|N||IREN|N\r\nY|IRET|Tidal Trust II iREIT - MarketVector
        Quality REIT Index ETF|P| |Y|100|N||IRET|IRET|N\r\nY|IRIX|IRIDEX Corporation
        - Common Stock|Q|G|N|100|N|N||IRIX|N\r\nY|IRM|Iron Mountain Incorporated (Delaware)Common
        Stock REIT|N| |N|100|N||IRM|IRM|N\r\nY|IRMD|iRadimed Corporation - Common
        Stock|Q|G|N|100|N|N||IRMD|N\r\nY|IROH|Iron Horse Acquisitions Corp. - Common
        Stock|Q|G|N|100|N|N||IROH|N\r\nY|IROHR|Iron Horse Acquisitions Corp. - one
        right to one-fifth (1/5) of one share of common stock|Q|G|N|100|N|N||IROHR|N\r\nY|IROHU|Iron
        Horse Acquisitions Corp. - Unit|Q|G|N|100|N|N||IROHU|N\r\nY|IROHW|Iron Horse
        Acquisitions Corp. - Warrant|Q|G|N|100|N|N||IROHW|N\r\nY|IRON|Disc Medicine,
        Inc. - Common Stock|Q|G|N|100|N|N||IRON|N\r\nY|IROQ|IF Bancorp, Inc. - Common
        Stock|Q|S|N|100|N|N||IROQ|N\r\nY|IRS|IRSA Inversiones Y Representaciones S.A.
        Global Depositary Shares (Each representing ten shares of Common Stock)|N|
        |N|100|N||IRS|IRS|N\r\nY|IRS.W|IRSA Inversiones Y Representaciones S.A. Warrants
        to purchase Common Shares|N| |N|100|N||IRS.WS|IRS+|N\r\nY|IRT|Independence
        Realty Trust, Inc. Common Stock|N| |N|100|N||IRT|IRT|N\r\nY|IRTC|iRhythm Technologies,
        Inc. - Common Stock|Q|Q|N|100|N|N||IRTC|N\r\nY|IRTR|iShares Trust iShares
        LifePath Retirement ETF|P| |Y|100|N||IRTR|IRTR|N\r\nY|IRVH|Global X Funds
        Global X Interest Rate Volatility & Inflation Hedge ETF|P| |Y|100|N||IRVH|IRVH|N\r\nY|IRWD|Ironwood
        Pharmaceuticals, Inc. - Class A Common Stock|Q|Q|N|100|N|N||IRWD|N\r\nY|ISCB|iShares
        Morningstar Small-Cap ETF|P| |Y|100|N||ISCB|ISCB|N\r\nY|ISCF|iShares International
        Small?Cap Equity Factor ETF|P| |Y|100|N||ISCF|ISCF|N\r\nY|ISCG|iShares Morningstar
        Small-Cap Growth ETF|P| |Y|100|N||ISCG|ISCG|N\r\nY|ISCV|iShares Morningstar
        Small-Cap Value ETF|P| |Y|100|N||ISCV|ISCV|N\r\nY|ISD|PGIM High Yield Bond
        Fund, Inc.|N| |N|100|N||ISD|ISD|N\r\nY|ISDB|Invesco Actively Managed Exchange-Traded
        Fund Trus Invesco Short Duration Bond ETF|Z| |Y|100|N||ISDB|ISDB|N\r\nY|ISDR|Issuer
        Direct Corporation Common Stock|A| |N|100|N||ISDR|ISDR|N\r\nY|ISEP|Innovator
        ETFs Trust Innovator International Developed Power Buffer ETF  September|P|
        |Y|100|N||ISEP|ISEP|N\r\nY|ISHG|iShares 1-3 Year International Treasury Bond
        ETF|Q|G|Y|100|N|N||ISHG|N\r\nY|ISHP|First Trust S-Network E-Commerce ETF|Q|G|Y|100|N|N||ISHP|N\r\nY|ISMD|Inspire
        Small/Mid Cap ETF|P| |Y|100|N||ISMD|ISMD|N\r\nY|ISPC|iSpecimen Inc. - Common
        Stock|Q|S|N|100|N|D||ISPC|N\r\nY|ISPO|Inspirato Incorporated - Class A Common
        Stock|Q|G|N|100|N|D||ISPO|N\r\nY|ISPOW|Inspirato Incorporated - Warrant|Q|G|N|100|N|N||ISPOW|N\r\nY|ISPR|Ispire
        Technology Inc. - Common Stock|Q|S|N|100|N|N||ISPR|N\r\nY|ISPY|ProShares Trust
        ProShares S&P 500 High Income ETF|Z| |Y|100|N||ISPY|ISPY|N\r\nY|ISRA|VanEck
        Israel ETF|P| |Y|100|N||ISRA|ISRA|N\r\nY|ISRG|Intuitive Surgical, Inc. - Common
        Stock|Q|Q|N|100|N|N||ISRG|N\r\nY|ISRL|Israel Acquisitions Corp - Class A Ordinary
        Shares|Q|G|N|100|N|N||ISRL|N\r\nY|ISRLU|Israel Acquisitions Corp - Unit|Q|G|N|100|N|N||ISRLU|N\r\nY|ISRLW|Israel
        Acquisitions Corp - Warrant|Q|G|N|100|N|N||ISRLW|N\r\nY|ISSC|Innovative Solutions
        and Support, Inc. - Common Stock|Q|Q|N|100|N|N||ISSC|N\r\nY|ISTB|iShares Core
        1-5 Year USD Bond ETF|Q|G|Y|100|N|N||ISTB|N\r\nY|ISTR|Investar Holding Corporation
        - Common Stock|Q|G|N|100|N|N||ISTR|N\r\nY|ISVL|iShares Trust iShares International
        Developed Small Cap Value Factor ETF|Z| |Y|100|N||ISVL|ISVL|N\r\nY|ISWN|Amplify
        BlackSwan ISWN ETF|P| |Y|100|N||ISWN|ISWN|N\r\nY|ISZE|iShares MSCI Intl Size
        Factor ETF|P| |Y|100|N||ISZE|ISZE|N\r\nY|IT|Gartner, Inc. Common Stock|N|
        |N|100|N||IT|IT|N\r\nY|ITA|iShares U.S. Aerospace & Defense ETF|Z| |Y|100|N||ITA|ITA|N\r\nY|ITAN|Sparkline
        Intangible Value ETF|P| |Y|100|N||ITAN|ITAN|N\r\nY|ITB|iShares U.S. Home Construction
        ETF|Z| |Y|100|N||ITB|ITB|N\r\nY|ITCI|Intra-Cellular Therapies Inc. - Common
        Stock|Q|Q|N|100|N|N||ITCI|N\r\nY|ITDA|iShares Trust iShares LifePath Target
        Date 2025 ETF|P| |Y|100|N||ITDA|ITDA|N\r\nY|ITDB|iShares Trust iShares LifePath
        Target Date 2030 ETF|P| |Y|100|N||ITDB|ITDB|N\r\nY|ITDC|iShares Trust iShares
        LifePath Target Date 2035 ETF|P| |Y|100|N||ITDC|ITDC|N\r\nY|ITDD|iShares Trust
        iShares LifePath Target Date 2040 ETF|P| |Y|100|N||ITDD|ITDD|N\r\nY|ITDE|iShares
        Trust iShares LifePath Target Date 2045 ETF|P| |Y|100|N||ITDE|ITDE|N\r\nY|ITDF|iShares
        Trust iShares LifePath Target Date 2050 ETF|P| |Y|100|N||ITDF|ITDF|N\r\nY|ITDG|iShares
        Trust iShares LifePath Target Date 2055 ETF|P| |Y|100|N||ITDG|ITDG|N\r\nY|ITDH|iShares
        Trust iShares LifePath Target Date 2060 ETF|P| |Y|100|N||ITDH|ITDH|N\r\nY|ITDI|iShares
        Trust iShares LifePath Target Date 2065 ETF|P| |Y|100|N||ITDI|ITDI|N\r\nY|ITEQ|Amplify
        ETF Trust Amplify BlueStar Israel Technology ETF|P| |Y|100|N||ITEQ|ITEQ|N\r\nY|ITGR|Integer
        Holdings Corporation Common Stock|N| |N|100|N||ITGR|ITGR|N\r\nY|ITI|Iteris,
        Inc. - Common Stock|Q|S|N|100|N|N||ITI|N\r\nY|ITIC|Investors Title Company
        - Common Stock|Q|Q|N|100|N|N||ITIC|N\r\nY|ITM|VanEck ETF Trust VanEck Intermediate
        Muni ETF|Z| |Y|100|N||ITM|ITM|N\r\nY|ITOS|iTeos Therapeutics, Inc. - Common
        Stock|Q|G|N|100|N|N||ITOS|N\r\nY|ITOT|iShares Core S&P Total U.S. Stock Market
        ETF|P| |Y|100|N||ITOT|ITOT|N\r\nY|ITP|IT Tech Packaging, Inc. Common Stock|A|
        |N|100|N||ITP|ITP|N\r\nY|ITRG|Integra Resources Corp. Common Shares|A| |N|100|N||ITRG|ITRG|N\r\nY|ITRI|Itron,
        Inc. - Common Stock|Q|Q|N|100|N|N||ITRI|N\r\nY|ITRM|Iterum Therapeutics plc
        - Ordinary Share|Q|S|N|100|N|D||ITRM|N\r\nY|ITRN|Ituran Location and Control
        Ltd. - Ordinary Shares|Q|Q|N|100|N|N||ITRN|N\r\nY|ITT|ITT Inc. Common Stock
        |N| |N|100|N||ITT|ITT|N\r\nY|ITUB|Itau Unibanco Banco Holding SA American
        Depositary Shares (Each repstg 500 Preferred shares)|N| |N|100|N||ITUB|ITUB|N\r\nY|ITW|Illinois
        Tool Works Inc. Common Stock|N| |N|100|N||ITW|ITW|N\r\nY|IUS|Invesco RAFI
        Strategic US ETF|Q|G|Y|100|N|N||IUS|N\r\nY|IUSB|iShares Core Total USD Bond
        Market ETF|Q|G|Y|100|N|N||IUSB|N\r\nY|IUSG|iShares Core S&P U.S. Growth ETF|Q|G|Y|100|N|N||IUSG|N\r\nY|IUSV|iShares
        Core S&P U.S. Value ETF|Q|G|Y|100|N|N||IUSV|N\r\nY|IVA|Inventiva S.A. - American
        Depository Shares|Q|G|N|100|N|N||IVA|N\r\nY|IVAC|Intevac, Inc. - Common Stock|Q|Q|N|100|N|N||IVAC|N\r\nY|IVAL|Alpha
        Architect International Quantitative Value ETF|Q|G|Y|100|N|N||IVAL|N\r\nY|IVCA|Investcorp
        India Acquisition Corp. - Class A Ordinary Shares|Q|G|N|100|N|N||IVCA|N\r\nY|IVCAU|Investcorp
        India Acquisition Corp. - Unit|Q|G|N|100|N|N||IVCAU|N\r\nY|IVCAW|Investcorp
        India Acquisition Corp. - Warrant|Q|G|N|100|N|N||IVCAW|N\r\nY|IVCB|Investcorp
        Europe Acquisition Corp I - Class A Ordinary Shares|Q|G|N|100|N|N||IVCB|N\r\nY|IVCBU|Investcorp
        Europe Acquisition Corp I - Unit|Q|G|N|100|N|N||IVCBU|N\r\nY|IVCBW|Investcorp
        Europe Acquisition Corp I - Warrant|Q|G|N|100|N|N||IVCBW|N\r\nY|IVCP|Swiftmerge
        Acquisition Corp. - Class A Ordinary Share|Q|S|N|100|N|N||IVCP|N\r\nY|IVCPU|Swiftmerge
        Acquisition Corp. - Unit|Q|S|N|100|N|N||IVCPU|N\r\nY|IVCPW|Swiftmerge Acquisition
        Corp. - Warrants|Q|S|N|100|N|N||IVCPW|N\r\nY|IVDA|Iveda Solutions, Inc. -
        Common Stock|Q|S|N|100|N|D||IVDA|N\r\nY|IVDAW|Iveda Solutions, Inc. - Warrant|Q|S|N|100|N|N||IVDAW|N\r\nY|IVE|iShares
        S&P 500 Value ETF|P| |Y|100|N||IVE|IVE|N\r\nY|IVEG|iShares Emergent Food and
        AgTech Multisector ETF|Q|G|Y|100|N|N||IVEG|N\r\nY|IVES|Amplify ETF Trust Amplify
        Global Cloud Technology ETF|P| |Y|100|N||IVES|IVES|N\r\nY|IVLU|iShares MSCI
        Intl Value Factor ETF|P| |Y|100|N||IVLU|IVLU|N\r\nY|IVOG|Vanguard S&P Mid-Cap
        400 Growth ETF|P| |Y|100|N||IVOG|IVOG|N\r\nY|IVOL|Quadratic Interest Rate
        Volatility and Inflation Hedge ETF|P| |Y|100|N||IVOL|IVOL|N\r\nY|IVOO|Vanguard
        S&P Mid-Cap 400 ETF|P| |Y|100|N||IVOO|IVOO|N\r\nY|IVOV|Vanguard S&P Mid-Cap
        400 Value ETF|P| |Y|100|N||IVOV|IVOV|N\r\nY|IVP|Inspire Veterinary Partners,
        Inc. - Class A Common Stock|Q|S|N|100|N|D||IVP|N\r\nY|IVR|INVESCO MORTGAGE
        CAPITAL INC Common Stock|N| |N|100|N||IVR|IVR|N\r\nY|IVR$B|Invesco Mortgage
        Capital Inc. Preferred Series B Cum Fxd to Fltg|N| |N|100|N||IVRpB|IVR-B|N\r\nY|IVR$C|INVESCO
        MORTGAGE CAPITAL INC 7.5% Fixed-to-Floating Series C Cumulative Redeemable
        Preferred Stock, Liquation Preference $25.00 per Share|N| |N|100|N||IVRpC|IVR-C|N\r\nY|IVRA|Invesco
        Real Assets ESG ETF|Z| |Y|100|N||IVRA|IVRA|N\r\nY|IVRS|iShares Trust iShares
        Future Metaverse Tech and Communications ETF|P| |Y|100|N||IVRS|IVRS|N\r\nY|IVT|InvenTrust
        Properties Corp. Common Stock|N| |N|100|N||IVT|IVT|N\r\nY|IVV|iShares Core
        S&P 500 ETF|P| |Y|100|N||IVV|IVV|N\r\nY|IVVB|BlackRock ETF Trust II iShares
        Large Cap Deep Buffer ETF|Z| |Y|100|N||IVVB|IVVB|N\r\nY|IVVD|Invivyd, Inc.
        - Common Stock|Q|G|N|100|N|N||IVVD|N\r\nY|IVVM|BlackRock ETF Trust II iShares
        Large Cap Moderate Buffer ETF|Z| |Y|100|N||IVVM|IVVM|N\r\nY|IVVW|iShares Trust
        iShares S&P 500 BuyWrite ETF|Z| |Y|100|N||IVVW|IVVW|N\r\nY|IVW|iShares S&P
        500 Growth ETF|P| |Y|100|N||IVW|IVW|N\r\nY|IVZ|Invesco Ltd Common Stock|N|
        |N|100|N||IVZ|IVZ|N\r\nY|IWB|iShares Russell 1000 ETF|P| |Y|100|N||IWB|IWB|N\r\nY|IWC|iShares
        Microcap ETF|P| |Y|100|N||IWC|IWC|N\r\nY|IWD|iShares Russell 1000 Value ETF|P|
        |Y|100|N||IWD|IWD|N\r\nY|IWDL|ETRACS 2x Leveraged US Value Factor TR ETN|P|
        |Y|100|N||IWDL|IWDL|N\r\nY|IWF|iShares Russell 1000 Growth ETF|P| |Y|100|N||IWF|IWF|N\r\nY|IWFG|IQ
        MacKay Municipal Insured ETF IQ Winslow Focused Large Cap Growth ETF|P| |Y|100|N||IWFG|IWFG|N\r\nY|IWFH|iShares
        Virtual Work and Life Multisector ETF|P| |Y|100|N||IWFH|IWFH|N\r\nY|IWFL|ETRACS
        2x Leveraged US Growth Factor TR ETN|P| |Y|100|N||IWFL|IWFL|N\r\nY|IWIN|Amplify
        ETF Trust Amplify Inflation Fighter ETF|P| |Y|100|N||IWIN|IWIN|N\r\nY|IWL|iShares
        Russell Top 200 ETF|P| |Y|100|N||IWL|IWL|N\r\nY|IWLG|IQ MacKay Municipal Insured
        ETF IQ Winslow Large Cap Growth ETF|P| |Y|100|N||IWLG|IWLG|N\r\nY|IWM|iShares
        Russell 2000 ETF|P| |Y|100|N||IWM|IWM|N\r\nY|IWMI|NEOS ETF Trust NEOS Russell
        2000 High Income ETF|Z| |Y|100|N||IWMI|IWMI|N\r\nY|IWML|ETRACS 2x Leveraged
        US Size Factor TR ETN|P| |Y|100|N||IWML|IWML|N\r\nY|IWMW|iShares Trust iShares
        Russell 2000 BuyWrite ETF|Z| |Y|100|N||IWMW|IWMW|N\r\nY|IWMY|Tidal Trust II
        Defiance R2000 Enhanced Options Income ETF|P| |Y|100|N||IWMY|IWMY|N\r\nY|IWN|iShares
        Russell 2000 Value ETF|P| |Y|100|N||IWN|IWN|N\r\nY|IWO|iShares Russell 2000
        Growth ETF|P| |Y|100|N||IWO|IWO|N\r\nY|IWP|iShares Russell Midcap Growth ETF|P|
        |Y|100|N||IWP|IWP|N\r\nY|IWR|iShares Russell Mid-Cap ETF|P| |Y|100|N||IWR|IWR|N\r\nY|IWS|iShares
        Russell Mid-cap Value ETF|P| |Y|100|N||IWS|IWS|N\r\nY|IWTR|iShares MSCI Water
        Management Multisector ETF|Q|G|Y|100|N|N||IWTR|N\r\nY|IWV|iShares Russell
        3000 ETF|P| |Y|100|N||IWV|IWV|N\r\nY|IWX|iShares Russell Top 200 Value ETF|P|
        |Y|100|N||IWX|IWX|N\r\nY|IWY|iShares Russell Top 200 Growth ETF|P| |Y|100|N||IWY|IWY|N\r\nY|IX|Orix
        Corp Ads Common Stock|N| |N|100|N||IX|IX|N\r\nY|IXAQ|IX Acquisition Corp.
        - Class A Ordinary Share|Q|G|N|100|N|D||IXAQ|N\r\nY|IXAQU|IX Acquisition Corp.
        - Unit|Q|G|N|100|N|N||IXAQU|N\r\nY|IXAQW|IX Acquisition Corp. - Warrant|Q|G|N|100|N|N||IXAQW|N\r\nY|IXC|iShares
        Global Energy ETF|P| |Y|100|N||IXC|IXC|N\r\nY|IXG|iShares Global Financial
        ETF|P| |Y|100|N||IXG|IXG|N\r\nY|IXHL|Incannex Healthcare Inc. - Common Stock|Q|G|N|100|N|N||IXHL|N\r\nY|IXJ|iShares
        Global Healthcare ETF|P| |Y|100|N||IXJ|IXJ|N\r\nY|IXN|iShares Global Tech
        ETF|P| |Y|100|N||IXN|IXN|N\r\nY|IXP|iShares Global Comm Services ETF|P| |Y|100|N||IXP|IXP|N\r\nY|IXUS|iShares
        Core MSCI Total International Stock ETF|Q|G|Y|100|N|N||IXUS|N\r\nY|IYC|iShares
        U.S. Consumer Discretionary ETF|P| |Y|100|N||IYC|IYC|N\r\nY|IYE|iShares U.S.
        Energy ETF|P| |Y|100|N||IYE|IYE|N\r\nY|IYF|iShares U.S. Financial ETF|P| |Y|100|N||IYF|IYF|N\r\nY|IYG|iShares
        U.S. Financial Services ETF|P| |Y|100|N||IYG|IYG|N\r\nY|IYH|iShares U.S. Healthcare
        ETF|P| |Y|100|N||IYH|IYH|N\r\nY|IYJ|iShares U.S. Industrials ETF|Z| |Y|100|N||IYJ|IYJ|N\r\nY|IYK|iShares
        U.S. Consumer Staples ETF|P| |Y|100|N||IYK|IYK|N\r\nY|IYLD|iShares Morningstar
        Multi-Asset Income ETF|Z| |Y|100|N||IYLD|IYLD|N\r\nY|IYM|iShares U.S. Basic
        Materials ETF|P| |Y|100|N||IYM|IYM|N\r\nY|IYR|iShares U.S. Real Estate ETF|P|
        |Y|100|N||IYR|IYR|N\r\nY|IYT|iShares Trust iShares U.S. Transportation ETF|Z|
        |Y|100|N||IYT|IYT|N\r\nY|IYW|iShares U.S. Technology ETF|P| |Y|100|N||IYW|IYW|N\r\nY|IYY|iShares
        Dow Jones U.S. ETF|P| |Y|100|N||IYY|IYY|N\r\nY|IYZ|iShares U.S. Telecommunications
        ETF|Z| |Y|100|N||IYZ|IYZ|N\r\nY|IZEA|IZEA Worldwide, Inc. - Common Stock|Q|S|N|100|N|N||IZEA|N\r\nY|IZM|ICZOOM
        Group Inc. - Class A Ordinary Shares|Q|S|N|100|N|N||IZM|N\r\nY|IZRL|ARK Israel
        Innovative Technology ETF|Z| |Y|100|N||IZRL|IZRL|N\r\nY|J|Jacobs Solutions
        Inc. Common Stock|N| |N|100|N||J|J|N\r\nY|JAAA|Janus Henderson AAA CLO ETF|P|
        |Y|100|N||JAAA|JAAA|N\r\nY|JACK|Jack In The Box Inc. - Common Stock|Q|Q|N|100|N|N||JACK|N\r\nY|JADE|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Active Developing Markets Equity
        ETF|P| |Y|100|N||JADE|JADE|N\r\nY|JAGX|Jaguar Health, Inc. - Common Stock|Q|S|N|100|N|N||JAGX|N\r\nY|JAKK|JAKKS
        Pacific, Inc. - Common Stock|Q|Q|N|100|N|N||JAKK|N\r\nY|JAMF|Jamf Holding
        Corp. - Common Stock|Q|Q|N|100|N|N||JAMF|N\r\nY|JAN|JanOne Inc. - Common Stock|Q|S|N|100|N|N||JAN|N\r\nY|JAND|Innovator
        ETFs Trust Innovator Premium Income 10 Barrier ETF - January|Z| |Y|100|N||JAND|JAND|N\r\nY|JANH|Innovator
        ETFs Trust Innovator Premium Income 20 Barrier ETF - January|Z| |Y|100|N||JANH|JANH|N\r\nY|JANJ|Innovator
        ETFs Trust Innovator Premium Income 30 Barrier ETF - January|Z| |Y|100|N||JANJ|JANJ|N\r\nY|JANP|PGIM
        US Large-Cap Buffer 12 ETF - January PGIM US Large-Cap Buffer 12 ETF - January|Z|
        |Y|100|N||JANP|JANP|N\r\nY|JANQ|Innovator ETFs Trust Innovator Premium Income
        40 Barrier ETF - January|Z| |Y|100|N||JANQ|JANQ|N\r\nY|JANT|AllianzIM U.S.
        Large Cap Buffer10 Jan ETF|P| |Y|100|N||JANT|JANT|N\r\nY|JANW|AllianzIM U.S.
        Large Cap Buffer20 Jan ETF|P| |Y|100|N||JANW|JANW|N\r\nY|JANX|Janux Therapeutics,
        Inc. - Common Stock|Q|G|N|100|N|N||JANX|N\r\nY|JANZ|TrueShares Structured
        Outcome (January) ETF|Z| |Y|100|N||JANZ|JANZ|N\r\nY|JAVA|JPMorgan Active Value
        ETF|P| |Y|100|N||JAVA|JAVA|N\r\nY|JAZZ|Jazz Pharmaceuticals plc - Ordinary
        Shares|Q|Q|N|100|N|N||JAZZ|N\r\nY|JBBB|Janus Detroit Street Trust Janus Henderson
        B-BBB CLO ETF|Z| |Y|100|N||JBBB|JBBB|N\r\nY|JBGS|JBG SMITH Properties Common
        Shares |N| |N|100|N||JBGS|JBGS|N\r\nY|JBHT|J.B. Hunt Transport Services, Inc.
        - Common Stock|Q|Q|N|100|N|N||JBHT|N\r\nY|JBI|Janus International Group, Inc.
        Common Stock|N| |N|100|N||JBI|JBI|N\r\nY|JBK|Lehman ABS 3.50 3.50% Adjustable
        Corp Backed Tr Certs GS Cap I|N| |N|100|N||JBK|JBK|N\r\nY|JBL|Jabil Inc. Common
        Stock|N| |N|100|N||JBL|JBL|N\r\nY|JBLU|JetBlue Airways Corporation - Common
        Stock|Q|Q|N|100|N|N||JBLU|N\r\nY|JBND|J.P. Morgan Exchange-Traded Fund Trust
        JPMorgan Active Bond ETF|N| |Y|100|N||JBND|JBND|N\r\nY|JBSS|John B. Sanfilippo
        & Son, Inc. - Common Stock|Q|Q|N|100|N|N||JBSS|N\r\nY|JBT|John Bean Technologies
        Corporation Common Stock|N| |N|100|N||JBT|JBT|N\r\nY|JCE|Nuveen Core Equity
        Alpha Fund Common Shares of Beneficial Interest|N| |N|100|N||JCE|JCE|N\r\nY|JCHI|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Active China ETF|P| |Y|100|N||JCHI|JCHI|N\r\nY|JCI|Johnson
        Controls International plc Ordinary Share|N| |N|100|N||JCI|JCI|N\r\nY|JCPB|JPMorgan
        Core Plus Bond ETF|Z| |Y|100|N||JCPB|JCPB|N\r\nY|JCPI|J P MORGAN EXCHANGE-TRADED
        FD TR JPMorgan Inflation Managed Bond ETF|Z| |Y|100|N||JCPI|JCPI|N\r\nY|JCSE|JE
        Cleantech Holdings Limited - Ordinary Shares|Q|S|N|100|N|D||JCSE|N\r\nY|JCTCF|Jewett-Cameron
        Trading Company - Common Shares|Q|S|N|100|N|N||JCTCF|N\r\nY|JCTR|JPMorgan
        Carbon Transition U.S. Equity ETF|P| |Y|100|N||JCTR|JCTR|N\r\nY|JD|JD.com,
        Inc. - American Depositary Shares|Q|Q|N|100|N|N||JD|N\r\nY|JDOC|JPMorgan Healthcare
        Leaders ETF|Q|G|Y|100|N|N||JDOC|N\r\nY|JDST|Direxion Daily Junior Gold Miners
        Index Bear 2X Shares|P| |Y|100|N||JDST|JDST|N\r\nY|JDVI|John Hancock Exchange-Traded
        Fund Trust John Hancock Disciplined Value International Select ETF|P| |Y|100|N||JDVI|JDVI|N\r\nY|JDZG|JIADE
        LIMITED - Common stock|Q|S|N|100|N|N||JDZG|N\r\nY|JEF|Jefferies Financial
        Group Inc. Common Stock|N| |N|100|N||JEF|JEF|N\r\nY|JELD|JELD-WEN Holding,
        Inc. Common Stock|N| |N|100|N||JELD|JELD|N\r\nY|JEMA|JPMorgan ActiveBuilders
        Emerging Markets Equity ETF|Z| |Y|100|N||JEMA|JEMA|N\r\nY|JEPI|JPMorgan Equity
        Premium Income ETF|P| |Y|100|N||JEPI|JEPI|N\r\nY|JEPQ|JPMorgan Nasdaq Equity
        Premium Income ETF|Q|G|Y|100|N|N||JEPQ|N\r\nY|JEPY|Tidal Trust II Defiance
        S&P 500 Enhanced Options Income ETF|P| |Y|100|N||JEPY|JEPY|N\r\nY|JEQ|abrdn
        Japan Equity Fund, Inc. Common Stock|N| |N|100|N||JEQ|JEQ|N\r\nY|JETD|Bank
        Of Montreal MAX Airlines -3X Inverse Leveraged ETNs|P| |Y|100|N||JETD|JETD|N\r\nY|JETS|U.S.
        Global Jets ETF|P| |Y|100|N||JETS|JETS|N\r\nY|JETU|Bank Of Montreal MAX Airlines
        3X Leveraged ETNs|P| |Y|100|N||JETU|JETU|N\r\nY|JEWL|Adamas One Corp. - Common
        Stock|Q|S|N|100|N|H||JEWL|N\r\nY|JFBR|Jeffs' Brands Ltd - Ordinary Shares|Q|S|N|100|N|D||JFBR|N\r\nY|JFBRW|Jeffs'
        Brands Ltd - Warrant|Q|S|N|100|N|N||JFBRW|N\r\nY|JFIN|Jiayin Group Inc. -
        American Depositary Shares|Q|G|N|100|N|N||JFIN|N\r\nY|JFR|Nuveen Floating
        Rate Income Fund Common Stock|N| |N|100|N||JFR|JFR|N\r\nY|JFU|9F Inc. - American
        Depositary Shares|Q|G|N|100|N|N||JFU|N\r\nY|JFWD|Jacob Funds Inc. Jacob Forward
        ETF|P| |Y|100|N||JFWD|JFWD|N\r\nY|JG|Aurora Mobile Limited - American Depositary
        Shares|Q|S|N|100|N|N||JG|N\r\nY|JGH|Nuveen Global High Income Fund Common
        Shares of Beneficial Interest|N| |N|100|N||JGH|JGH|N\r\nY|JGLO|JPMorgan Global
        Select Equity ETF|Q|G|Y|100|N|N||JGLO|N\r\nY|JGRO|J.P. Morgan Exchange-Traded
        Fund Trust JPMorgan Active Growth ETF|P| |Y|100|N||JGRO|JGRO|N\r\nY|JHAC|John
        Hancock Exchange-Traded Fund Trust John Hancock Fundamental All Cap Core ETF|P|
        |Y|100|N||JHAC|JHAC|N\r\nY|JHCB|John Hancock Corporate Bond ETF|P| |Y|100|N||JHCB|JHCB|N\r\nY|JHDV|John
        Hancock Exchange-Traded Fund Trust John Hancock U.S. High Dividend ETF|P|
        |Y|100|N||JHDV|JHDV|N\r\nY|JHEM|John Hancock Multifactor Emerging Markets
        ETF|P| |Y|100|N||JHEM|JHEM|N\r\nY|JHG|Janus Henderson Group plc Ordinary Shares|N|
        |N|100|N||JHG|JHG|N\r\nY|JHHY|John Hancock Exchange-Traded Fund Trust John
        Hancock High Yield ETF|P| |Y|100|N||JHHY|JHHY|N\r\nY|JHI|John Hancock Investors
        Trust Common Stock|N| |N|100|N||JHI|JHI|N\r\nY|JHID|John Hancock Exchange-Traded
        Fund Trust John Hancock International High Dividend ETF|P| |Y|100|N||JHID|JHID|N\r\nY|JHMB|John
        Hancock Mortgage-Backed Securities ETF|P| |Y|100|N||JHMB|JHMB|N\r\nY|JHMD|John
        Hancock Exchange-Traded Fund Trust John Hancock Multifactor Developed International
        ETF|P| |Y|100|N||JHMD|JHMD|N\r\nY|JHML|John Hancock Multifactor Large Cap
        ETF|P| |Y|100|N||JHML|JHML|N\r\nY|JHMM|John Hancock Multifactor Mid Cap ETF|P|
        |Y|100|N||JHMM|JHMM|N\r\nY|JHMU|John Hancock Exchange-Traded Fund Trust John
        Hancock Dynamic Municipal Bond ETF|P| |Y|100|N||JHMU|JHMU|N\r\nY|JHPI|John
        Hancock Exchange-Traded Fund Trust John Hancock Preferred Income ETF|P| |Y|100|N||JHPI|JHPI|N\r\nY|JHS|John
        Hancock Income Securities Trust Common Stock|N| |N|100|N||JHS|JHS|N\r\nY|JHSC|John
        Hancock Multifactor Small Cap ETF|P| |Y|100|N||JHSC|JHSC|N\r\nY|JHX|James
        Hardie Industries plc American Depositary Shares (Ireland)|N| |N|100|N||JHX|JHX|N\r\nY|JIG|JPMorgan
        International Growth ETF|P| |Y|100|N||JIG|JIG|N\r\nY|JILL|J. Jill, Inc. Common
        Stock|N| |N|100|N||JILL|JILL|N\r\nY|JIRE|J.P. Morgan Exchange-Traded Fund
        Trust JPMorgan International Research Enhanced Equity ETF|P| |Y|100|N||JIRE|JIRE|N\r\nY|JIVE|JPMorgan
        International Value ETF|Q|G|Y|100|N|N||JIVE|N\r\nY|JJSF|J & J Snack Foods
        Corp. - Common Stock|Q|Q|N|100|N|N||JJSF|N\r\nY|JKHY|Jack Henry & Associates,
        Inc. - Common Stock|Q|Q|N|100|N|N||JKHY|N\r\nY|JKS|JinkoSolar Holding Company
        Limited American Depositary Shares (each representing 4 Common Shares)|N|
        |N|100|N||JKS|JKS|N\r\nY|JL|J-Long Group Limited - Ordinary Shares|Q|G|N|100|N|D||JL|N\r\nY|JLL|Jones
        Lang LaSalle Incorporated Common Stock|N| |N|100|N||JLL|JLL|N\r\nY|JLQD|Janus
        Henderson Corporate Bond ETF|P| |Y|100|N||JLQD|JLQD|N\r\nY|JLS|Nuveen Mortgage
        and Income Fund|N| |N|100|N||JLS|JLS|N\r\nY|JMBS|Janus Henderson Mortgage-Backed
        Securities ETF|P| |Y|100|N||JMBS|JMBS|N\r\nY|JMEE|J.P. Morgan Exchange-Traded
        Fund Trust JPMorgan Market Expansion Enhanced Equity ETF|P| |Y|100|N||JMEE|JMEE|N\r\nY|JMHI|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan High Yield Municipal ETF|P| |Y|100|N||JMHI|JMHI|N\r\nY|JMIA|Jumia
        Technologies AG American Depositary Shares, each representing two Ordinary
        Shares|N| |N|100|N||JMIA|JMIA|N\r\nY|JMM|Nuveen Multi-Market Income Fund (MA)|N|
        |N|100|N||JMM|JMM|N\r\nY|JMOM|JPMorgan U.S. Momentum Factor ETF|P| |Y|100|N||JMOM|JMOM|N\r\nY|JMSB|John
        Marshall Bancorp, Inc. - Common Stock|Q|S|N|100|N|N||JMSB|N\r\nY|JMSI|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Sustainable Municipal Income ETF|P|
        |Y|100|N||JMSI|JMSI|N\r\nY|JMST|JPMorgan Ultra-Short Municipal Income ETF|Z|
        |Y|100|N||JMST|JMST|N\r\nY|JMUB|JPMorgan Municipal ETF|Z| |Y|100|N||JMUB|JMUB|N\r\nY|JNEU|SHL
        Telemedicine Ltd AllianzIM U.S. Equity Buffer15 Uncapped June ETF|Z| |Y|100|N||JNEU|JNEU|N\r\nY|JNJ|Johnson
        & Johnson Common Stock|N| |N|100|N||JNJ|JNJ|N\r\nY|JNK|SPDR Bloomberg High
        Yield Bond ETF|P| |Y|100|N||JNK|JNK|N\r\nY|JNPR|Juniper Networks, Inc. Common
        Stock|N| |N|100|N||JNPR|JNPR|N\r\nY|JNUG|Direxion Daily Junior Gold Miners
        Index Bull 2X Shares|P| |Y|100|N||JNUG|JNUG|N\r\nY|JNVR|Janover Inc. - Common
        Stock|Q|S|N|100|N|N||JNVR|N\r\nY|JOB|GEE Group Inc. Common Stock|A| |N|100|N||JOB|JOB|N\r\nY|JOBY|Joby
        Aviation, Inc. Common Stock|N| |N|100|N||JOBY|JOBY|N\r\nY|JOBY.W|Joby Aviation,
        Inc. Warrants|N| |N|100|N||JOBY.WS|JOBY+|N\r\nY|JOE|St. Joe Company (The)
        Common Stock|N| |N|100|N||JOE|JOE|N\r\nY|JOET|Virtus ETF Trust II Virtus Terranova
        U.S. Quality Momentum ETF|P| |Y|100|N||JOET|JOET|N\r\nY|JOF|Japan Smaller
        Capitalization Fund Inc Common Stock|N| |N|100|N||JOF|JOF|N\r\nY|JOJO|ATAC
        Credit Rotation ETF|P| |Y|100|N||JOJO|JOJO|N\r\nY|JOUT|Johnson Outdoors Inc.
        - Class A Common Stock|Q|Q|N|100|N|N||JOUT|N\r\nY|JPAN|Matthews International
        Funds Matthews Japan Active ETF|P| |Y|100|N||JPAN|JPAN|N\r\nY|JPC|Nuveen Preferred
        & Income Opportunities Fund|N| |N|100|N||JPC|JPC|N\r\nY|JPEF|JPMorgan Equity
        Focus ETF|Q|G|Y|100|N|N||JPEF|N\r\nY|JPEM|JPMorgan Diversified Return Emerging
        Markets Equity ETF|P| |Y|100|N||JPEM|JPEM|N\r\nY|JPI|Nuveen Preferred and
        Income Term Fund Common Shares of Beneficial Interest|N| |N|100|N||JPI|JPI|N\r\nY|JPIB|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan International Bond Opportunities
        ETF|Z| |Y|100|N||JPIB|JPIB|N\r\nY|JPIE|JPMorgan Income ETF|P| |Y|100|N||JPIE|JPIE|N\r\nY|JPIN|JPMorgan
        Diversified Return International Equity ETF|P| |Y|100|N||JPIN|JPIN|N\r\nY|JPLD|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Limited Duration Bond ETF|Z| |Y|100|N||JPLD|JPLD|N\r\nY|JPM|JP
        Morgan Chase & Co. Common Stock|N| |N|100|N||JPM|JPM|N\r\nY|JPM$C|J P Morgan
        Chase & Co Depositary Shares, each representing a 1/400th interest in a share
        of 6.00% Non-Cumulative  Preferred Stock, Series EE|N| |N|100|N||JPMpC|JPM-C|N\r\nY|JPM$D|J
        P Morgan Chase & Co Depositary Shares, each representing a 1/400th  interest
        in a share of 5.75% Non-Cumulative  Preferred Stock, Series DD|N| |N|100|N||JPMpD|JPM-D|N\r\nY|JPM$J|J
        P Morgan Chase & Co Depositary Shares, each representing a 1/400th interest
        in a share of JPMorgan Chase & Co. 4.75% Non-Cumulative Preferred Stock, Series
        GG|N| |N|100|N||JPMpJ|JPM-J|N\r\nY|JPM$K|J P Morgan Chase & Co Depositary
        Shares, each representing a 1/400th interest in a share of 4.55% Non-Cumulative
        Preferred Stock, Series JJ|N| |N|100|N||JPMpK|JPM-K|N\r\nY|JPM$L|J P Morgan
        Chase & Co Depositary Shares, each representing a 1/400th interest in a share
        of 4.625% Non-Cumulative Preferred Stock, Series LL|N| |N|100|N||JPMpL|JPM-L|N\r\nY|JPM$M|J
        P Morgan Chase & Co Depositary Shares, each representing a 1/400th interest
        in a share of 4.20% Non-Cumulative Preferred Stock, Series MM|N| |N|100|N||JPMpM|JPM-M|N\r\nY|JPMB|JPMorgan
        USD Emerging Markets Sovereign Bond ETF|P| |Y|100|N||JPMB|JPMB|N\r\nY|JPME|JPMorgan
        Diversified Return U.S. Mid Cap Equity ETF|P| |Y|100|N||JPME|JPME|N\r\nY|JPMO|Tidal
        Trust II YieldMax JPM Option Income Strategy ETF|P| |Y|100|N||JPMO|JPMO|N\r\nY|JPRE|J.P.
        Morgan Exchange-Traded Fund Trust JPMorgan Realty Income ETF|P| |Y|100|N||JPRE|JPRE|N\r\nY|JPSE|JPMorgan
        Diversified Return U.S. Small Cap Equity ETF|P| |Y|100|N||JPSE|JPSE|N\r\nY|JPST|JPMorgan
        Ultra-Short Income ETF|P| |Y|100|N||JPST|JPST|N\r\nY|JPSV|J.P. Morgan Exchange-Traded
        Fund Trust JPMorgan Active Small Cap Value ETF|P| |Y|100|N||JPSV|JPSV|N\r\nY|JPUS|JPMorgan
        Diversified Return U.S. Equity ETF|P| |Y|100|N||JPUS|JPUS|N\r\nY|JPXN|iShares
        JPX-Nikkei 400 ETF|P| |Y|100|N||JPXN|JPXN|N\r\nY|JQC|Nuveen Credit Strategies
        Income Fund Shares of Beneficial Interest|N| |N|100|N||JQC|JQC|N\r\nY|JQUA|JPMorgan
        U.S. Quality Factor ETF|P| |Y|100|N||JQUA|JQUA|N\r\nY|JRE|Janus Henderson
        U.S. Real Estate ETF|P| |Y|100|N||JRE|JRE|N\r\nY|JRI|Nuveen Real Asset Income
        and Growth Fund Common Shares of Beneficial Interest|N| |N|100|N||JRI|JRI|N\r\nY|JRNY|ALPS
        Global Travel Beneficiaries ETF|P| |Y|100|N||JRNY|JRNY|N\r\nY|JRS|Nuveen Real
        Estate Income Fund Common Shares of Beneficial Interest|N| |N|100|N||JRS|JRS|N\r\nY|JRSH|Jerash
        Holdings (US), Inc. - Common Stock|Q|S|N|100|N|N||JRSH|N\r\nY|JRVR|James River
        Group Holdings, Ltd. - Common Shares|Q|Q|N|100|N|N||JRVR|N\r\nY|JSCP|JPMorgan
        Short Duration Core Plus ETF|P| |Y|100|N||JSCP|JSCP|N\r\nY|JSI|Janus Detroit
        Street Trust Janus Henderson Securitized Income ETF|P| |Y|100|N||JSI|JSI|N\r\nY|JSM|Navient
        Corporation - 6% Senior Notes due December 15, 2043|Q|Q|N|100|N|N||JSM|N\r\nY|JSMD|Janus
        Henderson Small/Mid Cap Growth Alpha ETF|Q|G|Y|100|N|N||JSMD|N\r\nY|JSML|Janus
        Henderson Small Cap Growth Alpha ETF|Q|G|Y|100|N|N||JSML|N\r\nY|JSPR|Jasper
        Therapeutics, Inc. - Class A Common Stock|Q|S|N|100|N|N||JSPR|N\r\nY|JSPRW|Jasper
        Therapeutics, Inc. - Warrant|Q|S|N|100|N|N||JSPRW|N\r\nY|JSTC|Adasina Social
        Justice All Cap Global ETF|P| |Y|100|N||JSTC|JSTC|N\r\nY|JTAI|Jet.AI Inc.
        - Common Stock|Q|G|N|100|N|D||JTAI|N\r\nY|JTAIW|Jet.AI Inc. - Warrant|Q|S|N|100|N|N||JTAIW|N\r\nY|JTAIZ|Jet.AI
        Inc. - Merger Consideration Warrants|Q|G|N|100|N|D||JTAIZ|N\r\nY|JTEK|JPMorgan
        U.S. Tech Leaders ETF|Q|G|Y|100|N|N||JTEK|N\r\nY|JUCY|ETF Series Solutions
        Aptus Enhanced Yield ETF|Z| |Y|100|N||JUCY|JUCY|N\r\nY|JULD|Innovator ETFs
        Trust Innovator Premium Income 10 Barrier ETF - July|Z| |Y|100|N||JULD|JULD|N\r\nY|JULH|Innovator
        ETFs Trust Innovator Premium Income 20 Barrier ETF - July|Z| |Y|100|N||JULH|JULH|N\r\nY|JULJ|Innovator
        ETFs Trust Innovator Premium Income 30 Barrier ETF - July|Z| |Y|100|N||JULJ|JULJ|N\r\nY|JULP|SHL
        Telemedicine Ltd PGIM US Large-Cap Buffer 12 ETF - July|Z| |Y|100|N||JULP|JULP|N\r\nY|JULQ|Innovator
        ETFs Trust Innovator Premium Income 40 Barrier ETF - July|Z| |Y|100|N||JULQ|JULQ|N\r\nY|JULT|AllianzIM
        U.S. Large Cap Buffer10 Jul ETF|P| |Y|100|N||JULT|JULT|N\r\nY|JULW|AllianzIM
        U.S. Large Cap Buffer20 Jul ETF|P| |Y|100|N||JULW|JULW|N\r\nY|JULZ|TrueShares
        Structured Outcome (July) ETF|Z| |Y|100|N||JULZ|JULZ|N\r\nY|JUNE|Junee Limited
        - Ordinary Shares|Q|S|N|100|N|N||JUNE|N\r\nY|JUNM|SHL Telemedicine Ltd FT
        Vest U.S. Equity Max Buffer ETF - June|Z| |Y|100|N||JUNM|JUNM|N\r\nY|JUNP|SHL
        Telemedicine Ltd PGIM US Large-Cap Buffer 12 ETF - June|Z| |Y|100|N||JUNP|JUNP|N\r\nY|JUNT|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer10 Jun ETF|P| |Y|100|N||JUNT|JUNT|N\r\nY|JUNW|AIM
        ETF Products Trust AllianzIM U.S. Large Cap Buffer20 Jun ETF|P| |Y|100|N||JUNW|JUNW|N\r\nY|JUNZ|TrueShares
        Structured Outcome (June) ETF|Z| |Y|100|N||JUNZ|JUNZ|N\r\nY|JUST|Goldman Sachs
        JUST U.S. Large Cap Equity ETF|P| |Y|100|N||JUST|JUST|N\r\nY|JVA|Coffee Holding
        Co., Inc. - Common Stock|Q|S|N|100|N|N||JVA|N\r\nY|JVAL|JPMorgan U.S. Value
        Factor ETF|P| |Y|100|N||JVAL|JVAL|N\r\nY|JVSA|JVSPAC Acquisition Corp. - Class
        A Ordinary Share|Q|S|N|100|N|N||JVSA|N\r\nY|JVSAR|JVSPAC Acquisition Corp.
        - Right|Q|S|N|100|N|N||JVSAR|N\r\nY|JVSAU|JVSPAC Acquisition Corp. - Unit|Q|S|N|100|N|N||JVSAU|N\r\nY|JWEL|Jowell
        Global Ltd. - Ordinary Shares|Q|S|N|100|N|N||JWEL|N\r\nY|JWN|Nordstrom, Inc.
        Common Stock|N| |N|100|N||JWN|JWN|N\r\nY|JWSM|Jaws Mustang Acquisition Corp.
        Class A Ordinary Shares|A| |N|100|N||JWSM|JWSM|N\r\nY|JWSM.U|Jaws Mustang
        Acquisition Corp. Units, each consisting of one Class A ordinary share, and
        one-fourth of one redeemable warrant|A| |N|100|N||JWSM.U|JWSM=|N\r\nY|JWSM.W|Jaws
        Mustang Acquisition Corp. Redeemable Warrants, each whole warrant exercisable
        for one Class A ordinary share at an exercise price of $11.50|A| |N|100|N||JWSM.WS|JWSM+|N\r\nY|JXI|iShares
        Global Utilities ETF|P| |Y|100|N||JXI|JXI|N\r\nY|JXJT|JX Luxventure Limited
        - Common Stock|Q|S|N|100|N|N||JXJT|N\r\nY|JXN|Jackson Financial Inc. Class
      
... [truncated]
```

## High-Level Overview

This is a .yaml file containing 10726 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:40.385259
- Generator: World's Best Repo Book Generator v1.0.0
