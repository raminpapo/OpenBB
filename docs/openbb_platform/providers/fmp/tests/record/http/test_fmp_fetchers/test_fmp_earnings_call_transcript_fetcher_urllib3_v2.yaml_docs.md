# Documentation: openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_earnings_call_transcript_fetcher_urllib3_v2.yaml

## File Metadata
- **Path**: `openbb_platform/providers/fmp/tests/record/http/test_fmp_fetchers/test_fmp_earnings_call_transcript_fetcher_urllib3_v2.yaml`
- **Size**: 1,225,868 characters, 13,929 lines
- **Words**: 95,196
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
      - gzip, deflate, br, zstd
      Connection:
      - keep-alive
    method: GET
    uri: https://financialmodelingprep.com/stable/earnings-transcript-list?apikey=MOCK_API_KEY
  response:
    body:
      string: "[\n  {\n    \"symbol\": \"ALGN\",\n    \"companyName\": \"Align Technology,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"KMP-UN.TO\",\n
        \   \"companyName\": \"Killam Apartment REIT\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"HIT\",\n    \"companyName\": \"Health
        In Tech, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"MCB.L\",\n    \"companyName\": \"McBride plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"IQ\",\n    \"companyName\": \"iQIYI, Inc.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"BBCP\",\n    \"companyName\":
        \"Concrete Pumping Holdings, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"EPRT\",\n    \"companyName\": \"Essential Properties
        Realty Trust, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"JBI\",\n    \"companyName\": \"Janus International Group, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"FURCF\",\n    \"companyName\": \"Forvia
        SE\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"ACTG\",\n
        \   \"companyName\": \"Acacia Research Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"TKGBF\",\n    \"companyName\": \"Turkiye
        Garanti Bankasi A.S.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"SY1.DE\",\n    \"companyName\": \"Symrise AG\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"4523.T\",\n    \"companyName\": \"Eisai
        Co., Ltd.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\":
        \"DMGGF\",\n    \"companyName\": \"DMG Blockchain Solutions Inc.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"SBSI\",\n    \"companyName\": \"Southside
        Bancshares, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"GPRK\",\n    \"companyName\": \"GeoPark Limited\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"ATEC\",\n    \"companyName\": \"Alphatec
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"EXPE\",\n    \"companyName\": \"Expedia Group, Inc.\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"JMAT.L\",\n    \"companyName\": \"Johnson
        Matthey Plc\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"SNPS\",\n    \"companyName\": \"Synopsys, Inc.\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"TEAM\",\n    \"companyName\": \"Atlassian
        Corporation\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\":
        \"SPRB\",\n    \"companyName\": \"Spruce Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"RMS.PA\",\n    \"companyName\": \"Herm\xE8s
        International Soci\xE9t\xE9 en commandite par actions\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"TTE.PA\",\n    \"companyName\": \"TotalEnergies
        SE\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"AWEVF\",\n
        \   \"companyName\": \"Alphawave IP Group plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"ROMJ.V\",\n    \"companyName\": \"Rubicon
        Organics Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"YAYO\",\n    \"companyName\": \"EVmo, Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"GNRC\",\n    \"companyName\": \"Generac
        Holdings Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"CCL-B.TO\",\n    \"companyName\": \"CCL Industries Inc.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"LKOH.ME\",\n    \"companyName\": \"PJSC
        Lukoil\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"ABEV3.SA\",\n
        \   \"companyName\": \"Ambev S.A.\",\n    \"noOfTranscripts\": \"48\"\n  },\n
        \ {\n    \"symbol\": \"BEP\",\n    \"companyName\": \"Brookfield Renewable
        Partners L.P.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"CBSTF\",\n    \"companyName\": \"The Cannabist Company Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"YELP\",\n    \"companyName\":
        \"Yelp Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"2319.HK\",\n    \"companyName\": \"China Mengniu Dairy Company Limited\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"POFCF\",\n    \"companyName\":
        \"Petrofac Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"EQB.TO\",\n    \"companyName\": \"EQB Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"PLMR\",\n    \"companyName\": \"Palomar
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\":
        \"ACSO.L\",\n    \"companyName\": \"accesso Technology Group plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"VK.PA\",\n    \"companyName\": \"Vallourec
        S.A.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"BATL\",\n
        \   \"companyName\": \"Battalion Oil Corporation\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"HSBC\",\n    \"companyName\": \"HSBC
        Holdings plc\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"SAF.PA\",\n    \"companyName\": \"Safran S.A.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"RKFL\",\n    \"companyName\": \"RocketFuel
        Blockchain, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"RESI\",\n    \"companyName\": \"Kelly Residential & Apartment Real Estate
        ETF\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"OTLY\",\n
        \   \"companyName\": \"Oatly Group AB\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"DNLM.L\",\n    \"companyName\": \"Dunelm Group
        plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"ESVIF\",\n
        \   \"companyName\": \"Ensign Energy Services Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"TNG.PA\",\n    \"companyName\": \"Transgene
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"AMN\",\n
        \   \"companyName\": \"AMN Healthcare Services, Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"OCDGF\",\n    \"companyName\": \"Ocado
        Group plc\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"BMY\",\n    \"companyName\": \"Bristol-Myers Squibb Company\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"ERMAF\",\n    \"companyName\": \"Eramet
        S.a.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"MDRR\",\n
        \   \"companyName\": \"Medalist Diversified REIT, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"ASTE\",\n    \"companyName\": \"Astec
        Industries, Inc.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\":
        \"DARK.L\",\n    \"companyName\": \"Darktrace plc\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"INVO\",\n    \"companyName\": \"INVO Bioscience,
        Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"SOLV\",\n
        \   \"companyName\": \"Solventum Corporation\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"AEYGQ\",\n    \"companyName\": \"ADDvantage
        Technologies Group, Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n
        \   \"symbol\": \"XYZ\",\n    \"companyName\": \"Block, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"KURA\",\n    \"companyName\": \"Kura
        Oncology, Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\":
        \"LNZA\",\n    \"companyName\": \"LanzaTech Global, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"CRARF\",\n    \"companyName\": \"Cr\xE9dit
        Agricole S.A.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"CRSR\",\n    \"companyName\": \"Corsair Gaming, Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"CB\",\n    \"companyName\": \"Chubb Limited\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"ALNOV.PA\",\n
        \   \"companyName\": \"Novacyt S.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"EOSE\",\n    \"companyName\": \"Eos Energy Enterprises,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"ABL\",\n
        \   \"companyName\": \"Abacus Global Management, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"WIX\",\n    \"companyName\": \"Wix.com
        Ltd.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\": \"SESN\",\n
        \   \"companyName\": \"Sesen Bio, Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"CCM\",\n    \"companyName\": \"Concord Medical
        Services Holdings Limited\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n
        \   \"symbol\": \"DOLE\",\n    \"companyName\": \"Dole plc\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"VLEEY\",\n    \"companyName\": \"Valeo
        SE\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SDCCQ\",\n
        \   \"companyName\": \"SmileDirectClub, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"TMD.TO\",\n    \"companyName\": \"Titan
        Medical Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"CCHBF\",\n    \"companyName\": \"Coca-Cola HBC AG\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"SABR\",\n    \"companyName\": \"Sabre
        Corporation\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"LPK.DE\",\n    \"companyName\": \"LPKF Laser & Electronics AG\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"LITB\",\n    \"companyName\": \"LightInTheBox
        Holding Co., Ltd.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"ADBE\",\n    \"companyName\": \"Adobe Inc.\",\n    \"noOfTranscripts\":
        \"80\"\n  },\n  {\n    \"symbol\": \"QTRX\",\n    \"companyName\": \"Quanterix
        Corporation\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"PLBY\",\n    \"companyName\": \"Playboy, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"ZION\",\n    \"companyName\": \"Zions
        Bancorporation, National Association\",\n    \"noOfTranscripts\": \"72\"\n
        \ },\n  {\n    \"symbol\": \"OI\",\n    \"companyName\": \"O-I Glass, Inc.\",\n
        \   \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"HXGBF\",\n    \"companyName\":
        \"Hexagon AB (publ)\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"SHLLF\",\n    \"companyName\": \"Shelf Drilling, Ltd.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"BEKB.BR\",\n    \"companyName\": \"N.V.
        Bekaert S.A.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"ASNS\",\n    \"companyName\": \"Actelis Networks, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"IFX.DE\",\n    \"companyName\": \"Infineon
        Technologies AG\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"BRPHF\",\n    \"companyName\": \"Galaxy Digital Holdings Ltd.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BOCH.L\",\n    \"companyName\": \"Bank
        of Cyprus Holdings Public Limited Company\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"RBSFY\",\n    \"companyName\": \"Rubis\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"META\",\n    \"companyName\": \"Meta Platforms,
        Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\": \"2802.T\",\n
        \   \"companyName\": \"Ajinomoto Co., Inc.\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"8473.T\",\n    \"companyName\": \"SBI Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"DX\",\n
        \   \"companyName\": \"Dynex Capital, Inc.\",\n    \"noOfTranscripts\": \"54\"\n
        \ },\n  {\n    \"symbol\": \"DIM.PA\",\n    \"companyName\": \"Sartorius Stedim
        Biotech S.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"BIRG.IR\",\n    \"companyName\": \"Bank of Ireland Group plc\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"BNPQF\",\n    \"companyName\": \"BNP Paribas
        S.A.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"SLHG\",\n
        \   \"companyName\": \"Skylight Health Group Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"INFU\",\n    \"companyName\": \"InfuSystem
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"005930.KS\",\n    \"companyName\": \"Samsung Electronics Co., Ltd.\",\n
        \   \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"DCI\",\n    \"companyName\":
        \"Donaldson Company, Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n
        \   \"symbol\": \"FATE\",\n    \"companyName\": \"Fate Therapeutics, Inc.\",\n
        \   \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"QDEL\",\n    \"companyName\":
        \"QuidelOrtho Corporation\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n
        \   \"symbol\": \"TLX.DE\",\n    \"companyName\": \"Talanx AG\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"TRN.MI\",\n    \"companyName\": \"Terna
        - Rete Elettrica Nazionale Societ\xE0 per Azioni\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"GMED\",\n    \"companyName\": \"Globus
        Medical, Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"AFX.DE\",\n    \"companyName\": \"Carl Zeiss Meditec AG\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"AAT\",\n    \"companyName\": \"American
        Assets Trust, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"RAIL\",\n    \"companyName\": \"FreightCar America, Inc.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"TTEC\",\n    \"companyName\": \"TTEC
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"HLF\",\n    \"companyName\": \"Herbalife Nutrition Ltd.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"TE.PA\",\n    \"companyName\": \"Technip
        Energies N.V.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"ADT.AX\",\n    \"companyName\": \"Adriatic Metals PLC\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"WPC\",\n    \"companyName\": \"W. P. Carey
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"CTT.LS\",\n
        \   \"companyName\": \"CTT - Correios De Portugal, S.A.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"CRBG\",\n    \"companyName\": \"Corebridge
        Financial, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"BWXT\",\n    \"companyName\": \"BWX Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"PSYTF\",\n    \"companyName\": \"Pason
        Systems Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"HHH\",\n    \"companyName\": \"Howard Hughes Holdings Inc.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"MDVL\",\n    \"companyName\": \"MedAvail
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"SKIL\",\n    \"companyName\": \"Skillsoft Corp.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"ACCO\",\n    \"companyName\": \"ACCO
        Brands Corporation\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"BBAR\",\n    \"companyName\": \"Banco BBVA Argentina S.A.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"HLMA.L\",\n    \"companyName\": \"Halma
        plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"CWXZF\",\n
        \   \"companyName\": \"Doman Building Materials Group Ltd.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"NXST\",\n    \"companyName\": \"Nexstar
        Media Group, Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"EW\",\n    \"companyName\": \"Edwards Lifesciences Corporation\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"STT\",\n    \"companyName\": \"State
        Street Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"CPXGF\",\n    \"companyName\": \"Cineplex Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"SFD\",\n    \"companyName\": \"Smithfield
        Foods, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"VGPBF\",\n    \"companyName\": \"Vgp N.V.\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"IOVA\",\n    \"companyName\": \"Iovance Biotherapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"CCIF\",\n
        \   \"companyName\": \"Carlyle Credit Income Fund\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"SBHGF\",\n    \"companyName\": \"SBI Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"OSUR\",\n
        \   \"companyName\": \"OraSure Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"ORIC\",\n    \"companyName\": \"ORIC
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"BAR.BR\",\n    \"companyName\": \"Barco N.V.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"MONC.MI\",\n    \"companyName\": \"Moncler
        S.p.A.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"GLYC\",\n
        \   \"companyName\": \"GlycoMimetics, Inc.\",\n    \"noOfTranscripts\": \"28\"\n
        \ },\n  {\n    \"symbol\": \"SCND\",\n    \"companyName\": \"Scientific Industries,
        Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"INTU\",\n
        \   \"companyName\": \"Intuit Inc.\",\n    \"noOfTranscripts\": \"78\"\n  },\n
        \ {\n    \"symbol\": \"LOMA\",\n    \"companyName\": \"Loma Negra Compa\xF1\xEDa
        Industrial Argentina Sociedad An\xF3nima\",\n    \"noOfTranscripts\": \"26\"\n
        \ },\n  {\n    \"symbol\": \"GLIBA\",\n    \"companyName\": \"GCI Liberty,
        Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"HYFM\",\n
        \   \"companyName\": \"Hydrofarm Holdings Group, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BME.L\",\n    \"companyName\": \"B&M
        European Value Retail S.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"UCB.BR\",\n    \"companyName\": \"Ucb S.A.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"BVIC.L\",\n    \"companyName\": \"Britvic
        plc\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"MRAM\",\n
        \   \"companyName\": \"Everspin Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"DEZ.DE\",\n    \"companyName\": \"Deutz
        AG\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"SPX.L\",\n
        \   \"companyName\": \"Spirax-Sarco Engineering plc\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"NGVC\",\n    \"companyName\": \"Natural
        Grocers by Vitamin Cottage, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n
        \ {\n    \"symbol\": \"ONT.L\",\n    \"companyName\": \"Oxford Nanopore Technologies
        plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"ETST\",\n
        \   \"companyName\": \"Earth Science Tech, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"AWR\",\n    \"companyName\": \"American
        States Water Company\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"KGX.DE\",\n    \"companyName\": \"Kion Group AG\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"USEG\",\n    \"companyName\": \"U.S.
        Energy Corp.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"AC.TO\",\n    \"companyName\": \"Air Canada\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"OR.PA\",\n    \"companyName\": \"L'Or\xE9al
        S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"FLUX\",\n
        \   \"companyName\": \"Flux Power Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"FOR\",\n    \"companyName\": \"Forestar
        Group Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\":
        \"COE\",\n    \"companyName\": \"51Talk Online Education Group\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"9688.HK\",\n    \"companyName\": \"Zai
        Lab Limited\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"BLND.L\",\n    \"companyName\": \"British Land Company Plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"SUPV.BA\",\n    \"companyName\": \"Grupo
        Supervielle S.A.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"SRRTF\",\n    \"companyName\": \"Slate Grocery REIT\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"PARA\",\n    \"companyName\": \"Paramount
        Global\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"SUPV\",\n
        \   \"companyName\": \"Grupo Supervielle S.A.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"TRYG.CO\",\n    \"companyName\": \"Tryg
        A/S\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"KFY\",\n
        \   \"companyName\": \"Korn Ferry\",\n    \"noOfTranscripts\": \"62\"\n  },\n
        \ {\n    \"symbol\": \"FIORF\",\n    \"companyName\": \"Fiore Cannabis Ltd.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"VERB\",\n    \"companyName\":
        \"Verb Technology Company, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n
        \ {\n    \"symbol\": \"ADTN\",\n    \"companyName\": \"ADTRAN Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"NCTY\",\n    \"companyName\":
        \"The9 Limited\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"WCH.DE\",\n    \"companyName\": \"Wacker Chemie AG\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"HBAN\",\n    \"companyName\": \"Huntington
        Bancshares Incorporated\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"ICUI\",\n    \"companyName\": \"ICU Medical, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"SDF.DE\",\n    \"companyName\": \"K+s
        AG\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"GOOS\",\n
        \   \"companyName\": \"Canada Goose Holdings Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"HZNOF\",\n    \"companyName\": \"Dexterra
        Group Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"PRY.MI\",\n    \"companyName\": \"Prysmian S.p.A.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"HIMS\",\n    \"companyName\": \"Hims &
        Hers Health, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"BEST\",\n    \"companyName\": \"BEST Inc.\",\n    \"noOfTranscripts\": \"22\"\n
        \ },\n  {\n    \"symbol\": \"SUN\",\n    \"companyName\": \"Sunoco LP\",\n
        \   \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"VU.PA\",\n    \"companyName\":
        \"VusionGroup\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"ASC\",\n    \"companyName\": \"Ardmore Shipping Corporation\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"CHG.L\",\n    \"companyName\": \"Chemring
        Group PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"RMV.L\",\n
        \   \"companyName\": \"Rightmove plc\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"TOM2.AS\",\n    \"companyName\": \"TomTom N.V.\",\n
        \   \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"CIVI\",\n    \"companyName\":
        \"Civitas Resources, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n
        \   \"symbol\": \"EXAS\",\n    \"companyName\": \"Exact Sciences Corporation\",\n
        \   \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"ITOS\",\n    \"companyName\":
        \"iTeos Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n
        \   \"symbol\": \"CRWS\",\n    \"companyName\": \"Crown Crafts, Inc.\",\n
        \   \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\": \"PNW\",\n    \"companyName\":
        \"Pinnacle West Capital Corporation\",\n    \"noOfTranscripts\": \"71\"\n
        \ },\n  {\n    \"symbol\": \"VOE.VI\",\n    \"companyName\": \"Voestalpine
        AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"NSC\",\n
        \   \"companyName\": \"Norfolk Southern Corporation\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"GIFI\",\n    \"companyName\": \"Gulf
        Island Fabrication, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n
        \   \"symbol\": \"MATX\",\n    \"companyName\": \"Matson, Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"AZEK\",\n    \"companyName\": \"The AZEK
        Company Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"INGXF\",\n    \"companyName\": \"Innergex Renewable Energy Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"SDR.L\",\n    \"companyName\": \"Schroders
        plc\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"ADAP\",\n
        \   \"companyName\": \"Adaptimmune Therapeutics plc\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"DNBBY\",\n    \"companyName\": \"DNB
        Bank ASA\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"MTZ\",\n
        \   \"companyName\": \"MasTec, Inc.\",\n    \"noOfTranscripts\": \"71\"\n
        \ },\n  {\n    \"symbol\": \"ARR\",\n    \"companyName\": \"ARMOUR Residential
        REIT, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"HOV\",\n    \"companyName\": \"Hovnanian Enterprises, Inc.\",\n    \"noOfTranscripts\":
        \"75\"\n  },\n  {\n    \"symbol\": \"SCVL\",\n    \"companyName\": \"Shoe
        Carnival, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"NESR\",\n    \"companyName\": \"National Energy Services Reunited Corp.\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"PCAR\",\n    \"companyName\":
        \"PACCAR Inc\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"NN.AS\",\n    \"companyName\": \"NN Group N.V.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"BCAB\",\n    \"companyName\": \"BioAtla,
        Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"PRCT\",\n
        \   \"companyName\": \"PROCEPT BioRobotics Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"4477.T\",\n    \"companyName\": \"BASE,
        Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"EA\",\n
        \   \"companyName\": \"Electronic Arts Inc.\",\n    \"noOfTranscripts\": \"80\"\n
        \ },\n  {\n    \"symbol\": \"035420.KS\",\n    \"companyName\": \"NAVER Corporation\",\n
        \   \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"HESM\",\n    \"companyName\":
        \"Hess Midstream LP\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"BDRX\",\n    \"companyName\": \"Biodexa Pharmaceuticals Plc\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"HNSBF\",\n    \"companyName\": \"Hansa
        Biopharma AB (publ)\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"ENT.L\",\n    \"companyName\": \"Entain Plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"IRNT\",\n    \"companyName\": \"IronNet,
        Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"SW\",\n
        \   \"companyName\": \"Smurfit Westrock Plc\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"CDXC\",\n    \"companyName\": \"ChromaDex Corporation\",\n
        \   \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"LCID\",\n    \"companyName\":
        \"Lucid Group, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"HLI\",\n    \"companyName\": \"Houlihan Lokey, Inc.\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"VC2.SI\",\n    \"companyName\": \"Olam
        Group Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CAC\",\n    \"companyName\": \"Camden National Corporation\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"OPAL\",\n    \"companyName\": \"OPAL
        Fuels Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"ETE.AT\",\n    \"companyName\": \"National Bank of Greece S.A.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"ERF.PA\",\n    \"companyName\": \"Eurofins
        Scientific SE\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"MP\",\n    \"companyName\": \"MP Materials Corp.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"HAG.DE\",\n    \"companyName\": \"Hensoldt
        AG\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"SBS.DE\",\n
        \   \"companyName\": \"Stratec SE\",\n    \"noOfTranscripts\": \"7\"\n  },\n
        \ {\n    \"symbol\": \"SSW.JO\",\n    \"companyName\": \"Sibanye Stillwater
        Limited\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"GTBP\",\n
        \   \"companyName\": \"GT Biopharma, Inc.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"OMAB\",\n    \"companyName\": \"Grupo Aeroportuario
        del Centro Norte, S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"42\"\n  },\n
        \ {\n    \"symbol\": \"ABR\",\n    \"companyName\": \"Arbor Realty Trust,
        Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"GIPR\",\n
        \   \"companyName\": \"Generation Income Properties, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"ACA.PA\",\n    \"companyName\": \"Cr\xE9dit
        Agricole S.A.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"FSZ.TO\",\n    \"companyName\": \"Fiera Capital Corporation\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"BZLFF\",\n    \"companyName\": \"Bunzl
        plc\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"DIISF\",\n
        \   \"companyName\": \"Direct Line Insurance Group plc\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"0Y5X.L\",\n    \"companyName\": \"Pentair
        plc\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"GSAT\",\n
        \   \"companyName\": \"Globalstar, Inc.\",\n    \"noOfTranscripts\": \"46\"\n
        \ },\n  {\n    \"symbol\": \"CPNG\",\n    \"companyName\": \"Coupang, Inc.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"DMAC\",\n    \"companyName\":
        \"DiaMedica Therapeutics Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n
        \ {\n    \"symbol\": \"MOGU\",\n    \"companyName\": \"MOGU Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"STL\",\n    \"companyName\": \"Sterling
        Bancorp\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"RMR\",\n
        \   \"companyName\": \"The RMR Group Inc.\",\n    \"noOfTranscripts\": \"38\"\n
        \ },\n  {\n    \"symbol\": \"IBAB.BR\",\n    \"companyName\": \"Ion Beam Applications
        S.A.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"EXE\",\n
        \   \"companyName\": \"Expand Energy Corporation\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"FTCI\",\n    \"companyName\": \"FTC Solar,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"NDRA\",\n
        \   \"companyName\": \"ENDRA Life Sciences Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"6701.T\",\n    \"companyName\": \"NEC
        Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"PNFP\",\n    \"companyName\": \"Pinnacle Financial Partners, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"ELYS\",\n    \"companyName\": \"Elys
        BMG Group, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"ANGO\",\n    \"companyName\": \"AngioDynamics, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"RYI\",\n    \"companyName\": \"Ryerson
        Holding Corporation\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"ATO\",\n    \"companyName\": \"Atmos Energy Corporation\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"MGY\",\n    \"companyName\": \"Magnolia
        Oil & Gas Corporation\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"TAKOF\",\n    \"companyName\": \"Volatus Aerospace Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"CODI\",\n    \"companyName\": \"Compass
        Diversified\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\":
        \"SMBC\",\n    \"companyName\": \"Southern Missouri Bancorp, Inc.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"TGNA\",\n    \"companyName\": \"TEGNA
        Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"SO\",\n
        \   \"companyName\": \"The Southern Company\",\n    \"noOfTranscripts\": \"74\"\n
        \ },\n  {\n    \"symbol\": \"JUBPF\",\n    \"companyName\": \"Jubilee Metals
        Group PLC\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"WOSG.L\",\n
        \   \"companyName\": \"Watches of Switzerland Group plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"JAZZ\",\n    \"companyName\": \"Jazz Pharmaceuticals
        plc\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"VBLT\",\n
        \   \"companyName\": \"Vascular Biogenics Ltd.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"GNUS\",\n    \"companyName\": \"Genius
        Brands International, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"BL\",\n    \"companyName\": \"BlackLine, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"MQ\",\n    \"companyName\": \"Marqeta,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"INCY\",\n
        \   \"companyName\": \"Incyte Corporation\",\n    \"noOfTranscripts\": \"68\"\n
        \ },\n  {\n    \"symbol\": \"STKS\",\n    \"companyName\": \"The ONE Group
        Hospitality, Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"DOMO\",\n    \"companyName\": \"Domo, Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"FCX\",\n    \"companyName\": \"Freeport-McMoRan
        Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"HEN3.DE\",\n
        \   \"companyName\": \"Henkel AG & Co. KGaA\",\n    \"noOfTranscripts\": \"47\"\n
        \ },\n  {\n    \"symbol\": \"CHT\",\n    \"companyName\": \"Chunghwa Telecom
        Co., Ltd.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"BKH\",\n    \"companyName\": \"Black Hills Corporation\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"NANO.PA\",\n    \"companyName\": \"Nanobiotix
        S.A.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"EMAN\",\n
        \   \"companyName\": \"eMagin Corporation\",\n    \"noOfTranscripts\": \"43\"\n
        \ },\n  {\n    \"symbol\": \"AZUL\",\n    \"companyName\": \"Azul S.A.\",\n
        \   \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"ELVT\",\n    \"companyName\":
        \"Elevate Credit, Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"EGLXF\",\n    \"companyName\": \"Enthusiast Gaming Holdings Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"GENE\",\n    \"companyName\": \"Genetic
        Technologies Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"SIMO\",\n    \"companyName\": \"Silicon Motion Technology Corporation\",\n
        \   \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"9613.T\",\n
        \   \"companyName\": \"NTT DATA Corporation\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"WALD\",\n    \"companyName\": \"Waldencast plc\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"ARHOF\",\n    \"companyName\":
        \"AmRest Holdings SE\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"TCELL.IS\",\n    \"companyName\": \"Turkcell Iletisim Hizmetleri A.S.\",\n
        \   \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"GBF.DE\",\n
        \   \"companyName\": \"Bilfinger SE\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"WDFC\",\n    \"companyName\": \"WD-40 Company\",\n
        \   \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"TRST\",\n    \"companyName\":
        \"TrustCo Bank Corp NY\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"MAP.MC\",\n    \"companyName\": \"Mapfre, S.A.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"SAIA\",\n    \"companyName\": \"Saia,
        Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"TSPH\",\n
        \   \"companyName\": \"CreateAI Holdings Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"DMRC\",\n    \"companyName\": \"Digimarc
        Corporation\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\":
        \"VLN\",\n    \"companyName\": \"Valens Semiconductor Ltd.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"8411.T\",\n    \"companyName\": \"Mizuho
        Financial Group, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"DSHK\",\n    \"companyName\": \"Drive Shack Inc.\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"JOE\",\n    \"companyName\": \"The St.
        Joe Company\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"6869.T\",\n    \"companyName\": \"Sysmex Corporation\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"CBLL\",\n    \"companyName\": \"CeriBell,
        Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"ADW-A.TO\",\n
        \   \"companyName\": \"Andrew Peller Limited\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"SRTSF\",\n    \"companyName\": \"Gr.
        Sarantis S.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CHD\",\n    \"companyName\": \"Church & Dwight Co., Inc.\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"ELE.MC\",\n    \"companyName\": \"Endesa,
        S.A.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"SHSP\",\n
        \   \"companyName\": \"SharpSpring, Inc.\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"LSL.L\",\n    \"companyName\": \"LSL Property
        Services plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"AKER.OL\",\n    \"companyName\": \"Aker ASA\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"TACT\",\n    \"companyName\": \"TransAct
        Technologies Incorporated\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n
        \   \"symbol\": \"TRATF\",\n    \"companyName\": \"Traton SE\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"ACO-X.TO\",\n    \"companyName\": \"ATCO
        Ltd.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"NXPGF\",\n
        \   \"companyName\": \"Mobico Group Plc\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"CXB.TO\",\n    \"companyName\": \"Calibre Mining
        Corp.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"FDJU.PA\",\n
        \   \"companyName\": \"FDJ United\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"GDIFF\",\n    \"companyName\": \"GDI Integrated Facility
        Services Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"JMT.LS\",\n    \"companyName\": \"Jer\xF3nimo Martins, SGPS, S.A.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"ASG.V\",\n    \"companyName\": \"Aurora
        Spine Corporation\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"ONCY\",\n    \"companyName\": \"Oncolytics Biotech Inc.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"BHLB\",\n    \"companyName\": \"Berkshire
        Hills Bancorp, Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\":
        \"AMS.MC\",\n    \"companyName\": \"Amadeus IT Group, S.A.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"USIO\",\n    \"companyName\": \"Usio,
        Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"JAGX\",\n
        \   \"companyName\": \"Jaguar Health, Inc.\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"CCO.TO\",\n    \"companyName\": \"Cameco Corporation\",\n
        \   \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"SES.MI\",\n
        \   \"companyName\": \"SeSa S.p.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"ACS.MC\",\n    \"companyName\": \"ACS, Actividades
        de Construcci\xF3n y Servicios, S.A.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"PROX.BR\",\n    \"companyName\": \"Proximus PLC\",\n
        \   \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"MMYT\",\n    \"companyName\":
        \"MakeMyTrip Limited\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\":
        \"MPWR\",\n    \"companyName\": \"Monolithic Power Systems, Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"GNK\",\n    \"companyName\": \"Genco
        Shipping & Trading Limited\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n
        \   \"symbol\": \"JBL.JO\",\n    \"companyName\": \"Jubilee Metals Group PLC\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SHOP\",\n    \"companyName\":
        \"Shopify Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"SWBI\",\n    \"companyName\": \"Smith & Wesson Brands, Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"BERY\",\n    \"companyName\": \"Berry
        Global Group, Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"TRIP\",\n    \"companyName\": \"Tripadvisor, Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"EMLAF\",\n    \"companyName\": \"Empire
        Company Limited\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"AD.AS\",\n    \"companyName\": \"Koninklijke Ahold Delhaize N.V.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"TH\",\n    \"companyName\": \"Target
        Hospitality Corp.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"TSU.TO\",\n    \"companyName\": \"Trisura Group Ltd.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"AUPH\",\n    \"companyName\": \"Aurinia
        Pharmaceuticals Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"VLX.L\",\n    \"companyName\": \"Volex plc\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"RAA.DE\",\n    \"companyName\": \"Rational
        AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"ADT1.L\",\n
        \   \"companyName\": \"Adriatic Metals PLC\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"MPVD.TO\",\n    \"companyName\": \"Mountain Province
        Diamonds Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"CGO\",\n    \"companyName\": \"Calamos Global Total Return Fund\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"RDVT\",\n    \"companyName\": \"Red Violet,
        Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"SN\",\n
        \   \"companyName\": \"SharkNinja, Inc.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"WKEY\",\n    \"companyName\": \"WISeKey International
        Holding AG\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"LAR\",\n    \"companyName\": \"Lithium Argentina AG\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"BASE\",\n    \"companyName\": \"Couchbase,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"NVST\",\n
        \   \"companyName\": \"Envista Holdings Corp\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"RCH.TO\",\n    \"companyName\": \"Richelieu
        Hardware Ltd.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"PHIA.AS\",\n    \"companyName\": \"Koninklijke Philips N.V.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"CTOWY\",\n    \"companyName\": \"China
        Tower Corporation Limited\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"HUBB\",\n    \"companyName\": \"Hubbell Incorporated\",\n
        \   \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"AGL\",\n    \"companyName\":
        \"Agilon Health, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"STRL\",\n    \"companyName\": \"Sterling Infrastructure, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"SMGZY\",\n    \"companyName\": \"Smiths
        Group plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"CQP\",\n
        \   \"companyName\": \"Cheniere Energy Partners, L.P.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"FRU.TO\",\n    \"companyName\": \"Freehold
        Royalties Ltd.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"PANW\",\n    \"companyName\": \"Palo Alto Networks, Inc.\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"MTSS.ME\",\n    \"companyName\": \"Mobile
        TeleSystems Public Joint Stock Company\",\n    \"noOfTranscripts\": \"44\"\n
        \ },\n  {\n    \"symbol\": \"AEMD\",\n    \"companyName\": \"Aethlon Medical,
        Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"MELE.BR\",\n
        \   \"companyName\": \"Melexis N.V.\",\n    \"noOfTranscripts\": \"9\"\n  },\n
        \ {\n    \"symbol\": \"WJX.TO\",\n    \"companyName\": \"Wajax Corporation\",\n
        \   \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"GTLS\",\n    \"companyName\":
        \"Chart Industries, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n
        \   \"symbol\": \"Y92.SI\",\n    \"companyName\": \"Thai Beverage Public Company
        Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"PKE\",\n
        \   \"companyName\": \"Park Aerospace Corp.\",\n    \"noOfTranscripts\": \"54\"\n
        \ },\n  {\n    \"symbol\": \"DHR\",\n    \"companyName\": \"Danaher Corporation\",\n
        \   \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"AONC\",\n    \"companyName\":
        \"American Oncology Network, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n
        \ {\n    \"symbol\": \"BTVCF\",\n    \"companyName\": \"Britvic plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"GPL\",\n    \"companyName\": \"Great Panther
        Mining Limited\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"BTRS\",\n    \"companyName\": \"BTRS Holdings Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"VRN.TO\",\n    \"companyName\": \"Veren
        Inc.\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\": \"GGAL.BA\",\n
        \   \"companyName\": \"Grupo Financiero Galicia S.A.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"002202.SZ\",\n    \"companyName\": \"Goldwind
        Science&Technology Co., Ltd.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"TTE\",\n    \"companyName\": \"TotalEnergies SE\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"ORA.PA\",\n    \"companyName\": \"Orange
        S.A.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"VST\",\n
        \   \"companyName\": \"Vistra Corp.\",\n    \"noOfTranscripts\": \"33\"\n
        \ },\n  {\n    \"symbol\": \"KVHI\",\n    \"companyName\": \"KVH Industries,
        Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"SLNG\",\n
        \   \"companyName\": \"Stabilis Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"0T8B.F\",\n    \"companyName\": \"TCTM
        Kids IT Education Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"MTX.DE\",\n    \"companyName\": \"MTU Aero Engines AG\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"EQC\",\n    \"companyName\": \"Equity
        Commonwealth\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\":
        \"PVAC\",\n    \"companyName\": \"Penn Virginia Corporation\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"MU\",\n    \"companyName\": \"Micron
        Technology, Inc.\",\n    \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\":
        \"PBR\",\n    \"companyName\": \"Petr\xF3leo Brasileiro S.A. - Petrobras\",\n
        \   \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\": \"CCRN\",\n    \"companyName\":
        \"Cross Country Healthcare, Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n
        \ {\n    \"symbol\": \"IMDX\",\n    \"companyName\": \"Insight Molecular Diagnostics
        Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"CHYHY\",\n
        \   \"companyName\": \"Chr. Hansen Holding A/S\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"XPER\",\n    \"companyName\": \"Xperi
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"ALSEA.MX\",\n
        \   \"companyName\": \"Alsea, S.A.B. de C.V.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"EXP\",\n    \"companyName\": \"Eagle
        Materials Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"MINM\",\n    \"companyName\": \"Minim, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"MTRO.L\",\n    \"companyName\": \"Metro
        Bank PLC\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"DTI\",\n
        \   \"companyName\": \"Drilling Tools International Corp.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"TRGNF\",\n    \"companyName\": \"Transgene
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"ALCLS.PA\",\n
        \   \"companyName\": \"Cellectis S.A.\",\n    \"noOfTranscripts\": \"22\"\n
        \ },\n  {\n    \"symbol\": \"SSD\",\n    \"companyName\": \"Simpson Manufacturing
        Co., Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"NOV\",\n    \"companyName\": \"NOV Inc.\",\n    \"noOfTranscripts\": \"72\"\n
        \ },\n  {\n    \"symbol\": \"3690.HK\",\n    \"companyName\": \"Meituan\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"WIE.VI\",\n
        \   \"companyName\": \"Wienerberger AG\",\n    \"noOfTranscripts\": \"5\"\n
        \ },\n  {\n    \"symbol\": \"BRNK.DE\",\n    \"companyName\": \"Branicks Group
        AG\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"CBFV\",\n
        \   \"companyName\": \"CB Financial Services, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"RACE.MI\",\n    \"companyName\": \"Ferrari
        N.V.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"RNO.PA\",\n
        \   \"companyName\": \"Renault S.A.\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"AX\",\n    \"companyName\": \"Axos Financial,
        Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\": \"ATD.TO\",\n
        \   \"companyName\": \"Alimentation Couche-Tard Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"BBIG\",\n    \"companyName\": \"Vinco
        Ventures, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"SJR\",\n    \"companyName\": \"Shaw Communications Inc.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"TXMD\",\n    \"companyName\": \"TherapeuticsMD,
        Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"PSON.L\",\n
        \   \"companyName\": \"Pearson plc\",\n    \"noOfTranscripts\": \"18\"\n  },\n
        \ {\n    \"symbol\": \"SPT.L\",\n    \"companyName\": \"Spirent Communications
        plc\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"CLPS\",\n
        \   \"companyName\": \"CLPS Incorporation\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"KIE.L\",\n    \"companyName\": \"Kier Group plc\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"DCMDF\",\n    \"companyName\":
        \"DATA Communications Management Corp.\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"MUV2.DE\",\n    \"companyName\": \"M\xFCnchener
        R\xFCckversicherungs-Gesellschaft AG in M\xFCnchen\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"CSLLY\",\n    \"companyName\": \"CSL Limited\",\n
        \   \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"KNX\",\n    \"companyName\":
        \"Knight-Swift Transportation Holdings Inc.\",\n    \"noOfTranscripts\": \"46\"\n
        \ },\n  {\n    \"symbol\": \"RAY-B.TO\",\n    \"companyName\": \"Stingray
        Group Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"BIOX\",\n    \"companyName\": \"Bioceres Crop Solutions Corp.\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"ADMA\",\n    \"companyName\": \"ADMA
        Biologics, Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"CLCO\",\n    \"companyName\": \"Cool Company Ltd.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"SNFCA\",\n    \"companyName\": \"Security
        National Financial Corporation\",\n    \"noOfTranscripts\": \"3\"\n  },\n
        \ {\n    \"symbol\": \"CVLG\",\n    \"companyName\": \"Covenant Logistics
        Group, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"ZAL.DE\",\n    \"companyName\": \"Zalando SE\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"0002.HK\",\n    \"companyName\": \"CLP
        Holdings Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"NG\",\n    \"companyName\": \"NovaGold Resources Inc.\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"EONR\",\n    \"companyName\": \"EON Resources
        Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"ALFEN.AS\",\n
        \   \"companyName\": \"Alfen N.V.\",\n    \"noOfTranscripts\": \"7\"\n  },\n
        \ {\n    \"symbol\": \"5401.T\",\n    \"companyName\": \"Nippon Steel Corporation\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"WEX\",\n    \"companyName\":
        \"WEX Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"DYNDF\",\n    \"companyName\": \"Dye & Durham Limited\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"DGGXF\",\n    \"companyName\": \"DigitalX
        Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"ASML\",\n
        \   \"companyName\": \"ASML Holding N.V.\",\n    \"noOfTranscripts\": \"69\"\n
        \ },\n  {\n    \"symbol\": \"VYLD\",\n    \"companyName\": \"Inverse VIX Short-Term
        Futures ETNs due March 22 2045\",\n    \"noOfTranscripts\": \"4\"\n  },\n
        \ {\n    \"symbol\": \"NHIQ\",\n    \"companyName\": \"NantHealth, Inc.\",\n
        \   \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"HSBA.L\",\n
        \   \"companyName\": \"HSBC Holdings plc\",\n    \"noOfTranscripts\": \"54\"\n
        \ },\n  {\n    \"symbol\": \"BUFF\",\n    \"companyName\": \"Innovator Laddered
        Allocation Power Buffer ETF\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n
        \   \"symbol\": \"LAW\",\n    \"companyName\": \"CS Disco, Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"CCEP\",\n    \"companyName\": \"Coca-Cola
        Europacific Partners PLC\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n
        \   \"symbol\": \"SFNC\",\n    \"companyName\": \"Simmons First National Corporation\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"POR\",\n    \"companyName\":
        \"Portland General Electric Company\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"AVSFY\",\n    \"companyName\": \"AVI Limited\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"UUUU\",\n    \"companyName\":
        \"Energy Fuels Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"NTIC\",\n    \"companyName\": \"Northern Technologies International Corporation\",\n
        \   \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"AI\",\n    \"companyName\":
        \"C3.ai, Inc.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"BIOYF\",\n    \"companyName\": \"BioSyent Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"MND.TO\",\n    \"companyName\": \"Mandalay
        Resources Corporation\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"INGA.AS\",\n    \"companyName\": \"ING Groep N.V.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"CLDT\",\n    \"companyName\": \"Chatham
        Lodging Trust\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"SMTC\",\n    \"companyName\": \"Semtech Corporation\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"CIADF\",\n    \"companyName\": \"China
        Mengniu Dairy Company Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"ASAI3.SA\",\n    \"companyName\": \"Sendas Distribuidora
        S.A.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"HBCP\",\n
        \   \"companyName\": \"Home Bancorp, Inc.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"RLI\",\n    \"companyName\": \"RLI Corp.\",\n
        \   \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"HDD.DE\",\n
        \   \"companyName\": \"Heidelberger Druckmaschinen AG\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"EMG.L\",\n    \"companyName\": \"Man Group
        Limited\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"TPR\",\n
        \   \"companyName\": \"Tapestry, Inc.\",\n    \"noOfTranscripts\": \"80\"\n
        \ },\n  {\n    \"symbol\": \"HALL\",\n    \"companyName\": \"Hallmark Financial
        Services, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"PCFBF\",\n    \"companyName\": \"Pacific Basin Shipping Limited\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"FNKO\",\n    \"companyName\": \"Funko,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"EHTH\",\n
        \   \"companyName\": \"eHealth, Inc.\",\n    \"noOfTranscripts\": \"62\"\n
        \ },\n  {\n    \"symbol\": \"HLX\",\n    \"companyName\": \"Helix Energy Solutions
        Group, Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"SEVCF\",\n    \"companyName\": \"Sono Group N.V.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"PSM.DE\",\n    \"companyName\": \"ProSiebenSat.1
        Media SE\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"BTE.TO\",\n
        \   \"companyName\": \"Baytex Energy Corp.\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"CPLE6.SA\",\n    \"companyName\": \"Companhia
        Paranaense de Energia - COPEL\",\n    \"noOfTranscripts\": \"45\"\n  },\n
        \ {\n    \"symbol\": \"SECCF\",\n    \"companyName\": \"Serco Group plc\",\n
        \   \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"RIGL\",\n    \"companyName\":
        \"Rigel Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n
        \ {\n    \"symbol\": \"CLSH\",\n    \"companyName\": \"CLS Holdings USA, Inc.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"BXS\",\n    \"companyName\":
        \"BancorpSouth Bank\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"CRL\",\n    \"companyName\": \"Charles River Laboratories International,
        Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"MAYNF\",\n
        \   \"companyName\": \"Mayne Pharma Group Limited\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"ENQ.L\",\n    \"companyName\": \"EnQuest
        PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"CTKYY\",\n
        \   \"companyName\": \"CooTek (Cayman) Inc.\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"IKA.L\",\n    \"companyName\": \"Ilika plc\",\n
        \   \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"ACV\",\n    \"companyName\":
        \"Virtus Diversified Income & Convertible Fund\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"BAP\",\n    \"companyName\": \"Credicorp
        Ltd.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"AIR.NZ\",\n
        \   \"companyName\": \"Air New Zealand Limited\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"WPRT\",\n    \"companyName\": \"Westport
        Fuel Systems Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"TRP.TO\",\n    \"companyName\": \"TC Energy Corporation\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"ADEN.SW\",\n    \"companyName\": \"Adecco
        Group AG\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"017670.KS\",\n
        \   \"companyName\": \"SK Telecom Co.,Ltd\",\n    \"noOfTranscripts\": \"41\"\n
        \ },\n  {\n    \"symbol\": \"GHG\",\n    \"companyName\": \"GreenTree Hospitality
        Group Ltd.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"LTOUF\",\n    \"companyName\": \"Larsen & Toubro Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"TSE\",\n    \"companyName\": \"Trinseo
        PLC\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"CNTG\",\n
        \   \"companyName\": \"Centogene N.V.\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"NAVB\",\n    \"companyName\": \"Navidea Biopharmaceuticals,
        Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"FTNT\",\n
        \   \"companyName\": \"Fortinet, Inc.\",\n    \"noOfTranscripts\": \"57\"\n
        \ },\n  {\n    \"symbol\": \"ARHS\",\n    \"companyName\": \"Arhaus, Inc.\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"SYM\",\n    \"companyName\":
        \"Symbotic Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"OSW\",\n    \"companyName\": \"OneSpaWorld Holdings Limited\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"RIOT\",\n    \"companyName\": \"Riot
        Platforms, Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"ATRC\",\n    \"companyName\": \"AtriCure, Inc.\",\n    \"noOfTranscripts\":
        \"68\"\n  },\n  {\n    \"symbol\": \"JOYY\",\n    \"companyName\": \"JOYY
        Inc.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\": \"AIFU\",\n
        \   \"companyName\": \"AIFU Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n
        \ {\n    \"symbol\": \"FLEX\",\n    \"companyName\": \"Flex Ltd.\",\n    \"noOfTranscripts\":
        \"78\"\n  },\n  {\n    \"symbol\": \"NESN.SW\",\n    \"companyName\": \"Nestl\xE9
        S.A.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"LZ\",\n
        \   \"companyName\": \"LegalZoom.com, Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"ABBN.SW\",\n    \"companyName\": \"ABB Ltd\",\n
        \   \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"TMO\",\n    \"companyName\":
        \"Thermo Fisher Scientific Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n
        \ {\n    \"symbol\": \"VNRX\",\n    \"companyName\": \"VolitionRx Limited\",\n
        \   \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"VACN.SW\",\n
        \   \"companyName\": \"VAT Group AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n
        \ {\n    \"symbol\": \"SCL\",\n    \"companyName\": \"Stepan Company\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"TECN.SW\",\n
        \   \"companyName\": \"Tecan Group AG\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"TKR\",\n    \"companyName\": \"The Timken Company\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"AQST\",\n    \"companyName\":
        \"Aquestive Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"VZ\",\n    \"companyName\": \"Verizon Communications
        Inc.\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"QRVO\",\n
        \   \"companyName\": \"Qorvo, Inc.\",\n    \"noOfTranscripts\": \"67\"\n  },\n
        \ {\n    \"symbol\": \"CNGGF\",\n    \"companyName\": \"Cann Group Limited\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"STMN.SW\",\n
        \   \"companyName\": \"Straumann Holding AG\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"MOH\",\n    \"companyName\": \"Molina Healthcare,
        Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"SVC\",\n
        \   \"companyName\": \"Service Properties Trust\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"SCMN.SW\",\n    \"companyName\": \"Swisscom
        AG\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"ZDGE\",\n
        \   \"companyName\": \"Zedge, Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n
        \ {\n    \"symbol\": \"BQ\",\n    \"companyName\": \"Boqii Holding Limited\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"BJ\",\n    \"companyName\":
        \"BJ's Wholesale Club Holdings, Inc.\",\n    \"noOfTranscripts\": \"35\"\n
        \ },\n  {\n    \"symbol\": \"SOHO\",\n    \"companyName\": \"Sotherly Hotels
        Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"TEMN.SW\",\n
        \   \"companyName\": \"Temenos AG\",\n    \"noOfTranscripts\": \"16\"\n  },\n
        \ {\n    \"symbol\": \"LSPD\",\n    \"companyName\": \"Lightspeed Commerce
        Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"HP\",\n
        \   \"companyName\": \"Helmerich & Payne, Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"RRGB\",\n    \"companyName\": \"Red Robin
        Gourmet Burgers, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"ACIC\",\n    \"companyName\": \"American Coastal Insurance Corporation\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"PRIO3.SA\",\n
        \   \"companyName\": \"Prio S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n
        \ {\n    \"symbol\": \"MGNI\",\n    \"companyName\": \"Magnite, Inc.\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"MLM\",\n    \"companyName\":
        \"Martin Marietta Materials, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n
        \ {\n    \"symbol\": \"ALLGF\",\n    \"companyName\": \"Allego N.V.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"NLST\",\n    \"companyName\": \"Netlist,
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"VOW.OL\",\n
        \   \"companyName\": \"Vow ASA\",\n    \"noOfTranscripts\": \"9\"\n  },\n
        \ {\n    \"symbol\": \"PTN\",\n    \"companyName\": \"Palatin Technologies,
        Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"SDVKF\",\n
        \   \"companyName\": \"Sandvik AB (publ)\",\n    \"noOfTranscripts\": \"36\"\n
        \ },\n  {\n    \"symbol\": \"RXRX\",\n    \"companyName\": \"Recursion Pharmaceuticals,
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"NSPR\",\n
        \   \"companyName\": \"InspireMD, Inc.\",\n    \"noOfTranscripts\": \"37\"\n
        \ },\n  {\n    \"symbol\": \"ZURN.SW\",\n    \"companyName\": \"Zurich Insurance
        Group AG\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"SGHT\",\n
        \   \"companyName\": \"Sight Sciences, Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"XENE\",\n    \"companyName\": \"Xenon Pharmaceuticals
        Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"SUNE\",\n
        \   \"companyName\": \"SUNation Energy Inc.\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"IDS.L\",\n    \"companyName\": \"International
        Distributions Services plc\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"PAAS\",\n    \"companyName\": \"Pan American Silver Corp.\",\n
        \   \"noOfTranscripts\": \"77\"\n  },\n  {\n    \"symbol\": \"BYD\",\n    \"companyName\":
        \"Boyd Gaming Corporation\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n
        \   \"symbol\": \"ESCA\",\n    \"companyName\": \"Escalade, Incorporated\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"ZIM\",\n    \"companyName\":
        \"ZIM Integrated Shipping Services Ltd.\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"MLYS\",\n    \"companyName\": \"Mineralys Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"PNG.V\",\n
        \   \"companyName\": \"Kraken Robotics Inc.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"YMAB\",\n    \"companyName\": \"Y-mAbs Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"DPH.L\",\n
        \   \"companyName\": \"Dechra Pharmaceuticals PLC\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"BEAN.SW\",\n    \"companyName\": \"BELIMO
        Holding AG\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"GLPEF\",\n    \"companyName\": \"Galp Energia, SGPS, S.A.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"DNB\",\n    \"companyName\": \"Dun &
        Bradstreet Holdings, Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n
        \   \"symbol\": \"BALN.SW\",\n    \"companyName\": \"B\xE2loise Holding AG\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"XIN\",\n    \"companyName\":
        \"Xinyuan Real Estate Co., Ltd.\",\n    \"noOfTranscripts\": \"49\"\n  },\n
        \ {\n    \"symbol\": \"TDY\",\n    \"companyName\": \"Teledyne Technologies
        Incorporated\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"IB.V\",\n    \"companyName\": \"IBC Advanced Alloys Corp.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"SOON.SW\",\n    \"companyName\": \"Sonova
        Holding AG\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"DTNOF\",\n    \"companyName\": \"Dno Asa\",\n    \"noOfTranscripts\": \"28\"\n
        \ },\n  {\n    \"symbol\": \"PAGP\",\n    \"companyName\": \"Plains GP Holdings,
        L.P.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"IAS\",\n
        \   \"companyName\": \"Integral Ad Science Holding Corp.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"APEMY\",\n    \"companyName\": \"Aperam
        S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"SHEL\",\n
        \   \"companyName\": \"Shell plc\",\n    \"noOfTranscripts\": \"64\"\n  },\n
        \ {\n    \"symbol\": \"HLMN\",\n    \"companyName\": \"Hillman Solutions Corp.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"MOLN.SW\",\n
        \   \"companyName\": \"Molecular Partners AG\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"BSLN.SW\",\n    \"companyName\": \"Basilea
        Pharmaceutica AG\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"JCAP\",\n    \"companyName\": \"Jefferson Capital, Inc. Common Stock\",\n
        \   \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"KOD\",\n    \"companyName\":
        \"Kodiak Sciences Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"SIE.DE\",\n    \"companyName\": \"Siemens AG\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"ARLP\",\n    \"companyName\": \"Alliance
        Resource Partners, L.P.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"MMMB\",\n    \"companyName\": \"MamaMancini's Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"601318.SS\",\n    \"companyName\": \"Ping
        An Insurance (Group) Company of China, Ltd.\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"SGSN.SW\",\n    \"companyName\": \"Sgs S.A.\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"TFIN\",\n    \"companyName\":
        \"Triumph Financial, Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n
        \   \"symbol\": \"RICK\",\n    \"companyName\": \"RCI Hospitality Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"WB\",\n
        \   \"companyName\": \"Weibo Corporation\",\n    \"noOfTranscripts\": \"49\"\n
        \ },\n  {\n    \"symbol\": \"PGHN.SW\",\n    \"companyName\": \"Partners Group
        Holding AG\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"G\",\n    \"companyName\": \"Genpact Limited\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"SLGC\",\n    \"companyName\": \"SomaLogic,
        Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"KEN\",\n
        \   \"companyName\": \"Kenon Holdings Ltd.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"NU\",\n    \"companyName\": \"Nu Holdings Ltd.\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"PACB\",\n    \"companyName\":
        \"Pacific Biosciences of California, Inc.\",\n    \"noOfTranscripts\": \"50\"\n
        \ },\n  {\n    \"symbol\": \"YJ\",\n    \"companyName\": \"Yunji Inc.\",\n
        \   \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"EVTZF\",\n    \"companyName\":
        \"Evertz Technologies Limited\",\n    \"noOfTranscripts\": \"27\"\n  },\n
        \ {\n    \"symbol\": \"SIKA.SW\",\n    \"companyName\": \"Sika AG\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"HOLN.SW\",\n    \"companyName\": \"Holcim
        Ltd\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"MTX\",\n
        \   \"companyName\": \"Minerals Technologies Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"CLN.SW\",\n    \"companyName\": \"Clariant
        AG\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"AES\",\n
        \   \"companyName\": \"The AES Corporation\",\n    \"noOfTranscripts\": \"61\"\n
        \ },\n  {\n    \"symbol\": \"SNDL\",\n    \"companyName\": \"SNDL Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"SMR.AX\",\n
        \   \"companyName\": \"Stanmore Resources Limited\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"TD\",\n    \"companyName\": \"The Toronto-Dominion
        Bank\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"NX\",\n
        \   \"companyName\": \"Quanex Building Products Corporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"ECOR\",\n    \"companyName\": \"electroCore,
        Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"IMMR\",\n
        \   \"companyName\": \"Immersion Corporation\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"GPRO\",\n    \"companyName\": \"GoPro,
        Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"LDWY\",\n
        \   \"companyName\": \"Lendway, Inc.\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"LTM.SN\",\n    \"companyName\": \"LATAM Airlines
        Group S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CASI\",\n    \"companyName\": \"CASI Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"TRX\",\n    \"companyName\": \"TRX Gold
        Corporation\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"AEHR\",\n    \"companyName\": \"Aehr Test Systems\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"HOPE\",\n    \"companyName\": \"Hope
        Bancorp, Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"BRFS3.SA\",\n    \"companyName\": \"Brf S.a.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"DLG.L\",\n    \"companyName\": \"Direct
        Line Insurance Group plc\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"SRI\",\n    \"companyName\": \"Stoneridge, Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"AGZNF\",\n    \"companyName\": \"Aegean
        Airlines S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"DDI\",\n    \"companyName\": \"DoubleDown Interactive Co., Ltd.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"A5G.IR\",\n    \"companyName\": \"AIB
        Group plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"OTLK\",\n
        \   \"companyName\": \"Outlook Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"OSIS\",\n    \"companyName\": \"OSI Systems,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"MSFT\",\n
        \   \"companyName\": \"Microsoft Corporation\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"KRX.IR\",\n    \"companyName\": \"Kingspan
        Group plc\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"ROK\",\n    \"companyName\": \"Rockwell Automation, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"SMAR\",\n    \"companyName\": \"Smartsheet
        Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"RYA.IR\",\n
        \   \"companyName\": \"Ryanair Holdings plc\",\n    \"noOfTranscripts\": \"37\"\n
        \ },\n  {\n    \"symbol\": \"FEMSAUBD.MX\",\n    \"companyName\": \"Fomento
        Econ\xF3mico Mexicano, S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"54\"\n
        \ },\n  {\n    \"symbol\": \"0RAR.L\",\n    \"companyName\": \"Stratec SE\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"AXDX\",\n    \"companyName\":
        \"Accelerate Diagnostics, Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n
        \ {\n    \"symbol\": \"LULU\",\n    \"companyName\": \"Lululemon Athletica
        Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"TKLF\",\n
        \   \"companyName\": \"Tokyo Lifestyle Co., Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"UDMY\",\n    \"companyName\": \"Udemy,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"CMTL\",\n
        \   \"companyName\": \"Comtech Telecommunications Corp.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"CHGG\",\n    \"companyName\": \"Chegg,
        Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\": \"SAND.ST\",\n
        \   \"companyName\": \"Sandvik AB (publ)\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"MN\",\n    \"companyName\": \"Manning & Napier,
        Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"LSG.OL\",\n
        \   \"companyName\": \"Ler\xF8y Seafood Group ASA\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"OGN\",\n    \"companyName\": \"Organon
        & Co.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"KNEBV.HE\",\n
        \   \"companyName\": \"KONE Oyj\",\n    \"noOfTranscripts\": \"30\"\n  },\n
        \ {\n    \"symbol\": \"SBMO.AS\",\n    \"companyName\": \"SBM Offshore N.V.\",\n
        \   \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"W\",\n    \"companyName\":
        \"Wayfair Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\":
        \"VCSA\",\n    \"companyName\": \"Vacasa, Inc.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"QLGN\",\n    \"companyName\": \"Qualigen
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"WINT\",\n    \"companyName\": \"Windtree Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"GPX\",\n    \"companyName\": \"GP Strategies
        Corporation\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"YEXT\",\n    \"companyName\": \"Yext, Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"IART\",\n    \"companyName\": \"Integra
        LifeSciences Holdings Corporation\",\n    \"noOfTranscripts\": \"58\"\n  },\n
        \ {\n    \"symbol\": \"MDLZ\",\n    \"companyName\": \"Mondelez International,
        Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"6723.T\",\n
        \   \"companyName\": \"Renesas Electronics Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"RBCN\",\n    \"companyName\": \"Rubicon
        Technology, Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\":
        \"LVRO\",\n    \"companyName\": \"Lavoro Limited\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"SAAB-B.ST\",\n    \"companyName\": \"Saab
        AB (publ)\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"ACC.OL\",\n    \"companyName\": \"Aker Carbon Capture ASA\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"DERM\",\n    \"companyName\": \"Journey
        Medical Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"NLY\",\n    \"companyName\": \"Annaly Capital Management, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"BWLP\",\n    \"companyName\": \"BW LPG
        Limited\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"TEL2-B.ST\",\n
        \   \"companyName\": \"Tele2 AB (publ)\",\n    \"noOfTranscripts\": \"34\"\n
        \ },\n  {\n    \"symbol\": \"CARA\",\n    \"companyName\": \"Cara Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"QCOM\",\n
        \   \"companyName\": \"QUALCOMM Incorporated\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"HTHT\",\n    \"companyName\": \"H World
        Group Limited\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"SNOW\",\n    \"companyName\": \"Snowflake Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"RGS\",\n    \"companyName\": \"Regis
        Corporation\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"TELIA.ST\",\n    \"companyName\": \"Telia Company AB (publ)\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"GLPG.AS\",\n    \"companyName\": \"Galapagos
        N.V.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"GNLN\",\n
        \   \"companyName\": \"Greenlane Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"ADSE\",\n    \"companyName\": \"ADS-TEC
        Energy PLC\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"VTYX\",\n    \"companyName\": \"Ventyx Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"GETI-B.ST\",\n    \"companyName\": \"Getinge
        AB (publ)\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"NVFY\",\n    \"companyName\": \"Nova LifeStyle, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"LRE.L\",\n    \"companyName\": \"Lancashire
        Holdings Limited\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"CMGMF\",\n    \"companyName\": \"Chemring Group PLC\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SKA-B.ST\",\n    \"companyName\": \"Skanska
        AB (publ)\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\":
        \"SNCE\",\n    \"companyName\": \"Science 37 Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"FDR.MC\",\n    \"companyName\": \"Fluidra,
        S.A.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"ELISA.HE\",\n
        \   \"companyName\": \"Elisa Oyj\",\n    \"noOfTranscripts\": \"7\"\n  },\n
        \ {\n    \"symbol\": \"MNK\",\n    \"companyName\": \"Mallinckrodt plc\",\n
        \   \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"VLTSA.PA\",\n
        \   \"companyName\": \"Voltalia S.A.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"ASUUY\",\n    \"companyName\": \"ASUSTeK Computer
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"NEX.PA\",\n
        \   \"companyName\": \"Nexans S.A.\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"FRRPF\",\n    \"companyName\": \"Fiera Capital Corporation\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"GV\",\n    \"companyName\":
        \"Visionary Holdings Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n
        \   \"symbol\": \"RTO.L\",\n    \"companyName\": \"Rentokil Initial plc\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"6367.T\",\n    \"companyName\":
        \"Daikin Industries,Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"ESSITY-B.ST\",\n    \"companyName\": \"Essity AB (publ)\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"ZYME\",\n    \"companyName\": \"Zymeworks
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"ALC\",\n
        \   \"companyName\": \"Alcon Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"LDNXF\",\n    \"companyName\": \"London Stock Exchange
        Group plc\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"ATGN\",\n    \"companyName\": \"Altigen Communications, Inc.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"RROYF\",\n    \"companyName\": \"RE Royalties
        Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"CRGO\",\n
        \   \"companyName\": \"Freightos Limited Ordinary shares\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"PHR\",\n    \"companyName\": \"Phreesia,
        Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"3382.T\",\n
        \   \"companyName\": \"Seven & i Holdings Co., Ltd.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"MTRX\",\n    \"companyName\": \"Matrix
        Service Company\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"DLPN\",\n    \"companyName\": \"Dolphin Entertainment, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"AWRE\",\n    \"companyName\": \"Aware,
        Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"THNPY\",\n
        \   \"companyName\": \"Technip Energies N.V.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"CGECF\",\n    \"companyName\": \"Cogeco
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"MAN\",\n
        \   \"companyName\": \"ManpowerGroup Inc.\",\n    \"noOfTranscripts\": \"66\"\n
        \ },\n  {\n    \"symbol\": \"ABEV\",\n    \"companyName\": \"Ambev S.A.\",\n
        \   \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"LUG.TO\",\n
        \   \"companyName\": \"Lundin Gold Inc.\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"OUT1V.HE\",\n    \"companyName\": \"Outokumpu
        Oyj\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"BBY.L\",\n
        \   \"companyName\": \"Balfour Beatty plc\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"SDXOF\",\n    \"companyName\": \"Sodexo S.A.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"4543.T\",\n
        \   \"companyName\": \"Terumo Corporation\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"NOK\",\n    \"companyName\": \"Nokia Oyj\",\n
        \   \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\": \"BLUE\",\n    \"companyName\":
        \"bluebird bio, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"TRMB\",\n    \"companyName\": \"Trimble Inc.\",\n    \"noOfTranscripts\":
        \"68\"\n  },\n  {\n    \"symbol\": \"CATM\",\n    \"companyName\": \"Cardtronics
        plc\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"LUNA\",\n
        \   \"companyName\": \"Luna Innovations Incorporated\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"TREL-B.ST\",\n    \"companyName\": \"Trelleborg
        AB (publ)\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"LITE\",\n
        \   \"companyName\": \"Lumentum Holdings Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"KIMBERA.MX\",\n    \"companyName\": \"Kimberly-Clark
        de M\xE9xico, S. A. B. de C. V.\",\n    \"noOfTranscripts\": \"13\"\n  },\n
        \ {\n    \"symbol\": \"Y.TO\",\n    \"companyName\": \"Yellow Pages Limited\",\n
        \   \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"SU\",\n    \"companyName\":
        \"Suncor Energy Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"ICMB\",\n    \"companyName\": \"Investcorp Credit Management BDC, Inc.\",\n
        \   \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"ICL\",\n    \"companyName\":
        \"ICL Group Ltd\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"SK3.IR\",\n    \"companyName\": \"Smurfit Kappa Group Plc\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"LR.PA\",\n    \"companyName\": \"Legrand
        S.A.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"SOL.JO\",\n
        \   \"companyName\": \"Sasol Limited\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"EIGR\",\n    \"companyName\": \"Eiger BioPharmaceuticals,
        Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"HOG\",\n
        \   \"companyName\": \"Harley-Davidson, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"SKG.L\",\n    \"companyName\": \"Smurfit
        Kappa Group Plc\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"WISE.L\",\n    \"companyName\": \"Wise plc\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"OSPN\",\n    \"companyName\": \"OneSpan
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"UGRO\",\n
        \   \"companyName\": \"urban-gro, Inc.\",\n    \"noOfTranscripts\": \"13\"\n
        \ },\n  {\n    \"symbol\": \"KESKOA.HE\",\n    \"companyName\": \"Kesko Oyj\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"ENIC\",\n    \"companyName\":
        \"Enel Chile S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"CNMD\",\n    \"companyName\": \"CONMED Corporation\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"FAST\",\n    \"companyName\": \"Fastenal
        Company\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"MCD\",\n
        \   \"companyName\": \"McDonald's Corporation\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"NTZ\",\n    \"companyName\": \"Natuzzi
        S.p.A.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"COV.V\",\n
        \   \"companyName\": \"Covalon Technologies Ltd.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"MITT\",\n    \"companyName\": \"AG Mortgage
        Investment Trust, Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"LYRA\",\n    \"companyName\": \"Lyra Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"FCELB\",\n    \"companyName\": \"FuelCell
        Energy, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"ABNB\",\n    \"companyName\": \"Airbnb, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"PRKS\",\n    \"companyName\": \"United
        Parks & Resorts Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"BYCBF\",\n    \"companyName\": \"Barry Callebaut AG\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"OPTT\",\n    \"companyName\": \"Ocean
        Power Technologies, Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n
        \   \"symbol\": \"HUH1V.HE\",\n    \"companyName\": \"Huhtam\xE4ki Oyj\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"AKRTF\",\n    \"companyName\":
        \"Aker Solutions ASA\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"UPM.HE\",\n    \"companyName\": \"UPM-Kymmene Oyj\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"AAV.TO\",\n    \"companyName\": \"Advantage
        Energy Ltd.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"KLTR\",\n    \"companyName\": \"Kaltura, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"MBGAF\",\n    \"companyName\": \"Mercedes-Benz
        Group AG\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"OII\",\n
        \   \"companyName\": \"Oceaneering International, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"AMIVF\",\n    \"companyName\": \"Atrium
        Mortgage Investment Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n
        \ {\n    \"symbol\": \"BOSS.DE\",\n    \"companyName\": \"Hugo Boss AG\",\n
        \   \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"GXRFF\",\n    \"companyName\":
        \"Prospera Energy Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"SSAB-B.ST\",\n    \"companyName\": \"SSAB AB (publ)\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"AGF-B.TO\",\n    \"companyName\": \"AGF
        Management Limited\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"ALFA.ST\",\n    \"companyName\": \"Alfa Laval Corporate AB\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"CPIX\",\n    \"companyName\": \"Cumberland
        Pharmaceuticals Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"FNNTF\",\n    \"companyName\": \"flatexDEGIRO AG\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"AMCX\",\n    \"companyName\": \"AMC Networks
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"HM-B.ST\",\n
        \   \"companyName\": \"H & M Hennes & Mauritz AB (publ)\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"600036.SS\",\n    \"companyName\": \"China
        Merchants Bank Co., Ltd.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"CDNS\",\n    \"companyName\": \"Cadence Design Systems, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"LII\",\n    \"companyName\": \"Lennox
        International Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"NGRRF\",\n    \"companyName\": \"Nagarro SE\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"ZONNF\",\n    \"companyName\": \"Nos,
        S.g.p.s., S.a.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"FORA\",\n    \"companyName\": \"Forian Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"THULE.ST\",\n    \"companyName\": \"Thule
        Group AB (publ)\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"CIA\",\n    \"companyName\": \"Citizens, Inc.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"ACSYF\",\n    \"companyName\": \"Accsys
        Technologies PLC\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"ONTTF\",\n    \"companyName\": \"Oxford Nanopore Technologies plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"CRNCY\",\n    \"companyName\": \"Capricorn
        Energy PLC\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"ET\",\n    \"companyName\": \"Energy Transfer LP\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"TTGT\",\n    \"companyName\": \"TechTarget,
        Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"AOUT\",\n
        \   \"companyName\": \"American Outdoor Brands, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"RDUS\",\n    \"companyName\": \"Radius
        Recycling, Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"ALKS\",\n    \"companyName\": \"Alkermes plc\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"RANI\",\n    \"companyName\": \"Rani
        Therapeutics Holdings, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"GLRE\",\n    \"companyName\": \"Greenlight Capital Re, Ltd.\",\n
        \   \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"QTCOM.HE\",\n
        \   \"companyName\": \"Qt Group Oyj\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"KEM\",\n    \"companyName\": \"KraneShares Dynamic
        Emerging Markets Strategy ETF\",\n    \"noOfTranscripts\": \"40\"\n  },\n
        \ {\n    \"symbol\": \"MCY\",\n    \"companyName\": \"Mercury General Corporation\",\n
        \   \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\": \"AMPE\",\n    \"companyName\":
        \"Ampio Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"AGEN\",\n    \"companyName\": \"Agenus Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"BXSL\",\n    \"companyName\": \"Blackstone
        Secured Lending Fund\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"MARK\",\n    \"companyName\": \"Remark Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"SKSBF\",\n    \"companyName\": \"Skanska
        AB (publ)\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\":
        \"VBNK\",\n    \"companyName\": \"VersaBank\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"LONE\",\n    \"companyName\": \"Lonestar Resources
        US Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"SNMP\",\n
        \   \"companyName\": \"Evolve Transition Infrastructure LP\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"CBTX\",\n    \"companyName\": \"CBTX,
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"MTUS\",\n
        \   \"companyName\": \"Metallus Inc.\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"HES\",\n    \"companyName\": \"Hess Corporation\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"CBWBF\",\n    \"companyName\":
        \"Canadian Western Bank\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"KCR.HE\",\n    \"companyName\": \"Konecranes Plc\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"MITQ\",\n    \"companyName\": \"Moving
        iMage Technologies, Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n
        \   \"symbol\": \"PYNKF\",\n    \"companyName\": \"Perimeter Medical Imaging
        AI, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"NIBE-B.ST\",\n
        \   \"companyName\": \"NIBE Industrier AB (publ)\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"BBDC\",\n    \"companyName\": \"Barings
        BDC, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"NIPNF\",\n    \"companyName\": \"NEC Corporation\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"LPL\",\n    \"companyName\": \"LG Display
        Co., Ltd.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"SEMG\",\n    \"companyName\": \"EA Series Trust\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"RROTF\",\n    \"companyName\": \"Roots
        Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"FGEN\",\n    \"companyName\": \"FibroGen, Inc.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"INSM\",\n    \"companyName\": \"Insmed
        Incorporated\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\":
        \"TRSSF\",\n    \"companyName\": \"TerrAscend Corp.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"PDSB\",\n    \"companyName\": \"PDS Biotechnology
        Corporation\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"WRT1V.HE\",\n    \"companyName\": \"W\xE4rtsil\xE4 Oyj Abp\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"BOL.ST\",\n    \"companyName\": \"Boliden
        AB (publ)\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"IMPM\",\n    \"companyName\": \"Impac Mortgage Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"ORAN\",\n    \"companyName\": \"Orange
        S.A.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"GIVN.SW\",\n
        \   \"companyName\": \"Givaudan S.A.\",\n    \"noOfTranscripts\": \"10\"\n
        \ },\n  {\n    \"symbol\": \"DM.V\",\n    \"companyName\": \"Datametrex AI
        Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"NPNYY\",\n
        \   \"companyName\": \"Nippon Yusen Kabushiki Kaisha\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"GVP\",\n    \"companyName\": \"GSE Systems,
        Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"SCLP.L\",\n
        \   \"companyName\": \"Scancell Holdings plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MSGE\",\n    \"companyName\": \"Madison
        Square Garden Entertainment Corp.\",\n    \"noOfTranscripts\": \"19\"\n  },\n
        \ {\n    \"symbol\": \"SMTS\",\n    \"companyName\": \"Sierra Metals Inc.\",\n
        \   \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"VIPS\",\n    \"companyName\":
        \"Vipshop Holdings Limited\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n
        \   \"symbol\": \"CLDR\",\n    \"companyName\": \"Cloudera, Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"SPM.MI\",\n    \"companyName\": \"Saipem
        S.p.A.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"BSEM\",\n
        \   \"companyName\": \"BioStem Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"9698.HK\",\n    \"companyName\": \"GDS
        Holdings Limited\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"THGHY\",\n    \"companyName\": \"THG Plc\",\n    \"noOfTranscripts\": \"5\"\n
        \ },\n  {\n    \"symbol\": \"ABN.AS\",\n    \"companyName\": \"ABN AMRO Bank
        N.V.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"DSG.TO\",\n
        \   \"companyName\": \"The Descartes Systems Group Inc.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"7951.T\",\n    \"companyName\": \"Yamaha
        Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"WKL.AS\",\n    \"companyName\": \"Wolters Kluwer N.V.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"NTGY.MC\",\n    \"companyName\": \"Naturgy
        Energy Group, S.A.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"TCTZF\",\n    \"companyName\": \"Tencent Holdings Limited\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"MIR\",\n    \"companyName\": \"Mirion
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"NPSNY\",\n    \"companyName\": \"Naspers Limited\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"PBH\",\n    \"companyName\": \"Prestige
        Consumer Healthcare Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n
        \   \"symbol\": \"MNST\",\n    \"companyName\": \"Monster Beverage Corporation\",\n
        \   \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"7012.T\",\n
        \   \"companyName\": \"Kawasaki Heavy Industries, Ltd.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"GME\",\n    \"companyName\": \"GameStop
        Corp.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"9868.HK\",\n
        \   \"companyName\": \"XPeng Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n
        \ {\n    \"symbol\": \"SNCY\",\n    \"companyName\": \"Sun Country Airlines
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"DKNG\",\n    \"companyName\": \"DraftKings Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"WSFS\",\n    \"companyName\": \"WSFS
        Financial Corporation\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"4768.T\",\n    \"companyName\": \"Otsuka Corporation\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"KRKNF\",\n    \"companyName\": \"Kraken
        Robotics Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"RNMBF\",\n    \"companyName\": \"Rheinmetall AG\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"PWP\",\n    \"companyName\": \"Perella
        Weinberg Partners\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"F\",\n    \"companyName\": \"Ford Motor Company\",\n    \"noOfTranscripts\":
        \"76\"\n  },\n  {\n    \"symbol\": \"PUBM\",\n    \"companyName\": \"PubMatic,
        Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"TMICY\",\n
        \   \"companyName\": \"Trend Micro Incorporated\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"WFC\",\n    \"companyName\": \"Wells Fargo
        & Company\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"KOG.OL\",\n    \"companyName\": \"Kongsberg Gruppen ASA\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"TZOO\",\n    \"companyName\": \"Travelzoo\",\n
        \   \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"FCNCA\",\n    \"companyName\":
        \"First Citizens BancShares, Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n
        \ {\n    \"symbol\": \"DDCCF\",\n    \"companyName\": \"Branicks Group AG\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"WH\",\n    \"companyName\":
        \"Wyndham Hotels & Resorts, Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n
        \ {\n    \"symbol\": \"CRESY\",\n    \"companyName\": \"Cresud Sociedad An\xF3nima,
        Comercial, Inmobiliaria, Financiera y Agropecuaria\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"MEDP\",\n    \"companyName\": \"Medpace
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"SKYH\",\n    \"companyName\": \"Sky Harbour Group Corporation\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"ZNGA\",\n    \"companyName\": \"Zynga
        Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"MLCO\",\n
        \   \"companyName\": \"Melco Resorts & Entertainment Limited\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"WLDBF\",\n    \"companyName\": \"WildBrain
        Ltd.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"XPOF\",\n
        \   \"companyName\": \"Xponential Fitness, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"IVR\",\n    \"companyName\": \"Invesco
        Mortgage Capital Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"BLMN\",\n    \"companyName\": \"Bloomin' Brands, Inc.\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"055550.KS\",\n    \"companyName\": \"Shinhan
        Financial Group Co., Ltd.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n
        \   \"symbol\": \"YPF\",\n    \"companyName\": \"YPF Sociedad An\xF3nima\",\n
        \   \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"LAZR\",\n    \"companyName\":
        \"Luminar Technologies, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n
        \   \"symbol\": \"IOT\",\n    \"companyName\": \"Samsara Inc.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"BGOPF\",\n    \"companyName\": \"Bango
        PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SHIP\",\n
        \   \"companyName\": \"Seanergy Maritime Holdings Corp.\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"CDMO\",\n    \"companyName\": \"Avid
        Bioservices, Inc.\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"NPN.JO\",\n    \"companyName\": \"Naspers Limited\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"BCCLF\",\n    \"companyName\": \"Becle,
        S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"SGLFF\",\n    \"companyName\": \"SGL Carbon SE\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"ALAR\",\n    \"companyName\": \"Alarum
        Technologies Ltd.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"QIPT.TO\",\n    \"companyName\": \"Quipt Home Medical Corp.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"FAF.TO\",\n    \"companyName\": \"Fire
        & Flower Holdings Corp.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"IAC\",\n    \"companyName\": \"IAC InterActive Corp.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"GSHD\",\n    \"companyName\": \"Goosehead
        Insurance, Inc\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"AMD\",\n    \"companyName\": \"Advanced Micro Devices, Inc.\",\n    \"noOfTranscripts\":
        \"74\"\n  },\n  {\n    \"symbol\": \"SDMHF\",\n    \"companyName\": \"Sartorius
        Stedim Biotech S.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"CCOI\",\n    \"companyName\": \"Cogent Communications Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"SY\",\n    \"companyName\":
        \"So-Young International Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n
        \ {\n    \"symbol\": \"MRCY\",\n    \"companyName\": \"Mercury Systems, Inc.\",\n
        \   \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"ALEGF\",\n    \"companyName\":
        \"Allegro.eu S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"BPCGF\",\n    \"companyName\": \"Banco Comercial Portugu\xEAs, S.A.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"FPACX\",\n    \"companyName\":
        \"FPA Crescent Fund\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"ALV.V\",\n    \"companyName\": \"Alvopetro Energy Ltd.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"SOL\",\n    \"companyName\": \"Emeren
        Group, Ltd.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"PSHZF\",\n    \"companyName\": \"Pershing Square Holdings, Ltd.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"AMRC\",\n    \"companyName\": \"Ameresco,
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"HA\",\n
        \   \"companyName\": \"Hawaiian Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"TD.TO\",\n    \"companyName\": \"The
        Toronto-Dominion Bank\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"1179.HK\",\n    \"companyName\": \"H World Group Limited\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"UGP\",\n    \"companyName\": \"Ultrapar
        Participa\xE7\xF5es S.A.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n
        \   \"symbol\": \"AZO\",\n    \"companyName\": \"AutoZone, Inc.\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"MPLN\",\n    \"companyName\": \"MultiPlan
        Corporation\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"NA.TO\",\n    \"companyName\": \"National Bank of Canada\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"IMH\",\n    \"companyName\": \"Impac
        Mortgage Holdings, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"SRAD\",\n    \"companyName\": \"Sportradar Group AG\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"IMXI\",\n    \"companyName\": \"International
        Money Express, Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"TPC\",\n    \"companyName\": \"Tutor Perini Corporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"PRSU\",\n    \"companyName\": \"Pursuit
        Attractions and Hospitality, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n
        \ {\n    \"symbol\": \"EDEN.PA\",\n    \"companyName\": \"Edenred S.A.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"GNCA\",\n    \"companyName\":
        \"Genocea Biosciences, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n
        \   \"symbol\": \"NGL\",\n    \"companyName\": \"NGL Energy Partners LP\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"BRTX\",\n    \"companyName\":
        \"BioRestorative Therapies, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"BMO.TO\",\n    \"companyName\": \"Bank of Montreal\",\n
        \   \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"AENT\",\n    \"companyName\":
        \"Alliance Entertainment Holding Corporation\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MDV\",\n    \"companyName\": \"Modiv Inc.\",\n
        \   \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"HEPS\",\n    \"companyName\":
        \"D-Market Elektronik Hizmetler ve Ticaret A.S.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"GMPXF\",\n    \"companyName\": \"RF Capital
        Group Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\":
        \"IZEA\",\n    \"companyName\": \"IZEA Worldwide, Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"HDIUF\",\n    \"companyName\": \"ADENTRA
        Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"MPNGF\",\n
        \   \"companyName\": \"Meituan\",\n    \"noOfTranscripts\": \"18\"\n  },\n
        \ {\n    \"symbol\": \"ABSSF\",\n    \"companyName\": \"AirBoss of America
        Corp.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"PEGA\",\n
        \   \"companyName\": \"Pegasystems Inc.\",\n    \"noOfTranscripts\": \"61\"\n
        \ },\n  {\n    \"symbol\": \"FULT\",\n    \"companyName\": \"Fulton Financial
        Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"SYRS\",\n    \"companyName\": \"Syros Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"RM\",\n    \"companyName\": \"Regional
        Management Corp.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"MIGI\",\n    \"companyName\": \"Mawson Infrastructure Group, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"AGFS\",\n    \"companyName\": \"AgroFresh
        Solutions, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"WAF.DE\",\n    \"companyName\": \"Siltronic AG\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"ALE.WA\",\n    \"companyName\": \"Allegro.eu
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"SMT.TO\",\n
        \   \"companyName\": \"Sierra Metals Inc.\",\n    \"noOfTranscripts\": \"37\"\n
        \ },\n  {\n    \"symbol\": \"ASTL.TO\",\n    \"companyName\": \"Algoma Steel
        Group Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"CELC\",\n    \"companyName\": \"Celcuity Inc.\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"CEIX\",\n    \"companyName\": \"CONSOL
        Energy Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"XGN\",\n    \"companyName\": \"Exagen Inc.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"SYR.AX\",\n    \"companyName\": \"Syrah
        Resources Limited\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"MAPIF\",\n    \"companyName\": \"Mapletree Industrial Trust\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"SLCJY\",\n    \"companyName\": \"SLC Agr\xEDcola
        S.A.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"SAUHF\",\n
        \   \"companyName\": \"Straumann Holding AG\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"ALEAF\",\n    \"companyName\": \"Aleafia Health
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"GLT\",\n
        \   \"companyName\": \"Glatfelter Corporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"TGI\",\n    \"companyName\": \"Triumph
        Group, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"HLTH\",\n    \"companyName\": \"Cue Health Inc.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"VWAGY\",\n    \"companyName\": \"Volkswagen
        AG\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"WYGPF\",\n
        \   \"companyName\": \"Worley Limited\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"CHK\",\n    \"companyName\": \"Chesapeake Energy
        Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"PERF\",\n    \"companyName\": \"Perfect Corp.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"CSPI\",\n    \"companyName\": \"CSP Inc.\",\n
        \   \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"WSBC\",\n    \"companyName\":
        \"WesBanco, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"601628.SS\",\n    \"companyName\": \"China Life Insurance Company Limited\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"0R0V.L\",\n    \"companyName\":
        \"SunPower Corporation\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\":
        \"FNNNF\",\n    \"companyName\": \"Finnair Oyj\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"DBRG\",\n    \"companyName\": \"DigitalBridge
        Group, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"FAGR.BR\",\n    \"companyName\": \"Fagron N.V.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"GMS\",\n    \"companyName\": \"GMS Inc.\",\n
        \   \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"ATI\",\n    \"companyName\":
        \"ATI Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"ZOM\",\n    \"companyName\": \"Zomedica Corp.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"BBAS3.SA\",\n    \"companyName\": \"Banco
        do Brasil S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"VALMT.HE\",\n    \"companyName\": \"Valmet Oyj\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"EYPT\",\n    \"companyName\": \"EyePoint
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"CBIO\",\n    \"companyName\": \"Crescent Biopharma, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"1833.HK\",\n    \"companyName\": \"Ping
        An Healthcare and Technology Company Limited\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"NDA-FI.HE\",\n    \"companyName\": \"Nordea
        Bank Abp\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"QSR\",\n
        \   \"companyName\": \"Restaurant Brands International Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"DAC\",\n    \"companyName\": \"Danaos
        Corporation\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"CJT.TO\",\n    \"companyName\": \"Cargojet Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"SONVF\",\n    \"companyName\": \"Sonova
        Holding AG\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"WG.L\",\n    \"companyName\": \"John Wood Group PLC\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"QD\",\n    \"companyName\": \"Qudian
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"UAVS\",\n
        \   \"companyName\": \"AgEagle Aerial Systems, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"PTCT\",\n    \"companyName\": \"PTC Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"SBSAA\",\n
        \   \"companyName\": \"Spanish Broadcasting System, Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"MTYFF\",\n    \"companyName\": \"MTY Food
        Group Inc.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"AVACF\",\n    \"companyName\": \"Avance Gas Holding Ltd\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"EFX\",\n    \"companyName\": \"Equifax
        Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"FNMA\",\n
        \   \"companyName\": \"Federal National Mortgage Association\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"AXTI\",\n    \"companyName\": \"AXT,
        Inc.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"ALPMF\",\n
        \   \"companyName\": \"Astellas Pharma Inc.\",\n    \"noOfTranscripts\": \"22\"\n
        \ },\n  {\n    \"symbol\": \"NCPL\",\n    \"companyName\": \"Netcapital Inc.\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"TEM\",\n    \"companyName\":
        \"Tempus AI, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"AUTL\",\n    \"companyName\": \"Autolus Therapeutics plc\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"ASC.L\",\n    \"companyName\": \"ASOS
        Plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"006405.KS\",\n
        \   \"companyName\": \"Samsung SDI Co., Ltd.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"8113.T\",\n    \"companyName\": \"Unicharm
        Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"RCG\",\n    \"companyName\": \"RENN Fund, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MOBX\",\n    \"companyName\": \"Mobix
        Labs, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CWAN\",\n    \"companyName\": \"Clearwater Analytics Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"APN.JO\",\n
        \   \"companyName\": \"Aspen Pharmacare Holdings Limited\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"YELLQ\",\n    \"companyName\": \"Yellow
        Corporation\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"NLLSF\",\n    \"companyName\": \"Nel ASA\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"IDN\",\n    \"companyName\": \"Intellicheck,
        Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\": \"KRYS\",\n
        \   \"companyName\": \"Krystal Biotech, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"GRMN\",\n    \"companyName\": \"Garmin
        Ltd.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"TAGOF\",\n
        \   \"companyName\": \"TAG Immobilien AG\",\n    \"noOfTranscripts\": \"13\"\n
        \ },\n  {\n    \"symbol\": \"KGH.WA\",\n    \"companyName\": \"KGHM Polska
        Miedz S.A.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"TRUMF\",\n    \"companyName\": \"Terumo Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"IDHC.L\",\n    \"companyName\": \"Integrated
        Diagnostics Holdings plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"TLS\",\n    \"companyName\": \"Telos Corporation\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"FARO\",\n    \"companyName\": \"FARO
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"ALSRF\",\n    \"companyName\": \"alstria office REIT-AG\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"FULC\",\n    \"companyName\": \"Fulcrum
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"NWVCF\",\n    \"companyName\": \"EnWave Corporation\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"MRNS\",\n    \"companyName\": \"Marinus
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"CVAC\",\n    \"companyName\": \"CureVac N.V.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"PIPR\",\n    \"companyName\": \"Piper
        Sandler Companies\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"BXP\",\n    \"companyName\": \"BXP, Inc.\",\n    \"noOfTranscripts\": \"69\"\n
        \ },\n  {\n    \"symbol\": \"MRO\",\n    \"companyName\": \"Marathon Oil Corporation\",\n
        \   \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"NWL\",\n    \"companyName\":
        \"Newell Brands Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"PSMT\",\n    \"companyName\": \"PriceSmart, Inc.\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"TW\",\n    \"companyName\": \"Tradeweb
        Markets Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"BBDO\",\n    \"companyName\": \"Banco Bradesco S.A.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"BECTY\",\n    \"companyName\": \"Bechtle
        AG\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"VEON.AS\",\n
        \   \"companyName\": \"VEON Ltd.\",\n    \"noOfTranscripts\": \"64\"\n  },\n
        \ {\n    \"symbol\": \"ARQT\",\n    \"companyName\": \"Arcutis Biotherapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"SWDBF\",\n
        \   \"companyName\": \"Swedbank AB (publ)\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"LRCDF\",\n    \"companyName\": \"Laurentian Bank
        of Canada\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"9618.HK\",\n    \"companyName\": \"JD.com, Inc.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"GIII\",\n    \"companyName\": \"G-III
        Apparel Group, Ltd.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"YLWDF\",\n    \"companyName\": \"Yellow Pages Limited\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"CWT\",\n    \"companyName\": \"California
        Water Service Group\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"CDXS\",\n    \"companyName\": \"Codexis, Inc.\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"GLUE\",\n    \"companyName\": \"Monte
        Rosa Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"LPTX\",\n    \"companyName\": \"Leap Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"PRTH\",\n    \"companyName\": \"Priority
        Technology Holdings, Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n
        \   \"symbol\": \"PBTHF\",\n    \"companyName\": \"PointsBet Holdings Limited\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"FSR.JO\",\n
        \   \"companyName\": \"FirstRand Limited\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"EVA\",\n    \"companyName\": \"Enviva Inc.\",\n
        \   \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"AMPL\",\n    \"companyName\":
        \"Amplitude, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"CGTX\",\n    \"companyName\": \"Cognition Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"OUTFF\",\n    \"companyName\": \"Outokumpu
        Oyj\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"HAYN\",\n
        \   \"companyName\": \"Haynes International, Inc.\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"SPNE\",\n    \"companyName\": \"SeaSpine
        Holdings Corporation\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"WAL\",\n    \"companyName\": \"Western Alliance Bancorporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"EGBN\",\n    \"companyName\": \"Eagle
        Bancorp, Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"MASS\",\n    \"companyName\": \"908 Devices Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BDRL\",\n    \"companyName\": \"Blonder
        Tongue Laboratories, Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n
        \   \"symbol\": \"CFB\",\n    \"companyName\": \"CrossFirst Bankshares, Inc.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"AXFOF\",\n    \"companyName\":
        \"Axfood AB (publ)\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"CPCAY\",\n    \"companyName\": \"Cathay Pacific Airways Limited\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"SSUNF\",\n    \"companyName\": \"SIGNA
        Sports United N.V.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"ANSLF\",\n    \"companyName\": \"Ansell Limited\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"CSLR\",\n    \"companyName\": \"Complete
        Solaria, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"BAW.JO\",\n    \"companyName\": \"Barloworld Limited\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"AVI.JO\",\n    \"companyName\": \"AVI
        Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"YACAF\",\n
        \   \"companyName\": \"Yancoal Australia Ltd\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"JUSH.CN\",\n    \"companyName\": \"Jushi
        Holdings Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"SPRO\",\n    \"companyName\": \"Spero Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"PERI\",\n    \"companyName\": \"Perion
        Network Ltd.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\":
        \"LNDAF\",\n    \"companyName\": \"L\xEDnea Directa Aseguradora, S.A.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"HROW\",\n    \"companyName\":
        \"Harrow Health, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"FLG\",\n    \"companyName\": \"Flagstar Financial, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"REPYY\",\n    \"companyName\": \"Repsol,
        S.A.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"BSX\",\n
        \   \"companyName\": \"Boston Scientific Corporation\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"PFGC\",\n    \"companyName\": \"Performance
        Food Group Company\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"SGE.L\",\n    \"companyName\": \"The Sage Group plc\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"WBS\",\n    \"companyName\": \"Webster
        Financial Corporation\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\":
        \"ITMSF\",\n    \"companyName\": \"Intermap Technologies Corporation\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"GEG\",\n    \"companyName\":
        \"Great Elm Group, Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"ENG\",\n    \"companyName\": \"ENGlobal Corporation\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"WEED.TO\",\n    \"companyName\": \"Canopy
        Growth Corporation\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"KLNG\",\n    \"companyName\": \"Koil Energy Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"CFMS\",\n    \"companyName\": \"Conformis,
        Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"MPNGY\",\n
        \   \"companyName\": \"Meituan\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"CTGO\",\n    \"companyName\": \"Contango Ore, Inc.\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"SHWZ\",\n    \"companyName\":
        \"Medicine Man Technologies, Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n
        \ {\n    \"symbol\": \"KLIC\",\n    \"companyName\": \"Kulicke and Soffa Industries,
        Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"NICE\",\n
        \   \"companyName\": \"NICE Ltd.\",\n    \"noOfTranscripts\": \"58\"\n  },\n
        \ {\n    \"symbol\": \"CMCO\",\n    \"companyName\": \"Columbus McKinnon Corporation\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"GOEV\",\n    \"companyName\":
        \"Canoo Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"MSLP\",\n    \"companyName\": \"MusclePharm Corporation\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"0883.HK\",\n    \"companyName\": \"CNOOC
        Limited\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"AG\",\n
        \   \"companyName\": \"First Majestic Silver Corp.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"FF\",\n    \"companyName\": \"FutureFuel
        Corp.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"EQR\",\n
        \   \"companyName\": \"Equity Residential\",\n    \"noOfTranscripts\": \"69\"\n
        \ },\n  {\n    \"symbol\": \"DGICB\",\n    \"companyName\": \"Donegal Group
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"ABUS\",\n
        \   \"companyName\": \"Arbutus Biopharma Corporation\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"DSV.CO\",\n    \"companyName\": \"Dsv
        A/S\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"DII-B.TO\",\n
        \   \"companyName\": \"Dorel Industries Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"ALK-B.CO\",\n    \"companyName\": \"ALK-Abell\xF3
        A/S\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"NEOG\",\n
        \   \"companyName\": \"Neogen Corporation\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"SAR\",\n    \"companyName\": \"Saratoga Investment
        Corp.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"DRW3.DE\",\n
        \   \"companyName\": \"Dr\xE4gerwerk AG & Co. KGaA\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"AVAV\",\n    \"companyName\": \"AeroVironment,
        Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"NSIS-B.CO\",\n
        \   \"companyName\": \"Novozymes A/S\",\n    \"noOfTranscripts\": \"36\"\n
        \ },\n  {\n    \"symbol\": \"SEDG\",\n    \"companyName\": \"SolarEdge Technologies,
        Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"PNDORA.CO\",\n
        \   \"companyName\": \"Pandora A/S\",\n    \"noOfTranscripts\": \"33\"\n  },\n
        \ {\n    \"symbol\": \"PLX\",\n    \"companyName\": \"Protalix BioTherapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"KB\",\n
        \   \"companyName\": \"KB Financial Group Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"CGY.TO\",\n    \"companyName\": \"Calian
        Group Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"DCC.AX\",\n    \"companyName\": \"DigitalX Limited\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"SNV\",\n    \"companyName\": \"Synovus
        Financial Corp.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"OPRA\",\n    \"companyName\": \"Opera Limited\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"GB\",\n    \"companyName\": \"Global
        Blue Group Holding AG\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"MRKR\",\n    \"companyName\": \"Marker Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"AMTX\",\n    \"companyName\": \"Aemetis,
        Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"ALIZF\",\n
        \   \"companyName\": \"Allianz SE\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"UFAB\",\n    \"companyName\": \"Unique Fabricating,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"XRAY\",\n
        \   \"companyName\": \"DENTSPLY SIRONA Inc.\",\n    \"noOfTranscripts\": \"71\"\n
        \ },\n  {\n    \"symbol\": \"AF.PA\",\n    \"companyName\": \"Air France-KLM
        S.A.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"SAH\",\n
        \   \"companyName\": \"Sonic Automotive, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"SQSP\",\n    \"companyName\": \"Squarespace,
        Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"TSM\",\n
        \   \"companyName\": \"Taiwan Semiconductor Manufacturing Company Limited\",\n
        \   \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\": \"SOTK\",\n    \"companyName\":
        \"Sono-Tek Corporation\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"FMCC\",\n    \"companyName\": \"Federal Home Loan Mortgage Corporation\",\n
        \   \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"HRX.TO\",\n
        \   \"companyName\": \"H\xE9roux-Devtek Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"PIII\",\n    \"companyName\": \"P3 Health
        Partners Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"AKTX\",\n    \"companyName\": \"Akari Therapeutics, Plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SRCL\",\n    \"companyName\": \"Stericycle,
        Inc.\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"NHPEF\",\n
        \   \"companyName\": \"New Hope Corporation Limited\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"RF\",\n    \"companyName\": \"Regions
        Financial Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"KOMB.PR\",\n    \"companyName\": \"Komercn\xED banka, a.s.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"TTNMF\",\n    \"companyName\": \"Titanium
        Transportation Group Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"MNSO\",\n    \"companyName\": \"MINISO Group Holding Limited\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"MOMO\",\n    \"companyName\":
        \"Hello Group Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"GFSA3.SA\",\n    \"companyName\": \"Gafisa S.A.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"MDRX\",\n    \"companyName\": \"Veradigm
        Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"TLPPF\",\n
        \   \"companyName\": \"Telix Pharmaceuticals Limited\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"KDDIF\",\n    \"companyName\": \"KDDI
        Corporation\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"LAD\",\n    \"companyName\": \"Lithia Motors, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"FRTX\",\n    \"companyName\": \"Fresh
        Tracks Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n
        \   \"symbol\": \"APH\",\n    \"companyName\": \"Amphenol Corporation\",\n
        \   \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"VICI\",\n    \"companyName\":
        \"VICI Properties Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"SPTJF\",\n    \"companyName\": \"Sinopec Shanghai Petrochemical Company
        Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SFES\",\n
        \   \"companyName\": \"Safeguard Scientifics, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"WF\",\n    \"companyName\": \"Woori Financial
        Group Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"TOLWF\",\n    \"companyName\": \"Trican Well Service Ltd.\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"CPAC\",\n    \"companyName\": \"Cementos
        Pacasmayo S.A.A.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"MOTS\",\n    \"companyName\": \"Motus GI Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"HBR.L\",\n    \"companyName\": \"Harbour
        Energy plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"MKGAF\",\n    \"companyName\": \"Merck KGaA\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"ATZ.TO\",\n    \"companyName\": \"Aritzia
        Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"BBD\",\n
        \   \"companyName\": \"Banco Bradesco S.A.\",\n    \"noOfTranscripts\": \"48\"\n
        \ },\n  {\n    \"symbol\": \"AGYS\",\n    \"companyName\": \"Agilysys, Inc.\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"FOLD\",\n    \"companyName\":
        \"Amicus Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n
        \   \"symbol\": \"CGRN\",\n    \"companyName\": \"Capstone Green Energy Corporation\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"ISDR\",\n    \"companyName\":
        \"Issuer Direct Corporation\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n
        \   \"symbol\": \"AAALF\",\n    \"companyName\": \"Aareal Bank AG\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"NMTC\",\n    \"companyName\": \"NeuroOne
        Medical Technologies Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n
        \ {\n    \"symbol\": \"LUN.TO\",\n    \"companyName\": \"Lundin Mining Corporation\",\n
        \   \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"ENQUF\",\n    \"companyName\":
        \"EnQuest PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"LU\",\n    \"companyName\": \"Lufax Holding Ltd\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"JET.NE\",\n    \"companyName\": \"Global
        Crossing Airlines Group Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n
        \   \"symbol\": \"USFD\",\n    \"companyName\": \"US Foods Holding Corp.\",\n
        \   \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"NEWTP\",\n    \"companyName\":
        \"NewtekOne, Inc. Depositary Shares, Non-Cumulative Perpetual Preferred Stock,
        Series B\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"CWH\",\n
        \   \"companyName\": \"Camping World Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"MPFRF\",\n    \"companyName\": \"Mapfre,
        S.A.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"NTRS\",\n
        \   \"companyName\": \"Northern Trust Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"IBM\",\n    \"companyName\": \"International
        Business Machines Corporation\",\n    \"noOfTranscripts\": \"79\"\n  },\n
        \ {\n    \"symbol\": \"LCTX\",\n    \"companyName\": \"Lineage Cell Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"BKYI\",\n
        \   \"companyName\": \"BIO-key International, Inc.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"PNE.TO\",\n    \"companyName\": \"Pine
        Cliff Energy Ltd.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"ARKO\",\n    \"companyName\": \"Arko Corp.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"APPF\",\n    \"companyName\": \"AppFolio,
        Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"SEPGF\",\n
        \   \"companyName\": \"Superdry plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"DV\",\n    \"companyName\": \"DoubleVerify Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"NWHUF\",\n
        \   \"companyName\": \"NorthWest Healthcare Properties Real Estate Investment
        Trust\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"IP\",\n
        \   \"companyName\": \"International Paper Company\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"RKLB\",\n    \"companyName\": \"Rocket
        Lab USA, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"NEE\",\n    \"companyName\": \"NextEra Energy, Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"NNWWF\",\n    \"companyName\": \"The
        North West Company Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"TLMD\",\n    \"companyName\": \"SOC Telemed, Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"UBER\",\n    \"companyName\": \"Uber Technologies,
        Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"HPQ\",\n
        \   \"companyName\": \"HP Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n
        \ {\n    \"symbol\": \"VXTR.V\",\n    \"companyName\": \"Voxtur Analytics
        Corp.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"MDGEF\",\n
        \   \"companyName\": \"Medigene AG\",\n    \"noOfTranscripts\": \"8\"\n  },\n
        \ {\n    \"symbol\": \"PFC.L\",\n    \"companyName\": \"Petrofac Limited\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"RLLCF\",\n    \"companyName\":
        \"Rolls-Royce Holdings plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n
        \   \"symbol\": \"RPAY\",\n    \"companyName\": \"Repay Holdings Corporation\",\n
        \   \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"3402.T\",\n
        \   \"companyName\": \"Toray Industries, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"NPK.TO\",\n    \"companyName\": \"Verde
        AgriTech Ltd\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"ARKAY\",\n    \"companyName\": \"Arkema S.A.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MGRM\",\n    \"companyName\": \"Monogram
        Orthopaedics, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"NNOX\",\n    \"companyName\": \"Nano-X Imaging Ltd.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"AMX\",\n    \"companyName\": \"Am\xE9rica
        M\xF3vil, S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n
        \   \"symbol\": \"NTAP\",\n    \"companyName\": \"NetApp, Inc.\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"BURBY\",\n    \"companyName\": \"Burberry
        Group plc\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"CWCO\",\n    \"companyName\": \"Consolidated Water Co. Ltd.\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"METC\",\n    \"companyName\": \"Ramaco
        Resources, Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"SPCB\",\n    \"companyName\": \"SuperCom Ltd.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"YCBD\",\n    \"companyName\": \"cbdMD,
        Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"PENN\",\n
        \   \"companyName\": \"PENN Entertainment, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"OILSF\",\n    \"companyName\": \"Saturn
        Oil & Gas Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"ROKU\",\n    \"companyName\": \"Roku, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"MPVDF\",\n    \"companyName\": \"Mountain
        Province Diamonds Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"CFRHF\",\n    \"companyName\": \"Compagnie Financi\xE8re Richemont S.A.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"RJF\",\n    \"companyName\":
        \"Raymond James Financial, Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n
        \ {\n    \"symbol\": \"NOG\",\n    \"companyName\": \"Northern Oil and Gas,
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"SG\",\n
        \   \"companyName\": \"Sweetgreen, Inc.\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"TIGO-SDB.ST\",\n    \"companyName\": \"Millicom
        International Cellular S.A.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n
        \   \"symbol\": \"EXPRQ\",\n    \"companyName\": \"Express, Inc.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"LPTH\",\n    \"companyName\": \"LightPath
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"TTBXF\",\n    \"companyName\": \"Tritax Big Box REIT plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"FLWPF\",\n    \"companyName\": \"The Flowr
        Corporation\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"OSK\",\n    \"companyName\": \"Oshkosh Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"TPK.L\",\n    \"companyName\": \"Travis
        Perkins plc\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"LVO\",\n    \"companyName\": \"LiveOne, Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"8035.T\",\n    \"companyName\": \"Tokyo
        Electron Limited\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"MOND\",\n    \"companyName\": \"Mondee Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"LOAN\",\n    \"companyName\": \"Manhattan
        Bridge Capital, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"TCLRY\",\n    \"companyName\": \"Technicolor S.A.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"ROSN.ME\",\n    \"companyName\": \"PJSC
        Rosneft Oil Company\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"FEDU\",\n    \"companyName\": \"Four Seasons Education (Cayman) Inc.\",\n
        \   \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"ILU.AX\",\n
        \   \"companyName\": \"Iluka Resources Limited\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"TTCFQ\",\n    \"companyName\": \"Tattooed
        Chef, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"RET-A.V\",\n    \"companyName\": \"Reitmans (Canada) Limited\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"VKTX\",\n    \"companyName\": \"Viking
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\":
        \"HY\",\n    \"companyName\": \"Hyster-Yale Materials Handling, Inc.\",\n
        \   \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"SGBX\",\n    \"companyName\":
        \"Safe & Green Holdings Corp.\",\n    \"noOfTranscripts\": \"24\"\n  },\n
        \ {\n    \"symbol\": \"NBN\",\n    \"companyName\": \"Northeast Bank\",\n
        \   \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\": \"SUZ\",\n    \"companyName\":
        \"Suzano S.A.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"MAXN\",\n    \"companyName\": \"Maxeon Solar Technologies, Ltd.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"CRZBF\",\n    \"companyName\": \"Commerzbank
        AG\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"CX\",\n
        \   \"companyName\": \"CEMEX, S.A.B. de C.V.\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"ACSAF\",\n    \"companyName\": \"ACS,
        Actividades de Construcci\xF3n y Servicios, S.A.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"LGGNF\",\n    \"companyName\": \"Legal
        & General Group Plc\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"TSVT\",\n    \"companyName\": \"2seventy bio, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"YAR.OL\",\n    \"companyName\": \"Yara
        International ASA\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"MTTR\",\n    \"companyName\": \"Matterport, Inc.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"LNVGY\",\n    \"companyName\": \"Lenovo
        Group Limited\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"LGRVF\",\n    \"companyName\": \"Legrand S.A.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"OUST\",\n    \"companyName\": \"Ouster,
        Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"RMBS\",\n
        \   \"companyName\": \"Rambus Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n
        \ {\n    \"symbol\": \"KORE\",\n    \"companyName\": \"KORE Group Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"BOMBF\",\n
        \   \"companyName\": \"Bombardier Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"CANF.TA\",\n    \"companyName\": \"Can-Fite BioPharma
        Ltd.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"NRXP\",\n
        \   \"companyName\": \"NRx Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"JAN\",\n    \"companyName\": \"JanOne
        Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"VEXTF\",\n
        \   \"companyName\": \"Vext Science, Inc.\",\n    \"noOfTranscripts\": \"16\"\n
        \ },\n  {\n    \"symbol\": \"CRIS\",\n    \"companyName\": \"Curis, Inc.\",\n
        \   \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"ZWS\",\n    \"companyName\":
        \"Zurn Elkay Water Solutions Corporation\",\n    \"noOfTranscripts\": \"49\"\n
        \ },\n  {\n    \"symbol\": \"DAKT\",\n    \"companyName\": \"Daktronics, Inc.\",\n
        \   \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"MOWI.OL\",\n
        \   \"companyName\": \"Mowi ASA\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"PPL.TO\",\n    \"companyName\": \"Pembina Pipeline
        Corporation\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"CURV\",\n    \"companyName\": \"Torrid Holdings Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"MESO\",\n    \"companyName\": \"Mesoblast
        Limited\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"JRONF\",\n
        \   \"companyName\": \"Jer\xF3nimo Martins, SGPS, S.A.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"22UA.F\",\n    \"companyName\": \"BioNTech
        SE\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"NEON\",\n
        \   \"companyName\": \"Neonode Inc.\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"CVCO\",\n    \"companyName\": \"Cavco Industries,
        Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"INTR\",\n
        \   \"companyName\": \"Inter & Co, Inc.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"FVRR\",\n    \"companyName\": \"Fiverr International
        Ltd.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"PAGE.L\",\n
        \   \"companyName\": \"PageGroup plc\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"HCI\",\n    \"companyName\": \"HCI Group, Inc.\",\n
        \   \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"MESA\",\n    \"companyName\":
        \"Mesa Air Group, Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"XPON\",\n    \"companyName\": \"Expion360 Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"SPXCF\",\n    \"companyName\": \"Singapore
        Exchange Limited\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"CMIG4.SA\",\n    \"companyName\": \"Companhia Energ\xE9tica de Minas Gerais\",\n
        \   \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"BAK\",\n    \"companyName\":
        \"Braskem S.A.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"ADYEY\",\n    \"companyName\": \"Adyen N.V.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"VFF\",\n    \"companyName\": \"Village
        Farms International, Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n
        \   \"symbol\": \"CEZ.PR\",\n    \"companyName\": \"CEZ, a. s.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"KIERF\",\n    \"companyName\": \"Kier
        Group plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"NMRK\",\n
        \   \"companyName\": \"Newmark Group, Inc.\",\n    \"noOfTranscripts\": \"30\"\n
        \ },\n  {\n    \"symbol\": \"ALTI\",\n    \"companyName\": \"AlTi Global,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"AZREF\",\n
        \   \"companyName\": \"Azure Power Global Limited\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"TMRAY\",\n    \"companyName\": \"Tomra
        Systems ASA\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"LYV\",\n    \"companyName\": \"Live Nation Entertainment, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"DMTKQ\",\n    \"companyName\": \"DermTech,
        Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"LOG.MC\",\n
        \   \"companyName\": \"Logista Integral, S.A.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"DXYN\",\n    \"companyName\": \"The Dixie
        Group, Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"ATIP\",\n    \"companyName\": \"ATI Physical Therapy, Inc.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"DYNT\",\n    \"companyName\": \"Dynatronics
        Corporation\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"TG\",\n    \"companyName\": \"Tredegar Corporation\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"CIDM\",\n    \"companyName\": \"Cinedigm
        Corp.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"ALB\",\n
        \   \"companyName\": \"Albemarle Corporation\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"ADN\",\n    \"companyName\": \"Advent
        Technologies Holdings, Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n
        \   \"symbol\": \"CDMGF\",\n    \"companyName\": \"Icade S.A.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"OLN\",\n    \"companyName\": \"Olin Corporation\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"VID.MC\",\n
        \   \"companyName\": \"Vidrala, S.A.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"VIV.PA\",\n    \"companyName\": \"Vivendi SE\",\n
        \   \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"MAPS\",\n    \"companyName\":
        \"WM Technology, Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"NOAH\",\n    \"companyName\": \"Noah Holdings Limited\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"TCL-B.TO\",\n    \"companyName\": \"Transcontinental
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"USA.TO\",\n
        \   \"companyName\": \"Americas Gold and Silver Corporation\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"SNWV\",\n    \"companyName\": \"SANUWAVE
        Health, Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"PXS\",\n    \"companyName\": \"Pyxis Tankers Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"SEYMF\",\n    \"companyName\": \"Solaria
        Energ\xEDa y Medio Ambiente, S.A.\",\n    \"noOfTranscripts\": \"8\"\n  },\n
        \ {\n    \"symbol\": \"WHD\",\n    \"companyName\": \"Cactus, Inc.\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"CCDBF\",\n    \"companyName\": \"CCL
        Industries Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\":
        \"TNGRF\",\n    \"companyName\": \"Thungela Resources Limited\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"AMGDF\",\n    \"companyName\": \"Aston
        Martin Lagonda Global Holdings plc\",\n    \"noOfTranscripts\": \"11\"\n  },\n
        \ {\n    \"symbol\": \"ORSTED.CO\",\n    \"companyName\": \"\xD8rsted A/S\",\n
        \   \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"STER\",\n    \"companyName\":
        \"Sterling Check Corp.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"NM\",\n    \"companyName\": \"Navios Maritime Holdings Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"VIRT\",\n    \"companyName\": \"Virtu
        Financial, Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"RQHTF\",\n    \"companyName\": \"Reliq Health Technologies Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"NETL\",\n    \"companyName\": \"Fundamental
        Income Net Lease Real Estate ETF\",\n    \"noOfTranscripts\": \"8\"\n  },\n
        \ {\n    \"symbol\": \"PECO\",\n    \"companyName\": \"Phillips Edison & Company,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"ONEXF\",\n
        \   \"companyName\": \"Onex Corporation\",\n    \"noOfTranscripts\": \"47\"\n
        \ },\n  {\n    \"symbol\": \"FPAFY\",\n    \"companyName\": \"First Pacific
        Company Limited\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"AJINY\",\n    \"companyName\": \"Ajinomoto Co., Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"GCO\",\n    \"companyName\": \"Genesco
        Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"4901.T\",\n
        \   \"companyName\": \"FUJIFILM Holdings Corporation\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"BQSSF\",\n    \"companyName\": \"Boss
        Energy Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CIR\",\n    \"companyName\": \"CIRCOR International, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"CWD\",\n    \"companyName\": \"CaliberCos
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"IDCBY\",\n
        \   \"companyName\": \"Industrial & Commercial Bank of China Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"XLNX\",\n    \"companyName\": \"Xilinx,
        Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"POCI\",\n
        \   \"companyName\": \"Precision Optics Corporation, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"CVSI\",\n    \"companyName\": \"CV Sciences,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"MWRK\",\n
        \   \"companyName\": \"MetaWorks Platforms, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"ADXS\",\n    \"companyName\": \"Ayala
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"UFPT\",\n    \"companyName\": \"UFP Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"VLNSF\",\n    \"companyName\": \"Velan
        Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"CHALF\",\n
        \   \"companyName\": \"Chalice Brands Ltd.\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"PCAR3.SA\",\n    \"companyName\": \"Companhia
        Brasileira de Distribui\xE7\xE3o\",\n    \"noOfTranscripts\": \"30\"\n  },\n
        \ {\n    \"symbol\": \"H\",\n    \"companyName\": \"Hyatt Hotels Corporation\",\n
        \   \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\": \"RMGGF\",\n    \"companyName\":
        \"Resolute Mining Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n
        \   \"symbol\": \"BNED\",\n    \"companyName\": \"Barnes & Noble Education,
        Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"FRBA\",\n
        \   \"companyName\": \"First Bank\",\n    \"noOfTranscripts\": \"30\"\n  },\n
        \ {\n    \"symbol\": \"SVCBF\",\n    \"companyName\": \"Svenska Cellulosa
        Aktiebolaget SCA (publ)\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"CGBD\",\n    \"companyName\": \"Carlyle Secured Lending, Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"HERXF\",\n    \"companyName\": \"H\xE9roux-Devtek
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"PINC\",\n
        \   \"companyName\": \"Premier, Inc.\",\n    \"noOfTranscripts\": \"48\"\n
        \ },\n  {\n    \"symbol\": \"ZS\",\n    \"companyName\": \"Zscaler, Inc.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"RKT.L\",\n    \"companyName\":
        \"Reckitt Benckiser Group plc\",\n    \"noOfTranscripts\": \"38\"\n  },\n
        \ {\n    \"symbol\": \"PULM\",\n    \"companyName\": \"Pulmatrix, Inc.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"PMTS\",\n    \"companyName\":
        \"CPI Card Group Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"MEG.TO\",\n    \"companyName\": \"MEG Energy Corp.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"LOCL\",\n    \"companyName\": \"Local
        Bounti Corporation\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"STGW\",\n    \"companyName\": \"Stagwell Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"LVS\",\n    \"companyName\": \"Las Vegas
        Sands Corp.\",\n    \"noOfTranscripts\": \"77\"\n  },\n  {\n    \"symbol\":
        \"SBAC\",\n    \"companyName\": \"SBA Communications Corporation\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"DBX\",\n    \"companyName\": \"Dropbox,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"EIFZF\",\n
        \   \"companyName\": \"Exchange Income Corporation\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"DXCM\",\n    \"companyName\": \"DexCom,
        Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"EVVTY\",\n
        \   \"companyName\": \"Evolution AB (publ)\",\n    \"noOfTranscripts\": \"11\"\n
        \ },\n  {\n    \"symbol\": \"VNOM\",\n    \"companyName\": \"Viper Energy,
        Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"PDEX\",\n
        \   \"companyName\": \"Pro-Dex, Inc.\",\n    \"noOfTranscripts\": \"13\"\n
        \ },\n  {\n    \"symbol\": \"TNON\",\n    \"companyName\": \"Tenon Medical,
        Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"PRU\",\n
        \   \"companyName\": \"Prudential Financial, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"MTB\",\n    \"companyName\": \"M&T Bank
        Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"GLOB\",\n    \"companyName\": \"Globant S.A.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"IVFH\",\n    \"companyName\": \"Innovative
        Food Holdings, Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"PATK\",\n    \"companyName\": \"Patrick Industries, Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"ABT\",\n    \"companyName\": \"Abbott
        Laboratories\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"TRRSF\",\n    \"companyName\": \"Trisura Group Ltd.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"6460.T\",\n    \"companyName\": \"Sega
        Sammy Holdings Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"QNCX\",\n    \"companyName\": \"Quince Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"BWLKF\",\n    \"companyName\": \"Boardwalktech
        Software Corp.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"CESDF\",\n    \"companyName\": \"CES Energy Solutions Corp.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"JINFF\",\n    \"companyName\": \"China
        Gold International Resources Corp. Ltd.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"PCRFF\",\n    \"companyName\": \"Panasonic Holdings
        Corporation\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"3659.T\",\n    \"companyName\": \"NEXON Co., Ltd.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"NTXVF\",\n    \"companyName\": \"Nexteer
        Automotive Group Limited\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"STON\",\n    \"companyName\": \"StoneMor Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"NDSN\",\n    \"companyName\": \"Nordson
        Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"STOR\",\n    \"companyName\": \"STORE Capital Corporation\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"PLZL.IL\",\n    \"companyName\": \"PJSC
        Polyus\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"UBSI\",\n
        \   \"companyName\": \"United Bankshares, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"KITS.TO\",\n    \"companyName\": \"Kits
        Eyecare Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"HGHAF\",\n    \"companyName\": \"High Arctic Energy Services Inc\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"XBIO\",\n    \"companyName\": \"Xenetic
        Biosciences, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"BEEP\",\n    \"companyName\": \"Mobile Infrastructure Corporation\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"BKKT\",\n    \"companyName\": \"Bakkt
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"AMSSY\",\n    \"companyName\": \"ams-OSRAM AG\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"BMRRY\",\n    \"companyName\": \"B&M
        European Value Retail S.A.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"CHWY\",\n    \"companyName\": \"Chewy, Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"TSAT.TO\",\n    \"companyName\": \"Telesat
        Corporation\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"OCINF\",\n    \"companyName\": \"Oci N.V.\",\n    \"noOfTranscripts\": \"19\"\n
        \ },\n  {\n    \"symbol\": \"BBIO\",\n    \"companyName\": \"BridgeBio Pharma,
        Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"TCMD\",\n
        \   \"companyName\": \"Tactile Systems Technology, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"INSG\",\n    \"companyName\": \"Inseego
        Corp.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"QBEIF\",\n
        \   \"companyName\": \"QBE Insurance Group Limited\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MAHMF\",\n    \"companyName\": \"Mahindra
        & Mahindra Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"SPMC\",\n    \"companyName\": \"Sound Point Meridian Capital Inc\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"INLX\",\n    \"companyName\": \"Intellinetics,
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"HUSQF\",\n
        \   \"companyName\": \"Husqvarna AB (publ)\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"DNA\",\n    \"companyName\": \"Ginkgo Bioworks
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"QRTEA\",\n    \"companyName\": \"Qurate Retail, Inc.\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"NFYEF\",\n    \"companyName\": \"NFI
        Group Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"DAVA\",\n    \"companyName\": \"Endava plc\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"HPURF\",\n    \"companyName\": \"Hexagon
        Purus ASA\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"KKR\",\n
        \   \"companyName\": \"KKR & Co. Inc.\",\n    \"noOfTranscripts\": \"66\"\n
        \ },\n  {\n    \"symbol\": \"GRAL\",\n    \"companyName\": \"GRAIL, Inc.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"UHG\",\n    \"companyName\":
        \"United Homes Group, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"RNECF\",\n    \"companyName\": \"Renesas Electronics Corporation\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"CDE\",\n    \"companyName\":
        \"Coeur Mining, Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"BN\",\n    \"companyName\": \"Brookfield Corporation\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"CI\",\n    \"companyName\": \"The Cigna
        Group\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"JRONY\",\n
        \   \"companyName\": \"Jer\xF3nimo Martins, SGPS, S.A.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"AIRG\",\n    \"companyName\": \"Airgain,
        Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"EFX.TO\",\n
        \   \"companyName\": \"Enerflex Ltd.\",\n    \"noOfTranscripts\": \"34\"\n
        \ },\n  {\n    \"symbol\": \"MTL.TO\",\n    \"companyName\": \"Mullen Group
        Ltd.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"ARCT\",\n
        \   \"companyName\": \"Arcturus Therapeutics Holdings Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"FALC\",\n    \"companyName\": \"FalconStor
        Software, Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"XPEL\",\n    \"companyName\": \"XPEL, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"SIVB\",\n    \"companyName\": \"SVB Financial
        Group\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"ICCC\",\n
        \   \"companyName\": \"ImmuCell Corporation\",\n    \"noOfTranscripts\": \"44\"\n
        \ },\n  {\n    \"symbol\": \"ENZ\",\n    \"companyName\": \"Enzo Biochem,
        Inc.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"TYEKF\",\n
        \   \"companyName\": \"thyssenkrupp AG\",\n    \"noOfTranscripts\": \"34\"\n
        \ },\n  {\n    \"symbol\": \"CGC\",\n    \"companyName\": \"Canopy Growth
        Corporation\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"MTLS\",\n    \"companyName\": \"Materialise N.V.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"OCFC\",\n    \"companyName\": \"OceanFirst
        Financial Corp.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"4091.T\",\n    \"companyName\": \"Nippon Sanso Holdings Corporation\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"ENGGF\",\n    \"companyName\":
        \"Enag\xE1s, S.A.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"AVCN.TO\",\n    \"companyName\": \"Avicanna Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"ZEPP\",\n    \"companyName\": \"Zepp Health
        Corporation\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"LIFW\",\n    \"companyName\": \"MSP Recovery, Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"LAND\",\n    \"companyName\": \"Gladstone
        Land Corporation\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"ATCO\",\n    \"companyName\": \"Atlas Corp.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"B\",\n    \"companyName\": \"Barrick
        Mining Corporation\",\n    \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\":
        \"LFMD\",\n    \"companyName\": \"LifeMD, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"BAESY\",\n    \"companyName\": \"BAE
        Systems plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"GMGI\",\n    \"companyName\": \"Golden Matrix Group, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"PRIM\",\n    \"companyName\": \"Primoris
        Services Corporation\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"WISA\",\n    \"companyName\": \"WiSA Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"BNXA.V\",\n    \"companyName\": \"Banxa
        Holdings Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"FLIC\",\n    \"companyName\": \"The First of Long Island Corporation\",\n
        \   \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"MRE.TO\",\n    \"companyName\":
        \"Martinrea International Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n
        \ {\n    \"symbol\": \"EXPO\",\n    \"companyName\": \"Exponent, Inc.\",\n
        \   \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"NANX\",\n    \"companyName\":
        \"Nanophase Technologies Corporation\",\n    \"noOfTranscripts\": \"44\"\n
        \ },\n  {\n    \"symbol\": \"MRSN\",\n    \"companyName\": \"Mersana Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"TBIO\",\n
        \   \"companyName\": \"Telesis Bio, Inc.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"NAPA\",\n    \"companyName\": \"The Duckhorn
        Portfolio, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"ENW.V\",\n    \"companyName\": \"EnWave Corporation\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"MLSPF\",\n    \"companyName\": \"Melrose
        Industries PLC\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"ITP\",\n    \"companyName\": \"IT Tech Packaging, Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"ACGBY\",\n    \"companyName\": \"Agricultural
        Bank of China Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"ESALF\",\n    \"companyName\": \"Eisai Co., Ltd.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"PEG\",\n    \"companyName\": \"Public
        Service Enterprise Group Incorporated\",\n    \"noOfTranscripts\": \"76\"\n
        \ },\n  {\n    \"symbol\": \"ZIZTF\",\n    \"companyName\": \"Zip Co Limited\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"BRKR\",\n    \"companyName\":
        \"Bruker Corporation\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"BWLK.V\",\n    \"companyName\": \"Boardwalktech Software Corp.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"WJXFF\",\n    \"companyName\": \"Wajax
        Corporation\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"OMER\",\n    \"companyName\": \"Omeros Corporation\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"STCN\",\n    \"companyName\": \"Steel
        Connect, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"8591.T\",\n    \"companyName\": \"ORIX Corporation\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"BRSL\",\n    \"companyName\": \"Brightstar
        Lottery\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"BBTV.TO\",\n
        \   \"companyName\": \"BBTV Holdings Inc.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"VEDL\",\n    \"companyName\": \"Vedanta Limited\",\n
        \   \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"FLY.V\",\n    \"companyName\":
        \"FLYHT Aerospace Solutions Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n
        \ {\n    \"symbol\": \"ENZB\",\n    \"companyName\": \"Enzo Biochem, Inc.\",\n
        \   \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"SUM\",\n    \"companyName\":
        \"Summit Materials, Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n
        \   \"symbol\": \"6758.T\",\n    \"companyName\": \"Sony Group Corporation\",\n
        \   \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"RNWEF\",\n    \"companyName\":
        \"REC Silicon ASA\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"FLYLF\",\n    \"companyName\": \"FLYHT Aerospace Solutions Ltd.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"BA.L\",\n    \"companyName\": \"BAE Systems
        plc\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"BIOR\",\n
        \   \"companyName\": \"Biora Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"BWIN\",\n    \"companyName\": \"The Baldwin
        Insurance Group, Inc.\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\":
        \"SAIC\",\n    \"companyName\": \"Science Applications International Corporation\",\n
        \   \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"RET.V\",\n    \"companyName\":
        \"Reitmans (Canada) Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"TX\",\n    \"companyName\": \"Ternium S.A.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"VIOT\",\n    \"companyName\": \"Viomi
        Technology Co., Ltd\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"EVLO\",\n    \"companyName\": \"Evelo Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"EXK\",\n    \"companyName\": \"Endeavour
        Silver Corp.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"TYGO\",\n    \"companyName\": \"Tigo Energy, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"600028.SS\",\n    \"companyName\": \"China
        Petroleum & Chemical Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"NXP\",\n    \"companyName\": \"Nuveen Select Tax-Free
        Income Portfolio\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"ESLOF\",\n    \"companyName\": \"EssilorLuxottica S.A.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"PRAA\",\n    \"companyName\": \"PRA Group,
        Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"XERS\",\n
        \   \"companyName\": \"Xeris Biopharma Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"FLL\",\n    \"companyName\": \"Full House
        Resorts, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"6503.T\",\n    \"companyName\": \"Mitsubishi Electric Corporation\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"IDRSF\",\n    \"companyName\": \"Idorsia
        Ltd\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"DIIBF\",\n
        \   \"companyName\": \"Dorel Industries Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"EEX\",\n    \"companyName\": \"Emerald
        Holding, Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"RWAY\",\n    \"companyName\": \"Runway Growth Finance Corp.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"ZGN\",\n    \"companyName\": \"Ermenegildo
        Zegna N.V.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"RNGR\",\n    \"companyName\": \"Ranger Energy Services, Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"DPBSF\",\n    \"companyName\": \"Dampskibsselskabet
        Norden A/S\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"VLXGF\",\n    \"companyName\": \"Volex plc\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"IFNNF\",\n    \"companyName\": \"Infineon
        Technologies AG\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"LEN\",\n    \"companyName\": \"Lennar Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"PKKFF\",\n    \"companyName\": \"Tenet
        Fintech Group Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"AML.L\",\n    \"companyName\": \"Aston Martin Lagonda Global Holdings plc\",\n
        \   \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"VENU\",\n    \"companyName\":
        \"Venu Holding Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"TXT\",\n    \"companyName\": \"Textron Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"IAUX\",\n    \"companyName\": \"i-80
        Gold Corp.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"CULP\",\n    \"companyName\": \"Culp, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"JPPYY\",\n    \"companyName\": \"Jupai
        Holdings Limited\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"BANL\",\n    \"companyName\": \"CBL International Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"UIS\",\n    \"companyName\": \"Unisys
        Corporation\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"4578.T\",\n    \"companyName\": \"Otsuka Holdings Co., Ltd.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SSP\",\n    \"companyName\": \"The E.W.
        Scripps Company\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\":
        \"ZUO\",\n    \"companyName\": \"Zuora, Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"MUSA\",\n    \"companyName\": \"Murphy
        USA Inc.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"ISPO\",\n
        \   \"companyName\": \"Inspirato Incorporated\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"EKTAF\",\n    \"companyName\": \"Elekta
        AB (publ)\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"CALX\",\n    \"companyName\": \"Calix, Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"BSY\",\n    \"companyName\": \"Bentley
        Systems, Incorporated\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"AMWL\",\n    \"companyName\": \"American Well Corporation\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"FOOD.TO\",\n    \"companyName\": \"Goodfood
        Market Corp.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"VERX\",\n    \"companyName\": \"Vertex, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"BG\",\n    \"companyName\": \"Bunge Global
        S.A.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"PTEC.L\",\n
        \   \"companyName\": \"Playtech plc\",\n    \"noOfTranscripts\": \"20\"\n
        \ },\n  {\n    \"symbol\": \"SPGYF\",\n    \"companyName\": \"Whitecap Resources
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"SSTK\",\n
        \   \"companyName\": \"Shutterstock, Inc.\",\n    \"noOfTranscripts\": \"49\"\n
        \ },\n  {\n    \"symbol\": \"IPG\",\n    \"companyName\": \"The Interpublic
        Group of Companies, Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n
        \   \"symbol\": \"MRL.L\",\n    \"companyName\": \"Marlowe plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"WEN\",\n    \"companyName\": \"The Wendy's
        Company\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"SECOY\",\n
        \   \"companyName\": \"Secoo Holding Limited\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"GS\",\n    \"companyName\": \"The Goldman
        Sachs Group, Inc.\",\n    \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\":
        \"CXBMF\",\n    \"companyName\": \"Calibre Mining Corp.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"CF\",\n    \"companyName\": \"CF Industries
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"NBEV\",\n    \"companyName\": \"NewAge, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"IVN.TO\",\n    \"companyName\": \"Ivanhoe
        Mines Ltd.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"JD\",\n    \"companyName\": \"JD.com, Inc.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"JSNSF\",\n    \"companyName\": \"J Sainsbury
        plc\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"RZLV\",\n
        \   \"companyName\": \"Rezolve AI PLC\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"RGCO\",\n    \"companyName\": \"RGC Resources,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"BWEN\",\n
        \   \"companyName\": \"Broadwind, Inc.\",\n    \"noOfTranscripts\": \"53\"\n
        \ },\n  {\n    \"symbol\": \"BLND\",\n    \"companyName\": \"Blend Labs, Inc.\",\n
        \   \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"GARAN.IS\",\n
        \   \"companyName\": \"Turkiye Garanti Bankasi A.S.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"6702.T\",\n    \"companyName\": \"Fujitsu
        Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"PLTK\",\n
        \   \"companyName\": \"Playtika Holding Corp.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"AKRBP.OL\",\n    \"companyName\": \"Aker
        BP ASA\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"LIVN\",\n
        \   \"companyName\": \"LivaNova PLC\",\n    \"noOfTranscripts\": \"38\"\n
        \ },\n  {\n    \"symbol\": \"ACR\",\n    \"companyName\": \"ACRES Commercial
        Realty Corp.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"ENOV\",\n    \"companyName\": \"Enovis Corporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"NFE\",\n    \"companyName\": \"New Fortress
        Energy Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"UMC\",\n    \"companyName\": \"United Microelectronics Corporation\",\n
        \   \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\": \"HAL\",\n    \"companyName\":
        \"Halliburton Company\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"CNVVF\",\n    \"companyName\": \"ConvaTec Group Plc\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"EDNMF\",\n    \"companyName\": \"Edenred
        S.A.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"RELI\",\n
        \   \"companyName\": \"Reliance Global Group, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"PLT\",\n    \"companyName\": \"Defiance
        Leveraged Long Income PLTR ETF\",\n    \"noOfTranscripts\": \"58\"\n  },\n
        \ {\n    \"symbol\": \"TRIRF\",\n    \"companyName\": \"Triterras, Inc.\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"RTLR\",\n    \"companyName\":
        \"Rattler Midstream LP\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"CLAR\",\n    \"companyName\": \"Clarus Corporation\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"GTN\",\n    \"companyName\": \"Gray Media,
        Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"WEYS\",\n
        \   \"companyName\": \"Weyco Group, Inc.\",\n    \"noOfTranscripts\": \"57\"\n
        \ },\n  {\n    \"symbol\": \"SONM\",\n    \"companyName\": \"Sonim Technologies,
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"8058.T\",\n
        \   \"companyName\": \"Mitsubishi Corporation\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"VEEE\",\n    \"companyName\": \"Twin
        Vee Powercats Co.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"AC.MX\",\n    \"companyName\": \"Arca Continental, S.A.B. de C.V.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"EBR\",\n    \"companyName\": \"Centrais
        El\xE9tricas Brasileiras S.A. - Eletrobr\xE1s\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"MPH.V\",\n    \"companyName\": \"Medicure
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"VIASP\",\n
        \   \"companyName\": \"Via Renewables, Inc.\",\n    \"noOfTranscripts\": \"39\"\n
        \ },\n  {\n    \"symbol\": \"TBHC\",\n    \"companyName\": \"The Brand House
        Collective, Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"HWO.TO\",\n    \"companyName\": \"High Arctic Energy Services Inc\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"WMMVY\",\n    \"companyName\": \"Wal-Mart
        de M\xE9xico, S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n
        \   \"symbol\": \"WILD.TO\",\n    \"companyName\": \"WildBrain Ltd.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"NXPI\",\n    \"companyName\": \"NXP Semiconductors
        N.V.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"GIB\",\n
        \   \"companyName\": \"CGI Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n
        \ {\n    \"symbol\": \"ICLK\",\n    \"companyName\": \"iClick Interactive
        Asia Group Limited\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"ANNSF\",\n    \"companyName\": \"Aena S.M.E., S.A.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"MAC\",\n    \"companyName\": \"The Macerich
        Company\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"FUPBY\",\n
        \   \"companyName\": \"Fuchs Petrolub SE\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"TKC\",\n    \"companyName\": \"Turkcell Iletisim
        Hizmetleri A.S.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"CAR\",\n    \"companyName\": \"Avis Budget Group, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"INNV\",\n    \"companyName\": \"InnovAge
        Holding Corp.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"YMM\",\n    \"companyName\": \"Full Truck Alliance Co. Ltd.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"PBH.AX\",\n    \"companyName\": \"PointsBet
        Holdings Limited\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"SGH\",\n    \"companyName\": \"SMART Global Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"ASO\",\n    \"companyName\": \"Academy
        Sports and Outdoors, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n
        \   \"symbol\": \"NOMD\",\n    \"companyName\": \"Nomad Foods Limited\",\n
        \   \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"KRKR\",\n    \"companyName\":
        \"36Kr Holdings Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"K.TO\",\n    \"companyName\": \"Kinross Gold Corporation\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"MDT\",\n    \"companyName\": \"Medtronic
        plc\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"DNTUF\",\n
        \   \"companyName\": \"Dentsu Group Inc.\",\n    \"noOfTranscripts\": \"22\"\n
        \ },\n  {\n    \"symbol\": \"CNPOF\",\n    \"companyName\": \"RIV Capital
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"HUBG\",\n
        \   \"companyName\": \"Hub Group, Inc.\",\n    \"noOfTranscripts\": \"62\"\n
        \ },\n  {\n    \"symbol\": \"CRES.BA\",\n    \"companyName\": \"Cresud Sociedad
        An\xF3nima, Comercial, Inmobiliaria, Financiera y Agropecuaria\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"VC\",\n    \"companyName\": \"Visteon
        Corporation\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"EVS.BR\",\n    \"companyName\": \"EVS Broadcast Equipment S.A.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"HTHIY\",\n    \"companyName\": \"Hitachi,
        Ltd.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\": \"6762.T\",\n
        \   \"companyName\": \"TDK Corporation\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"HTLF\",\n    \"companyName\": \"Heartland Financial
        USA, Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"CWRK\",\n    \"companyName\": \"CurrencyWorks Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"SWAV\",\n    \"companyName\": \"ShockWave
        Medical, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"MAT\",\n    \"companyName\": \"Mattel, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"CELP\",\n    \"companyName\": \"Cypress
        Environmental Partners, L.P.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n
        \   \"symbol\": \"GAME\",\n    \"companyName\": \"GameSquare Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"0Y4Q.L\",\n
        \   \"companyName\": \"Willis Towers Watson Public Limited Company\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"SWDAF\",\n    \"companyName\": \"Software
        AG\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"HTGMQ\",\n
        \   \"companyName\": \"HTG Molecular Diagnostics, Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"SRZN\",\n    \"companyName\": \"Surrozen,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ROIV\",\n
        \   \"companyName\": \"Roivant Sciences Ltd.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"CACC\",\n    \"companyName\": \"Credit
        Acceptance Corporation\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"ORA\",\n    \"companyName\": \"Ormat Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"DNSKF\",\n    \"companyName\": \"Danske
        Bank A/S\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"TONX\",\n
        \   \"companyName\": \"TON Strategy Co.\",\n    \"noOfTranscripts\": \"16\"\n
        \ },\n  {\n    \"symbol\": \"KNRLF\",\n    \"companyName\": \"Kontrol Technologies
        Corp.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"PONY\",\n
        \   \"companyName\": \"Pony AI Inc. American Depositary Shares\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"CEO\",\n    \"companyName\": \"CNOOC Limited\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"MRK\",\n    \"companyName\":
        \"Merck & Co., Inc.\",\n    \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\":
        \"LMND\",\n    \"companyName\": \"Lemonade, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"TRAW\",\n    \"companyName\": \"Traws
        Pharma, Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"AFRAF\",\n    \"companyName\": \"Air France-KLM S.A.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"SVA\",\n    \"companyName\": \"Sinovac
        Biotech Ltd.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"HYMTF\",\n    \"companyName\": \"Hyundai Motor Company\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"IPN.PA\",\n    \"companyName\": \"Ipsen
        S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"CLI\",\n
        \   \"companyName\": \"Mack-Cali Realty Corporation\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"CGA\",\n    \"companyName\": \"China
        Green Agriculture, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"0656.HK\",\n    \"companyName\": \"Fosun International Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"ATAI\",\n    \"companyName\": \"Atai Life
        Sciences N.V.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"NATL\",\n    \"companyName\": \"NCR Atleos Corporation\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"NOGN\",\n    \"companyName\": \"Nogin,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SWI\",\n
        \   \"companyName\": \"SolarWinds Corporation\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"KEP\",\n    \"companyName\": \"Korea
        Electric Power Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n
        \   \"symbol\": \"ELUT\",\n    \"companyName\": \"Elutia Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"TMG.V\",\n    \"companyName\": \"Thermal
        Energy International Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n
        \   \"symbol\": \"SFL\",\n    \"companyName\": \"SFL Corporation Ltd.\",\n
        \   \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"LPSN\",\n    \"companyName\":
        \"LivePerson, Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\":
        \"PCYG\",\n    \"companyName\": \"Park City Group, Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"JSVGF\",\n    \"companyName\": \"Johnson
        Service Group PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"KMX\",\n    \"companyName\": \"CarMax, Inc.\",\n    \"noOfTranscripts\":
        \"76\"\n  },\n  {\n    \"symbol\": \"FND\",\n    \"companyName\": \"Floor
        & Decor Holdings, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"CVGW\",\n    \"companyName\": \"Calavo Growers, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"SRTS\",\n    \"companyName\": \"Sensus
        Healthcare, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"SMCI\",\n    \"companyName\": \"Super Micro Computer, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"LPTV\",\n    \"companyName\": \"Loop
        Media, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"RKNEF\",\n    \"companyName\": \"Optiva Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"4005.T\",\n    \"companyName\": \"Sumitomo
        Chemical Company, Limited\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"IVTJF\",\n    \"companyName\": \"Investec Group\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"LSF\",\n    \"companyName\": \"Laird
        Superfood, Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"BTTX\",\n    \"companyName\": \"Better Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"ASAPF\",\n    \"companyName\": \"Aurora
        Spine Corporation\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"LEG\",\n    \"companyName\": \"Leggett & Platt, Incorporated\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"JFIN\",\n    \"companyName\": \"Jiayin
        Group Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"MNDJF\",\n    \"companyName\": \"Mandalay Resources Corporation\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"4704.T\",\n    \"companyName\": \"Trend
        Micro Incorporated\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"CNVS\",\n    \"companyName\": \"Cineverse Corp.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"SAIL\",\n    \"companyName\": \"SailPoint,
        Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"GASNF\",\n
        \   \"companyName\": \"Naturgy Energy Group, S.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"RXT\",\n    \"companyName\": \"Rackspace
        Technology, Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"LGO\",\n    \"companyName\": \"Largo Inc.\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"KRUS\",\n    \"companyName\": \"Kura Sushi USA,
        Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"INR\",\n
        \   \"companyName\": \"Infinity Natural Resources, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"NOPMF\",\n    \"companyName\": \"Neo Performance
        Materials Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"EGHSF\",\n    \"companyName\": \"Enghouse Systems Limited\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"SCSC\",\n    \"companyName\": \"ScanSource,
        Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"NCMI\",\n
        \   \"companyName\": \"National CineMedia, Inc.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"MTP\",\n    \"companyName\": \"Midatech
        Pharma plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"DSP\",\n    \"companyName\": \"Viant Technology Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"IPH.PA\",\n    \"companyName\": \"Innate
        Pharma S.A.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"FUN\",\n    \"companyName\": \"Six Flags Entertainment Corporation\",\n
        \   \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"ZH\",\n    \"companyName\":
        \"Zhihu Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"INSE\",\n    \"companyName\": \"Inspired Entertainment, Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"MELI\",\n    \"companyName\": \"MercadoLibre,
        Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"AEYE\",\n
        \   \"companyName\": \"AudioEye, Inc.\",\n    \"noOfTranscripts\": \"30\"\n
        \ },\n  {\n    \"symbol\": \"MKFG\",\n    \"companyName\": \"Markforged Holding
        Corporation\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"KFS\",\n    \"companyName\": \"Kingsway Financial Services Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"VCISF\",\n    \"companyName\": \"Vinci
        S.A.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"EQNR.OL\",\n
        \   \"companyName\": \"Equinor ASA\",\n    \"noOfTranscripts\": \"70\"\n  },\n
        \ {\n    \"symbol\": \"8001.T\",\n    \"companyName\": \"ITOCHU Corporation\",\n
        \   \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"PHPRF\",\n    \"companyName\":
        \"Primary Health Properties PLC\",\n    \"noOfTranscripts\": \"3\"\n  },\n
        \ {\n    \"symbol\": \"ALA.TO\",\n    \"companyName\": \"AltaGas Ltd.\",\n
        \   \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\": \"GEBN.SW\",\n
        \   \"companyName\": \"Geberit AG\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"MDB\",\n    \"companyName\": \"MongoDB, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"KPN.AS\",\n    \"companyName\": \"Koninklijke
        KPN N.V.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"SHCR\",\n
        \   \"companyName\": \"Sharecare, Inc.\",\n    \"noOfTranscripts\": \"12\"\n
        \ },\n  {\n    \"symbol\": \"AAWH\",\n    \"companyName\": \"Ascend Wellness
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"BNP.PA\",\n    \"companyName\": \"BNP Paribas S.A.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"ERELY\",\n    \"companyName\": \"Eregli
        Demir ve \xC7elik Fabrikalari T.A.S.\",\n    \"noOfTranscripts\": \"5\"\n
        \ },\n  {\n    \"symbol\": \"GRTS\",\n    \"companyName\": \"Gritstone bio,
        Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"CURI\",\n
        \   \"companyName\": \"CuriosityStream Inc.\",\n    \"noOfTranscripts\": \"20\"\n
        \ },\n  {\n    \"symbol\": \"FTG.TO\",\n    \"companyName\": \"Firan Technology
        Group Corporation\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"MFC\",\n    \"companyName\": \"Manulife Financial Corporation\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"C\",\n    \"companyName\": \"Citigroup
        Inc.\",\n    \"noOfTranscripts\": \"74\"\n  },\n  {\n    \"symbol\": \"SYNH\",\n
        \   \"companyName\": \"Syneos Health, Inc.\",\n    \"noOfTranscripts\": \"31\"\n
        \ },\n  {\n    \"symbol\": \"WBD\",\n    \"companyName\": \"Warner Bros. Discovery,
        Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"AVVIY\",\n
        \   \"companyName\": \"Aviva plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n
        \ {\n    \"symbol\": \"SYNL\",\n    \"companyName\": \"Synalloy Corporation\",\n
        \   \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"ERO\",\n    \"companyName\":
        \"Ero Copper Corp.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"AXU\",\n    \"companyName\": \"Alexco Resource Corp.\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"IHRT\",\n    \"companyName\": \"iHeartMedia,
        Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"LBRT\",\n
        \   \"companyName\": \"Liberty Energy Inc.\",\n    \"noOfTranscripts\": \"31\"\n
        \ },\n  {\n    \"symbol\": \"YRD\",\n    \"companyName\": \"Yiren Digital
        Ltd.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"BMA.BA\",\n
        \   \"companyName\": \"Banco Macro S.A.\",\n    \"noOfTranscripts\": \"39\"\n
        \ },\n  {\n    \"symbol\": \"SOWG\",\n    \"companyName\": \"Sow Good Inc.\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"CONN\",\n    \"companyName\":
        \"Conn's, Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"HNGR\",\n    \"companyName\": \"Hanger, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"DMGI.V\",\n    \"companyName\": \"DMG
        Blockchain Solutions Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n
        \   \"symbol\": \"EAT.MC\",\n    \"companyName\": \"AmRest Holdings SE\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"JDEP.AS\",\n
        \   \"companyName\": \"JDE Peet's N.V.\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"RDN\",\n    \"companyName\": \"Radian Group Inc.\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"TGT\",\n    \"companyName\":
        \"Target Corporation\",\n    \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\":
        \"PETV\",\n    \"companyName\": \"PetVivo Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"ADXN\",\n    \"companyName\": \"Addex
        Therapeutics Ltd\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"OGFGF\",\n    \"companyName\": \"Origin Energy Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"NWBI\",\n    \"companyName\": \"Northwest
        Bancshares, Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"BIOVF\",\n    \"companyName\": \"Swedish Orphan Biovitrum AB (publ)\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"RWT\",\n    \"companyName\":
        \"Redwood Trust, Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"SON\",\n    \"companyName\": \"Sonoco Products Company\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"GOSS\",\n    \"companyName\": \"Gossamer
        Bio, Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"CLS\",\n    \"companyName\": \"Celestica Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"APLE\",\n    \"companyName\": \"Apple
        Hospitality REIT, Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"PHP.L\",\n    \"companyName\": \"Primary Health Properties PLC\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"SEG\",\n    \"companyName\": \"Seaport
        Entertainment Group Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"OPAP.AT\",\n    \"companyName\": \"Organization of Football Prognostics
        S.A.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"CYRNQ\",\n
        \   \"companyName\": \"Cyren Ltd.\",\n    \"noOfTranscripts\": \"39\"\n  },\n
        \ {\n    \"symbol\": \"GENTF\",\n    \"companyName\": \"G5 Entertainment AB
        (publ)\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"BHAT\",\n
        \   \"companyName\": \"Fujian Blue Hat Interactive Entertainment Technology
        Ltd.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"NES\",\n
        \   \"companyName\": \"Nuverra Environmental Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"NEUE\",\n    \"companyName\": \"NeueHealth,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"HCHC\",\n
        \   \"companyName\": \"HC2 Holdings, Inc.\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"WKC\",\n    \"companyName\": \"World Kinect Corporation\",\n
        \   \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"NEPH\",\n    \"companyName\":
        \"Nephros, Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"FIS\",\n    \"companyName\": \"Fidelity National Information Services, Inc.\",\n
        \   \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"ZMTBY\",\n    \"companyName\":
        \"Zumtobel Group AG\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"PILBF\",\n    \"companyName\": \"Pilbara Minerals Limited\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"XBIT\",\n    \"companyName\": \"XBiotech
        Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"ML.PA\",\n
        \   \"companyName\": \"Compagnie G\xE9n\xE9rale des \xC9tablissements Michelin
        Soci\xE9t\xE9 en commandite par actions\",\n    \"noOfTranscripts\": \"5\"\n
        \ },\n  {\n    \"symbol\": \"5108.T\",\n    \"companyName\": \"Bridgestone
        Corporation\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"MHCUF\",\n    \"companyName\": \"Flagship Communities Real Estate Investment
        Trust\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"BPYPO\",\n
        \   \"companyName\": \"Brookfield Property Partners L.P.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"NXDR\",\n    \"companyName\": \"Nextdoor
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CBZ\",\n    \"companyName\": \"CBIZ, Inc.\",\n    \"noOfTranscripts\": \"62\"\n
        \ },\n  {\n    \"symbol\": \"QNGY\",\n    \"companyName\": \"Quanergy Systems,
        Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"MS\",\n
        \   \"companyName\": \"Morgan Stanley\",\n    \"noOfTranscripts\": \"74\"\n
        \ },\n  {\n    \"symbol\": \"4502.T\",\n    \"companyName\": \"Takeda Pharmaceutical
        Company Limited\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"REFR\",\n    \"companyName\": \"Research Frontiers Incorporated\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"6301.T\",\n    \"companyName\": \"Komatsu
        Ltd.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"LTM\",\n
        \   \"companyName\": \"LATAM Airlines Group S.A.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"JAPAF\",\n    \"companyName\": \"Japan
        Tobacco Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"SYBX\",\n    \"companyName\": \"Synlogic, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"DOO.TO\",\n    \"companyName\": \"BRP
        Inc.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"KHC\",\n
        \   \"companyName\": \"The Kraft Heinz Company\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"TOM.OL\",\n    \"companyName\": \"Tomra
        Systems ASA\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"BLCO\",\n    \"companyName\": \"Bausch + Lomb Corporation\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"BIRD\",\n    \"companyName\": \"Allbirds,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"FTEK\",\n
        \   \"companyName\": \"Fuel Tech, Inc.\",\n    \"noOfTranscripts\": \"62\"\n
        \ },\n  {\n    \"symbol\": \"BOOM\",\n    \"companyName\": \"DMC Global Inc.\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"ENG.MC\",\n
        \   \"companyName\": \"Enag\xE1s, S.A.\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"NILSY\",\n    \"companyName\": \"PJSC Mining
        and Metallurgical Company Norilsk Nickel\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"LANC\",\n    \"companyName\": \"Lancaster Colony
        Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"HRI\",\n    \"companyName\": \"Herc Holdings Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"GRYP\",\n    \"companyName\": \"Gryphon
        Digital Mining, Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"INVP.L\",\n    \"companyName\": \"Investec Group\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"2317.TW\",\n    \"companyName\": \"Hon
        Hai Precision Industry Co., Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"NVX\",\n    \"companyName\": \"Novonix Limited\",\n
        \   \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"NRDY\",\n    \"companyName\":
        \"Nerdy, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"TTWO\",\n    \"companyName\": \"Take-Two Interactive Software, Inc.\",\n
        \   \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"ATO.PA\",\n
        \   \"companyName\": \"Atos SE\",\n    \"noOfTranscripts\": \"21\"\n  },\n
        \ {\n    \"symbol\": \"GATX\",\n    \"companyName\": \"GATX Corporation\",\n
        \   \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"ERO.TO\",\n
        \   \"companyName\": \"Ero Copper Corp.\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"TA\",\n    \"companyName\": \"TravelCenters of
        America Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\":
        \"AMVMF\",\n    \"companyName\": \"AMG Advanced Metallurgical Group N.V.\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"KLBAY\",\n    \"companyName\":
        \"Klabin S.A.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"PETS\",\n    \"companyName\": \"PetMed Express, Inc.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"FLNT\",\n    \"companyName\": \"Fluent,
        Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"DPW\",\n
        \   \"companyName\": \"DPW Holdings, Inc.\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"VOD.JO\",\n    \"companyName\": \"Vodacom Group
        Limited\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"REI\",\n
        \   \"companyName\": \"Ring Energy, Inc.\",\n    \"noOfTranscripts\": \"41\"\n
        \ },\n  {\n    \"symbol\": \"FLXS\",\n    \"companyName\": \"Flexsteel Industries,
        Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"TPEIR.AT\",\n
        \   \"companyName\": \"Piraeus Financial Holdings S.A.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"CAN\",\n    \"companyName\": \"Canaan
        Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"UCG.MI\",\n
        \   \"companyName\": \"UniCredit S.p.A.\",\n    \"noOfTranscripts\": \"19\"\n
        \ },\n  {\n    \"symbol\": \"TEN.MI\",\n    \"companyName\": \"Tenaris S.A.\",\n
        \   \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"DOCMF\",\n    \"companyName\":
        \"Dr. Martens plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CPTN\",\n    \"companyName\": \"Cepton, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"TSAT\",\n    \"companyName\": \"Telesat
        Corporation\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"SSEZF\",\n    \"companyName\": \"SSE plc\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"CRWV\",\n    \"companyName\": \"CoreWeave, Inc.
        Class A Common Stock\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"RE.V\",\n    \"companyName\": \"RE Royalties Ltd.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"PYR.TO\",\n    \"companyName\": \"PyroGenesis
        Canada Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"KWS.L\",\n    \"companyName\": \"Keywords Studios plc\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"BKSY\",\n    \"companyName\": \"BlackSky
        Technology Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"CIO\",\n    \"companyName\": \"City Office REIT, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"PAE\",\n    \"companyName\": \"PAE Incorporated\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"REGN\",\n    \"companyName\":
        \"Regeneron Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n
        \ {\n    \"symbol\": \"AHH\",\n    \"companyName\": \"Armada Hoffler Properties,
        Inc.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"RNW\",\n
        \   \"companyName\": \"ReNew Energy Global Plc\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"MYTE\",\n    \"companyName\": \"MYT Netherlands
        Parent B.V.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"HOOK\",\n    \"companyName\": \"HOOKIPA Pharma Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"DXPE\",\n    \"companyName\": \"DXP Enterprises,
        Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\": \"BGFV\",\n
        \   \"companyName\": \"Big 5 Sporting Goods Corporation\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"CNO\",\n    \"companyName\": \"CNO Financial
        Group, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"SZG.DE\",\n    \"companyName\": \"Salzgitter AG\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"PCELF\",\n    \"companyName\": \"PowerCell
        Sweden AB (publ)\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"NOA.TO\",\n    \"companyName\": \"North American Construction Group Ltd.\",\n
        \   \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\": \"HELE\",\n    \"companyName\":
        \"Helen of Troy Limited\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"DHC\",\n    \"companyName\": \"Diversified Healthcare Trust\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"WDH\",\n    \"companyName\": \"Waterdrop
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"BLCM\",\n
        \   \"companyName\": \"Bellicum Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"WEST\",\n    \"companyName\": \"Westrock
        Coffee Company, LLC\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"TIIAY\",\n    \"companyName\": \"Telecom Italia S.p.A.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"SPRU\",\n    \"companyName\": \"Spruce
        Power Holding Corporation\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n
        \   \"symbol\": \"CLVR\",\n    \"companyName\": \"Clever Leaves Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"KSFTF\",\n    \"companyName\":
        \"Kingsoft Corporation Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n
        \ {\n    \"symbol\": \"DND.TO\",\n    \"companyName\": \"Dye & Durham Limited\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"EMA.TO\",\n
        \   \"companyName\": \"Emera Incorporated\",\n    \"noOfTranscripts\": \"45\"\n
        \ },\n  {\n    \"symbol\": \"BBNX\",\n    \"companyName\": \"Beta Bionics,
        Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"REI-UN.TO\",\n
        \   \"companyName\": \"RioCan Real Estate Investment Trust\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"OSR.DE\",\n    \"companyName\": \"OSRAM
        Licht AG\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"MPC\",\n
        \   \"companyName\": \"Marathon Petroleum Corporation\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"HOEGF\",\n    \"companyName\": \"H\xF6egh
        Autoliners ASA\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"CSWI\",\n    \"companyName\": \"CSW Industrials, Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"TGS.OL\",\n    \"companyName\": \"Tgs
        Asa\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"USB\",\n
        \   \"companyName\": \"U.S. Bancorp\",\n    \"noOfTranscripts\": \"72\"\n
        \ },\n  {\n    \"symbol\": \"MLLGF\",\n    \"companyName\": \"Mullen Group
        Ltd.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"LUV\",\n
        \   \"companyName\": \"Southwest Airlines Co.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"CECO\",\n    \"companyName\": \"CECO
        Environmental Corp.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"BEAM\",\n    \"companyName\": \"Beam Therapeutics Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"6268.T\",\n    \"companyName\": \"Nabtesco
        Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"ETWO\",\n    \"companyName\": \"E2open Parent Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BNR.DE\",\n    \"companyName\": \"Brenntag
        SE\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"6770.T\",\n
        \   \"companyName\": \"Alps Alpine Co., Ltd.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"VGP.BR\",\n    \"companyName\": \"Vgp
        N.V.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"CPRX\",\n
        \   \"companyName\": \"Catalyst Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"ASLE\",\n    \"companyName\": \"AerSale
        Corporation\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"CYRE3.SA\",\n    \"companyName\": \"Cyrela Brazil Realty S.A. Empreendimentos
        e Participa\xE7\xF5es\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"TGSNF\",\n    \"companyName\": \"Tgs Asa\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"EDBL\",\n    \"companyName\": \"Edible Garden
        AG Incorporated\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"NGVT\",\n    \"companyName\": \"Ingevity Corporation\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"PX\",\n    \"companyName\": \"P10, Inc.\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"RUI.PA\",\n
        \   \"companyName\": \"Rubis\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n
        \   \"symbol\": \"GLW\",\n    \"companyName\": \"Corning Incorporated\",\n
        \   \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"VYX\",\n    \"companyName\":
        \"NCR Voyix Corporation\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"FTS\",\n    \"companyName\": \"Fortis Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"AYA.TO\",\n    \"companyName\": \"Aya
        Gold & Silver Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"ASTH\",\n    \"companyName\": \"Astrana Health, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"OTRK\",\n    \"companyName\": \"Ontrak,
        Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"CVALF\",\n
        \   \"companyName\": \"Covalon Technologies Ltd.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"KOS\",\n    \"companyName\": \"Kosmos
        Energy Ltd.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"IOBCF\",\n    \"companyName\": \"Ion Beam Applications S.A.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"SPKKY\",\n    \"companyName\": \"Spark
        New Zealand Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"GH\",\n    \"companyName\": \"Guardant Health, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"TMOAF\",\n    \"companyName\": \"TomTom
        N.V.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"SQM\",\n
        \   \"companyName\": \"Sociedad Qu\xEDmica y Minera de Chile S.A.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"CSAN3.SA\",\n    \"companyName\": \"Cosan
        S.A.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"EVGN.TA\",\n
        \   \"companyName\": \"Evogene Ltd.\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"JAMF\",\n    \"companyName\": \"Jamf Holding
        Corp.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"XHR\",\n
        \   \"companyName\": \"Xenia Hotels & Resorts, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"TCW.TO\",\n    \"companyName\": \"Trican
        Well Service Ltd.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"INSP\",\n    \"companyName\": \"Inspire Medical Systems, Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"VSTM\",\n    \"companyName\": \"Verastem,
        Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"STLA\",\n
        \   \"companyName\": \"Stellantis N.V.\",\n    \"noOfTranscripts\": \"43\"\n
        \ },\n  {\n    \"symbol\": \"ESGR\",\n    \"companyName\": \"Enstar Group
        Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"LGO.TO\",\n
        \   \"companyName\": \"Largo Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n
        \ {\n    \"symbol\": \"AXS\",\n    \"companyName\": \"AXIS Capital Holdings
        Limited\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"MLKN\",\n
        \   \"companyName\": \"MillerKnoll, Inc.\",\n    \"noOfTranscripts\": \"63\"\n
        \ },\n  {\n    \"symbol\": \"AMKAF\",\n    \"companyName\": \"A.P. M\xF8ller
        - M\xE6rsk A/S\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"TE\",\n    \"companyName\": \"T1 Energy Inc\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"CGO.TO\",\n    \"companyName\": \"Cogeco
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"UBSG.SW\",\n
        \   \"companyName\": \"UBS Group AG\",\n    \"noOfTranscripts\": \"55\"\n
        \ },\n  {\n    \"symbol\": \"DUSA\",\n    \"companyName\": \"Davis Select
        U.S. Equity ETF\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"SCGLF\",\n    \"companyName\": \"Soci\xE9t\xE9 G\xE9n\xE9rale S.A.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"AXL\",\n    \"companyName\":
        \"American Axle & Manufacturing Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"GBDC\",\n    \"companyName\": \"Golub
        Capital BDC, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"TCX\",\n    \"companyName\": \"Tucows Inc.\",\n    \"noOfTranscripts\":
        \"75\"\n  },\n  {\n    \"symbol\": \"ANZ.AX\",\n    \"companyName\": \"ANZ
        Group Holdings Limited\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"OUKPF\",\n    \"companyName\": \"Metso Oyj\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"ONVO\",\n    \"companyName\": \"Organovo
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"ARMP\",\n    \"companyName\": \"Armata Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"PGNY\",\n    \"companyName\": \"Progyny,
        Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"WANSF\",\n
        \   \"companyName\": \"Cirata plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"GTH\",\n    \"companyName\": \"Genetron Holdings Limited\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"MIND\",\n    \"companyName\":
        \"MIND Technology, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"HGBL\",\n    \"companyName\": \"Heritage Global Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"PYRGF\",\n    \"companyName\": \"PyroGenesis
        Canada Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"PEP\",\n    \"companyName\": \"PepsiCo, Inc.\",\n    \"noOfTranscripts\":
        \"75\"\n  },\n  {\n    \"symbol\": \"CTRN\",\n    \"companyName\": \"Citi
        Trends, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"005490.KS\",\n    \"companyName\": \"POSCO Holdings Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"CM.TO\",\n    \"companyName\": \"Canadian
        Imperial Bank of Commerce\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n
        \   \"symbol\": \"GOR.AX\",\n    \"companyName\": \"Gold Road Resources Limited\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"PLYM\",\n    \"companyName\":
        \"Plymouth Industrial REIT, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n
        \ {\n    \"symbol\": \"DAN\",\n    \"companyName\": \"Dana Incorporated\",\n
        \   \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"BDR\",\n    \"companyName\":
        \"Blonder Tongue Laboratories, Inc.\",\n    \"noOfTranscripts\": \"19\"\n
        \ },\n  {\n    \"symbol\": \"NCLH\",\n    \"companyName\": \"Norwegian Cruise
        Line Holdings Ltd.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"CALA\",\n    \"companyName\": \"Calithera Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"HPGLY\",\n    \"companyName\": \"Hapag-Lloyd
        AG\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"RCKY\",\n
        \   \"companyName\": \"Rocky Brands, Inc.\",\n    \"noOfTranscripts\": \"67\"\n
        \ },\n  {\n    \"symbol\": \"TFC\",\n    \"companyName\": \"Truist Financial
        Corporation\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"NDLS\",\n    \"companyName\": \"Noodles & Company\",\n    \"noOfTranscripts\":
        \"49\"\n  },\n  {\n    \"symbol\": \"GLBE\",\n    \"companyName\": \"Global-e
        Online Ltd.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"CSII\",\n    \"companyName\": \"Cardiovascular Systems, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"BHP.AX\",\n    \"companyName\": \"BHP
        Group Limited\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"GSY.TO\",\n    \"companyName\": \"goeasy Ltd.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"VINP\",\n    \"companyName\": \"Vinci
        Compass Investments Ltd.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n
        \   \"symbol\": \"BGI\",\n    \"companyName\": \"Birks Group Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"XAIR\",\n    \"companyName\": \"Beyond
        Air, Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"VEOEY\",\n    \"companyName\": \"Veolia Environnement S.A.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"SSYS\",\n    \"companyName\": \"Stratasys
        Ltd.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"RTMVF\",\n
        \   \"companyName\": \"Rightmove plc\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"SGU\",\n    \"companyName\": \"Star Group, L.P.\",\n
        \   \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"OPTN\",\n    \"companyName\":
        \"OptiNose, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"IRMD\",\n    \"companyName\": \"IRadimed Corporation\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"LYC.AX\",\n    \"companyName\": \"Lynas
        Rare Earths Limited\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"HIND\",\n    \"companyName\": \"Vyome Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"CSLT\",\n    \"companyName\": \"Castlight
        Health, Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"SKF-A.ST\",\n    \"companyName\": \"AB SKF (publ)\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"OPNT\",\n    \"companyName\": \"Opiant
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"CALTX.ST\",\n    \"companyName\": \"Calliditas Therapeutics AB (publ)\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"1910.HK\",\n
        \   \"companyName\": \"Samsonite International S.A.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"ANYYY\",\n    \"companyName\": \"Aena
        S.M.E., S.A.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"FSI\",\n    \"companyName\": \"Flexible Solutions International, Inc.\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"IMM.AX\",\n
        \   \"companyName\": \"Immutep Limited\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"XELA\",\n    \"companyName\": \"Exela Technologies,
        Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"GIGM\",\n
        \   \"companyName\": \"GigaMedia Limited\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"JAPAY\",\n    \"companyName\": \"Japan Tobacco
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"CMBT\",\n
        \   \"companyName\": \"Cmb.Tech N.V.\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"GOOD\",\n    \"companyName\": \"Gladstone Commercial
        Corporation\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"SEIC\",\n    \"companyName\": \"SEI Investments Company\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"4536.T\",\n    \"companyName\": \"Santen
        Pharmaceutical Co., Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"NSP\",\n    \"companyName\": \"Insperity, Inc.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"ENX.PA\",\n    \"companyName\": \"Euronext
        N.V.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"DGE.L\",\n
        \   \"companyName\": \"Diageo plc\",\n    \"noOfTranscripts\": \"16\"\n  },\n
        \ {\n    \"symbol\": \"STEP\",\n    \"companyName\": \"StepStone Group Inc.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"BARC.L\",\n
        \   \"companyName\": \"Barclays PLC\",\n    \"noOfTranscripts\": \"55\"\n
        \ },\n  {\n    \"symbol\": \"LDX.AX\",\n    \"companyName\": \"Lumos Diagnostics
        Holdings Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"MNGPF\",\n    \"companyName\": \"Man Group Limited\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"CPX.TO\",\n    \"companyName\": \"Capital
        Power Corporation\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"EGIE3.SA\",\n    \"companyName\": \"Engie Brasil Energia S.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"FRVIA.PA\",\n    \"companyName\": \"Forvia
        SE\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"SYIEF\",\n
        \   \"companyName\": \"Symrise AG\",\n    \"noOfTranscripts\": \"17\"\n  },\n
        \ {\n    \"symbol\": \"SMI\",\n    \"companyName\": \"VanEck HIP Sustainable
        Muni ETF\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"AIMC\",\n
        \   \"companyName\": \"Altra Industrial Motion Corp.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"RDNW\",\n    \"companyName\": \"RumbleON,
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"PGRE\",\n
        \   \"companyName\": \"Paramount Group, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"DPZ\",\n    \"companyName\": \"Domino's
        Pizza, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"EXE.TO\",\n    \"companyName\": \"Extendicare Inc.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"CLNFF\",\n    \"companyName\": \"Calian
        Group Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"HPP\",\n    \"companyName\": \"Hudson Pacific Properties, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"SOUHY\",\n    \"companyName\": \"South32
        Limited\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"DRT.TO\",\n
        \   \"companyName\": \"DIRTT Environmental Solutions Ltd.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"LQDA\",\n    \"companyName\": \"Liquidia
        Corporation\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"TEF\",\n    \"companyName\": \"Telef\xF3nica, S.A.\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"HTGM\",\n    \"companyName\": \"HTG Molecular
        Diagnostics, Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"MRIN\",\n    \"companyName\": \"Marin Software Incorporated\",\n    \"noOfTranscripts\":
        \"47\"\n  },\n  {\n    \"symbol\": \"8TRA.DE\",\n    \"companyName\": \"Traton
        SE\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"CATC\",\n
        \   \"companyName\": \"Cambridge Bancorp\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"SVYSF\",\n    \"companyName\": \"Solvay S.A.\",\n
        \   \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"STRA\",\n    \"companyName\":
        \"Strategic Education, Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n
        \   \"symbol\": \"NGG\",\n    \"companyName\": \"National Grid plc\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"HYQ.DE\",\n    \"companyName\": \"Hypoport
        SE\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"COL.AX\",\n
        \   \"companyName\": \"Coles Group Limited\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"ALKT\",\n    \"companyName\": \"Alkami Technology,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"NKLA\",\n
        \   \"companyName\": \"Nikola Corporation\",\n    \"noOfTranscripts\": \"23\"\n
        \ },\n  {\n    \"symbol\": \"SMPL\",\n    \"companyName\": \"The Simply Good
        Foods Company\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"BPMC\",\n    \"companyName\": \"Blueprint Medicines Corporation\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"CBK.DE\",\n    \"companyName\": \"Commerzbank
        AG\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"7201.T\",\n
        \   \"companyName\": \"Nissan Motor Co., Ltd.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"FTS.TO\",\n    \"companyName\": \"Fortis
        Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"SWTX\",\n
        \   \"companyName\": \"SpringWorks Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"CDLX\",\n    \"companyName\": \"Cardlytics,
        Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"RDSMY\",\n
        \   \"companyName\": \"Koninklijke DSM N.V.\",\n    \"noOfTranscripts\": \"39\"\n
        \ },\n  {\n    \"symbol\": \"DVN\",\n    \"companyName\": \"Devon Energy Corporation\",\n
        \   \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"DRO.AX\",\n
        \   \"companyName\": \"DroneShield Limited\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"HOLX\",\n    \"companyName\": \"Hologic, Inc.\",\n
        \   \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\": \"ASR\",\n    \"companyName\":
        \"Grupo Aeroportuario del Sureste, S. A. B. de C. V.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"BDN\",\n    \"companyName\": \"Brandywine
        Realty Trust\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"APX.AX\",\n    \"companyName\": \"Appen Limited\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"CNET\",\n    \"companyName\": \"ZW Data
        Action Technologies Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n
        \   \"symbol\": \"QTWO\",\n    \"companyName\": \"Q2 Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"GNFT.PA\",\n    \"companyName\": \"Genfit
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"GIB-A.TO\",\n
        \   \"companyName\": \"CGI Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n
        \ {\n    \"symbol\": \"HTL.V\",\n    \"companyName\": \"Hamilton Thorne Ltd.\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"CTIB\",\n    \"companyName\":
        \"Yunhong CTI Ltd.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"2357.TW\",\n    \"companyName\": \"ASUSTeK Computer Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"ASPU\",\n    \"companyName\": \"Aspen
        Group, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"IIP-UN.TO\",\n    \"companyName\": \"InterRent Real Estate Investment Trust\",\n
        \   \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"AKU\",\n    \"companyName\":
        \"Akumin Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"CTLT\",\n    \"companyName\": \"Catalent, Inc.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"NABL\",\n    \"companyName\": \"N-able,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"GLP\",\n
        \   \"companyName\": \"Global Partners LP\",\n    \"noOfTranscripts\": \"56\"\n
        \ },\n  {\n    \"symbol\": \"MDG1.DE\",\n    \"companyName\": \"Medigene AG\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"VTAK\",\n    \"companyName\":
        \"Catheter Precision, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"JRSH\",\n    \"companyName\": \"Jerash Holdings (US), Inc.\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"PIFYF\",\n    \"companyName\":
        \"Pine Cliff Energy Ltd.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"KZR\",\n    \"companyName\": \"Kezar Life Sciences, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"STOSF\",\n    \"companyName\": \"Santos
        Limited\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"CCEC\",\n
        \   \"companyName\": \"Capital Clean Energy Carriers Corp.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"VEV\",\n    \"companyName\": \"Vicinity
        Motor Corp.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"ALLO\",\n    \"companyName\": \"Allogene Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"X\",\n    \"companyName\": \"United States
        Steel Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"OET.OL\",\n    \"companyName\": \"Okeanis Eco Tankers Corp.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"NAVI\",\n    \"companyName\": \"Navient
        Corporation\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"OPGN\",\n    \"companyName\": \"OpGen, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"AIRI\",\n    \"companyName\": \"Air Industries
        Group\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"ABMD\",\n
        \   \"companyName\": \"Abiomed, Inc.\",\n    \"noOfTranscripts\": \"50\"\n
        \ },\n  {\n    \"symbol\": \"GSBD\",\n    \"companyName\": \"Goldman Sachs
        BDC, Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"CPSI\",\n    \"companyName\": \"Computer Programs and Systems, Inc.\",\n
        \   \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"VQSSF\",\n    \"companyName\":
        \"VIQ Solutions Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"VERI\",\n    \"companyName\": \"Veritone, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"SHG\",\n    \"companyName\": \"Shinhan
        Financial Group Co., Ltd.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n
        \   \"symbol\": \"KIO\",\n    \"companyName\": \"KKR Income Opportunities
        Fund\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"TESB.BR\",\n
        \   \"companyName\": \"Tessenderlo Group N.V.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"OLGPF\",\n    \"companyName\": \"Olam
        Group Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"OESX\",\n    \"companyName\": \"Orion Energy Systems, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"JBS\",\n    \"companyName\": \"Jbs N.v.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"FITB\",\n    \"companyName\":
        \"Fifth Third Bancorp\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"ECPG\",\n    \"companyName\": \"Encore Capital Group, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"TATASTEEL.NS\",\n    \"companyName\":
        \"Tata Steel Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"CSIQ\",\n    \"companyName\": \"Canadian Solar Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"NOVN.SW\",\n    \"companyName\": \"Novartis
        AG\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"OBDC\",\n
        \   \"companyName\": \"Blue Owl Capital Corporation\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"CRNX\",\n    \"companyName\": \"Crinetics
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"AYRWF\",\n    \"companyName\": \"Ayr Wellness Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"CWSFF\",\n    \"companyName\": \"Cielo
        Waste Solutions Corp.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"TRVG\",\n    \"companyName\": \"trivago N.V.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"NAN.AX\",\n    \"companyName\": \"Nanosonics
        Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"TGVSF\",\n
        \   \"companyName\": \"Tryg A/S\",\n    \"noOfTranscripts\": \"7\"\n  },\n
        \ {\n    \"symbol\": \"TBCRF\",\n    \"companyName\": \"Timbercreek Financial
        Corp.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"XTIA\",\n
        \   \"companyName\": \"XTI Aerospace, Inc.\",\n    \"noOfTranscripts\": \"33\"\n
        \ },\n  {\n    \"symbol\": \"BIPC\",\n    \"companyName\": \"Brookfield Infrastructure
        Corporation\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"NNDM\",\n    \"companyName\": \"Nano Dimension Ltd.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"WTC.AX\",\n    \"companyName\": \"WiseTech
        Global Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"BLHEY\",\n    \"companyName\": \"B\xE2loise Holding AG\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"STO.AX\",\n    \"companyName\": \"Santos
        Limited\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"WPP\",\n
        \   \"companyName\": \"WPP plc\",\n    \"noOfTranscripts\": \"51\"\n  },\n
        \ {\n    \"symbol\": \"AADI\",\n    \"companyName\": \"Aadi Bioscience, Inc.\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"CUV.AX\",\n
        \   \"companyName\": \"Clinuvel Pharmaceuticals Limited\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"SIA.TO\",\n    \"companyName\": \"Sienna
        Senior Living Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"RAND\",\n    \"companyName\": \"Rand Capital Corporation\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"CUTR\",\n    \"companyName\": \"Cutera,
        Inc.\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"POELF\",\n
        \   \"companyName\": \"The Navigator Company, S.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"SRPT\",\n    \"companyName\": \"Sarepta
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"SF.ST\",\n    \"companyName\": \"Stillfront Group AB (publ)\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"WNDLF\",\n    \"companyName\": \"Wendel\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"FGR.PA\",\n    \"companyName\":
        \"Eiffage S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CTSO\",\n    \"companyName\": \"Cytosorbents Corporation\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"4568.T\",\n    \"companyName\": \"Daiichi
        Sankyo Company, Limited\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"SSAAF\",\n    \"companyName\": \"SSAB AB (publ)\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"SBET\",\n    \"companyName\": \"SharpLink
        Gaming Ltd.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"EWCZ\",\n    \"companyName\": \"European Wax Center, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"MCO\",\n    \"companyName\": \"Moody's
        Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"BIG\",\n    \"companyName\": \"Big Lots, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"AAMC\",\n    \"companyName\": \"Altisource
        Asset Management Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n
        \   \"symbol\": \"APT\",\n    \"companyName\": \"Alpha Pro Tech, Ltd.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SEAC\",\n    \"companyName\":
        \"SeaChange International, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n
        \ {\n    \"symbol\": \"TECO2.BA\",\n    \"companyName\": \"Telecom Argentina
        S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"TLIS\",\n
        \   \"companyName\": \"Talis Biomedical Corporation\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"FIBK\",\n    \"companyName\": \"First
        Interstate BancSystem, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n
        \   \"symbol\": \"PCTY\",\n    \"companyName\": \"Paylocity Holding Corporation\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"NWC.TO\",\n
        \   \"companyName\": \"The North West Company Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"MLXSF\",\n    \"companyName\": \"Melexis
        N.V.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"MAPGF\",\n
        \   \"companyName\": \"Mapletree Logistics Trust\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"FNF\",\n    \"companyName\": \"Fidelity
        National Financial, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n
        \   \"symbol\": \"015760.KS\",\n    \"companyName\": \"Korea Electric Power
        Corporation\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"COLB\",\n    \"companyName\": \"Columbia Banking System, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"NMM\",\n    \"companyName\": \"Navios
        Maritime Partners L.P.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"RSG.AX\",\n    \"companyName\": \"Resolute Mining Limited\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"AMP.MI\",\n    \"companyName\": \"Amplifon
        S.p.A.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"ARIS.TO\",\n
        \   \"companyName\": \"Aris Mining Corporation\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"IRDM\",\n    \"companyName\": \"Iridium
        Communications Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"BRLT\",\n    \"companyName\": \"Brilliant Earth Group, Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"CNGO\",\n    \"companyName\": \"Cengage
        Learning Holdings II, Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n
        \   \"symbol\": \"MTSI\",\n    \"companyName\": \"MACOM Technology Solutions
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"TEG.DE\",\n    \"companyName\": \"TAG Immobilien AG\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"SGM.AX\",\n    \"companyName\": \"Sims
        Limited\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"POAI\",\n
        \   \"companyName\": \"Predictive Oncology Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"BDGI.TO\",\n    \"companyName\": \"Badger
        Infrastructure Solutions Ltd.\",\n    \"noOfTranscripts\": \"31\"\n  },\n
        \ {\n    \"symbol\": \"PRDSY\",\n    \"companyName\": \"Prada S.p.A.\",\n
        \   \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"NSSC\",\n    \"companyName\":
        \"Napco Security Technologies, Inc.\",\n    \"noOfTranscripts\": \"52\"\n
        \ },\n  {\n    \"symbol\": \"VQS.TO\",\n    \"companyName\": \"VIQ Solutions
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"IPDN\",\n
        \   \"companyName\": \"Professional Diversity Network, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"CJJD\",\n    \"companyName\": \"China
        Jo-Jo Drugstores, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"PMREF\",\n    \"companyName\": \"Primaris Real Estate Investment Trust\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"SRG.MI\",\n    \"companyName\":
        \"Snam S.p.A.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"FLOOF\",\n    \"companyName\": \"Flower One Holdings Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"GENSF\",\n    \"companyName\": \"Genus
        plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"SEBYY\",\n
        \   \"companyName\": \"Seb S.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"SK.PA\",\n    \"companyName\": \"Seb S.A.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"BSM\",\n    \"companyName\": \"Black Stone
        Minerals, L.P.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"CP.TO\",\n    \"companyName\": \"Canadian Pacific Kansas City Ltd.\",\n
        \   \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"AREC\",\n    \"companyName\":
        \"American Resources Corporation\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"BWAGF\",\n    \"companyName\": \"BAWAG Group AG\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"BDGSF\",\n    \"companyName\":
        \"Bank of Georgia Group PLC\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"JRV.AX\",\n    \"companyName\": \"Jervois Global Limited\",\n
        \   \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"FTGFF\",\n    \"companyName\":
        \"Firan Technology Group Corporation\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"5CV.DE\",\n    \"companyName\": \"CureVac N.V.\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"L\",\n    \"companyName\":
        \"Loews Corporation\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"WRAP\",\n    \"companyName\": \"Wrap Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"XOM\",\n    \"companyName\": \"Exxon
        Mobil Corporation\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"HWCC\",\n    \"companyName\": \"Houston Wire & Cable Company\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"COMS\",\n    \"companyName\": \"COMSovereign
        Holding Corp.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"FCEL\",\n    \"companyName\": \"FuelCell Energy, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"UCBI\",\n    \"companyName\": \"United
        Community Banks, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"FLGC\",\n    \"companyName\": \"Flora Growth Corp.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"RRL.AX\",\n    \"companyName\": \"Regis
        Resources Limited\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"PDYPY\",\n    \"companyName\": \"Flutter Entertainment plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"THRN\",\n    \"companyName\": \"Thorne
        HealthTech, Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"EXLS\",\n    \"companyName\": \"ExlService Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"GEMD.L\",\n    \"companyName\": \"Gem
        Diamonds Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"SHO\",\n    \"companyName\": \"Sunstone Hotel Investors, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"HYZN\",\n    \"companyName\": \"Hyzon
        Motors Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"GTM\",\n    \"companyName\": \"ZoomInfo Technologies Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"LNR.TO\",\n    \"companyName\": \"Linamar
        Corporation\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"REG\",\n    \"companyName\": \"Regency Centers Corporation\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"USM\",\n    \"companyName\": \"United
        States Cellular Corporation\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n
        \   \"symbol\": \"PROC\",\n    \"companyName\": \"Procaps Group S.A.\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"IVA.PA\",\n    \"companyName\":
        \"Inventiva S.A.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"MAMA\",\n    \"companyName\": \"Mama's Creations, Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"SID\",\n    \"companyName\": \"Companhia
        Sider\xFArgica Nacional\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"WDS.AX\",\n    \"companyName\": \"Woodside Energy Group Ltd\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"SILA\",\n    \"companyName\": \"Sila
        Realty Trust, Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"4528.T\",\n    \"companyName\": \"Ono Pharmaceutical Co., Ltd.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"D03.SI\",\n    \"companyName\": \"Del
        Monte Pacific Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"BPOSF\",\n    \"companyName\": \"bpost NV/SA\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"EVH\",\n    \"companyName\": \"Evolent
        Health, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"DXC\",\n    \"companyName\": \"DXC Technology Company\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"WIZZ.L\",\n    \"companyName\": \"Wizz
        Air Holdings Plc\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"WRLD\",\n    \"companyName\": \"World Acceptance Corporation\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"AINC\",\n    \"companyName\": \"Ashford
        Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"BSL.AX\",\n
        \   \"companyName\": \"BlueScope Steel Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"2914.T\",\n    \"companyName\": \"Japan
        Tobacco Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"PME.AX\",\n    \"companyName\": \"Pro Medicus Limited\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"NTB\",\n    \"companyName\": \"The Bank
        of N.T. Butterfield & Son Limited\",\n    \"noOfTranscripts\": \"35\"\n  },\n
        \ {\n    \"symbol\": \"BYND\",\n    \"companyName\": \"Beyond Meat, Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"ASPN\",\n    \"companyName\":
        \"Aspen Aerogels, Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\":
        \"CFR\",\n    \"companyName\": \"Cullen/Frost Bankers, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"UMG.AS\",\n    \"companyName\": \"Universal
        Music Group N.V.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"NTPIF\",\n    \"companyName\": \"Nam Tai Property Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"SSRM\",\n    \"companyName\": \"SSR Mining
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"PWCDF\",\n
        \   \"companyName\": \"Power Corporation of Canada\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"AEMMF\",\n    \"companyName\": \"A2A
        S.p.A.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"OGS\",\n
        \   \"companyName\": \"ONE Gas, Inc.\",\n    \"noOfTranscripts\": \"45\"\n
        \ },\n  {\n    \"symbol\": \"TRN\",\n    \"companyName\": \"Trinity Industries,
        Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"SYRA\",\n
        \   \"companyName\": \"Syra Health Corp. Class A Common Stock\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"ZBH\",\n    \"companyName\": \"Zimmer
        Biomet Holdings, Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"UA\",\n    \"companyName\": \"Under Armour, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"NEX.L\",\n    \"companyName\": \"National
        Express Group PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"DVAX\",\n    \"companyName\": \"Dynavax Technologies Corporation\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"PRTC\",\n    \"companyName\": \"PureTech
        Health plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"030200.KS\",\n    \"companyName\": \"KT Corporation\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"ARLN.DE\",\n    \"companyName\": \"Aareal
        Bank AG\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"LGDDF\",\n
        \   \"companyName\": \"Lagardere S.A.\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"PPL\",\n    \"companyName\": \"PPL Corporation\",\n
        \   \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"SLI\",\n    \"companyName\":
        \"Standard Lithium Ltd.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"MRG-UN.TO\",\n    \"companyName\": \"Morguard North American Residential
        Real Estate Investment Trust\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"CYAD\",\n    \"companyName\": \"Celyad Oncology S.A.\",\n
        \   \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"FBMS\",\n    \"companyName\":
        \"The First Bancshares, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"PHMMF\",\n    \"companyName\": \"Pharma Mar, S.A.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"CURN\",\n    \"companyName\": \"Currency
        Exchange International, Corp.\",\n    \"noOfTranscripts\": \"15\"\n  },\n
        \ {\n    \"symbol\": \"PYPL\",\n    \"companyName\": \"PayPal Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"MUFG\",\n    \"companyName\":
        \"Mitsubishi UFJ Financial Group, Inc.\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"ESPR\",\n    \"companyName\": \"Esperion Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"DXT.TO\",\n
        \   \"companyName\": \"Dexterra Group Inc.\",\n    \"noOfTranscripts\": \"29\"\n
        \ },\n  {\n    \"symbol\": \"SIGI\",\n    \"companyName\": \"Selective Insurance
        Group, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"NVO\",\n    \"companyName\": \"Novo Nordisk A/S\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"TRZ.TO\",\n    \"companyName\": \"Transat
        A.T. Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"INFO\",\n    \"companyName\": \"Harbor PanAgora Dynamic Large Cap Core ETF\",\n
        \   \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"XPEV\",\n    \"companyName\":
        \"XPeng Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"OS\",\n    \"companyName\": \"OneStream, Inc. Class A Common Stock\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"ACCS\",\n    \"companyName\":
        \"ACCESS Newswire Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"BILL\",\n    \"companyName\": \"Bill.com Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"VRAR\",\n    \"companyName\": \"The Glimpse
        Group, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"JAKK\",\n    \"companyName\": \"JAKKS Pacific, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"BTO.TO\",\n    \"companyName\": \"B2Gold
        Corp.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"FINW\",\n
        \   \"companyName\": \"FinWise Bancorp\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"PAYS\",\n    \"companyName\": \"PaySign, Inc.\",\n
        \   \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"CAE.TO\",\n
        \   \"companyName\": \"CAE Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n
        \ {\n    \"symbol\": \"CSNA3.SA\",\n    \"companyName\": \"Companhia Sider\xFArgica
        Nacional\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"SBSP3.SA\",\n
        \   \"companyName\": \"Companhia de Saneamento B\xE1sico do Estado de S\xE3o
        Paulo - SABESP\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"MXCHF\",\n    \"companyName\": \"Orbia Advance Corporation, S.A.B. de C.V.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"AEXAF\",\n    \"companyName\":
        \"Atos SE\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"7203.T\",\n    \"companyName\": \"Toyota Motor Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"ZIP.AX\",\n    \"companyName\": \"Zip
        Co Limited\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"BRKL\",\n    \"companyName\": \"Brookline Bancorp, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"BOUYF\",\n    \"companyName\": \"Bouygues
        S.A.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"GES\",\n
        \   \"companyName\": \"Guess', Inc.\",\n    \"noOfTranscripts\": \"65\"\n
        \ },\n  {\n    \"symbol\": \"LAMR\",\n    \"companyName\": \"Lamar Advertising
        Company\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"BBGI\",\n
        \   \"companyName\": \"Beasley Broadcast Group, Inc.\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"NERV\",\n    \"companyName\": \"Minerva
        Neurosciences, Inc.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"TPCS\",\n    \"companyName\": \"TechPrecision Corporation\",\n    \"noOfTranscripts\":
        \"47\"\n  },\n  {\n    \"symbol\": \"CYRN\",\n    \"companyName\": \"Cyren
        Ltd.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"LUCK\",\n
        \   \"companyName\": \"Lucky Strike Entertainment Corporation\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"ITMPF\",\n    \"companyName\": \"ITM
        Power Plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"FLT.V\",\n
        \   \"companyName\": \"Volatus Aerospace Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SMDS.L\",\n    \"companyName\": \"DS Smith
        Plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"USDP\",\n
        \   \"companyName\": \"USD Partners LP\",\n    \"noOfTranscripts\": \"29\"\n
        \ },\n  {\n    \"symbol\": \"IPXHY\",\n    \"companyName\": \"Inpex Corporation\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"UPLD\",\n    \"companyName\":
        \"Upland Software, Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"LSEG.L\",\n    \"companyName\": \"London Stock Exchange Group plc\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"WDGJF\",\n    \"companyName\": \"John
        Wood Group PLC\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"LIEN\",\n    \"companyName\": \"Chicago Atlantic BDC, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"AUKNY\",\n    \"companyName\": \"Auckland
        International Airport Limited\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"PUMP\",\n    \"companyName\": \"ProPetro Holding Corp.\",\n
        \   \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"NSA\",\n    \"companyName\":
        \"National Storage Affiliates Trust\",\n    \"noOfTranscripts\": \"36\"\n
        \ },\n  {\n    \"symbol\": \"ENTG.V\",\n    \"companyName\": \"Entourage Health
        Corp.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"GOCO\",\n
        \   \"companyName\": \"GoHealth, Inc.\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"NBTX\",\n    \"companyName\": \"Nanobiotix S.A.\",\n
        \   \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"0MV8.L\",\n
        \   \"companyName\": \"Vantiva S.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"FEEXF\",\n    \"companyName\": \"Ferrexpo plc\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ATY\",\n    \"companyName\":
        \"AcuityAds Holdings Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"ESTA\",\n    \"companyName\": \"Establishment Labs Holdings
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"CSTL\",\n
        \   \"companyName\": \"Castle Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"WIRE\",\n    \"companyName\": \"Encore
        Wire Corporation\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"TLYS\",\n    \"companyName\": \"Tilly's, Inc.\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"FNCTF\",\n    \"companyName\": \"Orange
        S.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ORGO\",\n
        \   \"companyName\": \"Organogenesis Holdings Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"KYMR\",\n    \"companyName\": \"Kymera
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"LTBR\",\n    \"companyName\": \"Lightbridge Corporation\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"WCN\",\n    \"companyName\": \"Waste
        Connections, Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"CNTMF\",\n    \"companyName\": \"Fluent Corp.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"GRRR\",\n    \"companyName\": \"Gorilla
        Technology Group Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"HZNP\",\n    \"companyName\": \"Horizon Therapeutics Public Limited Company\",\n
        \   \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\": \"DRSHF\",\n    \"companyName\":
        \"DroneShield Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CLNXF\",\n    \"companyName\": \"Cellnex Telecom, S.A.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"SESPF\",\n    \"companyName\": \"SeSa
        S.p.A.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SBRY.L\",\n
        \   \"companyName\": \"J Sainsbury plc\",\n    \"noOfTranscripts\": \"26\"\n
        \ },\n  {\n    \"symbol\": \"RECSI.OL\",\n    \"companyName\": \"REC Silicon
        ASA\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"PRSO\",\n
        \   \"companyName\": \"Peraso Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n
        \ {\n    \"symbol\": \"RSSS\",\n    \"companyName\": \"Research Solutions,
        Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"MIN.AX\",\n
        \   \"companyName\": \"Mineral Resources Limited\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"DXLG\",\n    \"companyName\": \"Destination
        XL Group, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"TLS.AX\",\n    \"companyName\": \"Telstra Group Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"DZSI\",\n    \"companyName\": \"DZS Inc.\",\n
        \   \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"DCGO\",\n    \"companyName\":
        \"DocGo Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"ATKR\",\n    \"companyName\": \"Atkore Inc.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"CBOE\",\n    \"companyName\": \"Cboe
        Global Markets, Inc.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\":
        \"KAHOT.OL\",\n    \"companyName\": \"Kahoot! ASA\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"KHOTF\",\n    \"companyName\": \"Kahoot!
        ASA\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"WZZAF\",\n
        \   \"companyName\": \"Wizz Air Holdings Plc\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"ELEZF\",\n    \"companyName\": \"Endesa,
        S.A.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"BLIN\",\n
        \   \"companyName\": \"Bridgeline Digital, Inc.\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"GNNSF\",\n    \"companyName\": \"Genscript
        Biotech Corporation\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"RNFTF\",\n    \"companyName\": \"PJSC Rosneft Oil Company\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"RUSMF\",\n    \"companyName\": \"Russel
        Metals Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"ZAG.VI\",\n    \"companyName\": \"Zumtobel Group AG\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"KINS\",\n    \"companyName\": \"Kingstone
        Companies, Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"TELDF\",\n    \"companyName\": \"Telef\xF3nica Deutschland Holding AG\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"SDC\",\n    \"companyName\":
        \"SmileDirectClub, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"KDDIY\",\n    \"companyName\": \"KDDI Corporation\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"POLY.ME\",\n    \"companyName\": \"Polymetal
        International plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"BIM.PA\",\n    \"companyName\": \"bioM\xE9rieux S.A.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"BENF\",\n    \"companyName\": \"Beneficient\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"ECRAF\",\n    \"companyName\":
        \"Ecora Resources PLC\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"AIRT\",\n    \"companyName\": \"Air T, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"IMGN\",\n    \"companyName\": \"ImmunoGen,
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"UNM\",\n
        \   \"companyName\": \"Unum Group\",\n    \"noOfTranscripts\": \"69\"\n  },\n
        \ {\n    \"symbol\": \"DRQ\",\n    \"companyName\": \"Dril-Quip, Inc.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"CAL\",\n    \"companyName\":
        \"Caleres, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"ALL\",\n    \"companyName\": \"The Allstate Corporation\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"RHI\",\n    \"companyName\": \"Robert
        Half International Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"TMST\",\n    \"companyName\": \"TimkenSteel Corporation\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"ACCD\",\n    \"companyName\": \"Accolade,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"DDEJF\",\n
        \   \"companyName\": \"Dundee Corporation\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"ACBI\",\n    \"companyName\": \"Atlantic Capital
        Bancshares, Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"VTR\",\n    \"companyName\": \"Ventas, Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"ICBK\",\n    \"companyName\": \"County
        Bancorp, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"FPH.NZ\",\n    \"companyName\": \"Fisher & Paykel Healthcare Corporation
        Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"TEP.PA\",\n
        \   \"companyName\": \"Teleperformance SE\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"GNSS\",\n    \"companyName\": \"Genasys Inc.\",\n
        \   \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\": \"BHST\",\n    \"companyName\":
        \"BioHarvest Sciences Inc. Common Stock\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"DLHC\",\n    \"companyName\": \"DLH Holdings
        Corp.\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\": \"GMRE\",\n
        \   \"companyName\": \"Global Medical REIT Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"AIT\",\n    \"companyName\": \"Applied
        Industrial Technologies, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n
        \ {\n    \"symbol\": \"MEGEF\",\n    \"companyName\": \"MEG Energy Corp.\",\n
        \   \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\": \"NTEC\",\n    \"companyName\":
        \"Intec Pharma Ltd\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"EOG\",\n    \"companyName\": \"EOG Resources, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"KRC\",\n    \"companyName\": \"Kilroy
        Realty Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"CPK\",\n    \"companyName\": \"Chesapeake Utilities Corporation\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"PARXF\",\n    \"companyName\": \"Parex
        Resources Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"AXS.AS\",\n    \"companyName\": \"Accsys Technologies PLC\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"0UVX.L\",\n    \"companyName\": \"Electra
        Battery Materials Corporation\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n
        \   \"symbol\": \"ZEVY\",\n    \"companyName\": \"Lightning eMotors, Inc.\",\n
        \   \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"IVQ.TO\",\n    \"companyName\":
        \"Invesque Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"IVCGF\",\n    \"companyName\": \"Iveco Group N.V.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"ITPOF\",\n    \"companyName\": \"Intertape
        Polymer Group Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"HGV\",\n    \"companyName\": \"Hilton Grand Vacations Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"AMS.JO\",\n    \"companyName\": \"Anglo
        American Platinum Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n
        \   \"symbol\": \"CNFR\",\n    \"companyName\": \"Conifer Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"DCPH\",\n    \"companyName\":
        \"Deciphera Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n
        \ {\n    \"symbol\": \"HKHC\",\n    \"companyName\": \"Horizon Kinetics Holding
        Corporation\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"FPH\",\n    \"companyName\": \"Five Point Holdings, LLC\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"OMVJF\",\n    \"companyName\": \"Omv
        AG\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"ULH\",\n
        \   \"companyName\": \"Universal Logistics Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"BROG\",\n    \"companyName\": \"Brooge
        Energy Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"MXCT\",\n    \"companyName\": \"MaxCyte, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"RNTX\",\n    \"companyName\": \"Rein
        Therapeutics Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"BABA\",\n    \"companyName\": \"Alibaba Group Holding Limited\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"GEO.TO\",\n    \"companyName\": \"Geodrill
        Limited\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"ACMR\",\n
        \   \"companyName\": \"ACM Research, Inc.\",\n    \"noOfTranscripts\": \"43\"\n
        \ },\n  {\n    \"symbol\": \"AXGN\",\n    \"companyName\": \"AxoGen, Inc.\",\n
        \   \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"IRS\",\n    \"companyName\":
        \"IRSA Inversiones y Representaciones Sociedad An\xF3nima\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"TRMLF\",\n    \"companyName\": \"Tourmaline
        Oil Corp.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"VT\",\n    \"companyName\": \"Vanguard Total World Stock Index Fund\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"IEP\",\n    \"companyName\":
        \"Icahn Enterprises L.P.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n
        \   \"symbol\": \"NSRGY\",\n    \"companyName\": \"Nestl\xE9 S.A.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"ABG\",\n    \"companyName\": \"Asbury
        Automotive Group, Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"ENELCHILE.SN\",\n    \"companyName\": \"Enel Chile S.A.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"USER\",\n    \"companyName\": \"UserTesting,
        Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"QVCGA\",\n
        \   \"companyName\": \"QVC Group Inc.\",\n    \"noOfTranscripts\": \"58\"\n
        \ },\n  {\n    \"symbol\": \"FLO\",\n    \"companyName\": \"Flowers Foods,
        Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"DHLGY\",\n
        \   \"companyName\": \"Deutsche Post AG\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"WBA\",\n    \"companyName\": \"Walgreens Boots
        Alliance, Inc.\",\n    \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\":
        \"ATER\",\n    \"companyName\": \"Aterian, Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"FENG\",\n    \"companyName\": \"Phoenix
        New Media Limited\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"TUYA\",\n    \"companyName\": \"Tuya Inc.\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"ELUX-B.ST\",\n    \"companyName\": \"AB Electrolux
        (publ)\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"TERRF\",\n
        \   \"companyName\": \"Terna - Rete Elettrica Nazionale Societ\xE0 per Azioni\",\n
        \   \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"DAO\",\n    \"companyName\":
        \"Youdao, Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"NEXT.TO\",\n    \"companyName\": \"NextSource Materials Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"NTUS\",\n    \"companyName\": \"Natus
        Medical Incorporated\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"CRTO\",\n    \"companyName\": \"Criteo S.A.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"TSYHY\",\n    \"companyName\": \"TravelSky
        Technology Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"MITSY\",\n    \"companyName\": \"Mitsui & Co., Ltd.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"CSL.AX\",\n    \"companyName\": \"CSL
        Limited\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"YUGVF\",\n
        \   \"companyName\": \"YouGov plc\",\n    \"noOfTranscripts\": \"10\"\n  },\n
        \ {\n    \"symbol\": \"BVNKF\",\n    \"companyName\": \"Bavarian Nordic A/S\",\n
        \   \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"SIRI\",\n    \"companyName\":
        \"Sirius XM Holdings Inc.\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n
        \   \"symbol\": \"WYNN\",\n    \"companyName\": \"Wynn Resorts, Limited\",\n
        \   \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"CION\",\n    \"companyName\":
        \"CION Investment Corporation\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"ACIW\",\n    \"companyName\": \"ACI Worldwide, Inc.\",\n
        \   \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\": \"ACRS\",\n    \"companyName\":
        \"Aclaris Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n
        \   \"symbol\": \"ECOR.L\",\n    \"companyName\": \"Ecora Resources PLC\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"NFI.TO\",\n    \"companyName\":
        \"NFI Group Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"AAVXF\",\n    \"companyName\": \"Abivax S.A.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"Z\",\n    \"companyName\": \"Zillow Group,
        Inc. Class C\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"CYAD.BR\",\n    \"companyName\": \"Celyad Oncology S.A.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"3436.T\",\n    \"companyName\": \"Sumco
        Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"EN.PA\",\n    \"companyName\": \"Bouygues S.A.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"XTRA.TO\",\n    \"companyName\": \"Xtract
        One Technologies Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"BLX\",\n    \"companyName\": \"Banco Latinoamericano de Comercio Exterior,
        S. A.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\": \"THQQF\",\n
        \   \"companyName\": \"Embracer Group AB (publ)\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"ENV\",\n    \"companyName\": \"Envestnet,
        Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"NVTK.ME\",\n
        \   \"companyName\": \"Pao Novatek\",\n    \"noOfTranscripts\": \"2\"\n  },\n
        \ {\n    \"symbol\": \"CBA.AX\",\n    \"companyName\": \"Commonwealth Bank
        of Australia\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"JPM\",\n    \"companyName\": \"JPMorgan Chase & Co.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"SMWB\",\n    \"companyName\": \"Similarweb
        Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"NURO\",\n
        \   \"companyName\": \"NeuroMetrix, Inc.\",\n    \"noOfTranscripts\": \"50\"\n
        \ },\n  {\n    \"symbol\": \"UNCRY\",\n    \"companyName\": \"UniCredit S.p.A.\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"CE\",\n    \"companyName\":
        \"Celanese Corporation\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"LNXSF\",\n    \"companyName\": \"Lanxess AG\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"CNXC\",\n    \"companyName\": \"Concentrix
        Corporation\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"BZAI\",\n    \"companyName\": \"Blaize Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"UNFI\",\n    \"companyName\": \"United
        Natural Foods, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"OGI\",\n    \"companyName\": \"Organigram Global Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"INFY.NS\",\n    \"companyName\": \"Infosys
        Limited\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"CGS.AX\",\n
        \   \"companyName\": \"Cogstate Limited\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"EE\",\n    \"companyName\": \"Excelerate Energy,
        Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"EHMEF\",\n
        \   \"companyName\": \"goeasy Ltd.\",\n    \"noOfTranscripts\": \"36\"\n  },\n
        \ {\n    \"symbol\": \"D\",\n    \"companyName\": \"Dominion Energy, Inc.\",\n
        \   \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\": \"ADI\",\n    \"companyName\":
        \"Analog Devices, Inc.\",\n    \"noOfTranscripts\": \"74\"\n  },\n  {\n    \"symbol\":
        \"ALE\",\n    \"companyName\": \"ALLETE, Inc.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"BEPC\",\n    \"companyName\": \"Brookfield
        Renewable Corporation\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"NMIH\",\n    \"companyName\": \"NMI Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"ACRX\",\n    \"companyName\": \"AcelRx
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\":
        \"CRTA.L\",\n    \"companyName\": \"Cirata plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"BYU\",\n    \"companyName\": \"BAIYU Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"RDGT\",\n
        \   \"companyName\": \"Ridgetech Inc.\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"SBUX\",\n    \"companyName\": \"Starbucks Corporation\",\n
        \   \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"FE\",\n    \"companyName\":
        \"FirstEnergy Corp.\",\n    \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\":
        \"IMCR\",\n    \"companyName\": \"Immunocore Holdings plc\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"APYX\",\n    \"companyName\": \"Apyx Medical
        Corporation\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"KPT.TO\",\n    \"companyName\": \"KP Tissue Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"CTARF\",\n    \"companyName\": \"Centaurus
        Energy Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"GRF.MC\",\n    \"companyName\": \"Grifols, S.A.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"HXGCF\",\n    \"companyName\": \"Hexagon
        Composites ASA\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"CORBF\",\n    \"companyName\": \"Global Cord Blood Corporation\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"ECELF\",\n    \"companyName\": \"Eurocell
        plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SGMO\",\n
        \   \"companyName\": \"Sangamo Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"IEX\",\n    \"companyName\": \"IDEX Corporation\",\n
        \   \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"SWM\",\n    \"companyName\":
        \"Schweitzer-Mauduit International, Inc.\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"TTAN\",\n    \"companyName\": \"ServiceTitan,
        Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"FEC.TO\",\n
        \   \"companyName\": \"Frontera Energy Corporation\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"LNSR\",\n    \"companyName\": \"LENSAR,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"DIE.BR\",\n
        \   \"companyName\": \"D'Ieteren Group S.A.\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"U\",\n    \"companyName\": \"Unity Software Inc.\",\n
        \   \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"JETMF\",\n    \"companyName\":
        \"Global Crossing Airlines Group Inc.\",\n    \"noOfTranscripts\": \"13\"\n
        \ },\n  {\n    \"symbol\": \"OEZVF\",\n    \"companyName\": \"Verbund AG\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"HCG.TO\",\n    \"companyName\":
        \"Home Capital Group Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n
        \   \"symbol\": \"DSS\",\n    \"companyName\": \"DSS, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"M0YN.DE\",\n    \"companyName\": \"Mynaric
        AG\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"HMCBF\",\n
        \   \"companyName\": \"Home Capital Group Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"SEEMF\",\n    \"companyName\": \"Seeing
        Machines Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"VERO\",\n    \"companyName\": \"Venus Concept Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"MD\",\n    \"companyName\": \"Pediatrix
        Medical Group, Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"IMOS\",\n    \"companyName\": \"ChipMOS TECHNOLOGIES Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"RPID\",\n    \"companyName\": \"Rapid
        Micro Biosystems, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"NYAX.TA\",\n    \"companyName\": \"Nayax Ltd.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"BMMJ\",\n    \"companyName\": \"Body and
        Mind Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"ZZHGF\",\n
        \   \"companyName\": \"ZhongAn Online P & C Insurance Co., Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"TIPT\",\n    \"companyName\": \"Tiptree
        Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\": \"OIBR3.SA\",\n
        \   \"companyName\": \"Oi S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n
        \ {\n    \"symbol\": \"EEFT\",\n    \"companyName\": \"Euronet Worldwide,
        Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\": \"ATM.NZ\",\n
        \   \"companyName\": \"The a2 Milk Company Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"AOSL\",\n    \"companyName\": \"Alpha
        and Omega Semiconductor Limited\",\n    \"noOfTranscripts\": \"46\"\n  },\n
        \ {\n    \"symbol\": \"SQZZF\",\n    \"companyName\": \"Serica Energy plc\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"LCHTF\",\n    \"companyName\":
        \"Text S.A.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"THTX\",\n    \"companyName\": \"Theratechnologies Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"MH\",\n    \"companyName\": \"McGraw
        Hill, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"BRP\",\n    \"companyName\": \"BRP Group, Inc.\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"QMCI\",\n    \"companyName\": \"QuoteMedia,
        Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"DBO.TO\",\n
        \   \"companyName\": \"D-BOX Technologies Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SZGPF\",\n    \"companyName\": \"Salzgitter
        AG\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"XXII\",\n
        \   \"companyName\": \"22nd Century Group, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"ORC\",\n    \"companyName\": \"Orchid
        Island Capital, Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"0788.HK\",\n    \"companyName\": \"China Tower Corporation Limited\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"EMR\",\n    \"companyName\":
        \"Emerson Electric Co.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"VSBGF\",\n    \"companyName\": \"VSBLTY Groupe Technologies Corp.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"LAB\",\n    \"companyName\": \"Standard
        BioTools Inc.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"0027.HK\",\n    \"companyName\": \"Galaxy Entertainment Group Limited\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"PSH.AS\",\n    \"companyName\":
        \"Pershing Square Holdings, Ltd.\",\n    \"noOfTranscripts\": \"10\"\n  },\n
        \ {\n    \"symbol\": \"CLPHY\",\n    \"companyName\": \"CLP Holdings Limited\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"BTE\",\n    \"companyName\":
        \"Baytex Energy Corp.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"DB1.DE\",\n    \"companyName\": \"Deutsche B\xF6rse AG\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"RKUNY\",\n    \"companyName\": \"Rakuten
        Group, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"GGBR4.SA\",\n    \"companyName\": \"Gerdau S.A.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"SGRY\",\n    \"companyName\": \"Surgery
        Partners, Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"MMB.PA\",\n    \"companyName\": \"Lagardere S.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"SHPW\",\n    \"companyName\": \"Shapeways
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"SIEGY\",\n    \"companyName\": \"Siemens AG\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"TEUM\",\n    \"companyName\": \"Pareteum
        Corporation\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"KPTSF\",\n    \"companyName\": \"KP Tissue Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"GPI\",\n    \"companyName\": \"Group
        1 Automotive, Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"BIIB\",\n    \"companyName\": \"Biogen Inc.\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"CLMT\",\n    \"companyName\": \"Calumet,
        Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"SMIN.L\",\n
        \   \"companyName\": \"Smiths Group plc\",\n    \"noOfTranscripts\": \"20\"\n
        \ },\n  {\n    \"symbol\": \"BRDCY\",\n    \"companyName\": \"Bridgestone
        Corporation\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"SREDF\",\n    \"companyName\": \"Storebrand ASA\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"PAIOF\",\n    \"companyName\": \"Paion
        AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"INTA\",\n
        \   \"companyName\": \"Intapp, Inc.\",\n    \"noOfTranscripts\": \"16\"\n
        \ },\n  {\n    \"symbol\": \"4755.T\",\n    \"companyName\": \"Rakuten Group,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"KIRK\",\n
        \   \"companyName\": \"Kirkland's, Inc.\",\n    \"noOfTranscripts\": \"54\"\n
        \ },\n  {\n    \"symbol\": \"ELVA\",\n    \"companyName\": \"Electrovaya Inc.\",\n
        \   \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"AMTD\",\n    \"companyName\":
        \"AMTD IDEA Group\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"NWHM\",\n    \"companyName\": \"The New Home Company Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"LX\",\n    \"companyName\": \"LexinFintech
        Holdings Ltd.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"ALCO\",\n    \"companyName\": \"Alico, Inc.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"ML\",\n    \"companyName\": \"MoneyLion
        Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"PST.MI\",\n
        \   \"companyName\": \"Poste Italiane S.p.A.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"EVRI\",\n    \"companyName\": \"Everi
        Holdings Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"ALEC\",\n    \"companyName\": \"Alector, Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"MYGN\",\n    \"companyName\": \"Myriad
        Genetics, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"DITHF\",\n    \"companyName\": \"DS Smith Plc\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"HLE.DE\",\n    \"companyName\": \"HELLA
        GmbH & Co. KGaA\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"MUX\",\n    \"companyName\": \"McEwen Mining Inc.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"AMS\",\n    \"companyName\": \"American
        Shared Hospital Services\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n
        \   \"symbol\": \"EVAX\",\n    \"companyName\": \"Evaxion Biotech A/S\",\n
        \   \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"GDI.TO\",\n
        \   \"companyName\": \"GDI Integrated Facility Services Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"SUI\",\n    \"companyName\": \"Sun Communities,
        Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"MET\",\n
        \   \"companyName\": \"MetLife, Inc.\",\n    \"noOfTranscripts\": \"71\"\n
        \ },\n  {\n    \"symbol\": \"NVAX\",\n    \"companyName\": \"Novavax, Inc.\",\n
        \   \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"MAERSK-B.CO\",\n
        \   \"companyName\": \"A.P. M\xF8ller - M\xE6rsk A/S\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"ENLT\",\n    \"companyName\": \"Enlight
        Renewable Energy Ltd\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"SWKH\",\n    \"companyName\": \"SWK Holdings Corporation\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"SLQT\",\n    \"companyName\": \"SelectQuote,
        Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\": \"ENSV\",\n
        \   \"companyName\": \"Enservco Corporation\",\n    \"noOfTranscripts\": \"34\"\n
        \ },\n  {\n    \"symbol\": \"CBH\",\n    \"companyName\": \"Virtus Convertible
        & Income 2024 Target Term Fund\",\n    \"noOfTranscripts\": \"2\"\n  },\n
        \ {\n    \"symbol\": \"PFLT\",\n    \"companyName\": \"PennantPark Floating
        Rate Capital Ltd.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"SWRAY\",\n    \"companyName\": \"Swire Pacific Limited\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"BAH\",\n    \"companyName\": \"Booz Allen
        Hamilton Holding Corporation\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n
        \   \"symbol\": \"RMD\",\n    \"companyName\": \"ResMed Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"MTLRP.ME\",\n    \"companyName\": \"Mechel
        PAO\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"ATEX\",\n
        \   \"companyName\": \"Anterix Inc.\",\n    \"noOfTranscripts\": \"31\"\n
        \ },\n  {\n    \"symbol\": \"IBE.MC\",\n    \"companyName\": \"Iberdrola,
        S.A.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"ASPS\",\n
        \   \"companyName\": \"Altisource Portfolio Solutions S.A.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"VNET\",\n    \"companyName\": \"VNET
        Group, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"SOLB.BR\",\n    \"companyName\": \"Solvay S.A.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"WTER\",\n    \"companyName\": \"The Alkaline
        Water Company Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"CTEC.L\",\n    \"companyName\": \"ConvaTec Group Plc\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"SYA.AX\",\n    \"companyName\": \"Sayona
        Mining Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CERS\",\n    \"companyName\": \"Cerus Corporation\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"DM\",\n    \"companyName\": \"Desktop
        Metal, Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"SRE\",\n    \"companyName\": \"Sempra\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"0142.HK\",\n    \"companyName\": \"First Pacific
        Company Limited\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"INUV\",\n    \"companyName\": \"Inuvo, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"SPR\",\n    \"companyName\": \"Spirit
        AeroSystems Holdings, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n
        \   \"symbol\": \"KGFHF\",\n    \"companyName\": \"Kingfisher plc\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"VCYT\",\n    \"companyName\": \"Veracyte,
        Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"NTTYY\",\n
        \   \"companyName\": \"NTT, Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"GECC\",\n    \"companyName\": \"Great Elm Capital Corp.\",\n
        \   \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"PMCUF\",\n    \"companyName\":
        \"Pro Medicus Limited\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"CHUY\",\n    \"companyName\": \"Chuy's Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"47\"\n  },\n  {\n    \"symbol\": \"LAS-A.TO\",\n    \"companyName\": \"Lassonde
        Industries Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"AI.PA\",\n    \"companyName\": \"L'Air Liquide S.A.\",\n    \"noOfTranscripts\":
        \"47\"\n  },\n  {\n    \"symbol\": \"FHB\",\n    \"companyName\": \"First
        Hawaiian, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"INPST.AS\",\n    \"companyName\": \"InPost S.A.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"MEDS\",\n    \"companyName\": \"TRxADE
        HEALTH, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"PODC\",\n    \"companyName\": \"PodcastOne, Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"NOTE\",\n    \"companyName\": \"FiscalNote
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"NI\",\n    \"companyName\": \"NiSource Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"KNOP\",\n    \"companyName\": \"KNOT
        Offshore Partners LP\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"BDX\",\n    \"companyName\": \"Becton, Dickinson and Company\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"IQE.L\",\n    \"companyName\": \"IQE
        plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"SUPGF\",\n
        \   \"companyName\": \"Superior Gold Inc.\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"UBS\",\n    \"companyName\": \"UBS Group AG\",\n
        \   \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"SSHPF\",\n    \"companyName\":
        \"Vow ASA\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"LMAT\",\n
        \   \"companyName\": \"LeMaitre Vascular, Inc.\",\n    \"noOfTranscripts\":
        \"68\"\n  },\n  {\n    \"symbol\": \"GLEN.L\",\n    \"companyName\": \"Glencore
        plc\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"RAC\",\n
        \   \"companyName\": \"Rithm Acquisition Corp.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MGIC.TA\",\n    \"companyName\": \"Magic
        Software Enterprises Ltd.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"PLL\",\n    \"companyName\": \"Piedmont Lithium Inc.\",\n
        \   \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"STIM\",\n    \"companyName\":
        \"Neuronetics, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"FRHLF\",\n    \"companyName\": \"Freehold Royalties Ltd.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"MSGM\",\n    \"companyName\": \"Motorsport
        Games Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"HIVE\",\n    \"companyName\": \"HIVE Digital Technologies Ltd.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"M44U.SI\",\n    \"companyName\": \"Mapletree
        Logistics Trust\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"NR\",\n    \"companyName\": \"Newpark Resources, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"GDS\",\n    \"companyName\": \"GDS Holdings
        Limited\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"TITN\",\n
        \   \"companyName\": \"Titan Machinery Inc.\",\n    \"noOfTranscripts\": \"64\"\n
        \ },\n  {\n    \"symbol\": \"LEAT\",\n    \"companyName\": \"Leatt Corporation\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"SMDM\",\n    \"companyName\":
        \"The Singing Machine Company, Inc.\",\n    \"noOfTranscripts\": \"11\"\n
        \ },\n  {\n    \"symbol\": \"STMH\",\n    \"companyName\": \"Stem Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"NYCB\",\n
        \   \"companyName\": \"New York Community Bancorp, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"BMA\",\n    \"companyName\": \"Banco
        Macro S.A.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"VLNS.TO\",\n    \"companyName\": \"The Valens Company Inc.\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"DLTNF\",\n    \"companyName\": \"Delta
        9 Cannabis Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"MNRO\",\n    \"companyName\": \"Monro, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"TGSU2.BA\",\n    \"companyName\": \"Transportadora
        de Gas del Sur S.A.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"AKSO.OL\",\n    \"companyName\": \"Aker Solutions ASA\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"TECH\",\n    \"companyName\": \"Bio-Techne
        Corporation\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"KLRS\",\n    \"companyName\": \"Kalaris Therapeutics Inc\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"KNDI\",\n    \"companyName\": \"Kandi
        Technologies Group, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n
        \   \"symbol\": \"TGSGY\",\n    \"companyName\": \"Tgs Asa\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"PAYO\",\n    \"companyName\": \"Payoneer
        Global Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"LHA.DE\",\n    \"companyName\": \"Deutsche Lufthansa AG\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"0K6O.L\",\n    \"companyName\": \"Farfetch
        Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"NTRA\",\n
        \   \"companyName\": \"Natera, Inc.\",\n    \"noOfTranscripts\": \"38\"\n
        \ },\n  {\n    \"symbol\": \"BAMM.CN\",\n    \"companyName\": \"Body and Mind
        Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"VIV\",\n
        \   \"companyName\": \"Telef\xF4nica Brasil S.A.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"BDI.TO\",\n    \"companyName\": \"Black
        Diamond Group Limited\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"VODAF\",\n    \"companyName\": \"Vodacom Group Limited\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"KRN.DE\",\n    \"companyName\": \"Krones
        AG\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"PHI\",\n
        \   \"companyName\": \"PLDT Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n
        \ {\n    \"symbol\": \"BNR\",\n    \"companyName\": \"Burning Rock Biotech
        Limited\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"WBX\",\n
        \   \"companyName\": \"Wallbox N.V.\",\n    \"noOfTranscripts\": \"15\"\n
        \ },\n  {\n    \"symbol\": \"GPS\",\n    \"companyName\": \"The Gap, Inc.\",\n
        \   \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\": \"SCHP.SW\",\n
        \   \"companyName\": \"Schindler Holding AG\",\n    \"noOfTranscripts\": \"24\"\n
        \ },\n  {\n    \"symbol\": \"FWONA\",\n    \"companyName\": \"Formula One
        Group\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"CABO\",\n
        \   \"companyName\": \"Cable One, Inc.\",\n    \"noOfTranscripts\": \"38\"\n
        \ },\n  {\n    \"symbol\": \"SEER\",\n    \"companyName\": \"Seer, Inc.\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"PCG\",\n    \"companyName\":
        \"Pacific Gas & Electric Co.\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n
        \   \"symbol\": \"TXN\",\n    \"companyName\": \"Texas Instruments Incorporated\",\n
        \   \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"TTM\",\n    \"companyName\":
        \"Tata Motors Limited\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"XTRAF\",\n    \"companyName\": \"Xtract One Technologies Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"SMHN.DE\",\n    \"companyName\": \"S\xDCSS
        MicroTec SE\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"PRN.TO\",\n    \"companyName\": \"Profound Medical Corp.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"TUEMQ\",\n    \"companyName\": \"Tuesday
        Morning Corporation\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"DPDW\",\n    \"companyName\": \"Koil Energy Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"HTWSF\",\n    \"companyName\": \"Helios
        Towers plc\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"SNN\",\n    \"companyName\": \"Smith & Nephew plc\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"VNNVF\",\n    \"companyName\": \"Vonovia
        SE\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"BRFS\",\n
        \   \"companyName\": \"Brf S.a.\",\n    \"noOfTranscripts\": \"45\"\n  },\n
        \ {\n    \"symbol\": \"JKS\",\n    \"companyName\": \"JinkoSolar Holding Co.,
        Ltd.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\": \"KMTUY\",\n
        \   \"companyName\": \"Komatsu Ltd.\",\n    \"noOfTranscripts\": \"10\"\n
        \ },\n  {\n    \"symbol\": \"CLSK\",\n    \"companyName\": \"CleanSpark, Inc.\",\n
        \   \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"SANM\",\n    \"companyName\":
        \"Sanmina Corporation\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"GTLB\",\n    \"companyName\": \"GitLab Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"CRDA.L\",\n    \"companyName\": \"Croda
        International Plc\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"KVUE\",\n    \"companyName\": \"Kenvue Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"ENTA\",\n    \"companyName\": \"Enanta
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\":
        \"TOBII.ST\",\n    \"companyName\": \"Tobii AB (publ)\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"RSLS\",\n    \"companyName\": \"ReShape
        Lifesciences Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"QGEN\",\n    \"companyName\": \"Qiagen N.V.\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"ICL.TA\",\n    \"companyName\": \"ICL
        Group Ltd\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\":
        \"CPRT\",\n    \"companyName\": \"Copart, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"TEVA.TA\",\n    \"companyName\": \"Teva
        Pharmaceutical Industries Limited\",\n    \"noOfTranscripts\": \"75\"\n  },\n
        \ {\n    \"symbol\": \"MB.MI\",\n    \"companyName\": \"Mediobanca Banca di
        Credito Finanziario S.p.A.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n
        \   \"symbol\": \"EDP.LS\",\n    \"companyName\": \"EDP - Energias de Portugal,
        S.A.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"PHG\",\n
        \   \"companyName\": \"Koninklijke Philips N.V.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"TOL\",\n    \"companyName\": \"Toll Brothers,
        Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"MCHP\",\n
        \   \"companyName\": \"Microchip Technology Incorporated\",\n    \"noOfTranscripts\":
        \"74\"\n  },\n  {\n    \"symbol\": \"ULCC\",\n    \"companyName\": \"Frontier
        Group Holdings, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"BLFY\",\n    \"companyName\": \"Blue Foundry Bancorp\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"PFS\",\n    \"companyName\": \"Provident
        Financial Services, Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n
        \   \"symbol\": \"TGE\",\n    \"companyName\": \"The Generation Essentials
        Group\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"NEWT\",\n
        \   \"companyName\": \"NewtekOne, Inc.\",\n    \"noOfTranscripts\": \"55\"\n
        \ },\n  {\n    \"symbol\": \"LYFT\",\n    \"companyName\": \"Lyft, Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"CTAS\",\n    \"companyName\":
        \"Cintas Corporation\",\n    \"noOfTranscripts\": \"74\"\n  },\n  {\n    \"symbol\":
        \"CLQDF\",\n    \"companyName\": \"Cliq Digital AG\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"HMN\",\n    \"companyName\": \"Horace
        Mann Educators Corporation\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n
        \   \"symbol\": \"BKCYF\",\n    \"companyName\": \"Bank of Cyprus Holdings
        Public Limited Company\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"PATH\",\n    \"companyName\": \"UiPath Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"CVC.AS\",\n    \"companyName\": \"CVC
        Capital Partners plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"IDEX\",\n    \"companyName\": \"Ideanomics, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"RY\",\n    \"companyName\": \"Royal Bank
        of Canada\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"ESAB\",\n    \"companyName\": \"ESAB Corporation\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"ICU\",\n    \"companyName\": \"SeaStar
        Medical Holding Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"HFFG\",\n    \"companyName\": \"HF Foods Group Inc.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"ORLY\",\n    \"companyName\":
        \"O'Reilly Automotive, Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n
        \   \"symbol\": \"COST\",\n    \"companyName\": \"Costco Wholesale Corporation\",\n
        \   \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\": \"SIG\",\n    \"companyName\":
        \"Signet Jewelers Limited\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n
        \   \"symbol\": \"MODVQ\",\n    \"companyName\": \"ModivCare Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"BWMX\",\n    \"companyName\": \"Betterware
        de M\xE9xico, S.A.P.I. de C.V.\",\n    \"noOfTranscripts\": \"18\"\n  },\n
        \ {\n    \"symbol\": \"ACGL\",\n    \"companyName\": \"Arch Capital Group
        Ltd.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"SLE\",\n
        \   \"companyName\": \"Super League Enterprise, Inc.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"GMKN.ME\",\n    \"companyName\": \"PJSC
        Mining and Metallurgical Company Norilsk Nickel\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"CAMLF\",\n    \"companyName\": \"Central
        Asia Metals plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"FIP\",\n    \"companyName\": \"FTAI Infrastructure Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"PSNL\",\n    \"companyName\": \"Personalis,
        Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"AUMN\",\n
        \   \"companyName\": \"Golden Minerals Company\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"RYTM\",\n    \"companyName\": \"Rhythm
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"MYCOF\",\n    \"companyName\": \"Mydecine Innovations Group Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"DRKTF\",\n    \"companyName\": \"Darktrace
        plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"LNZNF\",\n
        \   \"companyName\": \"Lenzing AG\",\n    \"noOfTranscripts\": \"8\"\n  },\n
        \ {\n    \"symbol\": \"GLPG\",\n    \"companyName\": \"Galapagos N.V.\",\n
        \   \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"ESLT\",\n    \"companyName\":
        \"Elbit Systems Ltd.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"SPIR\",\n    \"companyName\": \"Spire Global, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"PLOW\",\n    \"companyName\": \"Douglas
        Dynamics, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"COOP\",\n    \"companyName\": \"Mr. Cooper Group Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"FIHL\",\n    \"companyName\": \"Fidelis
        Insurance Holdings Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n
        \   \"symbol\": \"ACEL\",\n    \"companyName\": \"Accel Entertainment, Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"PWR\",\n    \"companyName\":
        \"Quanta Services, Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"EDRY\",\n    \"companyName\": \"EuroDry Ltd.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"XNET\",\n    \"companyName\": \"Xunlei
        Limited\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\": \"SURG\",\n
        \   \"companyName\": \"SurgePays, Inc.\",\n    \"noOfTranscripts\": \"14\"\n
        \ },\n  {\n    \"symbol\": \"BGO.L\",\n    \"companyName\": \"Bango PLC\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"PEI.V\",\n    \"companyName\":
        \"Prospera Energy Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"EVGN\",\n    \"companyName\": \"Evogene Ltd.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"NTLA\",\n    \"companyName\": \"Intellia
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"IMPL\",\n    \"companyName\": \"Impel Pharmaceuticals Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"MBG.DE\",\n    \"companyName\": \"Mercedes-Benz
        Group AG\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"CGJTF\",\n
        \   \"companyName\": \"Cargojet Inc.\",\n    \"noOfTranscripts\": \"25\"\n
        \ },\n  {\n    \"symbol\": \"TMXXF\",\n    \"companyName\": \"TMX Group Limited\",\n
        \   \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"SHLF.OL\",\n
        \   \"companyName\": \"Shelf Drilling, Ltd.\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"FOXA\",\n    \"companyName\": \"Fox Corporation\",\n
        \   \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"EVN.AX\",\n
        \   \"companyName\": \"Evolution Mining Limited\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"DRM.TO\",\n    \"companyName\": \"Dream
        Unlimited Corp.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"TISI\",\n    \"companyName\": \"Team, Inc.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"LDI\",\n    \"companyName\": \"loanDepot,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"RLXXF\",\n
        \   \"companyName\": \"RELX Plc\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"PLNH\",\n    \"companyName\": \"Planet 13 Holdings
        Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"CINT\",\n
        \   \"companyName\": \"CI&T Inc\",\n    \"noOfTranscripts\": \"15\"\n  },\n
        \ {\n    \"symbol\": \"ANPCY\",\n    \"companyName\": \"ANGLE plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"EMRAF\",\n    \"companyName\": \"Emera
        Incorporated\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"RELY\",\n    \"companyName\": \"Remitly Global, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"UNBLF\",\n    \"companyName\": \"Unibail-Rodamco-Westfield
        SE\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"VALE\",\n
        \   \"companyName\": \"Vale S.A.\",\n    \"noOfTranscripts\": \"55\"\n  },\n
        \ {\n    \"symbol\": \"105560.KS\",\n    \"companyName\": \"KB Financial Group
        Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"SWP.TO\",\n
        \   \"companyName\": \"Swiss Water Decaffeinated Coffee Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MFLTY\",\n    \"companyName\": \"Missfresh
        Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"BNTGY\",\n
        \   \"companyName\": \"Brenntag SE\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"VRME\",\n    \"companyName\": \"VerifyMe, Inc.\",\n
        \   \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"CM\",\n    \"companyName\":
        \"Canadian Imperial Bank of Commerce\",\n    \"noOfTranscripts\": \"58\"\n
        \ },\n  {\n    \"symbol\": \"AVT\",\n    \"companyName\": \"Avnet, Inc.\",\n
        \   \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"DS\",\n    \"companyName\":
        \"Drive Shack Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"DSEY\",\n    \"companyName\": \"Diversey Holdings, Ltd.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"LXFR\",\n    \"companyName\": \"Luxfer
        Holdings PLC\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\":
        \"WDC\",\n    \"companyName\": \"Western Digital Corporation\",\n    \"noOfTranscripts\":
        \"76\"\n  },\n  {\n    \"symbol\": \"ASTL\",\n    \"companyName\": \"Algoma
        Steel Group Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"AGM\",\n    \"companyName\": \"Federal Agricultural Mortgage Corporation\",\n
        \   \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"EVK.DE\",\n
        \   \"companyName\": \"Evonik Industries AG\",\n    \"noOfTranscripts\": \"25\"\n
        \ },\n  {\n    \"symbol\": \"PZCUY\",\n    \"companyName\": \"PZ Cussons plc\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"KNSA\",\n    \"companyName\":
        \"Kiniksa Pharmaceuticals, Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n
        \ {\n    \"symbol\": \"UHAL\",\n    \"companyName\": \"U-Haul Holding Company\",\n
        \   \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"KSPI\",\n    \"companyName\":
        \"Joint Stock Company Kaspi.kz\",\n    \"noOfTranscripts\": \"7\"\n  },\n
        \ {\n    \"symbol\": \"VIAOY\",\n    \"companyName\": \"VIA optronics AG\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"IQV\",\n    \"companyName\":
        \"IQVIA Holdings Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"FINGF\",\n    \"companyName\": \"Finning International Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"STX\",\n    \"companyName\": \"Seagate
        Technology Holdings plc\",\n    \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\":
        \"8604.T\",\n    \"companyName\": \"Nomura Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"UFI\",\n    \"companyName\": \"Unifi,
        Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\": \"LSB\",\n
        \   \"companyName\": \"LakeShore Biopharma Co., Ltd\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"WHR\",\n    \"companyName\": \"Whirlpool
        Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"DVLT\",\n    \"companyName\": \"Datavault AI Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"8031.T\",\n    \"companyName\": \"Mitsui
        & Co., Ltd.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"MRV.TO\",\n    \"companyName\": \"Nuvo Pharmaceuticals Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"BBLN\",\n    \"companyName\": \"Babylon
        Holdings Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"HVRRF\",\n    \"companyName\": \"Hannover R\xFCck SE\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"WBRBY\",\n    \"companyName\": \"Wienerberger
        AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"SKFRY\",\n
        \   \"companyName\": \"AB SKF (publ)\",\n    \"noOfTranscripts\": \"31\"\n
        \ },\n  {\n    \"symbol\": \"EME\",\n    \"companyName\": \"EMCOR Group, Inc.\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"LDO.MI\",\n
        \   \"companyName\": \"Leonardo S.p.A.\",\n    \"noOfTranscripts\": \"23\"\n
        \ },\n  {\n    \"symbol\": \"CMPR\",\n    \"companyName\": \"Cimpress plc\",\n
        \   \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\": \"BICEY\",\n    \"companyName\":
        \"Soci\xE9t\xE9 BIC S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n
        \   \"symbol\": \"AAPL\",\n    \"companyName\": \"Apple Inc.\",\n    \"noOfTranscripts\":
        \"80\"\n  },\n  {\n    \"symbol\": \"CCU\",\n    \"companyName\": \"Compa\xF1\xEDa
        Cervecer\xEDas Unidas S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n
        \   \"symbol\": \"BSBR\",\n    \"companyName\": \"Banco Santander (Brasil)
        S.A.\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"AS\",\n
        \   \"companyName\": \"Amer Sports, Inc.\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"FUNFF\",\n    \"companyName\": \"FansUnite Entertainment
        Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"LMFA\",\n
        \   \"companyName\": \"LM Funding America, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"RNSDF\",\n    \"companyName\": \"Renault
        S.A.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"EQGPF\",\n
        \   \"companyName\": \"EQB Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n
        \ {\n    \"symbol\": \"IDGXF\",\n    \"companyName\": \"Integrated Diagnostics
        Holdings plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"AXNX\",\n    \"companyName\": \"Axonics, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"BYRN\",\n    \"companyName\": \"Byrna
        Technologies Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"ASTVF\",\n    \"companyName\": \"Austevoll Seafood ASA\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"AMADF\",\n    \"companyName\": \"Amadeus
        IT Group, S.A.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"FXLV\",\n    \"companyName\": \"F45 Training Holdings Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"KGSPF\",\n    \"companyName\": \"Kingspan
        Group plc\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"OSBC\",\n    \"companyName\": \"Old Second Bancorp, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"IBN\",\n    \"companyName\": \"ICICI
        Bank Limited\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"LOOMIS.ST\",\n    \"companyName\": \"Loomis AB (publ)\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"WLFC\",\n    \"companyName\": \"Willis
        Lease Finance Corporation\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"DGWPF\",\n    \"companyName\": \"Dr\xE4gerwerk AG & Co.
        KGaA\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"YQ\",\n
        \   \"companyName\": \"17 Education & Technology Group Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"1316.HK\",\n    \"companyName\": \"Nexteer
        Automotive Group Limited\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"CFMOF\",\n    \"companyName\": \"Cofinimmo S.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"9433.T\",\n    \"companyName\": \"KDDI
        Corporation\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"BB.PA\",\n    \"companyName\": \"Soci\xE9t\xE9 BIC S.A.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"NOTV\",\n    \"companyName\": \"Inotiv,
        Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"NUE\",\n
        \   \"companyName\": \"Nucor Corporation\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"GCL.TO\",\n    \"companyName\": \"Colabor Group
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"JG\",\n
        \   \"companyName\": \"Aurora Mobile Limited\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"CANF\",\n    \"companyName\": \"Can-Fite
        BioPharma Ltd.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"NRG\",\n    \"companyName\": \"NRG Energy, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"MNR\",\n    \"companyName\": \"Mach Natural
        Resources LP\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"SJW\",\n    \"companyName\": \"SJW Group\",\n    \"noOfTranscripts\": \"60\"\n
        \ },\n  {\n    \"symbol\": \"NVDA\",\n    \"companyName\": \"NVIDIA Corporation\",\n
        \   \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\": \"HSTM\",\n    \"companyName\":
        \"HealthStream, Inc.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\":
        \"OMC\",\n    \"companyName\": \"Omnicom Group Inc.\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"CEPU\",\n    \"companyName\": \"Central
        Puerto S.A.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"RYAAY\",\n    \"companyName\": \"Ryanair Holdings plc\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"MAGN\",\n    \"companyName\": \"Magnera
        Corp.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"GPN\",\n
        \   \"companyName\": \"Global Payments Inc.\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"MRFG3.SA\",\n    \"companyName\": \"Marfrig Global
        Foods S.A.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"HCM\",\n    \"companyName\": \"HUTCHMED (China) Limited\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"CAIXY\",\n    \"companyName\": \"CaixaBank,
        S.A.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"2518.HK\",\n
        \   \"companyName\": \"Autohome Inc.\",\n    \"noOfTranscripts\": \"42\"\n
        \ },\n  {\n    \"symbol\": \"AATC\",\n    \"companyName\": \"Autoscope Technologies
        Corporation\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"ALO.PA\",\n    \"companyName\": \"Alstom S.A.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"PLTR\",\n    \"companyName\": \"Palantir
        Technologies Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"CLPBF\",\n    \"companyName\": \"Coloplast A/S\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"1698.HK\",\n    \"companyName\": \"Tencent
        Music Entertainment Group\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n
        \   \"symbol\": \"TBVPF\",\n    \"companyName\": \"Thai Beverage Public Company
        Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"LMNR\",\n
        \   \"companyName\": \"Limoneira Company\",\n    \"noOfTranscripts\": \"51\"\n
        \ },\n  {\n    \"symbol\": \"NBGIF\",\n    \"companyName\": \"National Bank
        of Greece S.A.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"VVPR\",\n    \"companyName\": \"VivoPower International PLC\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"BARK\",\n    \"companyName\": \"BARK,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"WRK\",\n
        \   \"companyName\": \"WestRock Company\",\n    \"noOfTranscripts\": \"64\"\n
        \ },\n  {\n    \"symbol\": \"CHMI\",\n    \"companyName\": \"Cherry Hill Mortgage
        Investment Corporation\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\":
        \"ABVX.PA\",\n    \"companyName\": \"Abivax S.A.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SIM.CO\",\n    \"companyName\": \"SimCorp
        A/S\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"PLSE\",\n
        \   \"companyName\": \"Pulse Biosciences, Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"CLDX\",\n    \"companyName\": \"Celldex
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"AGNC\",\n    \"companyName\": \"AGNC Investment Corp.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"SCS\",\n    \"companyName\": \"Steelcase
        Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"IDXX\",\n
        \   \"companyName\": \"IDEXX Laboratories, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"LEGN\",\n    \"companyName\": \"Legend
        Biotech Corporation\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"SNA\",\n    \"companyName\": \"Snap-on Incorporated\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"KMRPF\",\n    \"companyName\": \"Kenmare
        Resources plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CVHSY\",\n    \"companyName\": \"Cablevisi\xF3n Holding S.A.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"OCX\",\n    \"companyName\": \"OncoCyte
        Corporation\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"MDLY\",\n    \"companyName\": \"Medley Management Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"INFN\",\n    \"companyName\": \"Infinera
        Corporation\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"SNCR\",\n    \"companyName\": \"Synchronoss Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"CNM\",\n    \"companyName\": \"Core &
        Main, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"NTNX\",\n    \"companyName\": \"Nutanix, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"CRRFY\",\n    \"companyName\": \"Carrefour
        S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"SEMHF\",\n
        \   \"companyName\": \"Siemens Healthineers AG\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"HNNMY\",\n    \"companyName\": \"H &
        M Hennes & Mauritz AB (publ)\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n
        \   \"symbol\": \"EKDHF\",\n    \"companyName\": \"EKF Diagnostics Holdings
        plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"SCHP.PA\",\n
        \   \"companyName\": \"S\xE9ch\xE9 Environnement S.A.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"UIHC\",\n    \"companyName\": \"United
        Insurance Holdings Corp.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n
        \   \"symbol\": \"RDWR\",\n    \"companyName\": \"Radware Ltd.\",\n    \"noOfTranscripts\":
        \"56\"\n  },\n  {\n    \"symbol\": \"LESL\",\n    \"companyName\": \"Leslie's,
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"URBN\",\n
        \   \"companyName\": \"Urban Outfitters, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"ALIT\",\n    \"companyName\": \"Alight,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"EKTA-B.ST\",\n
        \   \"companyName\": \"Elekta AB (publ)\",\n    \"noOfTranscripts\": \"22\"\n
        \ },\n  {\n    \"symbol\": \"SBER.ME\",\n    \"companyName\": \"Sberbank of
        Russia\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"DLAKF\",\n
        \   \"companyName\": \"Deutsche Lufthansa AG\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"BORR\",\n    \"companyName\": \"Borr
        Drilling Limited\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"TELNY\",\n    \"companyName\": \"Telenor ASA\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"DBVT\",\n    \"companyName\": \"DBV Technologies
        S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"DCOM\",\n
        \   \"companyName\": \"Dime Community Bancshares, Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"7735.T\",\n    \"companyName\": \"SCREEN
        Holdings Co., Ltd.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"NSKFF\",\n    \"companyName\": \"Kongsberg Gruppen ASA\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"SUBCY\",\n    \"companyName\": \"Subsea
        7 S.A.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"SPHR\",\n
        \   \"companyName\": \"Sphere Entertainment Co.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"SCMWY\",\n    \"companyName\": \"Swisscom
        AG\",\n    \"noOfTranscripts\": \"32\"\n  },\n  {\n    \"symbol\": \"CNSL\",\n
        \   \"companyName\": \"Consolidated Communications Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"TDOC\",\n    \"companyName\": \"Teladoc
        Health, Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n  {\n    \"symbol\":
        \"ODMUF\",\n    \"companyName\": \"Old Mutual Limited\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"SEPJF\",\n    \"companyName\": \"Spectris
        plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"WTRG\",\n
        \   \"companyName\": \"Essential Utilities, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"API\",\n    \"companyName\": \"Agora,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"DBI\",\n
        \   \"companyName\": \"Designer Brands Inc.\",\n    \"noOfTranscripts\": \"64\"\n
        \ },\n  {\n    \"symbol\": \"CHX\",\n    \"companyName\": \"ChampionX Corporation\",\n
        \   \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"ASH\",\n    \"companyName\":
        \"Ashland Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"SDRL\",\n    \"companyName\": \"Seadrill Limited\",\n    \"noOfTranscripts\":
        \"40\"\n  },\n  {\n    \"symbol\": \"EVBN\",\n    \"companyName\": \"Evans
        Bancorp, Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"LBRDP\",\n    \"companyName\": \"Liberty Broadband Corporation\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"KOF\",\n    \"companyName\": \"Coca-Cola
        FEMSA, S.A.B. de C.V.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"CYBR\",\n    \"companyName\": \"CyberArk Software Ltd.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"YUMC\",\n    \"companyName\": \"Yum China
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\":
        \"SW.PA\",\n    \"companyName\": \"Sodexo S.A.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"CPSS\",\n    \"companyName\": \"Consumer
        Portfolio Services, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n
        \   \"symbol\": \"SNAX\",\n    \"companyName\": \"Stryve Foods, Inc.\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"CLNE\",\n    \"companyName\":
        \"Clean Energy Fuels Corp.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n
        \   \"symbol\": \"BPOST.BR\",\n    \"companyName\": \"bpost NV/SA\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"ISP.MI\",\n    \"companyName\": \"Intesa
        Sanpaolo S.p.A.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"VRNT\",\n    \"companyName\": \"Verint Systems Inc.\",\n    \"noOfTranscripts\":
        \"49\"\n  },\n  {\n    \"symbol\": \"XELB\",\n    \"companyName\": \"Xcel
        Brands, Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"BDSX\",\n    \"companyName\": \"Biodesix, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"DVCR\",\n    \"companyName\": \"Diversicare
        Healthcare Services, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n
        \   \"symbol\": \"POLA\",\n    \"companyName\": \"Polar Power, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"CATY\",\n    \"companyName\": \"Cathay
        General Bancorp\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"CWBHF\",\n    \"companyName\": \"Charlotte's Web Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"FWRD\",\n    \"companyName\": \"Forward
        Air Corporation\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\":
        \"CIHKY\",\n    \"companyName\": \"China Merchants Bank Co., Ltd.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"FL\",\n    \"companyName\": \"Foot Locker,
        Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"UCTT\",\n
        \   \"companyName\": \"Ultra Clean Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"PIA.MI\",\n    \"companyName\": \"Piaggio
        & C. S.p.A.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"MCRB\",\n    \"companyName\": \"Seres Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"0696.HK\",\n    \"companyName\": \"TravelSky
        Technology Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"LBLCF\",\n    \"companyName\": \"Loblaw Companies Limited\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"HMDPF\",\n    \"companyName\": \"Hammond
        Power Solutions Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"CNA\",\n    \"companyName\": \"CNA Financial Corporation\",\n    \"noOfTranscripts\":
        \"68\"\n  },\n  {\n    \"symbol\": \"6146.T\",\n    \"companyName\": \"Disco
        Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"HPE\",\n    \"companyName\": \"Hewlett Packard Enterprise Company\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"BZLYF\",\n    \"companyName\": \"Beazley
        plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"CVGI\",\n
        \   \"companyName\": \"Commercial Vehicle Group, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"CAST.ST\",\n    \"companyName\": \"Castellum
        AB (publ)\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"ITOCF\",\n    \"companyName\": \"ITOCHU Corporation\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"ECDA\",\n    \"companyName\": \"ECD Automotive
        Design, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"FR\",\n    \"companyName\": \"First Industrial Realty Trust, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"RDW\",\n    \"companyName\": \"Redwire
        Corporation\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"APPS\",\n    \"companyName\": \"Digital Turbine, Inc.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"CRDO\",\n    \"companyName\": \"Credo
        Technology Group Holding Ltd\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n
        \   \"symbol\": \"XLY.TO\",\n    \"companyName\": \"Auxly Cannabis Group Inc.\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"AMBFF\",\n    \"companyName\":
        \"Ambu A/S\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"VIVE\",\n    \"companyName\": \"Viveve Medical, Inc.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"AGR\",\n    \"companyName\": \"Avangrid,
        Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"HURN\",\n
        \   \"companyName\": \"Huron Consulting Group Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"1810.HK\",\n    \"companyName\": \"Xiaomi
        Corporation\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"DNUT\",\n    \"companyName\": \"Krispy Kreme, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"INOD\",\n    \"companyName\": \"Innodata
        Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\": \"CHGCF\",\n
        \   \"companyName\": \"Chugai Pharmaceutical Co., Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"STWD\",\n    \"companyName\": \"Starwood
        Property Trust, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"DTC\",\n    \"companyName\": \"Solo Brands, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"AXFO.ST\",\n    \"companyName\": \"Axfood
        AB (publ)\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"CORT\",\n
        \   \"companyName\": \"Corcept Therapeutics Incorporated\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"STAG\",\n    \"companyName\": \"STAG
        Industrial, Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\":
        \"TUIFF\",\n    \"companyName\": \"Tui AG\",\n    \"noOfTranscripts\": \"30\"\n
        \ },\n  {\n    \"symbol\": \"XEL\",\n    \"companyName\": \"Xcel Energy Inc.\",\n
        \   \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"SNI.OL\",\n
        \   \"companyName\": \"Stolt-Nielsen Limited\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"AMPX\",\n    \"companyName\": \"Amprius
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"CLPT\",\n    \"companyName\": \"ClearPoint Neuro, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"IH\",\n    \"companyName\": \"iHuman
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"LRLCF\",\n
        \   \"companyName\": \"L'Or\xE9al S.A.\",\n    \"noOfTranscripts\": \"12\"\n
        \ },\n  {\n    \"symbol\": \"LKQ\",\n    \"companyName\": \"LKQ Corporation\",\n
        \   \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"MKSI\",\n    \"companyName\":
        \"MKS Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"FLS\",\n    \"companyName\": \"Flowserve Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"EFN.TO\",\n    \"companyName\": \"Element
        Fleet Management Corp.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"MNDY\",\n    \"companyName\": \"monday.com Ltd.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"BOXD\",\n    \"companyName\": \"Boxed,
        Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"PNNT\",\n
        \   \"companyName\": \"PennantPark Investment Corporation\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"CME\",\n    \"companyName\": \"CME Group
        Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"6857.T\",\n
        \   \"companyName\": \"Advantest Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"KMI\",\n    \"companyName\": \"Kinder
        Morgan, Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"UNRV\",\n    \"companyName\": \"Unrivaled Brands, Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"AMZN\",\n    \"companyName\": \"Amazon.com,
        Inc.\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\": \"AGX\",\n
        \   \"companyName\": \"Argan, Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n
        \ {\n    \"symbol\": \"FISI\",\n    \"companyName\": \"Financial Institutions,
        Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"NROM\",\n
        \   \"companyName\": \"Noble Roman's, Inc.\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"SNEJF\",\n    \"companyName\": \"Sony Group Corporation\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"OLB\",\n    \"companyName\":
        \"The OLB Group, Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"DD\",\n    \"companyName\": \"DuPont de Nemours, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"UTRS\",\n    \"companyName\": \"Minerva
        Surgical, Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"UNVR\",\n    \"companyName\": \"Univar Solutions Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"601939.SS\",\n    \"companyName\": \"China
        Construction Bank Corporation\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n
        \   \"symbol\": \"2018.HK\",\n    \"companyName\": \"AAC Technologies Holdings
        Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"AGTC\",\n
        \   \"companyName\": \"Applied Genetic Technologies Corporation\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"BWMN\",\n    \"companyName\": \"Bowman
        Consulting Group Ltd.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"IMCC\",\n    \"companyName\": \"IM Cannabis Corp.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"FC\",\n    \"companyName\": \"Franklin
        Covey Co.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"SQ\",\n    \"companyName\": \"Block, Inc.\",\n    \"noOfTranscripts\": \"39\"\n
        \ },\n  {\n    \"symbol\": \"PRGS\",\n    \"companyName\": \"Progress Software
        Corporation\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"APP\",\n    \"companyName\": \"AppLovin Corporation\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"FBASF\",\n    \"companyName\": \"Fibra
        UNO\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"RVMD\",\n
        \   \"companyName\": \"Revolution Medicines, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"CTEV\",\n    \"companyName\": \"Claritev
        Corporation\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"BTLCY\",\n    \"companyName\": \"British Land Company Plc\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"STRR\",\n    \"companyName\": \"Star Equity
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"USEA\",\n    \"companyName\": \"United Maritime Corporation\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"DIC.DE\",\n    \"companyName\": \"DIC
        Asset AG\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"WLDN\",\n
        \   \"companyName\": \"Willdan Group, Inc.\",\n    \"noOfTranscripts\": \"46\"\n
        \ },\n  {\n    \"symbol\": \"PRTS\",\n    \"companyName\": \"CarParts.com,
        Inc.\",\n    \"noOfTranscripts\": \"57\"\n  },\n  {\n    \"symbol\": \"OABI\",\n
        \   \"companyName\": \"OmniAb, Inc.\",\n    \"noOfTranscripts\": \"11\"\n
        \ },\n  {\n    \"symbol\": \"ZEUS\",\n    \"companyName\": \"Olympic Steel,
        Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"AHC\",\n
        \   \"companyName\": \"A. H. Belo Corporation\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"FEIM\",\n    \"companyName\": \"Frequency
        Electronics, Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"BA\",\n    \"companyName\": \"The Boeing Company\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"DSDVF\",\n    \"companyName\": \"Dsv
        A/S\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"AIQUF\",\n
        \   \"companyName\": \"L'Air Liquide S.A.\",\n    \"noOfTranscripts\": \"47\"\n
        \ },\n  {\n    \"symbol\": \"SMEGF\",\n    \"companyName\": \"Siemens Energy
        AG\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"SLN\",\n
        \   \"companyName\": \"Silence Therapeutics plc\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"CWR.L\",\n    \"companyName\": \"Ceres
        Power Holdings plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"RHUHF\",\n    \"companyName\": \"Richelieu Hardware Ltd.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"NYXH\",\n    \"companyName\": \"Nyxoah
        S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"SES.TO\",\n
        \   \"companyName\": \"Secure Waste Infrastructure Corp.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"JBHT\",\n    \"companyName\": \"J.B.
        Hunt Transport Services, Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n
        \ {\n    \"symbol\": \"2331.HK\",\n    \"companyName\": \"Li Ning Company
        Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"APDN\",\n
        \   \"companyName\": \"Applied DNA Sciences, Inc.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"CENN\",\n    \"companyName\": \"Cenntro
        Electric Group Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"SMSI\",\n    \"companyName\": \"Smith Micro Software, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"PITAF\",\n    \"companyName\": \"Poste
        Italiane S.p.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"ACHC\",\n    \"companyName\": \"Acadia Healthcare Company, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"PCELL.ST\",\n    \"companyName\": \"PowerCell
        Sweden AB (publ)\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"TOST\",\n    \"companyName\": \"Toast, Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"IPSEY\",\n    \"companyName\": \"Ipsen
        S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"6060.HK\",\n
        \   \"companyName\": \"ZhongAn Online P & C Insurance Co., Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"UAL\",\n    \"companyName\": \"United
        Airlines Holdings, Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\":
        \"PI\",\n    \"companyName\": \"Impinj, Inc.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"GAXYQ\",\n    \"companyName\": \"Galaxy
        Next Generation, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"OMIC\",\n    \"companyName\": \"Singular Genomics Systems, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"BEZ.L\",\n    \"companyName\": \"Beazley
        plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"DK\",\n
        \   \"companyName\": \"Delek US Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"SMR\",\n    \"companyName\": \"NuScale
        Power Corporation\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"JCDXF\",\n    \"companyName\": \"JCDecaux SE\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"ACHR\",\n    \"companyName\": \"Archer
        Aviation Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"ULTA\",\n    \"companyName\": \"Ulta Beauty, Inc.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"IFC.TO\",\n    \"companyName\": \"Intact
        Financial Corporation\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"NBTB\",\n    \"companyName\": \"NBT Bancorp Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"CMLS\",\n    \"companyName\": \"Cumulus
        Media Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"PPRUF\",\n    \"companyName\": \"Kering S.A.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"USAP\",\n    \"companyName\": \"Universal
        Stainless & Alloy Products, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n
        \ {\n    \"symbol\": \"TPIC\",\n    \"companyName\": \"TPI Composites, Inc.\",\n
        \   \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"BYD.TO\",\n
        \   \"companyName\": \"Boyd Group Services Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"WEBNF\",\n    \"companyName\": \"Westpac
        Banking Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"NOVO-B.CO\",\n    \"companyName\": \"Novo Nordisk A/S\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"AME\",\n    \"companyName\": \"AMETEK,
        Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"THBRF\",\n
        \   \"companyName\": \"Thunderbird Entertainment Group Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"HKMPF\",\n    \"companyName\": \"Hikma
        Pharmaceuticals PLC\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"USCR\",\n    \"companyName\": \"U.S. Concrete, Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"GILD\",\n    \"companyName\": \"Gilead
        Sciences, Inc.\",\n    \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\":
        \"SCTL\",\n    \"companyName\": \"Societal CDMO, Inc.\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"DTEGF\",\n    \"companyName\": \"Deutsche
        Telekom AG\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\":
        \"TIXT\",\n    \"companyName\": \"TELUS International (Cda) Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"TSHA\",\n    \"companyName\": \"Taysha
        Gene Therapies, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"TH.TO\",\n    \"companyName\": \"Theratechnologies Inc.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"XP\",\n    \"companyName\": \"XP Inc.\",\n
        \   \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"USAS\",\n    \"companyName\":
        \"Americas Gold and Silver Corporation\",\n    \"noOfTranscripts\": \"5\"\n
        \ },\n  {\n    \"symbol\": \"RAY-A.TO\",\n    \"companyName\": \"Stingray
        Group Inc.\",\n    \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\":
        \"SPCE\",\n    \"companyName\": \"Virgin Galactic Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"UPST\",\n    \"companyName\": \"Upstart
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"UPMKF\",\n    \"companyName\": \"UPM-Kymmene Oyj\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"MAA\",\n    \"companyName\": \"Mid-America
        Apartment Communities, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n
        \   \"symbol\": \"CLVLY\",\n    \"companyName\": \"Clinuvel Pharmaceuticals
        Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"GOGO\",\n
        \   \"companyName\": \"Gogo Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n
        \ {\n    \"symbol\": \"POW.TO\",\n    \"companyName\": \"Power Corporation
        of Canada\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"RBB\",\n    \"companyName\": \"RBB Bancorp\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"LUNG\",\n    \"companyName\": \"Pulmonx
        Corporation\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"HL\",\n    \"companyName\": \"Hecla Mining Company\",\n    \"noOfTranscripts\":
        \"75\"\n  },\n  {\n    \"symbol\": \"CHCI\",\n    \"companyName\": \"Comstock
        Holding Companies, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"0OHK.L\",\n    \"companyName\": \"Stolt-Nielsen Limited\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"ANFGF\",\n    \"companyName\": \"Antofagasta
        plc\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"DIS.MI\",\n
        \   \"companyName\": \"d'Amico International Shipping S.A.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"TRP\",\n    \"companyName\": \"TC Energy
        Corporation\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"AVGO\",\n    \"companyName\": \"Broadcom Inc.\",\n    \"noOfTranscripts\":
        \"80\"\n  },\n  {\n    \"symbol\": \"CMS\",\n    \"companyName\": \"CMS Energy
        Corporation\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"WOR\",\n    \"companyName\": \"Worthington Industries, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"FLTR.L\",\n    \"companyName\": \"Flutter
        Entertainment plc\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"RVNC\",\n    \"companyName\": \"Revance Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"MXL\",\n    \"companyName\": \"MaxLinear,
        Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\": \"RPRX\",\n
        \   \"companyName\": \"Royalty Pharma plc\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"EPD\",\n    \"companyName\": \"Enterprise Products
        Partners L.P.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"CSGP\",\n    \"companyName\": \"CoStar Group, Inc.\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"CAAP\",\n    \"companyName\": \"Corporaci\xF3n
        Am\xE9rica Airports S.A.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n
        \   \"symbol\": \"SSKN\",\n    \"companyName\": \"STRATA Skin Sciences, Inc.\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"TMUS\",\n    \"companyName\":
        \"T-Mobile US, Inc.\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"TMGEF\",\n    \"companyName\": \"Thermal Energy International Inc.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"EVOTF\",\n    \"companyName\":
        \"Evotec SE\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\":
        \"WRBY\",\n    \"companyName\": \"Warby Parker Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"9898.HK\",\n    \"companyName\": \"Weibo
        Corporation\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"CDNA\",\n    \"companyName\": \"CareDx, Inc\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"HSDT\",\n    \"companyName\": \"Helius
        Medical Technologies, Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n
        \   \"symbol\": \"EQIX\",\n    \"companyName\": \"Equinix, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"NTCT\",\n    \"companyName\": \"NetScout
        Systems, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"FTEL\",\n    \"companyName\": \"Fitell Corporation\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"LOWLF\",\n    \"companyName\": \"Lowell
        Farms Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"0016.HK\",\n    \"companyName\": \"Sun Hung Kai Properties Limited\",\n
        \   \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"BR\",\n    \"companyName\":
        \"Broadridge Financial Solutions, Inc.\",\n    \"noOfTranscripts\": \"67\"\n
        \ },\n  {\n    \"symbol\": \"AQN\",\n    \"companyName\": \"Algonquin Power
        & Utilities Corp.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"FNTN.DE\",\n    \"companyName\": \"freenet AG\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"SMBMF\",\n    \"companyName\": \"Seatrium
        Limited\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"EDR\",\n
        \   \"companyName\": \"Endeavor Group Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"FECCF\",\n    \"companyName\": \"Frontera
        Energy Corporation\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"KBAGF\",\n    \"companyName\": \"Koninklijke BAM Groep nv\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"ONCT\",\n    \"companyName\": \"Oncternal
        Therapeutics, Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"LCUT\",\n    \"companyName\": \"Lifetime Brands, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"QTRH.TO\",\n    \"companyName\": \"Quarterhill
        Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"HON\",\n
        \   \"companyName\": \"Honeywell International Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"AYR-A.CN\",\n    \"companyName\": \"Ayr
        Wellness Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"DRIO\",\n    \"companyName\": \"DarioHealth Corp.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"CZMWF\",\n    \"companyName\": \"Carl
        Zeiss Meditec AG\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"CAPL\",\n    \"companyName\": \"CrossAmerica Partners LP\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"GROY\",\n    \"companyName\": \"Gold
        Royalty Corp.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"RPD\",\n    \"companyName\": \"Rapid7, Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"034220.KS\",\n    \"companyName\": \"LG
        Display Co., Ltd.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"MYX.AX\",\n    \"companyName\": \"Mayne Pharma Group Limited\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"CSCCF\",\n    \"companyName\": \"Capstone
        Copper Corp.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"SYZLF\",\n    \"companyName\": \"Sylogist Ltd.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"SPWH\",\n    \"companyName\": \"Sportsman's
        Warehouse Holdings, Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n
        \   \"symbol\": \"PGPHF\",\n    \"companyName\": \"Partners Group Holding
        AG\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"0001.HK\",\n
        \   \"companyName\": \"CK Hutchison Holdings Limited\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"SDIIF\",\n    \"companyName\": \"SDI Group
        plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"BBWI\",\n
        \   \"companyName\": \"Bath & Body Works, Inc.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"EDIT\",\n    \"companyName\": \"Editas
        Medicine, Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"BRY\",\n    \"companyName\": \"Berry Corporation\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"PLAB\",\n    \"companyName\": \"Photronics,
        Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"WDAY\",\n
        \   \"companyName\": \"Workday, Inc.\",\n    \"noOfTranscripts\": \"53\"\n
        \ },\n  {\n    \"symbol\": \"SWKS\",\n    \"companyName\": \"Skyworks Solutions,
        Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"CVS\",\n
        \   \"companyName\": \"CVS Health Corporation\",\n    \"noOfTranscripts\":
        \"79\"\n  },\n  {\n    \"symbol\": \"9961.HK\",\n    \"companyName\": \"Trip.com
        Group Limited\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"GPMT\",\n    \"companyName\": \"Granite Point Mortgage Trust Inc.\",\n    \"noOfTranscripts\":
        \"32\"\n  },\n  {\n    \"symbol\": \"RILY\",\n    \"companyName\": \"B. Riley
        Financial, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"MRNA\",\n    \"companyName\": \"Moderna, Inc.\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"CMPO\",\n    \"companyName\": \"CompoSecure,
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"INE.TO\",\n
        \   \"companyName\": \"Innergex Renewable Energy Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"0019.HK\",\n    \"companyName\": \"Swire
        Pacific Limited\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"CTMX\",\n    \"companyName\": \"CytomX Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"CHRS\",\n    \"companyName\": \"Coherus
        Oncology, Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"ATGFF\",\n    \"companyName\": \"AltaGas Ltd.\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"CYAN\",\n    \"companyName\": \"Cyanotech
        Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"ALFNF\",\n    \"companyName\": \"Alfen N.V.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MCN\",\n    \"companyName\": \"XAI Madison
        Equity Premium Income Fund\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"MLSS\",\n    \"companyName\": \"Milestone Scientific Inc.\",\n
        \   \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\": \"CXI.TO\",\n
        \   \"companyName\": \"Currency Exchange International, Corp.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"AAFRF\",\n    \"companyName\": \"Airtel
        Africa Plc\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"GALT\",\n    \"companyName\": \"Galectin Therapeutics Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"PSTG\",\n    \"companyName\": \"Pure Storage,
        Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"UVE\",\n
        \   \"companyName\": \"Universal Insurance Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"LIQT\",\n    \"companyName\": \"LiqTech
        International, Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\":
        \"NVZMF\",\n    \"companyName\": \"Novozymes A/S\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"KELYA\",\n    \"companyName\": \"Kelly
        Services, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"KRNGF\",\n    \"companyName\": \"Karoon Energy Ltd\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"GRA.TO\",\n    \"companyName\": \"NanoXplore
        Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"LGVN\",\n
        \   \"companyName\": \"Longeveron Inc.\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"EQX\",\n    \"companyName\": \"Equinox Gold Corp.\",\n
        \   \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"IPW\",\n    \"companyName\":
        \"iPower Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"MKTX\",\n    \"companyName\": \"MarketAxess Holdings Inc.\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"IFF\",\n    \"companyName\": \"International
        Flavors & Fragrances Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n
        \   \"symbol\": \"VIRI\",\n    \"companyName\": \"Virios Therapeutics, Inc.\",\n
        \   \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\": \"TRZBF\",\n    \"companyName\":
        \"Transat A.T. Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"RRC\",\n    \"companyName\": \"Range Resources Corporation\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"CSTE\",\n    \"companyName\": \"Caesarstone
        Ltd.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"NNGPF\",\n
        \   \"companyName\": \"NN Group N.V.\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"LZM\",\n    \"companyName\": \"Lifezone Metals
        Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"IMPP\",\n
        \   \"companyName\": \"Imperial Petroleum Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"ARCAD.AS\",\n    \"companyName\": \"Arcadis
        N.V.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"AMBA\",\n
        \   \"companyName\": \"Ambarella, Inc.\",\n    \"noOfTranscripts\": \"51\"\n
        \ },\n  {\n    \"symbol\": \"CS.PA\",\n    \"companyName\": \"Axa S.A.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"STKL\",\n    \"companyName\":
        \"SunOpta Inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\":
        \"WEGE3.SA\",\n    \"companyName\": \"Weg S.a.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"GEI.TO\",\n    \"companyName\": \"Gibson
        Energy Inc.\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\":
        \"TRE.MC\",\n    \"companyName\": \"T\xE9cnicas Reunidas, S.A.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"ELOX\",\n    \"companyName\": \"Eloxx
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"VLN.TO\",\n    \"companyName\": \"Velan Inc.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"IGT\",\n    \"companyName\": \"International
        Game Technology PLC\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"DOW\",\n    \"companyName\": \"Dow Inc.\",\n    \"noOfTranscripts\": \"67\"\n
        \ },\n  {\n    \"symbol\": \"BGC\",\n    \"companyName\": \"BGC Group, Inc\",\n
        \   \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\": \"LLY\",\n    \"companyName\":
        \"Eli Lilly and Company\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"NATU3.SA\",\n    \"companyName\": \"Natura & Co Holding S.A.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"TV\",\n    \"companyName\": \"Grupo Televisa,
        S.A.B.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"HTO\",\n
        \   \"companyName\": \"H2O America\",\n    \"noOfTranscripts\": \"3\"\n  },\n
        \ {\n    \"symbol\": \"AZN\",\n    \"companyName\": \"AstraZeneca PLC\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"GEHC\",\n    \"companyName\":
        \"GE HealthCare Technologies Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n
        \ {\n    \"symbol\": \"AEGN.AT\",\n    \"companyName\": \"Aegean Airlines
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"EMKR\",\n
        \   \"companyName\": \"EMCORE Corporation\",\n    \"noOfTranscripts\": \"61\"\n
        \ },\n  {\n    \"symbol\": \"RNR\",\n    \"companyName\": \"RenaissanceRe
        Holdings Ltd.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"TLSI\",\n    \"companyName\": \"TriSalus Life Sciences, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"THMO\",\n    \"companyName\": \"ThermoGenesis
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"IONS\",\n    \"companyName\": \"Ionis Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"ESMT\",\n    \"companyName\": \"EngageSmart,
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"ARBK\",\n
        \   \"companyName\": \"Argo Blockchain plc\",\n    \"noOfTranscripts\": \"10\"\n
        \ },\n  {\n    \"symbol\": \"ATHM\",\n    \"companyName\": \"Autohome Inc.\",\n
        \   \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"TFX\",\n    \"companyName\":
        \"Teleflex Incorporated\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"PAYX\",\n    \"companyName\": \"Paychex, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"ROAD\",\n    \"companyName\": \"Construction
        Partners, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"BTCY\",\n    \"companyName\": \"Biotricity, Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"PRMB\",\n    \"companyName\": \"Primo
        Brands Corporation\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"VMEO\",\n    \"companyName\": \"Vimeo, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"MIRM\",\n    \"companyName\": \"Mirum
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"ILMN\",\n    \"companyName\": \"Illumina, Inc.\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"VOD.L\",\n    \"companyName\": \"Vodafone
        Group Public Limited Company\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n
        \   \"symbol\": \"WMG\",\n    \"companyName\": \"Warner Music Group Corp.\",\n
        \   \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\": \"ICE\",\n    \"companyName\":
        \"Intercontinental Exchange, Inc.\",\n    \"noOfTranscripts\": \"73\"\n  },\n
        \ {\n    \"symbol\": \"HRTX\",\n    \"companyName\": \"Heron Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"LI\",\n
        \   \"companyName\": \"Li Auto Inc.\",\n    \"noOfTranscripts\": \"20\"\n
        \ },\n  {\n    \"symbol\": \"ACLLF\",\n    \"companyName\": \"ATCO Ltd.\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"HEXO\",\n    \"companyName\":
        \"HEXO Corp.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"TLX.AX\",\n    \"companyName\": \"Telix Pharmaceuticals Limited\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"BKRKY\",\n    \"companyName\": \"PT Bank
        Rakyat Indonesia (Persero) Tbk\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"SCATC.OL\",\n    \"companyName\": \"Scatec ASA\",\n
        \   \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"SLP\",\n    \"companyName\":
        \"Simulations Plus, Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n
        \   \"symbol\": \"KE\",\n    \"companyName\": \"Kimball Electronics, Inc.\",\n
        \   \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"CPRI\",\n    \"companyName\":
        \"Capri Holdings Limited\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n
        \   \"symbol\": \"CRUS\",\n    \"companyName\": \"Cirrus Logic, Inc.\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"KYYWF\",\n    \"companyName\":
        \"Keywords Studios plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"KGC\",\n    \"companyName\": \"Kinross Gold Corporation\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"IVA\",\n    \"companyName\": \"Inventiva
        S.A.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"CEVA\",\n
        \   \"companyName\": \"CEVA, Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n
        \ {\n    \"symbol\": \"ELP\",\n    \"companyName\": \"Companhia Paranaense
        de Energia - COPEL\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"STM\",\n    \"companyName\": \"STMicroelectronics N.V.\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"RMBL\",\n    \"companyName\": \"RumbleON,
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"PDFS\",\n
        \   \"companyName\": \"PDF Solutions, Inc.\",\n    \"noOfTranscripts\": \"59\"\n
        \ },\n  {\n    \"symbol\": \"CPB\",\n    \"companyName\": \"Campbell Soup
        Company\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"NSYS\",\n
        \   \"companyName\": \"Nortech Systems Incorporated\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"ITW\",\n    \"companyName\": \"Illinois
        Tool Works Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"BROS\",\n    \"companyName\": \"Dutch Bros Inc.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"MYO\",\n    \"companyName\": \"Myomo,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"LNW\",\n
        \   \"companyName\": \"Light & Wonder, Inc.\",\n    \"noOfTranscripts\": \"53\"\n
        \ },\n  {\n    \"symbol\": \"SLM.JO\",\n    \"companyName\": \"Sanlam Limited\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"PLAY\",\n    \"companyName\":
        \"Dave & Buster's Entertainment, Inc.\",\n    \"noOfTranscripts\": \"44\"\n
        \ },\n  {\n    \"symbol\": \"DRVN\",\n    \"companyName\": \"Driven Brands
        Holdings Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"ZLAB\",\n    \"companyName\": \"Zai Lab Limited\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"MKC\",\n    \"companyName\": \"McCormick
        & Company, Incorporated\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"FOX\",\n    \"companyName\": \"Fox Corporation\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"TYNPF\",\n    \"companyName\": \"Nippon
        Sanso Holdings Corporation\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"ENFN\",\n    \"companyName\": \"Enfusion, Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"UFPI\",\n    \"companyName\": \"UFP Industries,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"HOM-U.TO\",\n
        \   \"companyName\": \"BSR Real Estate Investment Trust\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"NSRCF\",\n    \"companyName\": \"NextSource
        Materials Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"VATE\",\n    \"companyName\": \"INNOVATE Corp.\",\n    \"noOfTranscripts\":
        \"41\"\n  },\n  {\n    \"symbol\": \"BCH\",\n    \"companyName\": \"Banco
        de Chile\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"KPLUY\",\n
        \   \"companyName\": \"K+s AG\",\n    \"noOfTranscripts\": \"30\"\n  },\n
        \ {\n    \"symbol\": \"KRR.TO\",\n    \"companyName\": \"Karora Resources
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"TER\",\n
        \   \"companyName\": \"Teradyne, Inc.\",\n    \"noOfTranscripts\": \"72\"\n
        \ },\n  {\n    \"symbol\": \"RHEP\",\n    \"companyName\": \"Regional Health
        Properties, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"DUK\",\n    \"companyName\": \"Duke Energy Corporation\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"BURL\",\n    \"companyName\": \"Burlington
        Stores, Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\":
        \"RDI\",\n    \"companyName\": \"Reading International, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"ZBRA\",\n    \"companyName\": \"Zebra
        Technologies Corporation\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n
        \   \"symbol\": \"AGGZF\",\n    \"companyName\": \"Ag Growth International
        Inc.\",\n    \"noOfTranscripts\": \"47\"\n  },\n  {\n    \"symbol\": \"FERG\",\n
        \   \"companyName\": \"Ferguson plc\",\n    \"noOfTranscripts\": \"36\"\n
        \ },\n  {\n    \"symbol\": \"STLAM.MI\",\n    \"companyName\": \"Stellantis
        N.V.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\": \"NTAR.CN\",\n
        \   \"companyName\": \"Nextech3D.AI Corporation\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"7267.T\",\n    \"companyName\": \"Honda
        Motor Co., Ltd.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"OSN\",\n    \"companyName\": \"Ossen Innovation Co., Ltd.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"BKRIF\",\n    \"companyName\": \"Bank
        of Ireland Group plc\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"NTR\",\n    \"companyName\": \"Nutrien Ltd.\",\n    \"noOfTranscripts\":
        \"68\"\n  },\n  {\n    \"symbol\": \"DIBS\",\n    \"companyName\": \"1stdibs.Com,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"ALYAF\",\n
        \   \"companyName\": \"Alithya Group Inc.\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"TAC\",\n    \"companyName\": \"TransAlta Corporation\",\n
        \   \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"HMC\",\n    \"companyName\":
        \"Honda Motor Co., Ltd.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"VOXX\",\n    \"companyName\": \"VOXX International Corporation\",\n    \"noOfTranscripts\":
        \"74\"\n  },\n  {\n    \"symbol\": \"NIU\",\n    \"companyName\": \"Niu Technologies\",\n
        \   \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"OSS.V\",\n    \"companyName\":
        \"OneSoft Solutions Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"TU\",\n    \"companyName\": \"TELUS Corporation\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"QBTS\",\n    \"companyName\": \"D-Wave
        Quantum Inc.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"CCSI\",\n    \"companyName\": \"Consensus Cloud Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"CWST\",\n    \"companyName\": \"Casella
        Waste Systems, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"TA.TO\",\n    \"companyName\": \"TransAlta Corporation\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"VIAV\",\n    \"companyName\": \"Viavi
        Solutions Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"NNXPF\",\n    \"companyName\": \"NanoXplore Inc.\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"OCFT\",\n    \"companyName\": \"OneConnect
        Financial Technology Co., Ltd.\",\n    \"noOfTranscripts\": \"15\"\n  },\n
        \ {\n    \"symbol\": \"PDS\",\n    \"companyName\": \"Precision Drilling Corporation\",\n
        \   \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"PENG\",\n    \"companyName\":
        \"Penguin Solutions, Inc.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n
        \   \"symbol\": \"PAA\",\n    \"companyName\": \"Plains All American Pipeline,
        L.P.\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\": \"QYOUF\",\n
        \   \"companyName\": \"QYOU Media Inc.\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"WW\",\n    \"companyName\": \"WW International,
        Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"KUKE\",\n
        \   \"companyName\": \"Kuke Music Holding Limited\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"CGNT\",\n    \"companyName\": \"Cognyte
        Software Ltd.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"MRLWF\",\n    \"companyName\": \"Marlowe plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SENS\",\n    \"companyName\": \"Senseonics
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"WLKP\",\n    \"companyName\": \"Westlake Chemical Partners LP\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"TEO\",\n    \"companyName\": \"Telecom
        Argentina S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n  {\n    \"symbol\":
        \"ISBC\",\n    \"companyName\": \"Investors Bancorp, Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"INT\",\n    \"companyName\": \"World
        Fuel Services Corporation\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n
        \   \"symbol\": \"ATMU\",\n    \"companyName\": \"Atmus Filtration Technologies
        Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"ZENV\",\n
        \   \"companyName\": \"Zenvia Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"PEBO\",\n    \"companyName\": \"Peoples Bancorp Inc.\",\n
        \   \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\": \"SSTI\",\n    \"companyName\":
        \"SoundThinking, Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"SWSSF\",\n    \"companyName\": \"Swiss Water Decaffeinated Coffee Inc.\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"FXPO.L\",\n    \"companyName\":
        \"Ferrexpo plc\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"ISEE\",\n    \"companyName\": \"IVERIC bio, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"CBAUF\",\n    \"companyName\": \"Commonwealth
        Bank of Australia\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"EPAY\",\n    \"companyName\": \"Bottomline Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"DIS\",\n    \"companyName\": \"The Walt
        Disney Company\",\n    \"noOfTranscripts\": \"77\"\n  },\n  {\n    \"symbol\":
        \"FPRUF\",\n    \"companyName\": \"Fraport AG\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"REKR\",\n    \"companyName\": \"Rekor
        Systems, Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\":
        \"LW\",\n    \"companyName\": \"Lamb Weston Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"PVH\",\n    \"companyName\": \"PVH Corp.\",\n
        \   \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"INBS\",\n    \"companyName\":
        \"Intelligent Bio Solutions Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n
        \ {\n    \"symbol\": \"TLLTF\",\n    \"companyName\": \"TILT Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\": \"REPYF\",\n    \"companyName\":
        \"Repsol, S.A.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"MKTW\",\n    \"companyName\": \"MarketWise, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"AIOT\",\n    \"companyName\": \"PowerFleet,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"GFF\",\n
        \   \"companyName\": \"Griffon Corporation\",\n    \"noOfTranscripts\": \"55\"\n
        \ },\n  {\n    \"symbol\": \"VRCA\",\n    \"companyName\": \"Verrica Pharmaceuticals
        Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"DEC.L\",\n
        \   \"companyName\": \"Diversified Energy Company PLC\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"AVTR\",\n    \"companyName\": \"Avantor,
        Inc.\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\": \"TEAD\",\n
        \   \"companyName\": \"Teads Holding Co.\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"RGNX\",\n    \"companyName\": \"REGENXBIO Inc.\",\n
        \   \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"MANU\",\n    \"companyName\":
        \"Manchester United plc\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"VTNR\",\n    \"companyName\": \"Vertex Energy, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"NSTG\",\n    \"companyName\": \"NanoString
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"IDCC\",\n    \"companyName\": \"InterDigital, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"STEM\",\n    \"companyName\": \"Stem,
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"BAFBF\",\n
        \   \"companyName\": \"Balfour Beatty plc\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"OGE\",\n    \"companyName\": \"OGE Energy Corp.\",\n
        \   \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"DLTR\",\n    \"companyName\":
        \"Dollar Tree, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"DRX.TO\",\n    \"companyName\": \"ADF Group Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"YY\",\n    \"companyName\": \"JOYY Inc.\",\n
        \   \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"LOW\",\n    \"companyName\":
        \"Lowe's Companies, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n
        \   \"symbol\": \"IHS\",\n    \"companyName\": \"IHS Holding Limited\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"UPS\",\n    \"companyName\":
        \"United Parcel Service, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n
        \ {\n    \"symbol\": \"GPUS\",\n    \"companyName\": \"Hyperscale Data, Inc.\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"EVLV\",\n    \"companyName\":
        \"Evolv Technologies Holdings, Inc.\",\n    \"noOfTranscripts\": \"15\"\n
        \ },\n  {\n    \"symbol\": \"USIM5.SA\",\n    \"companyName\": \"Usinas Sider\xFArgicas
        de Minas Gerais S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"GTG.AX\",\n    \"companyName\": \"Genetic Technologies Limited\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"BELYS.BR\",\n    \"companyName\": \"Belysse
        Group N.V.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"RGF\",\n    \"companyName\": \"The Real Good Food Company, Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MOGO\",\n    \"companyName\": \"Mogo Inc.\",\n
        \   \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"SZCRF\",\n    \"companyName\":
        \"SCOR Se\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"RESP\",\n    \"companyName\": \"WisdomTree U.S. ESG Fund\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"PSKY\",\n    \"companyName\": \"Paramount
        Skydance Corporation Class B Common Stock\",\n    \"noOfTranscripts\": \"79\"\n
        \ },\n  {\n    \"symbol\": \"ULTR\",\n    \"companyName\": \"IQ Ultra Short
        Duration ETF\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"BKR\",\n    \"companyName\": \"Baker Hughes Company\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"GDEV\",\n    \"companyName\": \"GDEV
        Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"MASI\",\n
        \   \"companyName\": \"Masimo Corporation\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"BLKB\",\n    \"companyName\": \"Blackbaud, Inc.\",\n
        \   \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"MMTOF\",\n    \"companyName\":
        \"Mitsubishi Motors Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n
        \ {\n    \"symbol\": \"SUUIF\",\n    \"companyName\": \"Superior Plus Corp.\",\n
        \   \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\": \"HDB\",\n    \"companyName\":
        \"HDFC Bank Limited\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"CLMB\",\n    \"companyName\": \"Climb Global Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"KW\",\n    \"companyName\": \"Kennedy-Wilson
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"FEVR.L\",\n    \"companyName\": \"Fevertree Drinks PLC\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"FOSL\",\n    \"companyName\": \"Fossil
        Group, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"AACG\",\n    \"companyName\": \"ATA Creativity Global\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"SLGWF\",\n    \"companyName\": \"SLANG
        Worldwide Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"BAINF\",\n    \"companyName\": \"BASE, Inc.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"BVS\",\n    \"companyName\": \"Bioventus
        Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"EVTC\",\n
        \   \"companyName\": \"EVERTEC, Inc.\",\n    \"noOfTranscripts\": \"50\"\n
        \ },\n  {\n    \"symbol\": \"TILE\",\n    \"companyName\": \"Interface, Inc.\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"KHNGF\",\n    \"companyName\":
        \"Kuehne + Nagel International AG\",\n    \"noOfTranscripts\": \"22\"\n  },\n
        \ {\n    \"symbol\": \"ISUN\",\n    \"companyName\": \"iSun, Inc.\",\n    \"noOfTranscripts\":
        \"10\"\n  },\n  {\n    \"symbol\": \"CIXX\",\n    \"companyName\": \"CI Financial
        Corp.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"NVX.AX\",\n
        \   \"companyName\": \"Novonix Limited\",\n    \"noOfTranscripts\": \"4\"\n
        \ },\n  {\n    \"symbol\": \"CFXTF\",\n    \"companyName\": \"Conifex Timber
        Inc.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"IAG\",\n
        \   \"companyName\": \"IAMGOLD Corporation\",\n    \"noOfTranscripts\": \"56\"\n
        \ },\n  {\n    \"symbol\": \"BBBY\",\n    \"companyName\": \"Bed Bath & Beyond
        Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\": \"GDOT\",\n
        \   \"companyName\": \"Green Dot Corporation\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"MBOT\",\n    \"companyName\": \"Microbot
        Medical Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"ALTS\",\n    \"companyName\": \"ALT5 Sigma Corporation\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"CALT\",\n    \"companyName\": \"Calliditas
        Therapeutics AB (publ)\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"STRM\",\n    \"companyName\": \"Streamline Health Solutions, Inc.\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"TEF.MC\",\n    \"companyName\": \"Telef\xF3nica,
        S.A.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"AXLA\",\n
        \   \"companyName\": \"Axcella Health Inc.\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"HGTY\",\n    \"companyName\": \"Hagerty, Inc.\",\n
        \   \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"AVIR\",\n    \"companyName\":
        \"Atea Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n
        \   \"symbol\": \"TDS\",\n    \"companyName\": \"Telephone and Data Systems,
        Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"CAJ\",\n
        \   \"companyName\": \"Canon Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n
        \ {\n    \"symbol\": \"TSP\",\n    \"companyName\": \"TuSimple Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"ROO.L\",\n    \"companyName\":
        \"Deliveroo plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"TNTFF\",\n    \"companyName\": \"PostNL N.V.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"CNOB\",\n    \"companyName\": \"ConnectOne
        Bancorp, Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"MAS\",\n    \"companyName\": \"Masco Corporation\",\n    \"noOfTranscripts\":
        \"70\"\n  },\n  {\n    \"symbol\": \"AH.TO\",\n    \"companyName\": \"Aleafia
        Health Inc.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"ATLC\",\n    \"companyName\": \"Atlanticus Holdings Corporation\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"NOVT\",\n    \"companyName\": \"Novanta
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"BLN.TO\",\n
        \   \"companyName\": \"Blackline Safety Corp.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"TAVHL.IS\",\n    \"companyName\": \"TAV
        Havalimanlari Holding A.S.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"TTNP\",\n    \"companyName\": \"Titan Pharmaceuticals, Inc.\",\n
        \   \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\": \"PESAF\",\n    \"companyName\":
        \"Panoro Energy ASA\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"AKAAF\",\n    \"companyName\": \"Aker ASA\",\n    \"noOfTranscripts\": \"20\"\n
        \ },\n  {\n    \"symbol\": \"IVTBF\",\n    \"companyName\": \"Investment AB
        Latour (publ)\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"SMFTF\",\n    \"companyName\": \"Smurfit Kappa Group Plc\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BX\",\n    \"companyName\": \"Blackstone
        Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"TXNM\",\n
        \   \"companyName\": \"TXNM Energy, Inc.\",\n    \"noOfTranscripts\": \"66\"\n
        \ },\n  {\n    \"symbol\": \"WKSP\",\n    \"companyName\": \"Worksport Ltd.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"SMFKY\",\n    \"companyName\":
        \"Smurfit Kappa Group Plc\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n
        \   \"symbol\": \"HUYA\",\n    \"companyName\": \"HUYA Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"HCKT\",\n    \"companyName\": \"The Hackett
        Group, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"ADEA\",\n    \"companyName\": \"Adeia Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"VERU\",\n    \"companyName\": \"Veru
        Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"MOS\",\n
        \   \"companyName\": \"The Mosaic Company\",\n    \"noOfTranscripts\": \"70\"\n
        \ },\n  {\n    \"symbol\": \"AXS.L\",\n    \"companyName\": \"Accsys Technologies
        PLC\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"SIL.TO\",\n
        \   \"companyName\": \"SilverCrest Metals Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"GEVO\",\n    \"companyName\": \"Gevo,
        Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\": \"ESALY\",\n
        \   \"companyName\": \"Eisai Co., Ltd.\",\n    \"noOfTranscripts\": \"15\"\n
        \ },\n  {\n    \"symbol\": \"ELV\",\n    \"companyName\": \"Elevance Health
        Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"BAM.TO\",\n
        \   \"companyName\": \"Brookfield Asset Management Ltd.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"SESG.PA\",\n    \"companyName\": \"Ses
        S.a.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"GTES\",\n
        \   \"companyName\": \"Gates Industrial Corporation plc\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"RAIFF\",\n    \"companyName\": \"Raiffeisen
        Bank International AG\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"QRHC\",\n    \"companyName\": \"Quest Resource Holding Corporation\",\n
        \   \"noOfTranscripts\": \"38\"\n  },\n  {\n    \"symbol\": \"AIM.TO\",\n
        \   \"companyName\": \"Aimia Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n
        \ {\n    \"symbol\": \"SFFYF\",\n    \"companyName\": \"Signify N.V.\",\n
        \   \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"TWMIF\",\n    \"companyName\":
        \"Tidewater Midstream and Infrastructure Ltd.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"IGIC\",\n    \"companyName\": \"International
        General Insurance Holdings Ltd.\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"NETZ.NE\",\n    \"companyName\": \"Carbon Streaming
        Corporation\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"SUMXF\",\n    \"companyName\": \"Supremex Inc.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"FORM\",\n    \"companyName\": \"FormFactor,
        Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"PACW\",\n
        \   \"companyName\": \"PacWest Bancorp\",\n    \"noOfTranscripts\": \"7\"\n
        \ },\n  {\n    \"symbol\": \"REPL\",\n    \"companyName\": \"Replimune Group,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"TECK\",\n
        \   \"companyName\": \"Teck Resources Limited\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"SNOA\",\n    \"companyName\": \"Sonoma
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"GBX\",\n    \"companyName\": \"The Greenbrier Companies, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"XFABF\",\n    \"companyName\": \"X-FAB
        Silicon Foundries SE\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"T\",\n    \"companyName\": \"AT&T Inc.\",\n    \"noOfTranscripts\": \"79\"\n
        \ },\n  {\n    \"symbol\": \"PSNY\",\n    \"companyName\": \"Polestar Automotive
        Holding UK PLC\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"NUTX\",\n    \"companyName\": \"Nutex Health, Inc.\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"MTNB\",\n    \"companyName\": \"Matinas
        BioPharma Holdings, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n
        \   \"symbol\": \"GSMG\",\n    \"companyName\": \"Glory Star New Media Group
        Holdings Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CRCT\",\n    \"companyName\": \"Cricut, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"INLB\",\n    \"companyName\": \"Item
        9 Labs Corp.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"PHUN\",\n    \"companyName\": \"Phunware, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"SNEX\",\n    \"companyName\": \"StoneX
        Group Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\":
        \"BKU\",\n    \"companyName\": \"BankUnited, Inc.\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"PACK\",\n    \"companyName\": \"Ranpak
        Holdings Corp.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"ORBIA.MX\",\n    \"companyName\": \"Orbia Advance Corporation, S.A.B. de
        C.V.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"KNW\",\n
        \   \"companyName\": \"Know Labs, Inc.\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"ITT\",\n    \"companyName\": \"ITT Inc.\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"LASR\",\n    \"companyName\":
        \"nLIGHT, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"EXXAF\",\n    \"companyName\": \"Exxaro Resources Limited\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"CUE\",\n    \"companyName\": \"Cue Biopharma,
        Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"FRRVF\",\n
        \   \"companyName\": \"Ferrovial, S.A.\",\n    \"noOfTranscripts\": \"19\"\n
        \ },\n  {\n    \"symbol\": \"WIPRO.NS\",\n    \"companyName\": \"Wipro Limited\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"DSGX\",\n    \"companyName\":
        \"The Descartes Systems Group Inc.\",\n    \"noOfTranscripts\": \"40\"\n  },\n
        \ {\n    \"symbol\": \"PALT\",\n    \"companyName\": \"Paltalk, Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"COHU\",\n    \"companyName\":
        \"Cohu, Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"LMPX\",\n    \"companyName\": \"LMP Automotive Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"ARRY\",\n    \"companyName\": \"Array
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"KMBIF\",\n    \"companyName\": \"Kambi Group plc\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"INFA\",\n    \"companyName\": \"Informatica
        Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"SQM-B.SN\",\n
        \   \"companyName\": \"Sociedad Qu\xEDmica y Minera de Chile S.A.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"FBP\",\n    \"companyName\": \"First
        BanCorp.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"FPLSF\",\n
        \   \"companyName\": \"5N Plus Inc.\",\n    \"noOfTranscripts\": \"12\"\n
        \ },\n  {\n    \"symbol\": \"TBABF\",\n    \"companyName\": \"Trelleborg AB
        (publ)\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"ANN.AX\",\n
        \   \"companyName\": \"Ansell Limited\",\n    \"noOfTranscripts\": \"8\"\n
        \ },\n  {\n    \"symbol\": \"AIVAF\",\n    \"companyName\": \"Aviva plc\",\n
        \   \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"BCEKF\",\n    \"companyName\":
        \"Bear Creek Mining Corporation\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"PANHF\",\n    \"companyName\": \"Ping An Healthcare
        and Technology Company Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"TK\",\n    \"companyName\": \"Teekay Corporation\",\n
        \   \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"EQRX\",\n    \"companyName\":
        \"EQRx, Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"CLZNF\",\n    \"companyName\": \"Clariant AG\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"EIGRQ\",\n    \"companyName\": \"Eiger
        BioPharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"AALBF\",\n    \"companyName\": \"Aalberts N.V.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"VLPNF\",\n    \"companyName\": \"Voestalpine
        AG\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"MUR\",\n
        \   \"companyName\": \"Murphy Oil Corporation\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"GOGL\",\n    \"companyName\": \"Golden
        Ocean Group Limited\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"PYTCF\",\n    \"companyName\": \"Playtech plc\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"AKAM\",\n    \"companyName\": \"Akamai
        Technologies, Inc.\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"WEC\",\n    \"companyName\": \"WEC Energy Group, Inc.\",\n    \"noOfTranscripts\":
        \"69\"\n  },\n  {\n    \"symbol\": \"WE\",\n    \"companyName\": \"WeWork
        Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"ABEO\",\n
        \   \"companyName\": \"Abeona Therapeutics Inc.\",\n    \"noOfTranscripts\":
        \"33\"\n  },\n  {\n    \"symbol\": \"OXY\",\n    \"companyName\": \"Occidental
        Petroleum Corporation\",\n    \"noOfTranscripts\": \"73\"\n  },\n  {\n    \"symbol\":
        \"IMC.AX\",\n    \"companyName\": \"Immuron Limited\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"MDNA.TO\",\n    \"companyName\": \"Medicenna
        Therapeutics Corp.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"KDP\",\n    \"companyName\": \"Keurig Dr Pepper Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"DIN\",\n    \"companyName\": \"Dine Brands
        Global, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"SDOT\",\n    \"companyName\": \"Sadot Group Inc.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"SMTGF\",\n    \"companyName\": \"SMA
        Solar Technology AG\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"MITK\",\n    \"companyName\": \"Mitek Systems, Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"GEAGF\",\n    \"companyName\": \"GEA
        Group AG\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"BLDR\",\n
        \   \"companyName\": \"Builders FirstSource, Inc.\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"ONC.TO\",\n    \"companyName\": \"Oncolytics
        Biotech Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"AYRO\",\n    \"companyName\": \"Ayro, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"NKE\",\n    \"companyName\": \"NIKE,
        Inc.\",\n    \"noOfTranscripts\": \"76\"\n  },\n  {\n    \"symbol\": \"CRI\",\n
        \   \"companyName\": \"Carter's, Inc.\",\n    \"noOfTranscripts\": \"61\"\n
        \ },\n  {\n    \"symbol\": \"POOL\",\n    \"companyName\": \"Pool Corporation\",\n
        \   \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"ROYMF\",\n    \"companyName\":
        \"International Distributions Services plc\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"LTRX\",\n    \"companyName\": \"Lantronix, Inc.\",\n
        \   \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\": \"VREX\",\n    \"companyName\":
        \"Varex Imaging Corporation\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n
        \   \"symbol\": \"PYYX\",\n    \"companyName\": \"Pyxus International, Inc.\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"CODA\",\n    \"companyName\":
        \"Coda Octopus Group, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n
        \   \"symbol\": \"ALPP\",\n    \"companyName\": \"Alpine 4 Holdings, Inc.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"KLDO\",\n    \"companyName\":
        \"Kaleido Biosciences, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"KPELF\",\n    \"companyName\": \"Keppel Corporation Limited\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"ALR\",\n    \"companyName\":
        \"AlerisLife Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"WILLF\",\n    \"companyName\": \"Demant A/S\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"STZ\",\n    \"companyName\": \"Constellation
        Brands, Inc.\",\n    \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\":
        \"ELKMF\",\n    \"companyName\": \"Gold Road Resources Limited\",\n    \"noOfTranscripts\":
        \"14\"\n  },\n  {\n    \"symbol\": \"NTRP\",\n    \"companyName\": \"NextTrip,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"SHB-A.ST\",\n
        \   \"companyName\": \"Svenska Handelsbanken AB (publ)\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"LE\",\n    \"companyName\": \"Lands'
        End, Inc.\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\":
        \"CMT\",\n    \"companyName\": \"Core Molding Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"UTSI\",\n    \"companyName\": \"UTStarcom
        Holdings Corp.\",\n    \"noOfTranscripts\": \"48\"\n  },\n  {\n    \"symbol\":
        \"IPAR\",\n    \"companyName\": \"Inter Parfums, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"ETTYF\",\n    \"companyName\": \"Essity
        AB (publ)\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"ENFY\",\n
        \   \"companyName\": \"Enlightify Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"EMN\",\n    \"companyName\": \"Eastman Chemical
        Company\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\": \"VNPKF\",\n
        \   \"companyName\": \"Verde AgriTech Ltd\",\n    \"noOfTranscripts\": \"2\"\n
        \ },\n  {\n    \"symbol\": \"NUFMF\",\n    \"companyName\": \"Nufarm Limited\",\n
        \   \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"AMSF\",\n    \"companyName\":
        \"AMERISAFE, Inc.\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"ARB\",\n    \"companyName\": \"AltShares Merger Arbitrage ETF\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"APTV\",\n    \"companyName\": \"Aptiv
        PLC\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"SCNI\",\n
        \   \"companyName\": \"Scinai Immunotherapeutics Ltd.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"GGB\",\n    \"companyName\": \"Gerdau
        S.A.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"CCLD\",\n
        \   \"companyName\": \"CareCloud, Inc.\",\n    \"noOfTranscripts\": \"44\"\n
        \ },\n  {\n    \"symbol\": \"WPM\",\n    \"companyName\": \"Wheaton Precious
        Metals Corp.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\":
        \"DAL\",\n    \"companyName\": \"Delta Air Lines, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"BRBR\",\n    \"companyName\": \"BellRing
        Brands, Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"VALN\",\n    \"companyName\": \"Valneva SE\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"ALT\",\n    \"companyName\": \"Altimmune,
        Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\": \"GLBS\",\n
        \   \"companyName\": \"Globus Maritime Limited\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"FPAY\",\n    \"companyName\": \"FlexShopper,
        Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\": \"TWI\",\n
        \   \"companyName\": \"Titan International, Inc.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"VSTO\",\n    \"companyName\": \"Vista
        Outdoor Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"IAFNF\",\n    \"companyName\": \"iA Financial Corporation Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"ADP.PA\",\n    \"companyName\": \"Aeroports
        de Paris S.A.\",\n    \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\":
        \"AFC.L\",\n    \"companyName\": \"AFC Energy plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"DMCOF\",\n    \"companyName\": \"d'Amico
        International Shipping S.A.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n
        \   \"symbol\": \"ARDX\",\n    \"companyName\": \"Ardelyx, Inc.\",\n    \"noOfTranscripts\":
        \"23\"\n  },\n  {\n    \"symbol\": \"CVV\",\n    \"companyName\": \"CVD Equipment
        Corporation\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\":
        \"CS.TO\",\n    \"companyName\": \"Capstone Copper Corp.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"PODD\",\n    \"companyName\": \"Insulet
        Corporation\",\n    \"noOfTranscripts\": \"60\"\n  },\n  {\n    \"symbol\":
        \"VOLV-A.ST\",\n    \"companyName\": \"AB Volvo (publ)\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"RES\",\n    \"companyName\": \"RPC, Inc.\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"WFAFF\",\n    \"companyName\":
        \"Wesfarmers Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"VBTX\",\n    \"companyName\": \"Veritex Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"EVOK\",\n    \"companyName\": \"Evoke
        Pharma, Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"GE\",\n    \"companyName\": \"GE Aerospace\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"FQVTF\",\n    \"companyName\": \"Fevertree
        Drinks PLC\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"ETRN\",\n    \"companyName\": \"Equitrans Midstream Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"CGNX\",\n    \"companyName\": \"Cognex
        Corporation\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"TCS\",\n    \"companyName\": \"The Container Store Group, Inc.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"TREX\",\n    \"companyName\": \"Trex
        Company, Inc.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"CEAD\",\n    \"companyName\": \"CEA Industries Inc.\",\n    \"noOfTranscripts\":
        \"19\"\n  },\n  {\n    \"symbol\": \"APAM.AS\",\n    \"companyName\": \"Aperam
        S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"CLNX.MC\",\n
        \   \"companyName\": \"Cellnex Telecom, S.A.\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"WFRSF\",\n    \"companyName\": \"West
        African Resources Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"QUIK\",\n    \"companyName\": \"QuickLogic Corporation\",\n
        \   \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\": \"STIXF\",\n    \"companyName\":
        \"Semantix, Inc.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"PCOR\",\n    \"companyName\": \"Procore Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"ALTR\",\n    \"companyName\": \"Altair
        Engineering Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"MMC\",\n    \"companyName\": \"Marsh & McLennan Companies, Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"CRON\",\n    \"companyName\": \"Cronos
        Group Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"HAUTO.OL\",\n    \"companyName\": \"H\xF6egh Autoliners ASA\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MRVL\",\n    \"companyName\": \"Marvell
        Technology, Inc.\",\n    \"noOfTranscripts\": \"75\"\n  },\n  {\n    \"symbol\":
        \"BTCM\",\n    \"companyName\": \"BIT Mining Limited\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"MRVI\",\n    \"companyName\": \"Maravai
        LifeSciences Holdings, Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n  {\n
        \   \"symbol\": \"AHT\",\n    \"companyName\": \"Ashford Hospitality Trust,
        Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"HEX.OL\",\n
        \   \"companyName\": \"Hexagon Composites ASA\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"SLFPF\",\n    \"companyName\": \"Abrdn
        Plc\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\": \"RMTI\",\n
        \   \"companyName\": \"Rockwell Medical, Inc.\",\n    \"noOfTranscripts\":
        \"55\"\n  },\n  {\n    \"symbol\": \"PARAA\",\n    \"companyName\": \"Paramount
        Global\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ITRI\",\n
        \   \"companyName\": \"Itron, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n
        \ {\n    \"symbol\": \"BSET\",\n    \"companyName\": \"Bassett Furniture Industries,
        Incorporated\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"LGIH\",\n    \"companyName\": \"LGI Homes, Inc.\",\n    \"noOfTranscripts\":
        \"46\"\n  },\n  {\n    \"symbol\": \"PFBC\",\n    \"companyName\": \"Preferred
        Bank\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"LNG\",\n
        \   \"companyName\": \"Cheniere Energy, Inc.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"PD.TO\",\n    \"companyName\": \"Precision
        Drilling Corporation\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"FIX\",\n    \"companyName\": \"Comfort Systems USA, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"AJX\",\n    \"companyName\": \"Great
        Ajax Corp.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\":
        \"QBCRF\",\n    \"companyName\": \"Quebecor Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"ORAAF\",\n    \"companyName\": \"Aura
        Minerals Inc.\",\n    \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\":
        \"VVI\",\n    \"companyName\": \"Viad Corp\",\n    \"noOfTranscripts\": \"58\"\n
        \ },\n  {\n    \"symbol\": \"ALLY\",\n    \"companyName\": \"Ally Financial
        Inc.\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\": \"RRX\",\n
        \   \"companyName\": \"Regal Rexnord Corporation\",\n    \"noOfTranscripts\":
        \"62\"\n  },\n  {\n    \"symbol\": \"PSFE\",\n    \"companyName\": \"Paysafe
        Limited\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"RBBN\",\n
        \   \"companyName\": \"Ribbon Communications Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"SUZB3.SA\",\n    \"companyName\": \"Suzano
        S.A.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"SRP.L\",\n
        \   \"companyName\": \"Serco Group plc\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"GDDY\",\n    \"companyName\": \"GoDaddy Inc.\",\n
        \   \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\": \"EMP-A.TO\",\n
        \   \"companyName\": \"Empire Company Limited\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"VOLARA.MX\",\n    \"companyName\": \"Controladora
        Vuela Compa\xF1\xEDa de Aviaci\xF3n, S.A.B. de C.V.\",\n    \"noOfTranscripts\":
        \"43\"\n  },\n  {\n    \"symbol\": \"CPS\",\n    \"companyName\": \"Cooper-Standard
        Holdings Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"PUB.PA\",\n    \"companyName\": \"Publicis Groupe S.A.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"MANH\",\n    \"companyName\": \"Manhattan
        Associates, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"DEUZF\",\n    \"companyName\": \"Deutz AG\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"SGMS\",\n    \"companyName\": \"Scientific Games
        Corporation\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"SXP.TO\",\n    \"companyName\": \"Supremex Inc.\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"S92.DE\",\n    \"companyName\": \"SMA
        Solar Technology AG\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"G.MI\",\n    \"companyName\": \"Assicurazioni Generali S.p.A.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"BEPTF\",\n    \"companyName\": \"Beach
        Energy Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"PBFX\",\n    \"companyName\": \"PBF Logistics LP\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"PRDO\",\n    \"companyName\": \"Perdoceo
        Education Corporation\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\":
        \"EGO\",\n    \"companyName\": \"Eldorado Gold Corporation\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"EVK\",\n    \"companyName\": \"Ever-Glory
        International Group, Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n
        \   \"symbol\": \"9901.HK\",\n    \"companyName\": \"New Oriental Education
        & Technology Group Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n  {\n    \"symbol\":
        \"NUMIF\",\n    \"companyName\": \"Numinus Wellness Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"BBY\",\n    \"companyName\": \"Best Buy
        Co., Inc.\",\n    \"noOfTranscripts\": \"77\"\n  },\n  {\n    \"symbol\":
        \"BCUCF\",\n    \"companyName\": \"Brunello Cucinelli S.p.A.\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"XFAB.PA\",\n    \"companyName\": \"X-FAB
        Silicon Foundries SE\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"AVAH\",\n    \"companyName\": \"Aveanna Healthcare Holdings Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"REED\",\n    \"companyName\": \"Reed's,
        Inc.\",\n    \"noOfTranscripts\": \"54\"\n  },\n  {\n    \"symbol\": \"TC\",\n
        \   \"companyName\": \"Token Cat Limited\",\n    \"noOfTranscripts\": \"9\"\n
        \ },\n  {\n    \"symbol\": \"CPLG\",\n    \"companyName\": \"CorePoint Lodging
        Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"S\",\n
        \   \"companyName\": \"SentinelOne, Inc.\",\n    \"noOfTranscripts\": \"17\"\n
        \ },\n  {\n    \"symbol\": \"PRAX\",\n    \"companyName\": \"Praxis Precision
        Medicines, Inc.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"WRDEF\",\n    \"companyName\": \"Wereldhave N.V.\",\n    \"noOfTranscripts\":
        \"12\"\n  },\n  {\n    \"symbol\": \"EVOP\",\n    \"companyName\": \"EVO Payments,
        Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"OIBZQ\",\n
        \   \"companyName\": \"Oi S.A.\",\n    \"noOfTranscripts\": \"31\"\n  },\n
        \ {\n    \"symbol\": \"APO\",\n    \"companyName\": \"Apollo Global Management,
        Inc.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\": \"CAKE\",\n
        \   \"companyName\": \"The Cheesecake Factory Incorporated\",\n    \"noOfTranscripts\":
        \"72\"\n  },\n  {\n    \"symbol\": \"KIDS\",\n    \"companyName\": \"OrthoPediatrics
        Corp.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"AKCCF\",\n
        \   \"companyName\": \"Aker Carbon Capture ASA\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"ENLC\",\n    \"companyName\": \"EnLink
        Midstream, LLC\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"DPSTF\",\n    \"companyName\": \"Deutsche Post AG\",\n    \"noOfTranscripts\":
        \"26\"\n  },\n  {\n    \"symbol\": \"DH\",\n    \"companyName\": \"Definitive
        Healthcare Corp.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"CRH\",\n    \"companyName\": \"CRH plc\",\n    \"noOfTranscripts\": \"21\"\n
        \ },\n  {\n    \"symbol\": \"TCON\",\n    \"companyName\": \"TRACON Pharmaceuticals,
        Inc.\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"ZLDSF\",\n
        \   \"companyName\": \"Zalando SE\",\n    \"noOfTranscripts\": \"26\"\n  },\n
        \ {\n    \"symbol\": \"AI.TO\",\n    \"companyName\": \"Atrium Mortgage Investment
        Corporation\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"4716.T\",\n    \"companyName\": \"Oracle Corporation Japan\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"URW.PA\",\n    \"companyName\": \"Unibail-Rodamco-Westfield
        SE\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"SWX\",\n
        \   \"companyName\": \"Southwest Gas Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"54\"\n  },\n  {\n    \"symbol\": \"HEAR\",\n    \"companyName\": \"Turtle
        Beach Corporation\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"CUB\",\n    \"companyName\": \"Lionheart Holdings\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"CGG.PA\",\n    \"companyName\": \"Cgg\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"SWR.L\",\n    \"companyName\":
        \"Smurfit Westrock Plc\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"HST\",\n    \"companyName\": \"Host Hotels & Resorts, Inc.\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"KT\",\n    \"companyName\": \"KT Corporation\",\n
        \   \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\": \"FGI\",\n    \"companyName\":
        \"FGI Industries Ltd.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"GXI.DE\",\n    \"companyName\": \"Gerresheimer AG\",\n    \"noOfTranscripts\":
        \"13\"\n  },\n  {\n    \"symbol\": \"DXR\",\n    \"companyName\": \"Daxor
        Corporation\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"TOON\",\n    \"companyName\": \"Kartoon Studios Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SZLS.TO\",\n    \"companyName\": \"StageZero
        Life Sciences Ltd.\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"FTK\",\n    \"companyName\": \"Flotek Industries, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"STNE\",\n    \"companyName\": \"StoneCo
        Ltd.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"MBLY\",\n
        \   \"companyName\": \"Mobileye Global Inc.\",\n    \"noOfTranscripts\": \"11\"\n
        \ },\n  {\n    \"symbol\": \"NIR\",\n    \"companyName\": \"Near Intelligence,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"NINE\",\n
        \   \"companyName\": \"Nine Energy Service, Inc.\",\n    \"noOfTranscripts\":
        \"36\"\n  },\n  {\n    \"symbol\": \"TEN\",\n    \"companyName\": \"Tsakos
        Energy Navigation Limited\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n
        \   \"symbol\": \"BZ\",\n    \"companyName\": \"Kanzhun Limited\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"DETRF\",\n    \"companyName\": \"Deterra
        Royalties Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"GECFF\",\n    \"companyName\": \"Gecina S.A.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"EVKIF\",\n    \"companyName\": \"Evonik
        Industries AG\",\n    \"noOfTranscripts\": \"25\"\n  },\n  {\n    \"symbol\":
        \"WTFC\",\n    \"companyName\": \"Wintrust Financial Corporation\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"GNFT\",\n    \"companyName\": \"Genfit
        S.A.\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\": \"601398.SS\",\n
        \   \"companyName\": \"Industrial & Commercial Bank of China Ltd.\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"UMICF\",\n    \"companyName\": \"Umicore
        S.A.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"TLSNF\",\n
        \   \"companyName\": \"Telia Company AB (publ)\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"MRETF\",\n    \"companyName\": \"Martinrea
        International Inc.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n    \"symbol\":
        \"HAE\",\n    \"companyName\": \"Haemonetics Corporation\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"SGBAF\",\n    \"companyName\": \"Ses
        S.a.\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"MDIBF\",\n
        \   \"companyName\": \"Mediobanca Banca di Credito Finanziario S.p.A.\",\n
        \   \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"GRCLF\",\n    \"companyName\":
        \"GrainCorp Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"EXPI\",\n    \"companyName\": \"eXp World Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"DHL.DE\",\n    \"companyName\": \"Deutsche
        Post AG\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\": \"PLUS\",\n
        \   \"companyName\": \"ePlus inc.\",\n    \"noOfTranscripts\": \"52\"\n  },\n
        \ {\n    \"symbol\": \"GILT.TA\",\n    \"companyName\": \"Gilat Satellite
        Networks Ltd.\",\n    \"noOfTranscripts\": \"61\"\n  },\n  {\n    \"symbol\":
        \"NPO\",\n    \"companyName\": \"EnPro Industries, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"FTV\",\n    \"companyName\": \"Fortive
        Corporation\",\n    \"noOfTranscripts\": \"37\"\n  },\n  {\n    \"symbol\":
        \"LSAK\",\n    \"companyName\": \"Lesaka Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"AMEH\",\n    \"companyName\": \"Apollo
        Medical Holdings, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"688235.SS\",\n    \"companyName\": \"BeOne Medicines Ltd. Class A\",\n    \"noOfTranscripts\":
        \"3\"\n  },\n  {\n    \"symbol\": \"IMIAF\",\n    \"companyName\": \"IMI plc\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"CA.PA\",\n    \"companyName\":
        \"Carrefour S.A.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\":
        \"BNGO\",\n    \"companyName\": \"Bionano Genomics, Inc.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"FORTUM.HE\",\n    \"companyName\": \"Fortum
        Oyj\",\n    \"noOfTranscripts\": \"51\"\n  },\n  {\n    \"symbol\": \"DG.PA\",\n
        \   \"companyName\": \"Vinci S.A.\",\n    \"noOfTranscripts\": \"19\"\n  },\n
        \ {\n    \"symbol\": \"MICT\",\n    \"companyName\": \"MICT, Inc.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"DBGI\",\n    \"companyName\": \"Digital
        Brands Group, Inc.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"WHF\",\n    \"companyName\": \"WhiteHorse Finance, Inc.\",\n    \"noOfTranscripts\":
        \"49\"\n  },\n  {\n    \"symbol\": \"KODK\",\n    \"companyName\": \"Eastman
        Kodak Company\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\":
        \"SNES\",\n    \"companyName\": \"SenesTech, Inc.\",\n    \"noOfTranscripts\":
        \"29\"\n  },\n  {\n    \"symbol\": \"INVE-B.ST\",\n    \"companyName\": \"Investor
        AB (publ)\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"IIVI\",\n
        \   \"companyName\": \"II-VI Incorporated\",\n    \"noOfTranscripts\": \"46\"\n
        \ },\n  {\n    \"symbol\": \"SMG\",\n    \"companyName\": \"The Scotts Miracle-Gro
        Company\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"SLB\",\n
        \   \"companyName\": \"Schlumberger Limited\",\n    \"noOfTranscripts\": \"72\"\n
        \ },\n  {\n    \"symbol\": \"NTES\",\n    \"companyName\": \"NetEase, Inc.\",\n
        \   \"noOfTranscripts\": \"69\"\n  },\n  {\n    \"symbol\": \"SIDU\",\n    \"companyName\":
        \"Sidus Space, Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\":
        \"JD.L\",\n    \"companyName\": \"JD Sports Fashion plc\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"BAESF\",\n    \"companyName\": \"BAE Systems
        plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"IMBBY\",\n
        \   \"companyName\": \"Imperial Brands PLC\",\n    \"noOfTranscripts\": \"11\"\n
        \ },\n  {\n    \"symbol\": \"RTOXF\",\n    \"companyName\": \"Rotork plc\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"VMC.V\",\n    \"companyName\":
        \"Vicinity Motor Corp.\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\":
        \"LEGIF\",\n    \"companyName\": \"LEG Immobilien SE\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"SUNWQ\",\n    \"companyName\": \"Sunworks,
        Inc.\",\n    \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"JSDA\",\n
        \   \"companyName\": \"Jones Soda Co.\",\n    \"noOfTranscripts\": \"57\"\n
        \ },\n  {\n    \"symbol\": \"VOYJF\",\n    \"companyName\": \"Valmet Oyj\",\n
        \   \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"BHC\",\n    \"companyName\":
        \"Bausch Health Companies Inc.\",\n    \"noOfTranscripts\": \"63\"\n  },\n
        \ {\n    \"symbol\": \"NVEE\",\n    \"companyName\": \"NV5 Global, Inc.\",\n
        \   \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"RAVE\",\n    \"companyName\":
        \"RAVE Restaurant Group, Inc.\",\n    \"noOfTranscripts\": \"14\"\n  },\n
        \ {\n    \"symbol\": \"LREN3.SA\",\n    \"companyName\": \"Lojas Renner S.A.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"PGR\",\n    \"companyName\":
        \"The Progressive Corporation\",\n    \"noOfTranscripts\": \"55\"\n  },\n
        \ {\n    \"symbol\": \"WLTW\",\n    \"companyName\": \"Willis Towers Watson
        Public Limited Company\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"AVTBF\",\n    \"companyName\": \"Avant Brands Inc.\",\n    \"noOfTranscripts\":
        \"11\"\n  },\n  {\n    \"symbol\": \"DLB\",\n    \"companyName\": \"Dolby
        Laboratories, Inc.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"VSBY.CN\",\n    \"companyName\": \"VSBLTY Groupe Technologies Corp.\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ANZGY\",\n    \"companyName\":
        \"ANZ Group Holdings Limited\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n
        \   \"symbol\": \"ATR\",\n    \"companyName\": \"AptarGroup, Inc.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"TOI\",\n    \"companyName\": \"The Oncology
        Institute, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"FTT.TO\",\n    \"companyName\": \"Finning International Inc.\",\n    \"noOfTranscripts\":
        \"48\"\n  },\n  {\n    \"symbol\": \"ALAR.TA\",\n    \"companyName\": \"Alarum
        Technologies Ltd.\",\n    \"noOfTranscripts\": \"10\"\n  },\n  {\n    \"symbol\":
        \"0293.HK\",\n    \"companyName\": \"Cathay Pacific Airways Limited\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"ROOT.TO\",\n    \"companyName\": \"Roots
        Corporation\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"SLVM\",\n    \"companyName\": \"Sylvamo Corporation\",\n    \"noOfTranscripts\":
        \"15\"\n  },\n  {\n    \"symbol\": \"CRVL\",\n    \"companyName\": \"CorVel
        Corporation\",\n    \"noOfTranscripts\": \"46\"\n  },\n  {\n    \"symbol\":
        \"BWA\",\n    \"companyName\": \"BorgWarner Inc.\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"AMTM\",\n    \"companyName\": \"Amentum
        Holdings, Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"YAL.AX\",\n    \"companyName\": \"Yancoal Australia Ltd\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"IKTSF\",\n    \"companyName\": \"Intertek
        Group plc\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"GMINF\",\n    \"companyName\": \"G Mining Ventures Corp.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"NHPAP\",\n    \"companyName\": \"National
        Healthcare Properties, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n
        \   \"symbol\": \"STTTF\",\n    \"companyName\": \"Splitit Payments Ltd\",\n
        \   \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"NSIT\",\n    \"companyName\":
        \"Insight Enterprises, Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n
        \   \"symbol\": \"SGML\",\n    \"companyName\": \"Sigma Lithium Corporation\",\n
        \   \"noOfTranscripts\": \"11\"\n  },\n  {\n    \"symbol\": \"FANDY\",\n    \"companyName\":
        \"FirstRand Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"GPC\",\n    \"companyName\": \"Genuine Parts Company\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"SKM\",\n    \"companyName\": \"SK Telecom
        Co.,Ltd\",\n    \"noOfTranscripts\": \"41\"\n  },\n  {\n    \"symbol\": \"CXAI\",\n
        \   \"companyName\": \"CXApp Inc.\",\n    \"noOfTranscripts\": \"9\"\n  },\n
        \ {\n    \"symbol\": \"DVA\",\n    \"companyName\": \"DaVita Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"EXPGF\",\n    \"companyName\": \"Experian
        plc\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"PLYA\",\n
        \   \"companyName\": \"Playa Hotels & Resorts N.V.\",\n    \"noOfTranscripts\":
        \"28\"\n  },\n  {\n    \"symbol\": \"OSTK\",\n    \"companyName\": \"Overstock.com,
        Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n  {\n    \"symbol\": \"CHTR\",\n
        \   \"companyName\": \"Charter Communications, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"UNP\",\n    \"companyName\": \"Union
        Pacific Corporation\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"FEAM\",\n    \"companyName\": \"5E Advanced Materials Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"TLGPY\",\n    \"companyName\": \"Telstra
        Group Limited\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"PHXM.PA\",\n    \"companyName\": \"PHAXIAM Therapeutics S.A.\",\n    \"noOfTranscripts\":
        \"20\"\n  },\n  {\n    \"symbol\": \"HLNE\",\n    \"companyName\": \"Hamilton
        Lane Incorporated\",\n    \"noOfTranscripts\": \"33\"\n  },\n  {\n    \"symbol\":
        \"CWB.TO\",\n    \"companyName\": \"Canadian Western Bank\",\n    \"noOfTranscripts\":
        \"24\"\n  },\n  {\n    \"symbol\": \"SCPH\",\n    \"companyName\": \"scPharmaceuticals
        Inc.\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"DGX\",\n
        \   \"companyName\": \"Quest Diagnostics Incorporated\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"JCI\",\n    \"companyName\": \"Johnson
        Controls International plc\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n
        \   \"symbol\": \"CTVA\",\n    \"companyName\": \"Corteva, Inc.\",\n    \"noOfTranscripts\":
        \"25\"\n  },\n  {\n    \"symbol\": \"SPT\",\n    \"companyName\": \"Sprout
        Social, Inc.\",\n    \"noOfTranscripts\": \"23\"\n  },\n  {\n    \"symbol\":
        \"CMI\",\n    \"companyName\": \"Cummins Inc.\",\n    \"noOfTranscripts\":
        \"71\"\n  },\n  {\n    \"symbol\": \"TOTZF\",\n    \"companyName\": \"Total
        Energy Services Inc.\",\n    \"noOfTranscripts\": \"39\"\n  },\n  {\n    \"symbol\":
        \"MDWD\",\n    \"companyName\": \"MediWound Ltd.\",\n    \"noOfTranscripts\":
        \"44\"\n  },\n  {\n    \"symbol\": \"OCGN\",\n    \"companyName\": \"Ocugen,
        Inc.\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"LGMK\",\n
        \   \"companyName\": \"LogicMark, Inc.\",\n    \"noOfTranscripts\": \"29\"\n
        \ },\n  {\n    \"symbol\": \"MYNA\",\n    \"companyName\": \"Mynaric AG\",\n
        \   \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"FNV\",\n    \"companyName\":
        \"Franco-Nevada Corporation\",\n    \"noOfTranscripts\": \"52\"\n  },\n  {\n
        \   \"symbol\": \"VNRFY\",\n    \"companyName\": \"Vienna Insurance Group
        AG\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\": \"JHX\",\n
        \   \"companyName\": \"James Hardie Industries plc\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"JMP\",\n    \"companyName\": \"JMP Group
        LLC\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"AMYT\",\n
        \   \"companyName\": \"Amryt Pharma plc\",\n    \"noOfTranscripts\": \"6\"\n
        \ },\n  {\n    \"symbol\": \"PAM\",\n    \"companyName\": \"Pampa Energ\xEDa
        S.A.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"PAR\",\n
        \   \"companyName\": \"PAR Technology Corporation\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"AU\",\n    \"companyName\": \"AngloGold
        Ashanti Plc\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"QIWI.ME\",\n    \"companyName\": \"QIWI plc\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"STLD\",\n    \"companyName\": \"Steel
        Dynamics, Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"CC\",\n    \"companyName\": \"The Chemours Company\",\n    \"noOfTranscripts\":
        \"39\"\n  },\n  {\n    \"symbol\": \"COR\",\n    \"companyName\": \"Cencora,
        Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"AREN\",\n
        \   \"companyName\": \"The Arena Group Holdings, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"ANA.MC\",\n    \"companyName\": \"Acciona,
        S.A.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"PDCO\",\n
        \   \"companyName\": \"Patterson Companies, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"TNK\",\n    \"companyName\": \"Teekay
        Tankers Ltd.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"CWBR\",\n    \"companyName\": \"CohBar, Inc.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"ARWR\",\n    \"companyName\": \"Arrowhead
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"BRG\",\n    \"companyName\": \"Bluerock Residential Growth REIT, Inc.\",\n
        \   \"noOfTranscripts\": \"26\"\n  },\n  {\n    \"symbol\": \"KULR\",\n    \"companyName\":
        \"KULR Technology Group, Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n
        \ {\n    \"symbol\": \"UHS\",\n    \"companyName\": \"Universal Health Services,
        Inc.\",\n    \"noOfTranscripts\": \"65\"\n  },\n  {\n    \"symbol\": \"BCS\",\n
        \   \"companyName\": \"Barclays PLC\",\n    \"noOfTranscripts\": \"55\"\n
        \ },\n  {\n    \"symbol\": \"TIGR\",\n    \"companyName\": \"UP Fintech Holding
        Limited\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"WKCMF\",\n
        \   \"companyName\": \"Wacker Chemie AG\",\n    \"noOfTranscripts\": \"43\"\n
        \ },\n  {\n    \"symbol\": \"BGAOF\",\n    \"companyName\": \"Proximus PLC\",\n
        \   \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"EXX.JO\",\n
        \   \"companyName\": \"Exxaro Resources Limited\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"IVSXF\",\n    \"companyName\": \"Investor
        AB (publ)\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\": \"SEGXF\",\n
        \   \"companyName\": \"SEGRO Plc\",\n    \"noOfTranscripts\": \"5\"\n  },\n
        \ {\n    \"symbol\": \"LNZ.VI\",\n    \"companyName\": \"Lenzing AG\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"WOOF\",\n    \"companyName\": \"Petco
        Health and Wellness Company, Inc.\",\n    \"noOfTranscripts\": \"19\"\n  },\n
        \ {\n    \"symbol\": \"JNCE\",\n    \"companyName\": \"Jounce Therapeutics,
        Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\": \"NCTKF\",\n
        \   \"companyName\": \"Nabtesco Corporation\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"CISS\",\n    \"companyName\": \"C3is Inc.\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"LEA\",\n    \"companyName\":
        \"Lear Corporation\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\":
        \"OMQS\",\n    \"companyName\": \"OMNIQ Corp.\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"BUKS\",\n    \"companyName\": \"Butler
        National Corporation\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\":
        \"VNO\",\n    \"companyName\": \"Vornado Realty Trust\",\n    \"noOfTranscripts\":
        \"53\"\n  },\n  {\n    \"symbol\": \"RS\",\n    \"companyName\": \"Reliance
        Steel & Aluminum Co.\",\n    \"noOfTranscripts\": \"64\"\n  },\n  {\n    \"symbol\":
        \"RERE\",\n    \"companyName\": \"ATRenew Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"FCN\",\n    \"companyName\": \"FTI Consulting,
        Inc.\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\": \"PAGS\",\n
        \   \"companyName\": \"PagSeguro Digital Ltd.\",\n    \"noOfTranscripts\":
        \"27\"\n  },\n  {\n    \"symbol\": \"CAE\",\n    \"companyName\": \"CAE Inc.\",\n
        \   \"noOfTranscripts\": \"52\"\n  },\n  {\n    \"symbol\": \"CEU.TO\",\n
        \   \"companyName\": \"CES Energy Solutions Corp.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"IESVF\",\n    \"companyName\": \"Invinity
        Energy Systems plc\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"ACOPF\",\n    \"companyName\": \"The a2 Milk Company Limited\",\n    \"noOfTranscripts\":
        \"5\"\n  },\n  {\n    \"symbol\": \"CTLP\",\n    \"companyName\": \"Cantaloupe,
        Inc.\",\n    \"noOfTranscripts\": \"43\"\n  },\n  {\n    \"symbol\": \"TLF\",\n
        \   \"companyName\": \"Tandy Leather Factory, Inc.\",\n    \"noOfTranscripts\":
        \"31\"\n  },\n  {\n    \"symbol\": \"KR\",\n    \"companyName\": \"The Kroger
        Co.\",\n    \"noOfTranscripts\": \"72\"\n  },\n  {\n    \"symbol\": \"BYON\",\n
        \   \"companyName\": \"Beyond, Inc.\",\n    \"noOfTranscripts\": \"74\"\n
        \ },\n  {\n    \"symbol\": \"HRTFF\",\n    \"companyName\": \"Silver Lake
        Ontario Inc.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"ERIE\",\n    \"companyName\": \"Erie Indemnity Company\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"GLASF\",\n    \"companyName\": \"Glass
        House Brands Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"DYAI\",\n    \"companyName\": \"Dyadic International, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"BOLT\",\n    \"companyName\": \"Bolt
        Biotherapeutics, Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"FA\",\n    \"companyName\": \"First Advantage Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"RDY\",\n    \"companyName\": \"Dr. Reddy's
        Laboratories Limited\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\":
        \"PEN\",\n    \"companyName\": \"Penumbra, Inc.\",\n    \"noOfTranscripts\":
        \"38\"\n  },\n  {\n    \"symbol\": \"BVT.JO\",\n    \"companyName\": \"The
        Bidvest Group Limited\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"UPBD\",\n    \"companyName\": \"Upbound Group, Inc.\",\n    \"noOfTranscripts\":
        \"63\"\n  },\n  {\n    \"symbol\": \"TCLCF\",\n    \"companyName\": \"Transcontinental
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"5EA.AX\",\n
        \   \"companyName\": \"5E Advanced Materials Inc.\",\n    \"noOfTranscripts\":
        \"2\"\n  },\n  {\n    \"symbol\": \"GEO\",\n    \"companyName\": \"The GEO
        Group, Inc.\",\n    \"noOfTranscripts\": \"59\"\n  },\n  {\n    \"symbol\":
        \"CHRD\",\n    \"companyName\": \"Chord Energy Corporation\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"ABBV\",\n    \"companyName\": \"AbbVie
        Inc.\",\n    \"noOfTranscripts\": \"50\"\n  },\n  {\n    \"symbol\": \"ENGH.TO\",\n
        \   \"companyName\": \"Enghouse Systems Limited\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"HO.PA\",\n    \"companyName\": \"Thales
        S.A.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"CERN\",\n
        \   \"companyName\": \"Cerner Corporation\",\n    \"noOfTranscripts\": \"57\"\n
        \ },\n  {\n    \"symbol\": \"NVRI\",\n    \"companyName\": \"Enviri Corporation\",\n
        \   \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\": \"STECF\",\n    \"companyName\":
        \"Scatec ASA\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"DISCA\",\n    \"companyName\": \"Warner Bros. Discovery, Inc.\",\n    \"noOfTranscripts\":
        \"51\"\n  },\n  {\n    \"symbol\": \"TEX\",\n    \"companyName\": \"Terex
        Corporation\",\n    \"noOfTranscripts\": \"71\"\n  },\n  {\n    \"symbol\":
        \"WOLF\",\n    \"companyName\": \"Wolfspeed, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"BEDU\",\n    \"companyName\": \"Bright
        Scholar Education Holdings Limited\",\n    \"noOfTranscripts\": \"22\"\n  },\n
        \ {\n    \"symbol\": \"TKA.DE\",\n    \"companyName\": \"thyssenkrupp AG\",\n
        \   \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"AC.PA\",\n    \"companyName\":
        \"Accor S.A.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\":
        \"MPX\",\n    \"companyName\": \"Marine Products Corporation\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"AVAL\",\n    \"companyName\": \"Grupo
        Aval Acciones y Valores S.A.\",\n    \"noOfTranscripts\": \"35\"\n  },\n  {\n
        \   \"symbol\": \"ITUB\",\n    \"companyName\": \"Ita\xFA Unibanco Holding
        S.A.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"AFE.V\",\n
        \   \"companyName\": \"Africa Energy Corp.\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"VSCO\",\n    \"companyName\": \"Victoria's Secret
        & Co.\",\n    \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"MTG\",\n
        \   \"companyName\": \"MGIC Investment Corporation\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"LAKE\",\n    \"companyName\": \"Lakeland
        Industries, Inc.\",\n    \"noOfTranscripts\": \"53\"\n  },\n  {\n    \"symbol\":
        \"SNAL\",\n    \"companyName\": \"Snail, Inc. Class A Common Stock\",\n    \"noOfTranscripts\":
        \"6\"\n  },\n  {\n    \"symbol\": \"HMST\",\n    \"companyName\": \"HomeStreet,
        Inc.\",\n    \"noOfTranscripts\": \"44\"\n  },\n  {\n    \"symbol\": \"VRNA\",\n
        \   \"companyName\": \"Verona Pharma plc\",\n    \"noOfTranscripts\": \"28\"\n
        \ },\n  {\n    \"symbol\": \"600688.SS\",\n    \"companyName\": \"Sinopec
        Shanghai Petrochemical Company Limited\",\n    \"noOfTranscripts\": \"1\"\n
        \ },\n  {\n    \"symbol\": \"FBIO\",\n    \"companyName\": \"Fortress Biotech,
        Inc.\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"LB.TO\",\n
        \   \"companyName\": \"Laurentian Bank of Canada\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"DPRO\",\n    \"companyName\": \"Draganfly
        Inc.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\": \"PRCH\",\n
        \   \"companyName\": \"Porch Group, Inc.\",\n    \"noOfTranscripts\": \"18\"\n
        \ },\n  {\n    \"symbol\": \"BLNE\",\n    \"companyName\": \"Beeline Holdings,
        Inc.\",\n    \"noOfTranscripts\": \"28\"\n  },\n  {\n    \"symbol\": \"INDB\",\n
        \   \"companyName\": \"Independent Bank Corp.\",\n    \"noOfTranscripts\":
        \"59\"\n  },\n  {\n    \"symbol\": \"TSCO\",\n    \"companyName\": \"Tractor
        Supply Company\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"BKE\",\n    \"companyName\": \"The Buckle, Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"PLUG\",\n    \"companyName\": \"Plug
        Power Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n  {\n    \"symbol\":
        \"IONM\",\n    \"companyName\": \"Assure Holdings Corp.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"HD\",\n    \"companyName\": \"The Home
        Depot, Inc.\",\n    \"noOfTranscripts\": \"79\"\n  },\n  {\n    \"symbol\":
        \"FLOW\",\n    \"companyName\": \"Global X U.S. Cash Flow Kings 100 ETF\",\n
        \   \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\": \"ITVPF\",\n    \"companyName\":
        \"ITV plc\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\": \"TELNF\",\n
        \   \"companyName\": \"Telenor ASA\",\n    \"noOfTranscripts\": \"33\"\n  },\n
        \ {\n    \"symbol\": \"FTHM\",\n    \"companyName\": \"Fathom Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\": \"VSH\",\n    \"companyName\":
        \"Vishay Intertechnology, Inc.\",\n    \"noOfTranscripts\": \"68\"\n  },\n
        \ {\n    \"symbol\": \"UONE\",\n    \"companyName\": \"Urban One, Inc.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"BECN\",\n    \"companyName\":
        \"Beacon Roofing Supply, Inc.\",\n    \"noOfTranscripts\": \"58\"\n  },\n
        \ {\n    \"symbol\": \"ESI.TO\",\n    \"companyName\": \"Ensign Energy Services
        Inc.\",\n    \"noOfTranscripts\": \"34\"\n  },\n  {\n    \"symbol\": \"HSAI\",\n
        \   \"companyName\": \"Hesai Group\",\n    \"noOfTranscripts\": \"10\"\n  },\n
        \ {\n    \"symbol\": \"NUS\",\n    \"companyName\": \"Nu Skin Enterprises,
        Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\": \"BOX\",\n
        \   \"companyName\": \"Box, Inc.\",\n    \"noOfTranscripts\": \"56\"\n  },\n
        \ {\n    \"symbol\": \"BEKE\",\n    \"companyName\": \"KE Holdings Inc.\",\n
        \   \"noOfTranscripts\": \"19\"\n  },\n  {\n    \"symbol\": \"AFIIQ\",\n    \"companyName\":
        \"Armstrong Flooring, Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n
        \   \"symbol\": \"STAB\",\n    \"companyName\": \"Statera Biopharma, Inc.\",\n
        \   \"noOfTranscripts\": \"16\"\n  },\n  {\n    \"symbol\": \"NNOCF\",\n    \"companyName\":
        \"Nanoco Group plc\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\":
        \"AIRS\",\n    \"companyName\": \"AirSculpt Technologies, Inc.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"OCSL\",\n    \"companyName\": \"Oaktree
        Specialty Lending Corporation\",\n    \"noOfTranscripts\": \"67\"\n  },\n
        \ {\n    \"symbol\": \"ATCO-A.ST\",\n    \"companyName\": \"Atlas Copco AB\",\n
        \   \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\": \"ARZTF\",\n    \"companyName\":
        \"Aryzta AG\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"IWSY\",\n    \"companyName\": \"ImageWare Systems, Inc.\",\n    \"noOfTranscripts\":
        \"34\"\n  },\n  {\n    \"symbol\": \"DFS\",\n    \"companyName\": \"Discover
        Financial Services\",\n    \"noOfTranscripts\": \"67\"\n  },\n  {\n    \"symbol\":
        \"VVV\",\n    \"companyName\": \"Valvoline Inc.\",\n    \"noOfTranscripts\":
        \"35\"\n  },\n  {\n    \"symbol\": \"GRRMF\",\n    \"companyName\": \"Gerresheimer
        AG\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n    \"symbol\": \"FOUR\",\n
        \   \"companyName\": \"Shift4 Payments, Inc.\",\n    \"noOfTranscripts\":
        \"21\"\n  },\n  {\n    \"symbol\": \"MIMO\",\n    \"companyName\": \"Airspan
        Networks Holdings Inc.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\":
        \"BRO\",\n    \"companyName\": \"Brown & Brown, Inc.\",\n    \"noOfTranscripts\":
        \"66\"\n  },\n  {\n    \"symbol\": \"UAMY\",\n    \"companyName\": \"United
        States Antimony Corporation\",\n    \"noOfTranscripts\": \"13\"\n  },\n  {\n
        \   \"symbol\": \"CREX\",\n    \"companyName\": \"Creative Realities, Inc.\",\n
        \   \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\": \"NXPL\",\n    \"companyName\":
        \"NextPlat Corp\",\n    \"noOfTranscripts\": \"2\"\n  },\n  {\n    \"symbol\":
        \"CBNT\",\n    \"companyName\": \"C-Bond Systems, Inc.\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"HEI.DE\",\n    \"companyName\": \"HeidelbergCement
        AG\",\n    \"noOfTranscripts\": \"12\"\n  },\n  {\n    \"symbol\": \"RVTY\",\n
        \   \"companyName\": \"Revvity, Inc.\",\n    \"noOfTranscripts\": \"71\"\n
        \ },\n  {\n    \"symbol\": \"LFST\",\n    \"companyName\": \"LifeStance Health
        Group, Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"FHSEY\",\n    \"companyName\": \"First High-School Education Group Co.,
        Ltd.\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\": \"SBFG\",\n
        \   \"companyName\": \"SB Financial Group, Inc.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"RUSHA\",\n    \"companyName\": \"Rush
        Enterprises, Inc.\",\n    \"noOfTranscripts\": \"55\"\n  },\n  {\n    \"symbol\":
        \"AVA\",\n    \"companyName\": \"Avista Corporation\",\n    \"noOfTranscripts\":
        \"64\"\n  },\n  {\n    \"symbol\": \"SBH\",\n    \"companyName\": \"Sally
        Beauty Holdings, Inc.\",\n    \"noOfTranscripts\": \"62\"\n  },\n  {\n    \"symbol\":
        \"ARKAF\",\n    \"companyName\": \"Arkema S.A.\",\n    \"noOfTranscripts\":
        \"37\"\n  },\n  {\n    \"symbol\": \"NEXN\",\n    \"companyName\": \"Nexxen
        International Ltd.\",\n    \"noOfTranscripts\": \"17\"\n  },\n  {\n    \"symbol\":
        \"YOKEF\",\n    \"companyName\": \"Yokogawa Electric Corporation\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"SEE.L\",\n    \"companyName\": \"Seeing
        Machines Limited\",\n    \"noOfTranscripts\": \"5\"\n  },\n  {\n    \"symbol\":
        \"MTDR\",\n    \"companyName\": \"Matador Resources Company\",\n    \"noOfTranscripts\":
        \"52\"\n  },\n  {\n    \"symbol\": \"DTCB\",\n    \"companyName\": \"Solo
        Brands, Inc.\",\n    \"noOfTranscripts\": \"15\"\n  },\n  {\n    \"symbol\":
        \"HUIZ\",\n    \"companyName\": \"Huize Holding Limited\",\n    \"noOfTranscripts\":
        \"22\"\n  },\n  {\n    \"symbol\": \"TME\",\n    \"companyName\": \"Tencent
        Music Entertainment Group\",\n    \"noOfTranscripts\": \"26\"\n  },\n  {\n
        \   \"symbol\": \"NEXPF\",\n    \"companyName\": \"Nexi S.p.A.\",\n    \"noOfTranscripts\":
        \"17\"\n  },\n  {\n    \"symbol\": \"BNS\",\n    \"companyName\": \"The Bank
        of Nova Scotia\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n    \"symbol\":
        \"AFGYF\",\n    \"companyName\": \"AFC Energy plc\",\n    \"noOfTranscripts\":
        \"1\"\n  },\n  {\n    \"symbol\": \"BVN\",\n    \"companyName\": \"Compa\xF1\xEDa
        de Minas Buenaventura S.A.A.\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n
        \   \"symbol\": \"BCE\",\n    \"companyName\": \"BCE Inc.\",\n    \"noOfTranscripts\":
        \"57\"\n  },\n  {\n    \"symbol\": \"SVNLF\",\n    \"companyName\": \"Svenska
        Handelsbanken AB (publ)\",\n    \"noOfTranscripts\": \"36\"\n  },\n  {\n    \"symbol\":
        \"GLMD\",\n    \"companyName\": \"Galmed Pharmaceuticals Ltd.\",\n    \"noOfTranscripts\":
        \"30\"\n  },\n  {\n    \"symbol\": \"NPI.TO\",\n    \"companyName\": \"Northland
        Power Inc.\",\n    \"noOfTranscripts\": \"42\"\n  },\n  {\n    \"symbol\":
        \"YELL\",\n    \"companyName\": \"Yellow Corporation\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"BIDU\",\n    \"companyName\": \"Baidu,
        Inc.\",\n    \"noOfTranscripts\": \"78\"\n  },\n  {\n    \"symbol\": \"TARS\",\n
        \   \"companyName\": \"Tarsus Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"KAP.IL\",\n    \"companyName\": \"JSC
        National Atomic Company Kazatomprom\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"ARMN\",\n    \"companyName\": \"Aris Mining Corporation\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"BNS.TO\",\n    \"companyName\":
        \"The Bank of Nova Scotia\",\n    \"noOfTranscripts\": \"56\"\n  },\n  {\n
        \   \"symbol\": \"CSSE\",\n    \"companyName\": \"Chicken Soup for the Soul
        Entertainment, Inc.\",\n    \"noOfTranscripts\": \"22\"\n  },\n  {\n    \"symbol\":
        \"AMED\",\n    \"companyName\": \"Amedisys, Inc.\",\n    \"noOfTranscripts\":
        \"50\"\n  },\n  {\n    \"symbol\": \"IMCC.CN\",\n    \"companyName\": \"IM
        Cannabis Corp.\",\n    \"noOfTranscripts\": \"14\"\n  },\n  {\n    \"symbol\":
        \"CCH.L\",\n    \"companyName\": \"Coca-Cola HBC AG\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"ICAD.PA\",\n    \"companyName\": \"Icade
        S.A.\",\n    \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"RHT.V\",\n
        \   \"companyName\": \"Reliq Health Technologies Inc.\",\n    \"noOfTranscripts\":
        \"8\"\n  },\n  {\n    \"symbol\": \"2015.HK\",\n    \"companyName\": \"Li
        Auto Inc.\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\":
        \"BLGO\",\n    \"companyName\": \"BioLargo, Inc.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"MEI\",\n    \"companyName\": \"Methode
        Electronics, Inc.\",\n    \"noOfTranscripts\": \"70\"\n  },\n  {\n    \"symbol\":
        \"7733.T\",\n    \"companyName\": \"Olympus Corporation\",\n    \"noOfTranscripts\":
        \"4\"\n  },\n  {\n    \"symbol\": \"AIJTY\",\n    \"companyName\": \"Jianpu
        Technology Inc.\",\n    \"noOfTranscripts\": \"18\"\n  },\n  {\n    \"symbol\":
        \"TM\",\n    \"companyName\": \"Toyota Motor Corporation\",\n    \"noOfTranscripts\":
        \"16\"\n  },\n  {\n    \"symbol\": \"IMO\",\n    \"companyName\": \"Imperial
        Oil Limited\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"CNQ\",\n    \"companyName\": \"Canadian Natural Resources Limited\",\n    \"noOfTranscripts\":
        \"73\"\n  },\n  {\n    \"symbol\": \"ARLUF\",\n    \"companyName\": \"Aristocrat
        Leisure Limited\",\n    \"noOfTranscripts\": \"3\"\n  },\n  {\n    \"symbol\":
        \"SLTTF\",\n    \"companyName\": \"Ravelin Properties REIT\",\n    \"noOfTranscripts\":
        \"18\"\n  },\n  {\n    \"symbol\": \"YGYI\",\n    \"companyName\": \"Youngevity
        International, Inc.\",\n    \"noOfTranscripts\": \"21\"\n  },\n  {\n    \"symbol\":
        \"NWSA\",\n    \"companyName\": \"News Corporation\",\n    \"noOfTranscripts\":
        \"77\"\n  },\n  {\n    \"symbol\": \"COWN\",\n    \"companyName\": \"Cowen
        Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\": \"AVCTF\",\n
        \   \"companyName\": \"Avacta Group Plc\",\n    \"noOfTranscripts\": \"3\"\n
        \ },\n  {\n    \"symbol\": \"BVHMF\",\n    \"companyName\": \"Vistry Group
        PLC\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"AIAGF\",\n
        \   \"companyName\": \"Aurubis AG\",\n    \"noOfTranscripts\": \"1\"\n  },\n
        \ {\n    \"symbol\": \"LFCR\",\n    \"companyName\": \"Lifecore Biomedical,
        Inc.\",\n    \"noOfTranscripts\": \"66\"\n  },\n  {\n    \"symbol\": \"AMRK\",\n
        \   \"companyName\": \"A-Mark Precious Metals, Inc.\",\n    \"noOfTranscripts\":
        \"42\"\n  },\n  {\n    \"symbol\": \"PETQ\",\n    \"companyName\": \"PetIQ,
        Inc.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\": \"SAP\",\n
        \   \"companyName\": \"Sap Se\",\n    \"noOfTranscripts\": \"69\"\n  },\n
        \ {\n    \"symbol\": \"ELUXY\",\n    \"companyName\": \"AB Electrolux (publ)\",\n
        \   \"noOfTranscripts\": \"8\"\n  },\n  {\n    \"symbol\": \"ADM\",\n    \"companyName\":
        \"Archer-Daniels-Midland Company\",\n    \"noOfTranscripts\": \"68\"\n  },\n
        \ {\n    \"symbol\": \"LASE\",\n    \"companyName\": \"Laser Photonics Corporation\",\n
        \   \"noOfTranscripts\": \"6\"\n  },\n  {\n    \"symbol\": \"HQY\",\n    \"companyName\":
        \"HealthEquity, Inc.\",\n    \"noOfTranscripts\": \"45\"\n  },\n  {\n    \"symbol\":
        \"KREF\",\n    \"companyName\": \"KKR Real Estate Finance Trust Inc.\",\n
        \   \"noOfTranscripts\": \"30\"\n  },\n  {\n    \"symbol\": \"CCOEY\",\n    \"companyName\":
        \"Capcom Co., Ltd.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\":
        \"CTHR\",\n    \"companyName\": \"Charles & Colvard, Ltd.\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"EGKLF\",\n    \"companyName\": \"ElringKlinger
        AG\",\n    \"noOfTranscripts\": \"7\"\n  },\n  {\n    \"symbol\": \"TPICQ\",\n
        \   \"companyName\": \"TPI Composites, Inc.\",\n    \"noOfTranscripts\": \"33\"\n
        \ },\n  {\n    \"symbol\": \"3888.HK\",\n    \"companyName\": \"Kingsoft Corporation
        Limited\",\n    \"noOfTranscripts\": \"20\"\n  },\n  {\n    \"symbol\": \"YTEN\",\n
        \   \"companyName\": \"Yield10 Bioscience, Inc.\",\n    \"noOfTranscripts\":
        \"60\"\n  },\n  {\n    \"symbol\": \"DEFTF\",\n    \"companyName\": \"DeFi
        Technologies Inc.\",\n    \"noOfTranscripts\": \"4\"\n  },\n  {\n    \"symbol\":
        \"PIAGF\",\n    \"companyName\": \"Piaggio & C. S.p.A.\",\n    \"noOfTranscripts\":
        \"9\"\n  },\n  {\n    \"symbol\": \"DRNA\",\n    \"companyName\": \"Dicerna
        Pharmaceuticals, Inc.\",\n    \"noOfTranscripts\": \"29\"\n  },\n  {\n    \"symbol\":
        \"PNR\",\n    \"companyName\": \"Pentair plc\",\n    \"noOfTranscripts\":
        \"65\"\n  },\n  {\n    \"symbol\": \"YHGJ\",\n    \"companyName\": \"Yunhong
        Green CTI Ltd.\",\n    \"noOfTranscripts\": \"27\"\n  },\n  {\n    \"symbol\":
        \"PEV\",\n    \"companyName\": \"Phoenix Motor Inc.\",\n    \"noOfTranscripts\":
        \"7\"\n  },\n  {\n    \"symbol\": \"MNTX\",\n    \"companyName\": \"Manitex
        International, Inc.\",\n    \"noOfTranscripts\": \"49\"\n  },\n  {\n    \"symbol\":
        \"WNS\",\n    \"companyName\": \"WNS (Holdings) Limited\",\n    \"noOfTranscripts\":
        \"45\"\n  },\n  {\n    \"symbol\": \"601288.SS\",\n    \"companyName\": \"Agricultural
        Bank of China Limited\",\n    \"noOfTranscripts\": \"9\"\n  },\n  {\n    \"symbol\":
        \"ANIK\",\n    \"companyName\": \"Anika Therapeutics, Inc.\",\n    \"noOfTranscripts\":
        \"67\"\n  },\n  {\n    \"symbol\": \"FIG\",\n    \"companyName\": \"Figma,
        Inc.\",\n    \"noOfTranscripts\": \"1\"\n  },\n  {\n    \"symbol\": \"ICFI\",\n
        \   \"companyName\": \"ICF International, Inc.\",\n    \"noOfTranscripts\":
        \"58\"\n  },\n  {\n    \"symbol\": \"PNTG\",\n    \"companyName\": \"The Pennant
        Group, Inc.\",\n    \"noOfTranscripts\": \"24\"\n  },\n  {\n    \"symbol\":
        \"WGO\",\n    \"companyName\": \"Winnebago Industries, Inc.\",\n    \"noOfTranscripts\":
        \"61\"\n  },\n  {\n    \"symbol\": \"JLP.L\",\n    \"companyName\": \"Jubilee
        Metals Group PLC\",\n    \"noOfTranscripts\": \"3\"\n  },
... [truncated]
```

## High-Level Overview

This is a .yaml file containing 13929 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:39.514272
- Generator: World's Best Repo Book Generator v1.0.0
