# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:40:39 2023

@author: Dongjae
"""
def split_text(text, max_chars):
    split_list = []
    start = 0
    remaining_text = text

    while len(remaining_text) > max_chars:
        end = start + max_chars
        last_newline_index = remaining_text[:end].rfind('\n')

        if last_newline_index != -1:
            end = start + last_newline_index

        split_list.append(remaining_text[start:end].strip())
        remaining_text = remaining_text[end:].strip()

    if remaining_text:
        split_list.append(remaining_text)

    return split_list

# 사용 예시
long_text = """

MAC Global Solar Index Consultation on the Addition of New Business Involvement Screens and Changes to the Governance Score Screen
Fidelity Quality Income Indices Consultation on Additional Business Activity and Controversies Exclusions and Enhancing Sustainability Criteria
Addition to the S&P BSE SME IPO Index
IHS Markit Benchmark Administration Limited Consultation on Removing Russian Ruble from the Universe of Eligible Currencies for the HSBC EM FX Indices
IHS Markit Benchmark Administration Limited Consultation on USD LIBOR Transition for the HSBC TRY Forward Implied 3 Month Rate Index
S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $9.7 Billion During Q1 2023; 12-Month Gain was $59.7 Billion
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite and S&P/TSX 60 Indices
Crane Set to Join S&P MidCap 400; PacWest  Bancorp to Join S&P SmallCap 600
Additions to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
N-able Set to Join S&P SmallCap 600
S&P CORELOGIC CASE-SHILLER INDEX DECLINING TREND CONTINUED IN JANUARY
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Changes to the S&P BSE Indices
IHS Markit Benchmark Administration Limited Consultation on the Cessation of Certain LGIM Matching Plus Indices – Results
Changes to the S&P BSE Indices
Addition to the S&P BSE SME IPO Index
Modification to the Methodology of the S&P Global Clean Energy Indices
S&P 500 Q4 2022 Buybacks Tick up, As 2022 Sets A Record
S&P/Experian Consumer Credit Default Indices Show Fourth Consecutive Increase in Composite Rate for February 2023
Changes to the S&P BSE Indices
Modification to the Methodology of the iBoxx Contingent Convertible Liquid Developed Europe AT1 Index
Addition to the S&P BSE SME IPO Index
Postponement of Transition to S&P Global Business Involvement Screens
Exponent Set to Join S&P MidCap 400; CVR Energy and Certara to Join S&P SmallCap 600
Modification to the Methodology of the 33% (iBoxx ABF Singapore Government + iBoxx SGD Statutory Boards) + 67% (iBoxx SGD Corporates Investment Grade) (2023-05) Index
IHS Markit Benchmark Administration Limited Consultation on the European, North American, and Global iBoxx Indices – Results (Updated)
Notice: S&P Dow Jones Indices Announces Changes updated to the S&P IPSA
Addition to the S&P BSE IPO Index
S&P 500 ESG Exclusions II Index
Bunge Set to Join S&P 500
Modification to the Methodology of the S&P/ASX Agribusiness Index
Notice: S&P Dow Jones Indices Treatment for Sri Lanka, Nigeria, Russia, Lebanon and Argentina
Additions to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BVL Peru Select Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P IPSA  Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P/BMV China SX20 Index
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P Colombia Select Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the Dow Jones U.S. Select Dividend Index
S&P Dow Jones Indices Announces Rebalancing  Results for the S&P MERVAL Index
Insulet Set to Join S&P 500
Modification to the Methodologies of the S&P BSE Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces March 2023 Quarterly Rebalance of the S&P/TOPIX 150 Index
IHS Markit Benchmark Administration Limited Announces the Cessation of Certain UBS Indices
Additions to the S&P BSE SME IPO Index
IHS Markit Benchmark Administration Limited Consultation on the iBoxx € Liquid Germany Covered Diversified Index – Results
IHS Markit Benchmark Administration Limited Consultation on USD LIBOR Transition for BNP Paribas TRY 3 Month FX Forward Implied Rate Index – Results
IHS Markit Benchmark Administration Limited Consultation on Capital Controls of International and National Debt
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Fair Isaac & Co. Set to Join S&P 500; Others to Join S&P MidCap 400 and S&P SmallCap 600
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces March 2023 Quarterly Rebalance of the S&P Europe 350 Indices
Changes to the S&P BSE Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces March 2023 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces March 2023 Quarterly Rebalance of the S&P/NZX Indices
Modification to the Methodology of S&P BSE Power Index
Additions to the S&P BSE SME IPO Index
Modification to the Methodologies of Certain S&P Kensho Indices – Updated
S&P CORELOGIC CASE-SHILLER INDEX DECLINE CONTINUED IN DECEMBER
S&P Dow Jones Indices Introduces Environmental Metrics for Commodities with the Launch of the S&P GSCI Climate  Aware Index
S&P Select Industry Indices Consultation on Constituent Weighting – Updated
Modification to the Methodology of the Dow Jones Brookfield Global Infrastructure Corporate Bond Indices
S&P/BMV China SX20 Index Consultation on Constituent Selection – Results
IHS Markit Benchmark Administration Limited Consultation on the iBoxx ALBI Government Investible Universe ex-High Yield (60%) & CNH Deposit Rate (40%) Custom Index (2023-02) – Results
IHS Markit Benchmark Administration Limited Consultation on the Cessation of EMIX Indices – Results
IHS Markit Benchmark Administration Limited Consultation on the European, North American, and Global iBoxx Indices – Results
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Columbia Banking System Set to Join S&P MidCap 400; Verra Mobility to Join S&P SmallCap 600
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Modification to the Methodology of the S&P Global Clean Energy Indices
Modification to the Methodologies of Certain S&P Kensho Indices
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
IHS Markit Benchmark Administration Limited Consultation on the Cessation of Certain UBS Market Beta Indices – Results
S&P Paris-Aligned ESG+ Indices Consultation on Eligibility Requirements – Results
IHS Markit Benchmark Administration Limited Consultation on the iBoxx USD Liquid Investment Grade Indices – Results
Notice: Constituent Change Announced for the S&P 500 Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
IHS Markit Benchmark Administration Limited Consultation on the Cessation of certain LGIM Matching Plus Indices
S&P Dow Jones Indices Announces the Reopening of the S&P/BMV Fixed Income Indices Consultation on Cash Reinvestments
S&P/Experian Consumer Credit Default Indices Show Third Consecutive Increase in Composite Rate for January 2023
Addition to the S&P BSE SME IPO Index
Transition to S&P Global Business Involvement Screens
IHS Markit Benchmark Administration Limited Consultation on the Cessation of the First Republic Bank Indices – Results
S&P Select Industry Indices Consultation on Constituent Weighting
Changes to the S&P BSE 100 ESG Index
UFP Industries Set to Join S&P MidCap 400; Otter Tail to Join S&P SmallCap 600
IHS Markit Benchmark Administration Limited Consultation on USD LIBOR Transition for BNP Paribas TRY 3 Month FX Forward Implied Rate Index
IHS Markit Benchmark Administration Limited Consultation on the Cash Return Rate for the iTraxx-CDX IG Global Credit Steepener Index and iTraxx-CDX IG Global Credit Flattener Index – Results
Modification to the Methodology of the Dow Jones Islamic Market Indices
IHS Markit Benchmark Administration Limited Consultation on the Cessation of Certain CDS Benchmark Indices – Results
Modification to the Methodology of S&P/BYMA Indices
Changes to the S&P BSE Indices
S&P/JPX Carbon Efficient Series, S&P/TSX Carbon Efficient Index Series and S&P Global Carbon Efficient Index Series Consultation – Results (Updated)
S&P MERVAL Index Consultation on Selection Universe and Constituent Selection Criteria – Results
S&P NextGenerationEU Recovery Equity Index Methodology Update
S&P/ASX All Technology Index Consultation on Membership Classification – Results
Consultation on Potential Changes to the Dow Jones REIT/RESI Industry Classification Hierarchy and the S&P Property Peer Group Classification - Results
S&P/JPX Carbon Efficient Series, S&P/TSX Carbon Efficient Index Series and S&P Global Carbon Efficient Index Series Consultation - Results
S&P 500 Net Zero 2050 Paris-Aligned Sustainability Screened Index Consultation on Eligibility Requirements and Constraints – Results (Updated)
Reconstitution of S&P BSE Indices
Modification to Methodology of the S&P Europe 350 Index Family
Addition to the S&P BSE SME IPO Index
S&P Paris-Aligned ESG+ Indices Consultation on Eligibility Requirements
IHS Markit Benchmark Administration Limited Announces the Reopening of the Consultation on the Cessation of EMIX Indices
IHS Markit Benchmark Administration Limited Consultation on the Cessation of Certain UBS Market Beta Indices
Modification to the Methodology of the Dow Jones International Internet Index
Adani Enterprises to be removed from Dow Jones Sustainability Indices
Addition to the S&P BSE SME IPO Index
S&P U.S. Retiree Spending Index Methodology Update
S&P CoreLogic Case-Shiller Index Continued To Decline in November
Addition to the S&P BSE SME IPO Index
Agree Realty Set to Join S&P MidCap 400; Comstock Resources to Join S&P SmallCap 600
IHS Markit Benchmark Administration Limited Consultation on the iBoxx € Liquid Germany Covered Diversified Index
S&P/BMV China SX20 Index Consultation on Constituent Selection – Updated
S&P 1500 TBCAM Index Methodology Update
Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index Family
Northern Oil and Gas Set to Join S&P SmallCap 600
Modification to the Methodology of the S&P/NZX Indices
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
DoubleVerify Holdings to Join S&P SmallCap 600
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Dividend Aristocrats Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P High Yield Dividend Aristocrats Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P 500 Dividend Aristocrats
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
IHS Markit Benchmark Administration Limited Consultation on the iBoxx ALBI Government Investible Universe ex-High Yield (60%) & CNH Deposit Rate (40%) Custom Index (2023-02)
IHS Markit Benchmark Administration Limited Consultation on the Cessation of Certain CDS Benchmark Indices
IHS Markit Benchmark Administration Limited Consultation on the Cash Return Rate for the iTraxx-CDX IG Global Credit Steepener Index and iTraxx-CDX IG Global Credit Flattener Index
IHS Markit Benchmark Administration Limited Consultation on the Cessation of the First Republic Bank Indices
S&P/Experian Consumer Credit Default Indices Show Higher Composite Rate For December 2022
Addition to the S&P BSE SME IPO Index
Changes to the S&P BSE Indices
Clarification to the iBoxx EUR European Union Select Index Methodology
IHS Markit Benchmark Administration Limited Consultation on the iBoxx USD Liquid Investment Grade Indices
S&P/JPX Carbon Efficient Series, S&P/TSX Carbon Efficient Index Series and S&P Global Carbon Efficient Index Series Consultation – Updated
Additions to the S&P BSE SME IPO Index
Modification to the Methodology of the S&P Consumer Finance Index
S&P/JPX Carbon Efficient Series, S&P/TSX Carbon Efficient Index Series and S&P Global Carbon Efficient Index Series Consultation
S&P/BMV China SX20 Index Consultation on Constituent Selection
Modification to the Methodology of the S&P 500 Shariah Industry Exclusions Index
S&P MERVAL Index Consultation on Selection Universe and Constituent Selection Criteria
Pendal Group Limited to be removed from the S&P/ASX 200 Index
S&P Technology Dividend Aristocrats Index Methodology Update
S&P Global BMI and Dow Jones Global Indices Consultation on Eligibility Criteria – Results
S&P Dow Jones Indices Announces Update to S&P Composite 1500 Market Cap Guidelines and Results of S&P Composite 1500 Index Consultation on Market Capitalization and Liquidity Eligibility Criteria
S&P Dow Jones Indices Announces Changes in  Dividend Withholding Tax Rates
S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $14.6 Billion During Q4 2022 and $68.2 Billion in 2022
Index Reconstitution Calendar 2023
Changes to the S&P BSE Indices
S&P 500 Net Zero 2050 Paris-Aligned Sustainability Screened Index Consultation on Eligibility Requirements and Constraints – Results
IHS Markit Benchmark Administration Limited Consultation on EMIX World Indices Market Classification – Results
Addition to the S&P BSE IPO Index
Addition to the S&P BSE IPO
Modification to the Methodology of the S&P/ASX Indices
GE HealthCare Technologies Set to Join S&P 500; Vornado Realty Trust to Join S&P MidCap 400; RXO to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Continued To Decline In October
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
IHS Markit Benchmark Administration Limited Consultation on Japanese and Korean Dividends Treatment for EMIX (EMICS) and EMIX World Index Families — Results (Updated)
Additions to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Modification to the Methodology of the S&P Global Luxury Index
S&P/TSX SmallCap Index Consultation on Eligibility Factors – Results
IHS Markit Benchmark Administration Limited Consultation on the European, North American, and Global iBoxx Indices
Addition to the S&P BSE IPO Index
Modification to the Methodology for the S&P 500 Rate Sensitivity Indices
Modification to the Methodology for the S&P 500 Buyback Indices
S&P Dow Jones Indices Announces Change to the S&P/TSX Canadian Dividend Aristocrats Index
S&P/ASX All Technology Index Consultation on Membership Classification
S&P/Experian Consumer Credit Default Indices Show Higher Composite Rate for November 2022
Addition to the S&P BSE SME IPO
IHS Markit Benchmark Administration Limited Consultation on LGIM Matching Plus and Core Indices Hedging Calculation – Results
IHS Markit Benchmark Administration Limited Consultation on the iBoxx MSCI EUR/USD High Yield Paris Aligned Capped TCA Indices – Results
Steel Dynamics Set to Join S&P 500; Super Micro Computer to Join S&P MidCap 400
S&P 500 Buybacks Decline 4.0% but Energy Buybacks increase 64.5%
IHS Markit Benchmark Administration Limited Consultation on the Cessation of EMIX Indices
S&P Select Industry Indices Consultation on Membership Classification – Results
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
First Solar Set to Join S&P 500; Fortune Brands  Innovations to Join S&P MidCap 400; MasterBrand  to Join S&P SmallCap 600
Additions to the S&P BSE IPO Index
S&P Commodity Producers Agribusiness and S&P Global Agribusiness Equity Indices Eligible RBICS Methodology Update
S&P Dow Jones Indices Announces Dow Jones Sustainability Indices 2022 Review Results
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV IPC CompMx Trailing Income Equities ESG Tilted Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV FIBRAS Index
Reconstitution of S&P BSE Indices
IHS Markit Benchmark Administration Limited Consultation on Publication Schedule and Constituent Pricing Source Changes to the IHS Markit Global Carbon Index – Results (Updated)
Addition to the S&P BSE IPO Index
IHS Markit Benchmark Administration Limited Consultation on USD LIBOR Transition for Danish Government Bond Index Hedged into USD and Danish Callable Mortgage Bond Index Hedged into USD – Results
S&P Dow Jones Equity Indices’ Short-Term Stock Suspensions Policy Update
IHS Markit Benchmark Administration Limited Consultation on LGIM Matching Plus and Core Indices Hedging Calculation – Updated
IHS Markit Benchmark Administration Limited Consultation on LGIM Matching Plus and Core Indices Hedging Calculation
IHS Markit Benchmark Administration Limited Consultation on the iBoxx MSCI EUR/USD High Yield Paris Aligned Capped TCA Indices
Modification to the Methodology of the S&P Access China Enterprises Enhanced Value Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Allegro Microsystems and CubeSmart Set to Join S&P MidCap 400; Others to Join S&P SmallCap 600
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
Brookfield Asset Management Inc. (TSX:BAM.A) asset management business spinoff
S&P Global BMI and Dow Jones Global Indices Consultation on Eligibility Criteria – Extended
S&P Dow Jones Indices Announces December 2022 Quarterly Rebalance of the S&P Europe 350 Indices
Addition to the S&P BSE SME IPO Index
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Treatment for Sri Lanka, Russia, Lebanon, Argentina and Nigeria
S&P Dow Jones Indices Announces December 2022 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces December 2022 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces December 2022 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices Announces 2023 Weights for the Dow Jones Commodity Index
S&P France 40 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements – Results
S&P BOCHK China Hong Kong Greater Bay Area Net Zero 2050 Climate Transition Index Consultation on Constraints – Results
Consultation on Potential Changes to the Dow Jones REIT/RESI Industry Classification Hierarchy and the S&P Property Peer Group Classification
IHS Markit Benchmark Administration Limited Consultation on the iBoxx MSCI ESG USD Asia ex-Japan High Yield Capped TCA Index Eligibility Criteria – Results
S&P China 500 Index Consultation on Eligibility Criteria – Results
Notice: S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
S&P CoreLogic Case-Shiller Index Continued To Decline In September
Nexstar Media Group and PBF Energy Set to Join S&P MidCap 400; Sabre and Nu Skin Enterprises to Join S&P SmallCap 600
S&P/BMV Fixed Income Indices Consultation on Cash Reinvestments
IHS Markit Benchmark Administration Limited Consultation on Publication Schedule and Constituent Pricing Source Changes to the IHS Markit Global Carbon Index – Results
IHS Markit Benchmark Administration Limited Consultation on the Methodology update for the iBoxx MSCI EUR Senior Corporates Investment Grade ESG Factor Weighted (Version 3) Index – Results
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Addition to the S&P BSE IPO Index
Changes to the S&P BSE Indices
S&P U.S. Preferred Stock Index Family Consultation on the Potential Exclusion of Publicly Traded Partnerships, Limited Partnerships, and Master Limited Partnerships — Results
S&P Core Eurozone 50 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements – Results
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Addition to the S&P BSE IPO Index
IHS Markit Benchmark Administration Limited Consultation on the iBoxx MSCI ESG USD Asia ex-Japan High Yield Capped TCA Index Eligibility Criteria
Addition to the S&P BSE IPO Index
S&P Core Eurozone 50 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements - Updated
S&P France 40 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements - Updated
Additions to the S&P BSE IPO Index
Modification to Methodology of the S&P Kensho Moonshots Index
Modification to the Methodology of the Dow Jones Sector Titans Indices
Reconstitution of S&P BSE Indices
Changes to the S&P BSE Indices
S&P GSCI Dynamic Roll 2023 Contract Eligibility Calendar
S&P Dow Jones Indices Announces 2023 Eligible Contract Months for the S&P GSCI Dynamic Roll
S&P Core Eurozone 50 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements
S&P France 40 Paris-Aligned Transition ESG Index Consultation on Eligibility Requirements
IHS Markit Benchmark Administration Limited Consultation on USD LIBOR Transition for Danish Government Bond Index Hedged into USD and Danish Callable Mortgage Bond Index Hedged into USD
S&P BSE SENSEX Index - Consultation Results
S&P BOCHK China Hong Kong Greater Bay Area Net Zero 2050 Climate Transition Index Consultation on Constraints - Updated
Changes to the S&P BSE Indices
S&P BOCHK China Hong Kong Greater Bay Area Net Zero 2050 Climate Transition Index Consultation on Constraints
S&P/EXPERIAN CONSUMER CREDIT DEFAULT INDICES SHOW COMPOSITE RATE STEADY FOR THE THIRD CONSECUTIVE MONTH IN OCTOBER 2022
Addition to the S&P BSE IPO Index
Addition to the S&P BSE SME IPO Index
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announces 2023 S&P GSCI Weights
S&P Select Industry Indices Consultation on Membership Classification
S&P 500 GARP Index Consultation on Constituent Selection – Results
S&P U.S. Preferred Stock Index Family Consultation on the Potential Exclusion of Publicly Traded Partnerships, Limited Partnerships, and Master Limited Partnerships - Updated
S&P Technology Dividend Aristocrats Index Methodology Update
S&P Global BMI and Dow Jones Global Indices Consultation on Eligibility Criteria
IHS Markit Benchmark Administration Limited Consultation on EMIX World Indices Market Classification
Modification to the Methodology of the S&P UAE BMI Liquid 20/35 Capped Index and S&P UAE Domestic Shariah Liquid 35/20 Capped Index
S&P U.S. Preferred Stock Index Family Consultation on the Potential Exclusion of Publicly Traded Partnerships, Limited Partnerships, and Master Limited Partnerships - Updated
Changes to the S&P BSE Indices
Modification to the Methodology of the S&P Eurozone Bund/SV Climate Transition ESG Select Index
Arch Capital Group Set to Join S&P 500; RXO to Join S&P MidCap 400; Bread Financial Holdings to Join S&P SmallCap 600
Modification to the Methodology of the S&P Paris-Aligned & Climate Transition (PACT) Indices
Modification to the Methodology of the Dow Jones Brookfield Global Infrastructure Net Zero 2050 Climate Transition ESG Index
S&P China 500 Index Consultation on Eligibility Criteria
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P Dow Jones Indices Consultation on S&P 1500 Share Class Eligibility Rules
S&P CoreLogic Case-Shiller Index Continued To Decelerate In August
IHS Markit Benchmark Administration Limited Consultation on the Treatment of Securitized Bonds with an Underlying Term Loan in iBoxx Indices — Results
IHS Markit Benchmark Administration Limited Consultation on the Methodology update for the iBoxx MSCI EUR Senior Corporates Investment Grade ESG Factor Weighted (Version 3) Index
S&P U.S. Preferred Stock Index Family Consultation on the Potential Exclusion of Publicly Traded Partnerships, Limited Partnerships, and Master Limited Partnerships
S&P 500 GARP Index Consultation on Constituent Selection
Changes to the S&P BSE Indices
IHS Markit Benchmark Administration Limited Consultation on Japanese and Korean Dividends Treatment for EMIX (EMICS) and EMIX World Index Families - Results
S&P Dow Jones Indices Consultation on the S&P Developed Ex-Korea LargeMidCap Sustainability Enhanced Indices Diversification 20/35 Constraint Modification — Results
S&P/Experian Consumer Credit Default Indices Show Composite, Auto Loans and First Mortgage Rate Steady in September 2022
Special Trading Session for S&P BSE Indices
Antero Resources Set to Join S&P MidCap 400
Addition to the S&P BSE IPO Index
S&P 500 Net Zero 2050 Paris-Aligned Sustainability Screened Index Consultation on Eligibility Requirements and Constraints
Reconstitution of S&P BSE Indices
Modification to the Methodology of S&P BSE SENSEX Next 50
Westlake Set to Join S&P MidCap 400; MillerKnoll to Join S&P SmallCap 600
S&P GSCI Advisory Panel Meeting: Review of 2023 S&P GSCI Index Rebalancing
Changes to the S&P BSE Indices
S&P/TSX SmallCap Index Consultation on Eligibility Factors
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Consultation on the S&P Developed Ex-Korea LargeMidCap Sustainability Enhanced Indices Diversification 20/35 Constraint Modification
Additions to the S&P BSE SME IPO Index
S&P/BMV Investable Select Sector Indices Constituent Weightings Methodology Update
S&P BSE SENSEX Consultation on Derivative Market Linkage
Targa Resources Set to Join S&P 500; Lantheus Holdings to Join S&P MidCap 400; Payoneer Global to Join S&P SmallCap 600
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $17.7 Billion During Q3 2022; 12-Month Gain as of September 2022 Was $71.5 Billion
S&P Dow Jones Indices 2022 Country Classification Consultation — Results
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Consultation on the Introduction of an Adjustment Factor for Return Based Index Level Calculations in Commodity Indices - Results
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P Dow Jones Indices Launches Net Zero 2050 Paris-Aligned Climate Bond Index
Frontier Communications Set to Join S&P MidCap 400; Hain Celestial Group to Join S&P SmallCap 600
IHS Markit Benchmark Administration Limited Consultation on the iBoxx Asian Local Bond Index — Results
S&P CoreLogic Case-Shiller Index Continued Its Deceleration In July
Addition to the S&P BSE IPO Index
PG&E and EQT Set to Join S&P 500; ExlService to  Join S&P MidCap 400; Others to Join S&P SmallCap  600
IHS Markit Benchmark Administration Limited Consultation on the Treatment of Securitized Bonds with an Underlying Term Loan in iBoxx Indices
S&P U.S., Canada & Mexico Timber & Forestry Index Methodology Update
S&P Composite 1500 Index Consultation on Market Capitalization and Liquidity Eligibility Criteria — Updated
S&P/Experian Consumer Credit Default Indices Show Composite and First Mortgage Rates Steady in August 2022
S&P Composite 1500 Index Consultation on Market Capitalization and Liquidity Eligibility Criteria
Addition to the S&P BSE SME IPO Index
S&P Commodity Producers Agribusiness Index Consultation on Eligibility Factors, Index Construction, and Constituent Weighting — Results
S&P Global Agribusiness Equity Index Consultation on Liquidity Threshold, Index Construction, Constituent Weightings, and Rebalancing Schedule — Results
S&P Global Infrastructure Index Consultation — Results
Additions to the S&P BSE Indices
2021 Annual Survey of Indexed Assets
IHS Markit Benchmark Administration Limited Consultation on Japanese and Korean Dividends Treatment for EMIX (EMICS) and EMIX World Index Families
S&P Global Clean Energy Index Eligible RBICS Methodology Update - Updated
Addition to the S&P BSE SME IPO Index
S&P Global E-Commerce Ecosystem Index Eligible RBICS Methodology Update
Catalyst Pharmaceuticals Set to Join S&P SmallCap  600
S&P Global Clean Energy Index Eligible RBICS Methodology Update
S&P US & China Electric Vehicle Index Eligible RBICS Methodology Update
S&P Dow Jones Indices Announces Rebalancing Results for the S&P MERVAL Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P Colombia Select Index
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC CompMx Trailing Income Equities ESG Tilted Index
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV China SX20 Index
Reconstitution of S&P BSE Indices
S&P Global Water Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule — Results
S&P Dow Jones Indices and S&P Global Sustainable1 Launch S&P Net Zero 2050 Carbon Budget Index Series
Addition to the S&P BSE SME IPO Index
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P IPSA Index
S&P Global Timber and Forestry Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule — Results (Updated)
IHS Markit Benchmark Administration Limited Consultation on Publication Schedule and Constituent Pricing Source Changes to the IHS Markit Global Carbon Index
Addition to the S&P BSE IPO Index
Addition to the S&P BSE SME IPO Index
AMENDED: S&P Dow Jones Indices Announces September 2022 Quarterly Rebalance of the S&P/NZX Indices
SP BVL Peru Select September 2022 Rebalance Announcement
S&P Global Timber and Forestry Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule — Results
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index and S&P/TSX 60 Index
CoStar Group, Invitation Homes Set to Join S&P 500; Others to Join S&P 100, S&P MidCap 400, and S&P SmallCap 600
iBoxx EUR Corporates Senior 1-10 (EU CA CH NO US) Index Relaunch
S&P Dow Jones Indices Announces September 2022 Quarterly Rebalance of the S&P Europe 350 Indices
S&P Dow Jones Indices Treatment for Sri Lanka, Russia, Lebanon, Argentina and Nigeria
Reconstitution of S&P BSE Indices
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces September 2022 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces September 2022 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces September 2022 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P Global Infrastructure Index Consultation - Extended
IHS Markit Benchmark Administration Limited Consultation on Transaction Costs Adjustment Inclusion for Certain iBoxx MSCI ESG Custom Indices - Results (Updated)
IHS Markit Benchmark Administration Limited Consultation on Transaction Costs Adjustment Inclusion for Certain iBoxx MSCI ESG Custom Indices - Results
S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks (2022)
S&P CoreLogic Case-Shiller Index Decelerated In June
S&P Dow Jones Indices Announces Replacement  Addition for the S&P/BMV China SX20 Index
Avid Technology Set to Join S&P SmallCap 600
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
IHS Markit Benchmark Administration Limited Consultation on the iBoxx Asian Local Bond Index
Changes to the S&P BSE Indices
Addition to the S&P BSE IPO Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P France 40 Paris-Aligned Transition ESG Index Methodology Update
Modification to the Methodology of the S&P 900 Dividend Revenue-Weighted Index
S&P Dow Jones Indices and Bolsas y Mercados Argentinos (BYMA) Expand S&P/BYMA Index Family with Two New CEDEAR Indices
Notice: S&P Dow Jones Announces Changes to the S&P/BMV China SX20 Index
Notice: S&P Dow Jones Announces Changes to the S&P/BVL Indices
S&P Global Infrastructure Index Consultation
S&P Global Water Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule - Updated
S&P Commodity Producers Agribusiness Index Consultation on Eligibility Factors, Index Construction, and Constituent Weighting - Updated
Modification to Methodology of the S&P/CLX INTER
S&P/Experian Consumer Credit Default Indices Show Eighth Consecutive Rise in Composite Rate in July 2022
Changes to the S&P BSE Indices
Modification to the Methodology of the S&P ESG Leaders Indices
Modification to the Methodology of the S&P Carbon Control Index Series
MACOM Technology Solutions Holdings Set to Join  S&P MidCap 400
Reconstitution of S&P BSE Indices
S&P Africa Hard Currency Sovereign Bond Select Index Consultation
IHS Markit Benchmark Administration Limited Consultation on Transaction Costs Adjustment Inclusion for Certain iBoxx MSCI ESG Custom Indices – Updated
Celsius Holdings Set to Join S&P MidCap 400; Clearfield to Join S&P SmallCap 600
S&P Quality Indices Consultation – Results (Updated)
S&P Dow Jones Indices Launches S&P GSCI Freight Indices Tracking Dry Bulk Sector
S&P Quality Indices Consultation – Results
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
IHS Markit Benchmark Administration Limited Consultation on Transaction Costs Adjustment Inclusion for Certain iBoxx MSCI ESG Custom Indices
S&P Global Agribusiness Equity Index Consultation on Liquidity Threshold, Index Construction, Constituent Weightings, and Rebalancing Schedule
AdaptHealth Set to Join S&P SmallCap 600
S&P Commodity Producers Agribusiness Index Consultation on Eligibility Factors, Index Construction, and Constituent Weighting
S&P Global Water Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule
S&P Global Timber and Forestry Index Consultation on Eligibility Factors, Index Construction, Constituent Weighting, and Rebalancing Schedule
Modification to the Methodology of the S&P Access Hong Kong Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P CoreLogic Case-Shiller Index Reports Annual Home Price Gain Of 19.7% In May
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P Dow Jones Indices Consultation on the Treatment of Spin-offs with Long Lead Times and Uncertain Valuations – Results
S&P Colombia Select Index Consultation on Constituent Selection and Weighting – Results
Treatment of Iluka Resources Limited Demerger  within the S&P/ASX 200 Index
MP Materials Set to Join S&P MidCap 400
Novanta Set to Join S&P MidCap 400; Six Flags Entertainment to Join S&P SmallCap 600
S&P/Experian Consumer Credit Default Indices Show Seventh Consecutive Rise in Composite Rate in June 2022
Sunstone Hotel Investors Set to Join S&P SmallCap 600
Addition to the S&P BSE SME IPO Index
Uniti Group Limited to be removed from the  S&P/ASX 200 Index
Healthcare Trust of America & Coca-Cola Consolidated Set to Join S&P MidCap 400; Green Brick Partners to Join S&P SmallCap 600
Additions to the S&P BSE SME IPO Index
S&P Merger Arbitrage Indices Consultation on the Cash Component Buffer – Results
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
Addition to the S&P BSE SME IPO Index
BOCHK and S&P Dow Jones Indices Launches the First Climate Transition Index Targeting the Greater Bay Area
Addition to the S&P BSE SME IPO Index
Addition to the S&P BSE SME IPO Index
Modification to the Methodology of the Dow Jones Asia ESG Select Dividend 30 Index
S&P DOW JONES INDICES AND MSCI ANNOUNCE SELECT LIST OF COMPANIES IMPACTED BY REVISIONS TO THE GLOBAL INDUSTRY CLASSIFICATION STANDARD (GICS®) STRUCTURE IN 2023
S&P Quality Indices Consultation – Updated
Omnicell, Southwestern Energy and Ormat Technologies Set to Join S&P MidCap 400; Others to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite and S&P/TSX Canadian Dividend Aristocrats Indices
S&P Dow Jones Indices Country Classification 2023 Watchlist
S&P CoreLogic Case-Shiller Index Reports Annual Home Price Gain of 20.4%
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Portland General Electric Set to Join S&P MidCap 400; Digital Turbine to Join S&P SmallCap 600
S&P Dow Jones Indices’ 2022 Country Classification Consultation
Changes to the S&P BSE Indices
S&P Quality Indices Consultation
S&P/Experian Consumer Credit Default Indices Show Sixth Consecutive Rise in Composite Rate in May 2022
S&P Colombia Select Index Consultation on Eligibility Criteria and Index Construction – Results
S&P Colombia Select Index Consultation on Constituent Selection and Weighting
S&P Merger Arbitrage Indices Consultation on the Cash Component Buffer
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Country Classification Methodology Consultation – Results
S&P 500 Buybacks Set Quarterly and 12-Month Records - Again
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
Crown Resorts Limited to be removed from the S&P/ASX 200 Index
Modification to Methodology of the Dow Jones Sustainability Indices
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV IPC CompMx Trailing Income Equities ESG Tilted Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV FIBRAS Index
National Vision Holdings Set to Join S&P SmallCap  600
S&P Colombia Select Index Consultation on Eligibility Criteria and Index Construction – Update
S&P Paris-Aligned & Climate Transition (PACT) Transition Pathway Select Indices Consultation on Physical Risk Eligibility Requirements – Results
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Keurig Dr Pepper, VICI Properties and ON Semiconductor Set to Join S&P 500; Others to Join S&P MidCap 400, and S&P SmallCap 600
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces June 2022 Quarterly Rebalance of the S&P Europe 350 Indices
Notice: S&P Dow Jones Indices Treatment for Sri Lanka, Russia, Lebanon, Argentina and Nigeria
Reconstitution of S&P BSE Indices
Addition to the S&P BSE IPO Index
S&P Dow Jones Indices Announces June 2022 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces June 2022 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces June 2022 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices’ Consultation on the Removal of Emerging Markets from Eurozone Indices – Results
Dow Jones Select Real Estate Securities Indices Consultation on the Eligibility of Certain Data Center REIT Revenue Segments – Results
Addition to the S&P BSE IPO Index
S&P CoreLogic Case-Shiller Index Reports Annual Home Price Gain Of 20.6% In March
S&P Dow Jones Indices and ASX Launch S&P/ASX Agribusiness Index to Track Australia’s Agribusiness Sector
Addition to the S&P BSE IPO Index
Addition to the S&P BSE IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P Paris-Aligned & Climate Transition (PACT) Transition Pathway Select Indices Consultation on Physical Risk Eligibility Requirements
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Additions to the S&P BSE IPO Index
S&P Colombia Select Index Consultation on Eligibility Criteria and Index Construction
Addition to the S&P BSE IPO Index
Reconstitution of S&P BSE Indices
Modification to the Methodology of S&P BSE Enhanced Value and S&P BSE Quality Indices
S&P BSE 100 ESG Index - Consultation Results
Update Regarding Crown Resorts Limited in the S&P/ASX 200 Index
S&P Dow Jones Indices’ Consultation on the Removal of Emerging Markets from Eurozone Indices – Extended
Crown Resorts Limited to be removed from the S&P/ASX 200 Index
Modification to Methodology of the S&P Europe 350 Index Family
S&P/Experian Consumer Credit Default Indices Show Fifth Straight Increase in Composite Rate in April 2022
Addition to the S&P BSE IPO Index
Modification to the Methodology of S&P BSE Indices
Treatment of Tabcorp Holdings Limited  Demerger within the S&P/ASX 200 Index
Modification to Methodology of the S&P Euro 50 Equal Weight Index
Reconstitution of S&P BSE Indices
Independence Realty Trust Set to Join S&P MidCap  400; Alpha and Omega Semiconductor & Dynavax  Technologies to Join S&P SmallCap 600
Changes to the S&P BSE Indices
Modification to Methodology of the S&P Japan Shariah Top 20 Index
Addition to the S&P BSE IPO Index
Addition to the S&P BSE IPO Index
Additions to the S&P BSE SME IPO Index
Additions to the S&P BSE SME IPO Index
Inari Medical Set to Join S&P MidCap 400; Tri Pointe Homes to Join S&P SmallCap 600
S&P Dow Jones Indices’ Consultation on the Removal of Emerging Markets from Eurozone Indices
Modification to the Methodology of the S&P Select Frontier and S&P Extended Frontier 150 Indices – Updated
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Dow Jones Select Real Estate Securities Indices Consultation on the Eligibility of Certain Data Center REIT Revenue Segments
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Increased To 19.8% In February
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Z Energy Limited to be removed from the S&P/NZX  Indices
S&P Dow Jones Indices Announces April 2022 Rebalance of the S&P 500 ESG Index
S&P Dow Jones Indices Announces April 2022 Rebalance of the S&P Europe 350 ESG Index
A10 Networks Set to Join S&P SmallCap 600
S&P/Experian Consumer Credit Default Indices Show Fourth Straight Increase in Composite Rate in March 2022
S&P BSE 100 ESG Index Consultation on Eligibility Requirements
S&P Global Resources Select Equal Weighted Index Consultation on Index Eligibility and Target Constituent Count – Results
Additions to the S&P BSE Indices
Modification to the Methodology of S&P BSE SmallCap Select Index
Modification to the Methodology of the S&P Select Frontier and S&P Extended Frontier 150 Indices
Additions to the S&P BSE SME IPO Index
Addition to the S&P BSE IPO Index
Reconstitution of S&P BSE Indices
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
S&P Dow Jones Indices Announces Treatment of AT&T Transaction with Discovery
CIMIC Group Limited to be removed from the S&P/ASX 200 Index
Gogo Set to Join S&P SmallCap 600
Changes to the S&P BSE Indices
Arcus Biosciences Set to Join S&P SmallCap 600
S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $18.2 Billion in Q1 2022; 12-Month Gain was $70.1 Billion
S&P IPSA ESG Tilted Index Consultation on Eligibility Requirements – Results
S&P/B3 Brazil ESG Index Consultation on Eligibility Requirements – Results
S&P 500 ESG Elite Index Consultation on Eligibility Requirements – Results
S&P ESG Dividend Aristocrats Indices and Dow Jones Asia ESG Select Dividend 30 Index Consultation on Eligibility Requirements – Results
S&P/TSX ESG Indices Consultation on Eligibility Requirements – Results
S&P/BMV ESG Indices Consultation on Eligibility Requirements – Results
S&P Eurozone 50 ESG Select Equal Weight Index and S&P Transatlantic 100 ESG Select Equal Weight Index Consultation on Eligibility Requirements – Results
S&P ESG Index Series, S&P ESG Tilted Index Series, S&P Equal Weight ESG Leaders Select Indices, and S&P Gender Equality & Inclusion Equal Weight Indices Consultation on Eligibility Requirements – Results
S&P DOW JONES INDICES AND MSCI ANNOUNCE REVISIONS TO THE GLOBAL INDUSTRY CLASSIFICATION STANDARD (GICS®) STRUCTURE IN 2023
REVISIONS TO THE GLOBAL INDUSTRY CLASSIFICATION STANDARD (GICS®) STRUCTURE EFFECTIVE MARCH, 2023
ESAB Set to Join S&P MidCap 400; PROG Holdings to Join S&P SmallCap 600
UPDATE: S&P Dow Jones Indices’ Consultation on Sanctions and Russia Market Accessibility for Fixed Income Indices – Results
S&P Dow Jones Indices Launches Index Tracking Commodities Used In Electric Vehicle Production
Additions to the S&P BSE SME IPO Index
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P 500 Dividend Aristocrats Index
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Camden Property Trust Set to Join S&P 500; Matador Resources to Join S&P MidCap 400; Vir Biotechnology to Join S&P SmallCap 600
S&P/JPX Carbon Efficient Index and S&P Global Ex-Japan LargeMidCap Carbon Efficient Index Announcement on Task Force on Climate-Related Financial Disclosures Reporting Integration
S&P CoreLogic Case-Shiller Index Reports 19.2% Annual Home Price Gain To Start 2022
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Japan Exchange Group and S&P Dow Jones Indices Launch S&P/JPX 500 ESG Score Tilted Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P 500 Dividend Aristocrats Index
Chart Industries Set to Join S&P MidCap 400; Sonos & Embecta to Join S&P SmallCap 600
Update: S&P Dow Jones Indices Announcement Regarding Russia Standalone Indices and Sanctions
Addition to the S&P BSE SME IPO Index
Update: Postponement SP Colombia Select Rebalance
S&P Managed Risk 2.0 Index Series Consultation on Target Volatility and Final Asset Weights – Results
Fidelity Quality Income and Value Income Indices Consultation on Additional Business Activity Exclusions and the Monthly Rebalancing – Results
Notice: S&P Dow Jones Indices Announces Rebalancing Postponement for the S&P Colombia Select Index
S&P Dow Jones Indices’ Consultation on Sanctions and Russia Market Accessibility for Fixed Income Indices – Results
S&P/Experian Consumer Credit Default Indices Show Third Straight Increase in Composite Rate in February 2022
Modification to the Methodology of the S&P Target Date Index Series
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV China SX20
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P Colombia Select Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P MERVAL Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV Dividend Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BVL Peru Select Index
Results of the S&P/TSX Venture Composite Index Consultation on Constituent Weighting and Minimum Size Threshold
Academy Sports and Outdoors Set to Join S&P SmallCap 600
Notice: Rebalance Results Announced for the Dow Jones U.S. Select Dividend Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P IPSA Index
S&P Dow Jones Indices Country Classification Methodology Consultation – Extended
Reconstitution of S&P BSE Indices
Treatment of Nickel in S&P Dow Jones Commodity Indices
S&P Dow Jones Indices’ Consultation on Sanctions and Russia Market Accessibility for Fixed Income Indices
Fidelity Emerging Markets Quality Income Index Consultation on Sanctions and Russia Market Accessibility – Results
S&P Dow Jones Indices Consultation on the Treatment of Spin-offs with Long Lead Times and Uncertain Valuations
Fidelity Emerging Markets Quality Income Index Consultation on Sanctions and Russia Market Accessibility – Updated
Fidelity Emerging Markets Quality Income Index Consultation on Sanctions and Russia Market Accessibility
S&P Dow Jones Indices Treatment for Lebanon, Argentina and Nigeria
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index and S&P/TSX 60 Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
Charles Schwab Set to Join S&P 100; BellRing Brands to Join S&P MidCap 400; Cerence to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Update to S&P Composite 1500 Market Cap Guidelines
S&P Dow Jones Indices’ Consultation on Sanctions and Russia Market Accessibility – Results
S&P Dow Jones Indices Announces March 2022 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces March 2022 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces March 2022 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces March 2022 Quarterly Rebalance of the S&P/NZX Indices
S&P 500 Members Continue to Increase Job Listings in  2022 Lead by Utility, Energy, and Financial Companies
S&P South Africa Composite Capped Indices Consultation on Constituent Weighting – Results
S&P Dow Jones Indices’ Consultation on Sanctions and Russia Market Accessibility
S&P Dow Jones Indices Announcement Regarding Russia-Related Sanctions
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P/TSX ESG Indices Consultation on Eligibility Requirements
S&P/B3 Brazil ESG Index Consultation on Eligibility Requirements
S&P IPSA ESG Tilted Index Consultation on Eligibility Requirements
S&P/BMV ESG Indices Consultation on Eligibility Requirements
S&P 500 ESG Elite Index Consultation on Eligibility Requirements
S&P Eurozone 50 ESG Select Equal Weight Index and S&P Transatlantic 100 ESG Select Equal Weight Index Consultation on Eligibility Requirements
S&P ESG Dividend Aristocrats Indices and Dow Jones Asia ESG Select Dividend 30 Index Consultation on Eligibility Requirements
S&P ESG Index Series, S&P ESG Tilted Index Series, S&P Equal Weight ESG Leaders Select Indices, and S&P Gender Equality & Inclusion Equal Weight Indices Consultation on Eligibility Requirements
Molina Healthcare Set to Join S&P 500; Range Resources to Join S&P MidCap 400; Golden Entertainment to Join S&P SmallCap 600
S&P Dow Jones Indices Announcement Regarding Russia-Related Sanctions
S&P Paris-Aligned & Climate Transition (PACT) Indices Consultation on Eligibility Requirements and Constraints – Results
Fidelity Quality Income and Value Income Indices Consultation on Additional Business Activity Exclusions and the Monthly Rebalancing
S&P Dow Jones Indices Announcement Regarding Russia-Related Sanctions
S&P Managed Risk 2.0 Index Series Consultation on Target Volatility and Final Asset Weights – Updated
S&P BSE AllCap and Sector Indices Consultation – Clarification
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
ZimVie to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P Dow Jones Indices updates in the Annual Assessment of Solvency II Eligibility – Update
S&P Global Resources Select Equal Weighted Index Consultation on Index Eligibility and Target Constituent Count
S&P CoreLogic Case-Shiller Index Reports 18.8% Annual Home Price Gain For Calendar 2021
S&P UK and Euro High Yield Dividend Aristocrats Indices Consultation on the Treatment of Monthly Dividend Review Replacements – Results
S&P IPSA Consultation on Selection Universe – Results
Additions to the S&P BSE Indices
Old National Bancorp Set to Join S&P MidCap 400; Urban Edge Properties & Corsair Gaming to Join S&P SmallCap 600
S&P/Experian Consumer Credit Default Indices Show Second Straight Increase in Composite Rate in January 2022
Reconstitution of S&P BSE Indices
Nordson Set to Join S&P 500; PDC Energy to Join S&P MidCap 400; XPEL to Join S&P SmallCap 600
Additions to the S&P BSE SME IPO Index
S&P South Africa Composite Capped Indices Consultation on Constituent Weighting
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite and S&P/TSX 60 Indices
Modification to the Methodology of the S&P U.S. Indices
Job Listings at S&P 500 Companies up 1.8% in January 2022 According to S&P 500 LinkUp Jobs Index
Sydney Airport to be removed from the S&P/ASX 200  Index
Modification to the Methodology of Certain S&P Custom Slice & Dice Indices
Addition to the S&P BSE SME IPO Index
AusNet Services Limited to be removed from the  S&P/ASX 200 Index
S&P Dow Jones Indices and the Lima Stock Exchange Launch the S&P/BVL Ingenius Index Bringing Global Innovation to the Peruvian Markets
S&P BSE AllCap and Sector Indices Consultation – Results
Addition to the S&P BSE IPO Index
S&P/TSX Venture Composite Index Consultation on Constituent Weighting and Minimum Size Threshold
S&P Paris-Aligned & Climate Transition (PACT) Indices Consultation on Eligibility Requirements and Constraints
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Constellation Energy Set to Join S&P 500; Others to  Join S&P MidCap 400 and S&P SmallCap 600
Exelon to remain in Dow Jones Utility Average after Spin-off Transaction
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P Dow Jones Indices and the Santiago Exchange Launch the S&P/CLX Ingenius Index Bringing Global Innovation to the Chilean Markets
S&P CoreLogic Case-Shiller Index Reports 18.8% Annual Home Price Gain In November
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Notice: Rebalancing Results Announced for the S&P 500 Dividend Aristocrats Index
Notice: Rebalancing Results Announced for the S&P High Yield Dividend Aristocrats Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Dividend Aristocrats Index
SELECT LIST OF COMPANIES THAT MAY BE IMPACTED BY PROPOSED CONSULTATION ON GICS® STRUCTURE CHANGES IN S&P DJI INDICES
S&P DOW JONES INDICES AND MSCI ANNOUNCE SELECT LIST OF COMPANIES THAT MAY BE IMPACTED BY PROPOSED CONSULTATION ON GICS® STRUCTURE CHANGES
HSBC Pan Arab MultiFactor Index Series Consultation on Index Business Days – Results
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
Update on S&P Dow Jones Indices Announcement of Additional Removals due to Sanctions for Equity Indices
Update on S&P Dow Jones Indices Announcement of Additional Removals due to Sanctions for Equity Indices
S&P UK and Euro High Yield Dividend Aristocrats Indices Consultation on the Treatment of Monthly Dividend Review Replacements
S&P/Experian Consumer Credit Default Indices Show Higher Rates For All Loan Types in December 2021
S&P IPSA Consultation on Selection Universe
S&P Dow Jones Indices Country Classification Methodology Consultation
Reconstitution of S&P BSE Indices
Afterpay Limited to be removed from the S&P/ASX  200 Index
Index Reconstitution Calendar 2022
Addition to the S&P BSE SME IPO Index
Modification to the Methodology of the S&P Dividend Opportunities Indices
S&P/ASX Indices Consultation on the Implementation of BHP’s Potential Unification – Results
S&P Dow Jones Indices Announces Changes to the S&P IPSA and other S&P/CLX Indices
S&P Managed Risk 2.0 Index Series Consultation on Target Volatility and Final Asset Weights
Changes to the S&P BSE Indices
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announces Change in  Dividend Withholding Tax Rate
Changes to the S&P BSE Indices
Changes to the S&P BSE Indices
S&P Dow Jones Indices Reports U.S. Indicated Dividend Payments Increased $18.0 Billion in Q4 2021and a Record $69.8 Billion in 2021
iTeos Therapeutics Set to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Changes in Dividend Withholding Tax Rates
Additions to the S&P BSE Indices
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Calix Set to Join S&P MidCap 400; Douglas Elliman to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Reports 19.1% Annual Home Price Gain In October
Addition to the S&P BSE IPO Index
Addition to the S&P BSE IPO Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Addition to the S&P BSE IPO Index
Update: S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
HSBC Long-Short Factor Index Series and HSBC Vantage5 Index Series Consultation on Potential Replacement Rates for USD and EUR London Interbank Offered Rates – Results
HSBC Pan Arab MultiFactor Index Series Consultation on Index Business Days – Updated
Addition to the S&P BSE IPO Index
Voya Financial Set to Join S&P MidCap 400
S&P 500 Buybacks Set A Record High
S&P/Experian Consumer Credit Default Indices Show Lower Bank Card and Composite Rates in November 2021
Addition to the S&P BSE IPO Index
Modification to the Methodology of the S&P South Africa Preference Share Index
Addition to the S&P BSE IPO Index
S&P Dow Jones Indices Announces a Delay in the Annual Assessment of Solvency II Eligibility
Addition to the S&P BSE IPO Index
S&P/ASX Indices Consultation on the Implementation of BHP’s Potential Unification – Updated
Modification to the Methodology of the Dow Jones Sustainability MILA Pacific Alliance Index
Addition to the S&P BSE IPO Index
Alcoa Set to Join S&P MidCap 400
S&P Dow Jones Indices Announces 2022 Weights for the Dow Jones Commodity Index
Addition to the S&P BSE IPO Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV FIBRAS Index
HSBC Pan Arab MultiFactor Index Series Consultation on Index Business Days
Reconstitution of S&P BSE Indices
Addition to the S&P BSE IPO Index
S&P Dow Jones Indices Treatment for Lebanon, Argentina and Nigeria
Treatment of Chalice Mining Limited Demerger within the S&P/ASX 200 Index
Old Dominion Freight Line Set to Join Dow Jones  Transportation Average
EPAM Systems Set to Join S&P 500
Addition to the S&P BSE SME IPO Index
Oil Search Limited to be removed from the S&P/ASX 200 Index
HSBC Long-Short Factor Index Series and HSBC Vantage5 Index Series Consultation on Potential Replacement Rates for USD and EUR London Interbank Offered Rates
Signature Bank, SolarEdge Technologies and FactSet  Research Systems Set to Join S&P 500; Others to  Join S&P MidCap 400 and S&P SmallCap 600
Clarifications to S&P Dow Jones Indices’ Index Mathematics Methodology
Modification to the Methodology of Certain S&P BMI Indices
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Modification to Methodology of the S&P Global SmallCap Select Index Series
S&P Dow Jones Indices Announces December 2021 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P BSE AllCap and Sector Indices Consultation on Constituent Selection and Weighting Scheme
S&P Dow Jones Indices Announces December 2021 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces December 2021 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces December 2021 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for USD London Interbank Offered Rates – Results
S&P/CSE Sector and Industry Group Indices Consultation on Constituent Weighting Scheme – Results
S&P Japanese Indices Consultation on the Constituent Selection Buffer Rules – Results
S&P CoreLogic Case-Shiller Index Reports 19.5% Annual Home Price Gain In September
Addition to the S&P BSE IPO Index
Consultation on Potential Changes to the Global Industry Classification Standard (GICS®) Structure in 2022 Indices – Updated
S&P DJI and MSCI Announce Extension of the Feedback Period for the Consultation on Potential Changes to GICS
Addition to the S&P BSE SME IPO Index
Addition to the S&P BSE IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
S&P/ASX All Technology Index Consultation Results
S&P Risk Premia Rates Indices Consultation on Rate Replacements – Results
Bruker BioSciences Set to Join S&P MidCap 400; Others to Join S&P SmallCap 600
Spark Infrastructure Group to be removed from the  S&P/ASX 200 Index
S&P Dynamic Currency Hedged Indices Consultation – Results
Addition to the S&P BSE IPO Index
SiTime Set to Join S&P MidCap 400; Emergent  BioSolutions to Join S&P SmallCap 600
Modification to the Methodology of the S&P Low Carbon Low Volatility High Dividend Indices
Modification to the Methodology of the S&P ESG-Momentum Equal Weight Indices
S&P Dow Jones Indices Launches Net Zero 2050 Climate Transition and Paris-Aligned Select Indices
Modification to the Methodology of the S&P/BMV Ingenius Index
S&P Dow Jones Indices Announces 2022 Eligible Contract Months for the S&P GSCI Dynamic Roll
S&P GSCI Dynamic Roll 2022 Contract Eligibility Calendar
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for USD London Interbank Offered Rates – Updated
What Does "Everyone" Think? S&P Dow Jones Indices Introduces S&P 500 Twitter Sentiment Index
Reconstitution of S&P BSE Indices
Additions to the S&P BSE IPO Index
Thryv Holdings Set to Join S&P SmallCap 600
Modification to the Methodology of the Dow Jones Sustainability Europe Diversified High Beta High Dividend Index
S&P/CSE Sector and Industry Group Indices Consultation on Constituent Weighting Scheme
S&P Dow Jones Indices Launches ESG Version of the S&P 500 Equal Weight Index
S&P/ASX Indices Consultation on the Implementation of BHP’s Potential Unification
S&P/Experian Consumer Credit Default Indices Show Lower Bank Card and Composite Rates in October 2021
Addition to the S&P BSE SME IPO Index
S&P Risk Premia Rates Indices Consultation on Rate Replacements
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for USD London Interbank Offered Rates
Additions to the S&P BSE IPO Index
Modification to the Methodology of the S&P 500 (4 PM CET Level) (USD) TR
S&P Dow Jones Indices Announces Dow Jones Sustainability Indices 2021 Review Results
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announces 2022 S&P GSCI Weights
S&P Dow Jones Indices Consultation on the Introduction of an Adjustment Factor for Return Based Index Level Calculations in Commodity Indices – Updated
Changes to the S&P BSE Indices
Orion Office REIT Set to Join S&P SmallCap 600
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P 500 Dividend Aristocrats Index
S&P Dow Jones Indices and the Lima Stock Exchange Launch the S&P/BVL Peru General ESG Index
Modification to the Methodology of the S&P Asia 50
S&P Dow Jones Indices Consultation on the Introduction of an Adjustment Factor for Return Based Index Level Calculations in Commodity Indices
Modification to the Rebalancing Reference Date for Certain S&P Asia Pacific Indices
Loyalty Ventures Set to Join S&P SmallCap 600
S&P/ASX All Technology Index Consultation
S&P Japanese Indices Consultation on the Constituent Selection Buffer Rules
Job Listings at S&P 500 Companies up 55% in 2021  According to S&P 500 LinkUp Jobs Index
IBM to remain in Dow Jones Industrial Average after Spin-off Transaction
Kyndryl Holdings Set to Join S&P MidCap 400; NetScout Systems to Join S&P SmallCap 600
S&P Dynamic Currency Hedged Indices Consultation
Results of the S&P/BMV Sovereign BONDESD Bond Index Family Consultation on Eligibility
Reminder: S&P Dow Jones Indices’ Replacement Rates for Key London Interbank Offered Rates
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Annual Home Price Gains Remained High In August According To S&P CoreLogic Case-Shiller Index
Special Trading Session for S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Avid Bioservices Set to Join S&P SmallCap 600
S&P GSCI Advisory Panel Meeting: Review of 2022 S&P GSCI Index Rebalancing
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
S&P/Experian Consumer Credit Default Indices Show Composite Rate Stable in September 2021
S&P DJI and MSCI Announce Consultation on Potential Changes to GICS
Consultation on Potential Changes to the Global Industry Classification Standard (GICS®) Structure in 2022
Kite Realty Group Trust Set to Join S&P MidCap 400; Harmony Biosciences Holdings & LendingTree to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Modification to the Methodology of the S&P Environmental & Socially Responsible Indices
Additions to the S&P BSE SME IPO Index
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for Key London Interbank Offered Rates – Results
Addition to the S&P BSE SME IPO Index
Additions to the S&P BSE indices
Modification to the Methodology of the S&P BMI North American Natural Resources Indices
Results of the Ossiam Emerging Markets Minimum Variance Index Series Consultation on Changes to the Methodology
Reconstitution of S&P BSE Indices
Results of the Dow Jones Sustainability Indices Consultation on Index Membership Review Process
Consensus Cloud Solutions Set to Join S&P SmallCap 600
S&P Dow Jones Indices Reports U.S. Indicated  Dividend Payments Increased $20.9 Billion in Q3 2021, Best Gain Since Q1 2012
Modification to the Methodology of the S&P 500 UK  Tax NTR GBP Index
Addition to the S&P BSE IPO Index
SunPower Set to Join S&P MidCap 400
OptimizeRx Set to Join S&P SmallCap 600
Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Sylvamo Set to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Reports Record High 19.7% Annual Home Price Gain In July
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Additions to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Addition to the S&P BSE IPO Index
Q2 2021 S&P 500 Buybacks Approach Record Highs
S&P Dow Jones Indices Introduces S&P Multi-Asset Dynamic Inflation Strategy Index
S&P Global Clean Energy Index Consultation on Index Universe Expansion, Weighting Scheme Changes, and Incorporation of Exclusion Criteria Results
S&P Global Clean Energy Select Index Consultation on Index Universe Expansion and Incorporation of Exclusion Criteria Results
S&P Dow Jones Indices Announces changes to the S&P Europe 350 Indices
S&P/Experian Consumer Credit Default Indices Show Fifth Straight Drop in Composite Rate in August 2021
S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite and S&P/TSX 60 Indices
Additions to the S&P BSE IPO Index
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BVL Peru Select  Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P Colombia Select Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV China SX20
Notice: S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P IPSA Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P MERVAL Index
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
S&P Dow Jones Indices’ 2021 Country Classification Consultation Results
Modification to the Rebalancing Reference Date for Certain S&P/NZX Indices
Modification to the Methodology of the S&P Global Carbon Efficient Index Series
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P IPSA Index
Match Group, Ceridian HCM and Brown & Brown Set to Join S&P 500; Others to Join S&P MidCap 400 and S&P SmallCap 600
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BVL Peru Select Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P Latin America 40 Index
S&P Dow Jones Indices Announces September 2021 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces September 2021 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces September 2021 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces September 2021 Quarterly Rebalance of the S&P/NZX Indices
Dow Jones Select Green Real Estate Securities Indices Consultation on Business Activity Exclusions Results
Modification to the Rebalancing Reference Date for Certain S&P/ASX Indices
Addition to the S&P BSE SME IPO Index
Modification to the Pro-forma Period of the S&P/TSX 60 Fossil Fuel Free Index
Modification to the Rebalancing Reference Date for Certain S&P Dow Jones Custom Slice & Dice Indices
S&P/BMV Sovereign BONDESD Bond Index Family Consultation on Eligibility
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gain Topped 18.6% In June
Consultation on the Construction of the S&P Global BMI Size Benchmark Indices Results
Performance Food Group & Digital Turbine Set to Join S&P MidCap 400; TreeHouse Foods & Ligand Pharmaceuticals to Join S&P SmallCap 600
S&P Dow Jones Indices’ Float Adjustment Methodology Clarification
Monthly Rebalancing Announced for the S&P/NZX New ZEALAND Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX  Australian Fixed Interest Index Series
Changes to the S&P BSE Indices
Bio-Techne Set to Join S&P 500; Saia, Mimecast & Option Care Health to Join S&P MidCap 400; Others to Join S&P SmallCap 600
Modification to the Methodology of the S&P ESG Exclusion Indices and S&P Sustainability Screened Indices
Additions to the S&P BSE IPO Index
Addition to the S&P BSE IPO Index
Results of the Consultation on the Eligibility of STAR Market Listings in S&P Dow Jones Indices' Global Benchmarks
S&P Global Clean Energy Index Consultation on Index Universe Expansion, Weighting Scheme Changes, and Incorporation of Exclusion Criteria
S&P Global Clean Energy Select Index Consultation on Index Universe Expansion and Incorporation of Exclusion Criteria
Addition to the S&P BSE IPO Index
Modification to the Methodology of the S&P/BMV INMEX
Ossiam Emerging Markets Minimum Variance Index Series Consultation on Changes to the Methodology
S&P/Experian Consumer Credit Default Indices Show Fourth Straight Drop in Composite Rate in July 2021
Modifications to the S&P China Convertible Bond Index
Additions to the S&P BSE IPO Index
Reconstitution of S&P BSE Indices
Dow Jones Sustainability Indices Consultation on Index Membership Review Process
Additions to S&P BSE IPO Indices
S&P Dow Jones Indices Consultation on the Quarterly Rebalancing Process – Results
Modification to the Methodologies of the S&P/TSX Indices
Consultation on the Eligibility of STAR Market Listings in S&P Dow Jones Indices' Global Benchmarks – Updated
Addition to the S&P BSE IPO Index
Consultation on the Eligibility of STAR Market Listings in S&P Dow Jones Indices' Global Benchmarks
Modification to the Methodology of the Dow Jones Islamic Market China A 100 Index
S&P Dow Jones Indices Country Classification Update on the 2020 Watchlist and Argentina
S&P Dow Jones Indices’ 2021 Country Classification Consultation
Modification to the Methodologies of the S&P BSE Factor Indices and S&P BSE 100 ESG Index
Addition to the S&P BSE IPO Index
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for Key London Interbank Offered Rates – Updated
Monthly Rebalancing Announced for the S&P/NZX New ZEALAND Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX  Australian Fixed Interest Index Series
GXO Logistics, Victoria's Secret & GameStop Set to Join S&P MidCap 400
Dow Jones Select Green Real Estate Securities Indices Consultation on Business Activity Exclusions
S&P CoreLogic Case-Shiller Index Reports Record High Annual Home Price Gain Of 16.6% In May
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Dow Jones Israel Select Sector Indices and S&P/Harel Sector Indices Consultation on the Treatment of Suspended Stocks – Results
Addition to the S&P BSE IPO Index
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite and S&P/TSX 60 Indices
S&P/Experian Consumer Credit Default Indices Show Third Straight Drop in Composite Rate in June 2021
New Zealand’s Exchange and S&P Dow Jones Indices launch S&P/NZX 50 Portfolio ESG Tilted  Index
Additions to the S&P BSE IPO Index
Moderna Set to Join S&P 500
S&P Municipal Bond Indices Consultation on the Exclusion of Anticipation Notes – Results
S&P Dow Jones Indices Launches S&P Cryptocurrency Broad Digital Market Index
Addition to the S&P BSE SME IPO Index
Middlesex Water Set to Join S&P SmallCap 600
Modification to the Methodology of the S&P Japanese Indices
Reconstitution of S&P BSE Indices
Bingo Industries Limited to be removed from the  S&P/ASX 200 Index
Update on S&P Dow Jones Indices Announcement  of Additional Removals due to Sanctions for Equity  Indices
Update on S&P Dow Jones Indices Announcement of Additional Removals due to Sanctions for Fixed Income Indices
Important information regarding the S&P/BVL IBGC Index annual rebalancing
S&P Dow Jones Indices’ Consultation on Potential Replacement Rates for Key London Interbank Offered Rates
Consultation on the Construction of S&P Global BMI Size Benchmark Indices
S&P Dow Jones Indices and the Lima Stock Exchange to Launch a new ESG index to replace the S&P/BVL Good Corporate Governance Index
S&P Dow Jones Indices Reports U.S. Indicated  Dividend Payments Increased $12.9 Billion in Q2 2021
Addition to the S&P BSE IPO Index
Cerence Set to Join S&P MidCap 400; Adtalem Global Education to Join S&P SmallCap 600
Addition to the S&P BSE SME IPO Index
2020 Annual Survey of Indexed Assets
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Surged To 14.6% In April
DT Midstream Set to Join S&P 400
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
S&P Dow Jones Indices Wins Environmental Finance’s ESG Index Provider of the Year Award
Additions to the S&P BSE indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Modification to the Methodology of the S&P/BMV Total Mexico ESG Index
Addition to the S&P BSE SME IPO Index
Dow Jones Israel Select Sector Indices and S&P/Harel Sector Indices Consultation on the Treatment of Suspended Stocks
Additions to the S&P BSE IPO Index
S&P Global Natural Resources and Water Shariah Index Consultation – Results
Modification to the Accelerated Implementation of Non-Mandatory Share and Investable Weight Factor (IWF) Updates in S&P and Dow Jones Global Equity Indices
Vocus Group Limited to be removed from the S&P/ASX 200 Index
S&P Global Resources Select Equal Weighted Index Consultation Results
Treatment of Woolworths Group Limited Demerger within the S&P/ASX 200 Index
Two Harbors Investment Set to Join S&P SmallCap 600
S&P 500 Buybacks Double their Post Covid Low; Companies repurchased 36.5% more  shares than in Q4 2020
S&P/Experian Consumer Credit Default Indices Show Second Straight Drop in Composite Rate in May 2021
S&P Dow Jones Indices Treatment for Lebanon, Argentina, Nigeria and Bangladesh
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV FIBRAS Index
S&P Dow Jones Indices Announces June 2021 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces June 2021 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces June 2021 Quarterly Rebalance of the S&P/ASX 200 Index
Callaway Golf Set to Join S&P MidCap 400; Apollo Medical to Join S&P SmallCap 600
S&P Global Resources Select Equal Weighted Index Consultation – Updated
Modification to the Methodology of the S&P UK / Euro High Yield Dividend Aristocrats Indices
SelectQuote Set to Join S&P SmallCap 600
S&P Global Resources Select Equal Weighted Index Consultation – Updated
Targa Resources & Envestnet Set to Join S&P MidCap 400
S&P Dow Jones Indices Announces Update to S&P Composite 1500 Market Cap Guidelines
Results of the S&P New China Sectors Index Series Consultation on the Index Universe
Results of the Consultation on the Investable Weight Factor Threshold for the S&P Japanese Indices
Results of S&P Dow Jones Indices’ Consultation on the Market Classification of Lebanon and the Removal of Lebanon-Domiciled Constituents from the S&P Frontier BMI and S&P Pan Arab Indices
S&P Dow Jones Indices Launches Dividend Growers Index Series
Notice: Important information Regarding the Dow Jones Sustainability Indices Annual Rebalancing
Merck & Co. to remain in Dow Jones Industrial Average after Spin-off Transaction
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Organon Set to Join S&P 500; HollyFrontier to Join S&P MidCap 400; Service Properties Trust to Join S&P SmallCap 600
S&P Municipal Bond Indices Consultation on the Exclusion of Anticipation Notes – Updated
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Crocs Set to Join S&P MidCap 400 and Organogenesis to Join S&P SmallCap 600
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P/BMV IPC and other S&P/BMV Indices
Notice: S&P Dow Jones Indices Announces Changes to the S&P Latin America 40 Index
S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Climbed To 13.2% In March
The Joint Corp Set to Join S&P SmallCap 600
Results of the Dow Jones Islamic Market U.S. Style Indices Consultation on the Constituent Weightings
Reconstitution of S&P BSE Indices
Results of the S&P Paris-Aligned & Climate Transition (PACT) Indices Consultation on Eligibility Requirements and Constraints
S&P Global Natural Resources and Water Shariah Index Consultation
S&P Global Resources Select Equal Weighted Index Consultation
S&P/Experian Consumer Credit Default Indices Show Drop in Composite Rate in April 2021
S&P Dow Jones Indices Reaches Settlement With SEC
S&P Dow Jones Indices Consultation on the Quarterly Rebalancing Process
Reconstitution of S&P BSE Indices
Changes to the S&P BSE Indices
Charles River Laboratories International Set to Join S&P 500; Others to Join S&P MidCap 400 and S&P SmallCap 600
S&P New China Sectors Index Series Consultation on the Index Universe
Federal Government of Germany Selects S&P Dow Jones Indices to Create EU Climate Transition Index
S&P Municipal Bond Indices Consultation on the Exclusion of Anticipation Notes – Updated
S&P Dow Jones Indices Launches Cryptocurrency Index  Series Including S&P Bitcoin Index
R1 RCM Set to Join S&P MidCap 400; Bancorp to Join S&P SmallCap 600
New Zealand's Exchange and S&P Dow Jones  Indices Launch Carbon-Efficient Indices
S&P Dow Jones Indices’ Consultation on the Market Classification of Lebanon and the Removal of Lebanon-Domiciled Constituents from the S&P Frontier BMI and S&P Pan Arab Indices
S&P Municipal Bond Indices Consultation on the Exclusion of Anticipation Notes
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Genpact Set to Join S&P MidCap 400; Unitil &  Genworth Financial to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Reports 12.0% Annual Home Price Gain In February 2021
S&P Dow Jones Indices Launches ESG Dividend Aristocrats Index Series
S&P Dow Jones Indices Announces April 2021 Rebalance of the S&P 500 ESG Index
Modification to the Methodology of the S&P U.S. Dollar Global Corporate Bond Indices
S&P Dow Jones Indices Announces April 2021 Rebalance of the S&P Europe 350 ESG Index
Change to the S&P BSE 100 ESG Index
S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
Consultation on the Investable Weight Factor Threshold for the S&P Japanese Indices
S&P Paris-Aligned & Climate Transition (PACT) Indices Consultation on Eligibility Requirements and Constraints
S&P/Experian Consumer Credit Default Indices Show Third Straight Increase in Composite Rate in March 2021
Additions to the S&P BSE indices
Dow Jones Islamic Market U.S. Style Indices Consultation on Constituent Weightings
Coca-Cola Amatil Limited to be removed from the  S&P/ASX 200 Index
PTC Set to Join S&P 500; Lattice Semiconductor & Progyny to Join S&P MidCap 400; Domtar to Join S&P SmallCap 600
Addition to the S&P BSE SME IPO Index
Results of S&P Dow Jones Indices’ Consultation on Certain Bond Indices’ Security Universe Reference Dates
Modification to the Methodologies of the S&P 500 Bond Index, S&P Global LargeMidCap Commodity and Resources Corporate Bond Index, and Dow Jones Global Select Real Estate Securities Corporate Bond Index
B. Riley Financial Set to Join S&P SmallCap 600
Notice: Adani Ports and Special Economic Zone to be Removed from Dow Jones Sustainability Indices
Reconstitution of S&P BSE Indices
Additions to the S&P BSE indices
S&P Dow Jones Indices Launches First SPIVA Scorecard for the MENA Region
Envista Holdings Set to Join S&P MidCap 400; InterDigital to Join S&P SmallCap 600
S&P Dow Jones Indices Reports U.S. Indicated  Dividend Payments Increased $18.0 Billion in Q1 2021
Changes to the S&P BSE Indices
S&P Dow Jones Indices’ Consultation on the Investor Perspective for Certain Regional Fixed Income Indices - Results
Cara Therapeutics Set to Join S&P SmallCap 600
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P CoreLogic Case-Shiller Index Reports 11.2% Annual Home Price Gain To Start 2021
Addition to the S&P BSE IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Additions to the S&P BSE IPO Index
Additions to the S&P BSE IPO Index
S&P Global Clean Energy Index Consultation on Exposure Scores, Target Constituent Count and Constituent Weightings - Results
Neurocrine Biosciences Set to Join S&P MidCap 400; O-I Glass to Join S&P SmallCap 600
S&P 500 Buybacks Increase 28.2% in Q4 2020 from Q3 2020; Full Year 2020 down 28.7% from  2019
Addition to the S&P BSE IPO Index
S&P/BMV Dividend Index Consultation - Results
Changes to the S&P BSE Indices
Notice: S&P Dow Jones Indices Announcement for Luokung Technology and Xiaomi Corporation
Modification to the Methodology of the S&P 500 NDF KRW Hedged Index - Updated
Addition to the S&P BSE SME IPO Index
Addition to the S&P BSE IPO Index
S&P Dow Jones Indices’ Consultation on the Investor Perspective for Certain Regional China Benchmark Indices - Results
S&P Dow Jones Indices Announces Update to S&P Composite 1500 Market Cap Guidelines
Vericel Set to Join S&P SmallCap 600
Modification to the Methodology of the S&P International Corporate Bond Index – Update
S&P/Experian Consumer Credit Default Indices Show Second Straight Increase in Composite Rate in February 2021
Addition to the S&P BSE IPO Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P/BMV Dividend Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P Colombia Select
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P MERVAL Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P/BVL Peru Select
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P IPSA Index
Notice: S&P Dow Jones Indices Announces  Rebalancing Results for the S&P/BMV China SX20
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P Latin America 40
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the Dow Jones U.S. Select Dividend Index
NXP Semiconductors, Penn National Gaming, Generac Holdings and Caesars Entertainment Set to Join S&P 500; Others to Join S&P MidCap 400, S&P SmallCap 600 and S&P 100
Notice: S&P Dow Jones Indices Announces March 2021 Quarterly Rebalance of the S&P Europe 350 Indices
S&P Global Clean Energy Index Consultation on Exposure Scores, Target Constituent Count, and Constituent Weightings - Updated
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces March 2021 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces March 2021 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces March 2021 Quarterly Rebalance of the S&P/NZX Indices
Update on S&P Dow Jones Indices Announcement of Additional Removals due to Sanctions
S&P/BMV Dividend Index Consultation on Dividend Payments & Quarterly Dividend Review - Results
Modification to the Methodologies of the S&P Global BMI and Dow Jones Global Index Families
Notice: S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
Addition to the S&P BSE IPO Index
Modification to the Methodology of the S&P National AMT-Free Municipal Bond Indices and S&P AMT-Free Municipal Series Bond Indices
Modification to the Methodology of the S&P/ASX Corporate Issuer Equal-Weight Index
S&P Global Clean Energy Index Consultation on Exposure Scores, Target Constituent Count, and Constituent Weightings
S&P Dow Jones Indices Treatment for Lebanon, Argentina, Nigeria and Bangladesh
Modification to the Methodology of the S&P 500 NDF KRW Hedged Index - Implementation
Modification to the Monthly Dividend Review for certain Dow Jones Dividend-themed Indices
Addition to the S&P BSE IPO Index
Dow Jones Emerging Markets Consumer Titans Index Consultation on Replacement Policy and Constituent Weighting - Results
S&P Dow Jones Indices’ Consultation on the Investor Perspective for Certain Regional China Fixed Income Indices
S&P Dow Jones Indices’ Consultation on the Investor Perspective for Certain Regional China Benchmark Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Cleveland-Cliffs Set to Join S&P MidCap 400; WSFS Financial to Join S&P SmallCap 600
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
S&P Dow Jones Indices’ Consultation on Certain Bond Indices’ Security Universe Reference Dates
S&P CoreLogic Case-Shiller Index Reports 10.4% Annual Home Price Gain To End 2020
S&P/BMV China SX20 Index Consultation on the Index Universe, Constituent Weightings, and Constituent Replacement - Results
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices’ Fixed Income Indices Sanctioned Securities Policy Update
S&P Dow Jones Equity Indices’ Sanctioned Securities Policy Update
S&P/Experian Consumer Credit Default Indices Show Higher Composite Rate in January 2021
Reconstitution of S&P BSE Indices
S&P Global Clean Energy Index Consultation on Constituent Weighting, Liquidity Screen, Target Constituent Count and Rebalancing Results
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P Dow Jones Indices Wins ESG Investing’s Best ESG Index Provider Award
Amkor Technology Set to Join S&P MidCap 400; HNI to Join S&P SmallCap 600
Monolithic Power Systems Set to Join S&P 500; Iridium Communications to Join S&P MidCap 400; Collegium Pharmaceutical to Join S&P SmallCap 600
Dow Jones Emerging Markets Consumer Titans Index Consultation
Addition to the S&P BSE IPO Index
S&P/BMV China SX20 Index Consultation on the Index Universe, Constituent Weightings, and Constituent Replacement - Extended
Modification to the Methodology of the Dow Jones Country Titan Indices
Modification to the Methodology of the S&P/ASX Infrastructure Index
S&P Dow Jones Indices Expands Global ESG Suite with Launch of S&P MidCap 400 ESG and S&P SmallCap 600 ESG Indices
Addition to the S&P BSE IPO Index
Modification to the Methodology of the S&P 500 NDF KRW Hedged Index - Updated
Investors Bancorp to Join S&P SmallCap 600
Addition to the S&P BSE IPO Index
S&P/BMV China SX20 Index Consultation on the Index Universe, Constituent Weightings, and Constituent Replacement - Updated
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announcement for Additional Upcoming Removals Due to Sanctions
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Saracen Mineral Holdings Limited to be removed from the S&P/ASX 200 Index
S&P Dow Jones Indices Announcement for Additional Upcoming Removals Due to Sanctions
S&P/BMV China SX20 Index Consultation on the Index Universe, Constituent Weightings, and Constituent Replacement
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Climbed To 9.5% In November
Staar Surgical Set to Join S&P MidCap 400; Prestige Consumer Healthcare & Bridge Bancorp to Join S&P SmallCap 600
Updated: S&P Dow Jones Indices Announcement for Removal of CNOOC from S&P Fixed Income Indices Due to Sanctions
S&P Dow Jones Indices Announcement for Additional Upcoming Removals Due to Sanctions
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P 500 Dividend Aristocrats Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the S&P High Yield Dividend Aristocrats Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Dividend Aristocrats Index
S&P Global Clean Energy Index Consultation on Constituent Weighting, Liquidity Screen, Target Constituent Count and Rebalancing - Updated
S&P Dow Jones Indices Introduces New ESG Aligned Target Risk Index Series
S&P Dow Jones Indices and the Santiago Exchange Launch the S&P IPSA ESG Tilted Index
Modification to the Monthly Divdend Review for Certain S&P & Dow Jones Dividend-themed Indices
S&P/Experian Consumer Credit Default Indices Show Composite Rate Unchanged in December 2020
Trimble Set to Join S&P 500; YETI Holdings to Join S&P MidCap 400; Hilltop Holdings to Join S&P SmallCap 600
S&P Dow Jones Indices Announcement for Removal of CNOOC due to Sanctions
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announcement for Additional Removals due to Sanctions
S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
Index Reconstitution Calendar 2021
S&P Dow Jones Indices Announcement for China ADR Delistings
Modification to the Methodology of the S&P ADR Index
S&P Dow Jones Indices Reports U.S. Indicated Dividend Payments Increased $9.5 Billion in Q4 2020, a reversal from Q3’s $2.3 billion decline
Addition to the S&P BSE IPO Index
Enphase Energy Set to Join S&P 500; Capri Holdings & Brooks Automation to Join S&P MidCap 400; Celsius Holdings & e.l.f. Beauty to Join S&P SmallCap 600
Modification to the Methodology of the S&P 500 NDF KRW Hedged Index - Updated
Modification to the Methodology of the S&P Global LargeMidCap Commodity and Resources Corporate Bond Index and Dow Jones Global Select Real Estate Securities Corporate Bond Index
Modification to the Methodology of the S&P 500 NDF KRW Hedged Index
S&P Dow Jones Indices’ Consultation of the S&P International Sovereign Ex-U.S. Bond Indices Eligibility Criteria Results
S&P Dow Jones Indices Announces Changes in Dividend Withholding Tax Rates
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Remained Strong In October
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P/NZX 50 High Dividend Index Consultation on the Index Objective, Eligibility Criteria, and Index Construction Results
Addition to the S&P BSE IPO Index
Changes to the S&P BSE Indices
Ossiam Emerging Markets Minimum Variance Index Series Consultation on India Country Weight Caps Results
Kinsale Capital Group Set to Join S&P MidCap 400; The Simply Good Foods Company to Join S&P SmallCap 600
Modification to the Methodology of the S&P/OIC COMCEC 50 Shariah
S&P 500 Buybacks Rebound 14.8% in Q3 2020; Remain 42.1% Lower than Q3 2019
S&P/Experian Consumer Credit Default Indices Show Lower Composite Rate in November 2020
Addition to the S&P BSE IPO Index
Tesla Set to Join S&P 500 & 100; Apartment Income REIT to Join S&P MidCap 400
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
Notice: S&P Dow Jones Indices Announces December 2020 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces December 2020 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces December 2020 Quarterly Rebalance of the S&P/ASX 200 Index
S&P Dow Jones Indices Announces December 2020 Quarterly Rebalance of the S&P/NZX Indices
Modification to the Methodology of the S&P/BMV Indices Methodology
S&P Dow Jones Indices’ Consultation on the Executive Order Prohibiting U.S. Transactions in Certain Chinese Companies Results
S&P Global Clean Energy Index Consultation on Constituent Weighting, Liquidity Screen, and Target Constituent Count
S&P Dow Jones Indices and MSCI Announce the Postponement of the Global Industry Classification Standard (GICS) Advisory Panel Scheduled for 2020
S&P Dow Jones Indices Announces Update to S&P Composite 1500 Market Cap Guidelines
S&P Dow Jones Indices’ Updates to the S&P U.S. Indices Methodology
Changes to the S&P BSE Indices
Modifications to S&P Dow Jones Indices’ Equity Indices Policies & Practices Methodology
S&P Dow Jones Indices Builds Crypto Indexing Capabilities with Lukka
S&P/NZX 50 High Dividend Index Consultation on the Index Objective, Eligibility Criteria, and Index Construction
S&P Dow Jones Indices Announces 2021 Weights for the Dow Jones Commodity Index
Modification to the Methodology of the Dow Jones Brookfield Global Infrastructure ex MLP Corporate Bond Index
S&P Dow Jones Indices Consultation on the Implementation of Tesla’s Addition to the S&P 500 - Results
Modification to the Methodology of the S&P Global Agribusiness Equity Index
S&P Dow Jones Indices Launches S&P/KRX Carbon Efficient Capped Index
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Concentrix Set to Join S&P MidCap 400; AMC Networks & The Aaron's Company to Join S&P SmallCap 600
Changes to the S&P BSE Indices
S&P Dow Jones Indices Consultation on the Executive Order Prohibiting U.S. Transactions in Certain Chinese Companies
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Soared To 7% In September
Dow Jones Global Titans 50 Index Consultation on Constituent Weighting Results
S&P/BMV Dividend Index Consultation on Dividend Payments & Quarterly Dividend Review
S&P Dow Jones Indices Announces 2021 Eligible Contract Months for the S&P GSCI Dynamic Roll
S&P Dow Jones Indices 2020 Country Classification Consultation Results
Modification to the Methodology of the S&P International Corporate Bond Index
S&P International Sovereign Ex-U.S. Bond Indices Consultation on Eligibility Criteria
Reconstitution of S&P BSE Indices
Addition to the S&P BSE IPO Index
Notice: S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
Modification to the Methodology of the S&P China Composite Bond Index
S&P/Experian Consumer Credit Default Indices Show Lower Composite Rate in October 2020
S&P Dow Jones Indices Consultation on the Implementation of Tesla’s Addition to the S&P 500
Tesla Set to Join S&P 500
Notice: S&P Dow Jones Indices Announces Changes to the Dow Jones Sustainability World Index
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces 2021 S&P GSCI Weights
Results of the S&P Managed Risk 2.0 Index Series Mark-to-Market Weighting Method Consultation
S&P Africa Hard Currency Sovereign Bond Index USD Consultation on Bonds with Multiple Tranches Results
S&P Managed Risk 2.0 Index Series Consultation on Mark-to-Market Weighting Method − Updated
Modification to the Methodology of the S&P Sri Lanka 20
MGIC Investment & Halozyme Therapeutics Set to Join S&P MidCap 400; First Bancorp, The Geo Group & Mednax to Join S&P SmallCap 600
Notice: Special Trading Session for S&P BSE Indices
Results of the HSBC Pan Arab MultiFactor Index Series Consultation on Index Business Day Convention
Additions to the S&P BSE Indices
S&P Managed Risk 2.0 Index Series Consultation on Mark-to-Market Weighting Method − Updated
S&P U.S. IPO and Spin-Off and S&P U.S. Spin-Off Indices Consultation on Constituent Weightings Results
S&P Managed Risk 2.0 Index Series Consultation on Mark-to-Market Weighting Method
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P CoreLogic Case-Shiller Index Shows Annual Home Price Gains Increased To 5.7% In August
Modification to the Methodology of the S&P Global Luxury Index
Atmos Energy and Xcel Energy Set to Join Dow Jones Utility Average
S&P/Experian Consumer Credit Default Indices Show Lower Composite Rate in September 2020
Addition to the S&P BSE SME IPO Index
Treatment of Iluka Resources Limited Demerger within the S&P/ASX 200 Index
S&P South Africa Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening Results
Changes to the S&P BSE Indices
Addition to the S&P BSE SME IPO Index
Metlifecare Limited to be removed from the S&P/NZX Indices
Dow Jones Global Titans 50 Index Consultation on Constituent Weighting
Addition to the S&P BSE IPO Index
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Reports $2.3 Billion Decrease in U.S. Indicated Dividend Payments for Q3 2020, Up from Q2’s $42.5 Billion Decline
S&P Dow Jones Indices Launches S&P/TSX ESG Indices
S&P Africa Hard Currency Sovereign Bond Index USD Consultation on Bonds with Multiple Tranches
Addition to the S&P BSE SME IPO Index
Vontier Set to Join S&P 500
Addition to the S&P BSE IPO Index
Pool Set to Join S&P 500; Neogen & Simpson Manufacturing to Join S&P MidCap 400; Others to Join S&P SmallCap 600
Additions to the S&P BSE Indices
SailPoint Technologies Holdings Set to Join S&P MidCap 400; Sally Beauty Holdings to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Reports 4.8% Annual Home Price Gain In July
Changes to the S&P BSE Indices
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Addition to the S&P BSE SME IPO Index
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Chesapeake Utilities to Join S&P SmallCap 600
S&P South Africa Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening
S&P Dow Jones Indices Launches Sustainability Screened Versions of Flagship U.S. Equity Indices
S&P U.S. IPO and Spin-Off and S&P U.S. Spin-Off Indices Consultation on Constituent Weightings
S&P Dow Jones Indices Announces Change in Dividend Withholding Tax Rate
Changes to the S&P BSE Indices
SIEMENS ENERGY AG SET TO JOIN S&P EUROPE 350
Fulgent Genetics Set to Join S&P SmallCap 600
HSBC Pan Arab MultiFactor Index Series Consultation on Index Business Day Convention
Addition to the S&P BSE IPO Index
Reminder: Exclusion of Contingent Convertible Bonds from the S&P Corporate Bond Indices
Addition to the S&P BSE IPO Index
Changes to the S&P BSE Indices
S&P UK / Euro High Yield Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening Results − Updated
S&P 500 Buybacks Decline 55.4% to $88.7 Billion; Significant Reductions Expected to continue in Q3 2020
S&P/Experian Consumer Credit Default Indices Show Composite Rate Steady in August 2020
S&P Dow Jones Indices Announces Rebalancing Results for the S&P MERVAL Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P Colombia Select Index
S&P Dow Jones Indices Announces Final Rebalancing Results for the S&P/BMV IPC Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV China SX20 Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P Dow Jones Indices Announces September 2020 Extraordinary Rebalance of the S&P 500 ESG Index
Changes to the S&P BSE Indices
Reconstitution of S&P BSE Indices
Modification to the Methodologies of the S&P Global BMI and Dow Jones Global Indices Index Families − Updated
Changes to the S&P BSE Indices
S&P Dow Jones Indices Announces Rebalancing Results for the S&P IPSA Index
S&P Dow Jones Indices and B3 S.A. Launch the S&P/B3 Brazil ESG Index
S&P Dow Jones Indices Announces Preliminary Rebalancing Results for the S&P/BMV IPC Index
Etsy, Teradyne and Catalent Set to Join S&P 500; Others to Join S&P MidCap 400 and S&P SmallCap 600
Modification to the Methodology of the S&P/B3 Ingenius Index
Natura & Co Holding SA is Set to Join S&P Latin America 40
S&P UK / Euro High Yield Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening Results
Notice: S&P Dow Jones Indices Announces September 2020 Quarterly Rebalance of the S&P Europe 350 Indices
S&P GIVI and S&P/JPX GIVI Indices Consultation on Rebalancing Schedule Results − Updated
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces September 2020 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces September 2020 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices Announces September 2020 Quarterly Rebalance of the S&P/ASX 200 Index
Modification to the Methodologies of the S&P Global BMI and Dow Jones Global Indices Index Families
Modification to the Methodology of the S&P South Africa Preference Share Index
Dow Jones Arabia Titans 50 Index Consultation on Eligible Index Universe Results
S&P GIVI and S&P/JPX GIVI Indices Consultation on Rebalancing Schedule Results
Modification to the Methodology of the Select Sector Indices
Consultation Results on the Eligibility of ChiNext Stocks in S&P Dow Jones Indices' Global Benchmarks
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
S&P Asia 50 Consultation Results
Lithia Motors Set to Join S&P MidCap 400; BankUnited & Trupanion to Join S&P SmallCap 600
Reminder: Extraordinary Rebalancing of the S&P ESG Index Series and S&P ESG Tilted Index Series
Modification to the Methodology of the S&P/TSX ESG Indices
S&P CoreLogic Case-Shiller Index Reports 4.3% Annual Home Price Gain In June
Salesforce.com, Amgen and Honeywell International Set to Join Dow Jones Industrial Average
S&P UK / Euro High Yield Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening − Updated
S&P/BNY Mellon India Select DR Index Consultation Results
S&P Dow Jones Indices’ 2020 Country Classification Consultation
Modification to the Methodology of the S&P/BVL Peru Indices
Modification to the Methodologies of the S&P Corporate Bond Indices
S&P GIVI and S&P/JPX GIVI Indices Consultation on Rebalancing Schedule − Updated
S&P/Experian Consumer Credit Default Indices Show Composite Rate Unchanged in July 2020
S&P GIVI and S&P/JPX GIVI Indices Consultation on Rebalancing Schedule
Changes to the S&P BSE Indices
Reconstitution of S&P BSE Indices
Dow Jones Arabia Titans 50 Index Consultation on Eligible Index Universe
Addition to the S&P BSE SME IPO Index
S&P/ASX 300 Shareholder Yield Index Consultation Results
Builders FirstSource Set to Join S&P MidCap 400; FB Financial & CoreCivic to Join S&P SmallCap 600
Modification to the Methodology of the Dow Jones Sustainability Indices
S&P UK / Euro High Yield Dividend Aristocrats Consultation on Constituent Weighting and Liquidity Screening
Modification to the Methodology of the S&P Global Carbon Efficient Indices
S&P/BMV Dividend Index Consultation
Consultation on the Eligibility of ChiNext Stocks in S&P Dow Jones Indices' Global Benchmarks
S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks
S&P Asia 50 Consultation
Park National Set to Join S&P SmallCap 600
Modification to the Methodology of the S&P Kensho New Economies Sector Rotator Index
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Sunrun, IAA & Rexford Industrial Realty Set to Join S&P MidCap 400; Bancfirst, Deluxe & Carpenter Technology to Join S&P SmallCap 600
S&P CoreLogic Case-Shiller Index Reports 4.5% Annual Home Price Gain In May
Addition to the S&P BSE IPO Index
S&P/ASX 300 Shareholder Yield Index Consultation
S&P/Experian Consumer Credit Default Indices Show Lower Composite Rate For Fourth Consecutive Month
Emergent BioSolutions Set to Join S&P MidCap 400; First Hawaiian to Join S&P SmallCap 600
S&P/BNY Mellon India Select DR Index Consultation
Addition to the S&P BSE SME IPO Index
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Reports $42.5 Billion Decrease in U.S. Indicated Dividend Payments for Q2 2020
Results of S&P Dow Jones Indices Consultation on Proposals Related to Negatively Priced Commodities Futures Contracts
Annual Home Price Gains Remained Steady In April According To S&P CoreLogic Case-Shiller Index
Addition to the S&P BSE SME IPO Index
Tuas Limited to be removed from the S&P/ASX 200 Index
Updated Monthly Rebalancing Results for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
SITE Centers Set to Join S&P SmallCap 600
Notice: S&P Dow Jones Indices Announces Changes to the S&P Europe 350 Index
S&P 500 Buybacks Return to $200 Billion Range in Q1 2020; Expectations for Q2 2020 are Low as Companies Suspend Programs
Treatment of TPG Telecom Limited Demerger and Merger within the S&P/ASX 200 Index
TopBuild Set to Join S&P MidCap 400; Retail Properties of America and Brandywine Realty Trust to Join S&P SmallCap 600
Constituent Change Announced for the S&P/BMV Dividend Index
S&P Dow Jones Indices Announces Change to the S&P/TSX Canadian Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P 500 Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
Grocery Outlet Holding Set to Join S&P MidCap 400; Brinker International to Join S&P SmallCap 600
Modification to the Methodology of the S&P Japan Sovereign 20+ Year Bond Index (AUD) and S&P Japan Sovereign 20+ Year AUD Hedged Bond Index
S&P Dow Jones Indices and the Mexican Stock Exchange Launch S&P/BMV Total Mexico ESG Index
Independent Bank Group Set to Join S&P SmallCap 600
S&P/Experian Consumer Credit Default Indices Show Drop In Composite Rate in May 2020
2019 Annual Survey of Indexed Assets
S&P Dow Jones Indices Announces Tyler Technologies, Bio-Rad Laboratories and Teledyne Technologies Set to Join S&P 500; Others to Join S&P MidCap 400 and S&P SmallCap 600
S&P Global 1200 Fossil Fuel Free Indices Consultation on Fossil Fuel Reserves Exclusion Screening Results
S&P ESG Index Series and S&P ESG Tilted Index Series Consultation on Thermal Coal Exclusion Results
S&P Dow Jones Indices Announces Rebalancing Results for the S&P IPSA Index
Magazine Luiza SA and WEG SA are Set to Join S&P Latin America 40
S&P Dow Jones Indices Announces Rebalancing Results for the S&P MERVAL Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV FIBRAS Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV China SX20 Index
S&P Dow Jones Indices Announces Rebalancing Results for the S&P/BMV Dividend Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index and S&P/TSX 60 Index
Notice: S&P Dow Jones Indices Announces Rebalancing Results for the Dow Jones U.S. Select Dividend Index
S&P Dow Jones Indices Announces June 2020 Quarterly Rebalance of the S&P Europe 350 Indices
Reconstitution of S&P BSE Indices
S&P Dow Jones Indices Announces June 2020 Quarterly Rebalance of the S&P/TOPIX 150 Index
S&P Dow Jones Indices Announces June 2020 Quarterly Rebalance of the S&P/NZX Indices
S&P Dow Jones Indices Announces June 2020 Quarterly Rebalance of the S&P/ASX 200 Index
Modification to the Methodology of the Dow Jones U.S. Thematic Neutral Indices − Updated
Zynex Set to Join S&P SmallCap 600
Important Information Regarding the Dow Jones Sustainability Indices Annual Rebalancing
S&P All Africa ex-South Africa Indices Consultation on Offshore Company Eligibility Results
Modification to the Methodology of the S&P SMIT 40 Index
Results of the Alerian Dividend-Weighted Indices Consultation on Changes to the Quarterly Rebalancing Process
Changes to the S&P BSE Indices
S&P China A-Share Indices Consultation Results
Modification to the Methodology of the S&P/BVL Lima 25 Index
S&P/TSX High Income Energy Index Consultation on Constituent Weighting Results
Dow Jones U.S. Dividend 100 Index Consultation on Constituent Weightings Results
HSBC VantageZ Index Series Consultation
Hudson Pacific Properties Set to Join S&P MidCap 400; Diversified Healthcare Trust, Palomar Holdings & Simulations Plus to Join S&P SmallCap 600
S&P UK High Yield Dividend Aristocrats Index Consultation on Constituent Selection Results
Monthly Rebalancing Announced for the S&P/ASX Australian Fixed Interest Index Series
Monthly Rebalancing Announced for the S&P/NZX New Zealand Fixed Interest Index Series
Essent Group Set to Join S&P MidCap 400; Coherus BioSciences, Patterson-UTI Energy to Join S&P SmallCap 600
Modification to the S&P Dow Jones Indices REIT/RESI Industry Classification Hierarchy
S&P Global Developed Fixed Income Indices Country Inclusion Consultation Results
Annual Home Price Gains Increased To 4.4% In March According To S&P CoreLogic Case-Shiller Index
CORRECTION - S&P Dow Jones Indices Announces Change to the S&P/TSX Canadian Dividend Aristocrats Index
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Dividend Aristocrats Index
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
Reconstitution of S&P BSE Indices
Modification to the Methodology of the S&P Long-Only Merger Arbitrage Ex-Cash Liquid Index (Custom)
June Roll Period of WTI Crude Oil in S&P Dow Jones Commodity Indices
Modification to the Methodologies of the S&P and Dow Jones China Indices
West Pharmaceutical Services Set to Join S&P 500; Physicians Realty Trust to Join S&P MidCap 400; Helmerich & Payne to Join S&P SmallCap 600
S&P/TSX High Income Energy Index Consultation on Constituent Weighting
Modification to the Methodology of the S&P 500 Quality High Dividend Index
Dow Jones U.S. Dividend 100 Index Consultation on Constituent Weightings
Modification to the Methodology of the Dow Jones Israel Select Sector Indices
Notice: S&P Dow Jones Indices Announces Index Treatment for Nigeria
S&P UK High Yield Dividend Aristocrats Index Consultation on Constituent Selection − Updated
Reconstitution of S&P BSE Indices
DexCom & Domino's Pizza Set to Join S&P 500; Salesforce.com to Join S&P 100; STORE Capital to Join S&P MidCap 400; Capri Holdings to Join S&P SmallCap 600
Modification to the Methodology of the S&P UAE Domestic Shariah Liquid 35/20 Capped Index and S&P UAE BMI Liquid 20/35 Capped Index
S&P ESG Index Series and S&P ESG Titled Index Series Consultation on Thermal Coal Exclusion − Updated
May Roll Period of WTI Crude Oil in S&P Dow Jones Commodity Indices
S&P Global 1200 Fossil Fuel Free Indices Consultation on Fossil Fuel Reserves Exclusion Screening
S&P Dow Jones Indices Announces Changes to the S&P/TSX Composite Index
S&P China A-Share Indices Consultation
S&P UK High Yield Dividend Aristocrats Index Consultation on Constituent Selection
Modification to the Methodology of the S&P/BVL Enhanced Dividend Index
MONTHLY REBALANCING ANNOUNCED FOR THE S&P/NZX NEW ZEALAND FIXED INTEREST INDEX SERIES
MONTHLY REBALANCING ANNOUNCED FOR THE S&P/ASX AUSTRALIAN FIXED INTEREST INDEX SERIES
S&P Dow Jones Indices Consultation on Proposals Related to Negatively Priced Commodities Futures Contracts
Enphase Energy and Paylocity Set to Join S&P MidCap 400; Core Laboratories and Meredith to Join S&P SmallCap 600
Modification to the Methodology of the S&P 500 Low Volatility, S&P MidCap 400 Low Volatility, and S&P SmallCap 600 Low Volatility Indices
Notice: Constituent Change Announced for the S&P High Yield Dividend Aristocrats Index
S&P Dow Jones Indices Announces Change to the S&P/TSX Canadian Dividend Aristocrats Index
Notice: Constituent Change Announced for the Dow Jones U.S. Select Dividend Index
S&P DJI Creates New Sustainable Version of S&P 500 for iShares
Modification to the Methodology of the S&P 500 Low Volatility Rate Response Index
Information Regarding Negative Futures Contract Prices and Index Levels in S&P Dow Jones Indices
Alerian Dividend-Weighted Indices Consultation on Changes to the Quarterly Rebalancing Process
S&P Dow Jones Indices Launches Paris-Aligned Climate (PA) and Climate Transition (CT) Eurozone Indices
Modification to the Methodology of the S&P High Beta Indices
Modification to the Methodology of the S&P Volatility – Highest Quintile Indices
S&P Dow Jones Indices Launches S&P Riskcasting Index Series
Reconstitution of S&P BSE Indices
S&P All Africa ex-South Africa Indices Consultation on Offshore Company Eligibility
Modification to the Methodology of the S&P Target Date Index Series
LHC Group Set to Join S&P MidCap 400 and YETI Holdings to Join S&P SmallCap 600
Reconstitution of S&P BSE Indices
Addition to the S&P BSE SME IPO Index
S&P Dow Jones Indices Reports $5.5 Billion Decrease in U.S. Indicated Dividend Payments for Q1 2020; Worst Quarter since Q1 2009
S&P Dow Jones Indices and IHS Markit Announce Index Collaboration
S&P Dow Jones Indices Releases SPIVA® India Year-End 2019 Results
S&P Dow Jones Indices and ASX Mark 20th Anniversary of S&P/ASX Index Series
Dan Draper Appointed CEO of S&P Dow Jones Indices
S&P 500 Buybacks up 3.2% in Q4 2019; Full Year 2019 Down 9.6% From Record 2018, as Companies Brace for a More Volatile 2020
Modification to the Methodology of the S&P/NZX Swap Indices
S&P Dow Jones Indices Launches First-of-its-Kind Carbon Emissions Single-Commodity Index
S&P Dow Jones Indices and the Mexican Stock Exchange to Launch a new ESG Index to Replace the S&P/BMV IPC Sustainable Index
Japan’s Ministry of Environment Awards S&P Dow Jones Indices Gold Prize for ESG Finance Award
S&P Dow Jones Indices Announces Treatment of Argentina Capital Controls - Update
S&P Dow Jones Indices and ASX Jointly Launch S&P/ASX All Technology Index to Capture Australia's Growing Technology Sector
S&P Dow Jones Indices to Calculate Four New Custom Indices for Ágora Investimentos in Brazil
S&P Dow Jones Indices Wins Prestigious Tokyo Financial Award for ESG Index Innovation
S&P Dow Jones Indices Reports $10.6 Billion Increase in U.S. Dividend Payments for Q4 2019 and $45.4 billion for 2019
S&P Dow Jones Indices Launches S&P/MX International Cannabis Index
S&P 500 Buybacks Reverse Declines in Q3 2019; Expenditures Remain Lower than 2018 Levels
S&P Dow Jones Indices to Calculate Taiwan Sustainability Value Index
S&P Dow Jones Indices Releases SPIVA® India Mid-Year 2019 Results
S&P Dow Jones Indices Launches Market’s First Skim Milk Powder Index
S&P 500 Buybacks Decline Significantly in Q2 2019; Expenditures Still Remain Higher than the pre-2018 Levels
S&P Dow Jones Indices and BYMA Launch Argentinian Market's First Sector Indices
S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks
S&P Dow Jones Indices Releases Annual Survey of Assets
S&P/JPX JGB VIX Real-time Index to Launch: Access to Intraday Moves of the Index Helps Global Investors Manage Volatility Trades in Japan’s Bond Market
S&P Dow Jones Indices Reports $8.4 Billion Increase in U.S. Dividend Payments for Q2 2019
S&P 500 Buybacks Decline in Q1 2019 after Four Consecutive Record Quarters; Still Post 2nd Highest Quarter Ever
S&P Dow Jones Indices and NZX Jointly Launch Geographic Revenue Exposure Indices
S&P Dow Jones Indices Launches Global ESG Index Series Based on Core Regional and Country Benchmarks
Who’s Hiring? New S&P 500® LinkUp Jobs Indices Measure Global Open Job Listings
Modification to the Methodology of the S&P China LargeMidCap Shariah 10% Capped Index
S&P Dow Jones Indices Introduces Factor Index Solutions to Mexican Financial Market
S&P Dow Jones Indices Launches ESG Index Based on Iconic S&P 500®
S&P Dow Jones Indices Launches S&P/Drucker Institute Corporate Effectiveness Index
S&P Dow Jones Indices Reports $11.8 Billion Increase in U.S. Dividend Payments for Q1 2019
S&P Dow Jones Indices Announces Retirement of David Blitzer
Matarin Capital Selects S&P Dow Jones Indices to Calculate New Custom Indices
S&P 500 Q4 2018 Buybacks Set 4th Consecutive Quarterly Record at $223 Billion; 2018 Sets Record $806 Billion
S&P 500® and Dow Jones Industrial Average® first benchmarks endorsed into the EU under the Benchmark Regulation
S&P Dow Jones Indices Expands Factor-Based Index Strategy with S&P GCC Indices
S&P DJI and the Mexican Stock Exchange Select RobecoSAM as the Official Score Provider for Future S&P BMV ESG Indices
S&P Dow Jones Indices Launches S&P Europe 350 Economic Cycle Factor Rotator Index
S&P Dow Jones Indices Launches Global SmallCap Select Index Series
S&P Dow Jones Indices Reports Record $58.4 Billion Increase in U.S. Dividend Payments for 2018
S&P 500 Q3 2018 Buybacks Surpass $200 Billion Mark for the First Time Ever
S&P Dow Jones Indices Launches Market’s First Index Series That Incorporates Iron Ore Contract
S&P Dow Jones Indices (S&P DJI) Establishes EU Authorised Benchmark Administrator in Amsterdam
Axioma and S&P Dow Jones Indices Announce Collaboration to Accelerate Innovation in Factor Indices
S&P Dow Jones Indices Reports $19.2 Billion Increase in U.S. Dividends for Q3 2018
GPIF, World’s Largest Pension Fund, Selects New Environmental Indices Launched by S&P Dow Jones Indices
S&P 500 Q2 2018 Buybacks Increase 58.7% Year-Over-Year to Record $190.6 Billion
S&P 500 Foreign Sales for 2017 Total 43.6%
S&P Dow Jones Indices Launches Index Family for Risk Parity Strategy
S&P Dow Jones Indices to Calculate Premia FactSet Asia Innovative Technology Index
S&P Dow Jones Indices Launches the First Index Series that Incorporate Future Carbon Price Risks
S&P Dow Jones Indices Reports U.S. Dividend Activity for Q2 2018
FMDQ OTC Securities Exchange and S&P Dow Jones Indices Commence Co-branding of Indices
S&P 500 Q1 2018 Buybacks Rose 38% to Record $189.1 Billion
SDG Evaluation Tool Launched by Trucost
S&P Dow Jones Indices and Taiwan Futures Exchange Jointly Launch Taiwan’s First RMB Futures Indices
Trucost Expands Environmental Analysis of Japan’s Listed Companies in Response to Growing Demand
Modification to the Methodology of the Dow Jones Australia LPT Index
S&P Dow Jones Indices Reports U.S. Dividend Activity for Q1 2018
The Santiago Exchange Indices Maintenance Consultation
The Santiago Exchange Indices Methodology Consultation
BYMA and S&P Dow Jones Indices Sign Index Agreement
S&P 500 Q4 2017 Buybacks Rose 6.0% to $137.0 Billion; Full-Year 2017 Fell 3.2% to $519.4 Billion
S&P Colombia Select Index Consultation Results
S&P Dow Jones Indices Launches S&P 500 Bond Mega 30 Index Family
Consultation for Dow Jones U.S. Select Sector Specialty Indices
S&P Dow Jones Indices Reports U.S. Dividend Activity for Q4 2017 and Full-Year 2017
S&P 500 Q3 2017 Buybacks Increase 7.5% to $129.2 Billion
S&P Municipal Bond 50% Investment Grade / 50% High Yield Index Consultation
S&P Dow Jones Indices Debuts Carbon Metrics on Indices
S&P Dow Jones Indices, RobecoSAM, IFC and MILA Launch Dow Jones Sustainability Mila Pacific Alliance Index
S&P Dow Jones Indices Reports Increased Growth in U.S. Dividend Activity for Q3 2017
Q2 2017 S&P 500 Buybacks Fall 9.8% from Q1, to $120.1 Billion
S&P Dow Jones Indices Launches S&P Target Tuition Inflation Index
S&P Dow Jones Indices Expands Africa Index Family with New East Africa Indices
S&P Dow Jones Indices Appointed by Korea Exchange and Taiwan Index Plus to Calculate a New Custom Index
Trucost Assesses Hidden Environmental Costs of China’s Coal-to-Chemical Sector
Trucost Launches Global Carbon Pricing Tool
S&P 500 Foreign Sales Decline to 43.2%, at Lowest Level Since 2003
S&P Dow Jones Indices Completes its Fourth Annual Review of Adherence with IOSCO Principles for Financial Benchmarks
S&P Dow Jones Indices Reports Slower Growth in U.S. Dividend Activity for Q2 2017
S&P Dow Jones Indices Releases Annual Survey of Assets
S&P Preferred Stock Indices Consultation Results
S&P 500 Buybacks Fall 17.5% Year-over-Year to $133.1 Billion for Q1 2017
S&P Dow Jones Indices’ Annual Country Classification Consultation
B3 and S&P Dow Jones Indices Launch S&P/BOVESPA Non-State Owned Enterprises Index
The Mexican Stock Exchange and S&P Dow Jones Indices Complete Successful Transition of Indices
S&P Dow Jones Indices and BVL Launch Index Tracking Dividend-Paying Stocks
S&P Dow Jones Indices and B3 Launch Commodity Benchmark for the Brazilian Market
S&P Dow Jones Indices Publishes Barometer of Financial Markets’ Carbon Efficiency
S&P Dow Jones Indices Selected as Benchmark Administrator for the HSBC Vantage5 Index
S&P Dow Jones Indices to Calculate CFRA-Stovall Seasonal Rotation Indices
S&P Dow Jones Indices Reports Significant Increase in U.S. Dividend Activity for Q1 2017
S&P 500 Buybacks Total $135.3 Billion for Q4 2016, Decline for Full-Year 2016
S&P Dow Jones Indices Launches S&P Green Bond Select Index
S&P Dow Jones Indices (S&P DJI) and the Mexican Stock Exchange (Bolsa Mexicana de Valores (BMV) Equity Indices Transition
S&P Dow Jones Indices Named “Best Islamic Index Provider” in IFN Service Providers Poll 2016
S&P Dow Jones Indices Signs Agreement to Develop a New ESG Index for MILA Region
FMDQ OTC Securities Exchange and S&P Dow Jones Indices Sign Memorandum of Understanding
S&P Dow Jones Indices Launches S&P Global Revenue Exposure Index Family
S&P Dow Jones Indices Reports U.S. Dividend Activity for Q4 2016 and Full-Year 2016
S&P 500 Buybacks Continues Fall in Q3 2016
Modification to the Methodology of the Dow Jones Islamic Market Indices
S&P Dow Jones Indices Launches New China Sectors Index
Asia Index Private Limited launches S&P BSE SENSEX 50 Index
Asia Index Appointed Index Provider for the new ETF comprising shares of CPSE and other corporate entities
S&P Dow Jones Indices and MarketAxess Enter Strategic Agreement to Build U.S. Corporate Bond Indices
S&P Dow Jones Indices Acquires Trucost
S&P 500 Buybacks Fall 21% in Q2 2016
G R S&P Dow Jones Indices to Calculate Four New Custom Indices for Peak Capital Management
S&P U.S. Treasury Bills Index Consultation
Santiago Exchange and S&P Dow Jones Indices Sign Agreement To Develop New Generation of Chilean Indices
S&P Dow Jones Indices Announces Methodology Updates for Long Term Stock Suspensions, Share Freeze Period & In Specie Distributions
S&P 500 Foreign Sales at 44.3%, Lowest Level Since 2006
U.S. Dividends Remain Under Pressure
S&P 500 Q1 Buybacks Jump 12%
Dow Jones Industrial Average Celebrates 120 Years as the World’s Benchmark
S&P Southeast Asia 40 Index Consultation
Groundbreaking JPX/S&P CAPEX & Human Capital Index Launched by Japan Exchange Group, Inc., Tokyo Stock Exchange, Inc. and S&P Dow Jones Indices
S&P Dow Jones Indices and RobecoSAM the First to Launch Indices Using ESG as a Smart Beta Factor
Cobranded Environmental Index Series Introduced by S&P Dow Jones Indices and Tokyo Stock Exchange
Carbon Emissions From S&P 500 Companies Equivalent to Total Produced in France, Germany and UK Combined
S&P/CSE Sector and Industry Group Indices Jointly Launched by S&P Dow Jones Indices, Colombo Stock Exchange
Dividend Increases Post Sharp Decline As Energy Issue Cuts Dominate
S&P Monthly Australian Consumer Price Indicator Introduced by S&P Dow Jones Indices
S&P 500 Low Volatility Target Beta Index Launched; Adds to S&P Dow Jones Indices Growing Family of Smart Beta Indices
S&P DJI: S&P 500 Q4 Buybacks Tick Down 3.1% From Q3 2015, Up 10.0% Year-Over-Year
New Inflation-Linked Index Launched by BM&FBOVESPA and S&P Dow Jones Indices
TSX and S&P Dow Jones Indices Sign Multi-Year Agreement
Innovative Indexing Approach to Manage Uncertainty of Retirement Income Launched by S&P Dow Jones Indices
University of Miami Selects S&P Dow Jones Indices to Calculate New Custom Hybrid Index
S&P Dow Jones Indices Announces Changes to the S&P U.S. Spin-Off Index Consultation
S&P Dow Jones Indices Announces Changes to the S&P U.S. Activist Interest Index
Q4’15 Dividends: Increases Lose Pace, Decreases Dominated by Energy
S&P/JPX Dividend Aristocrats Index Launches in Japan
S&P DJI: S&P 500 Q3 Buybacks Increases 14.5% Over Q2 2015, Up 3.7% Year-Over-Year
Asia Index Private Limited Launches Four S&P BSE Factor Indices
S&P 500 Low Volatility Target Beta Index Launched; Adds to S&P Dow Jones Indices Growing Family of Smart Beta Indices
S&P Dow Jones Indices Appointed by CLSA to Calculate a New Custom Index
Dow Jones Sustainability Europe Diversified High Beta High Dividend Index Launched by S&P Dow Jones Indices
S&P/ASX 200 Futures Index Unveiled by S&P Dow Jones Indices
S&P Dow Jones Indices Unveils S&P/NZX Real Estate Select Index
Three New Climate Change Index Series Launched by S&P Dow Jones Indices and Toronto Stock Exchange
Monthly rebalance announcement for the S&P/NZX New Zealand fixed interest indices
S&P Dow Jones Indices Named “Best Islamic Index Provider” in IFN Service Providers Poll 2015
S&P Dow Jones Indices to Calculate Two New Custom Indices for RIA W.E. Donoghue
Two New Pan Arab Smart Beta Indices Launched by S&P Dow Jones Indices
S&P Dow Jones Indices and Japan Exchange Group/Tokyo Stock Exchange to Introduce Co-branded Smart Beta Index Series in Japan
S&P/JPX JGB VIX Index Introduced by S&P Dow Jones Indices and Japan Exchange Group
S&P Dow Jones Indices Wins Index Provider of the Year at Global Derivatives Awards
U.S. Companies Continue To Slow Pace of Dividend Net Increases
Dow Jones Sustainability South Africa Composite Diversified Index Launched by S&P Dow Jones Indices
Santiago Exchange and S&P Dow Jones Indices Launch First Chilean Sustainability Index; Agree to Explore Broader Indexing Agreement
S&P Dow Jones Indices Recognized in Asia-Pacific Structured Products & Derivatives Awards 2015
Monthly rebalance announcement for the S&P/NZX New Zealand fixed interest indices
S&P DJI: S&P 500 Q2 Buybacks Decline 8.7% Over Q1 2015, Up 13.2% Year-Over-Year
S&P Dow Jones Indices Unveils Headline S&P China 500 Index
Three New Climate Change Index Series Launched by S&P Dow Jones Indices
Real Estate and Financial Services Select Sector Indices Launched
S&P Dow Jones Indices Wins Two Industry Awards for Market Leadership and Innovation
S&P 500 Catholic Values Index Launched by S&P Dow Jones Indices
Asia Index Private Limited launches S&P BSE Dividend Stability Index
S&P Dow Jones Indices Launches Spin-Off, IPO and Activist Interest Indices
S&P Dow Jones Indices and Japan Exchange Group to Launch First Ever Full-Scale Fixed Income Volatility Index in Japan
S&P 500 Foreign Sales Report: Sales to Asia Rise, U.K. Moves Lower, Taxes Paid to U.S. Climbs Dramatically
S&P Dow Jones Indices Statement on Resumption of Trading at NYSE
S&P Dow Jones Indices Statement on NYSE Floor Trading Halt Impact on Previously Announced Changes to the S&P 500
S&P Dow Jones Indices Statement on NYSE Floor Trading Halt
Asia Index Private Limited Launches S&P BSE MidCap Select and S&P BSE SmallCap Select Indices
S&P Dow Jones Indices Launches First of Its Kind Index Tracking the Debt of the S&P 500® Companies
U.S. Companies Slow Pace of Dividend Net Increases
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Indices
S&P Dow Jones Indices Statement on Closure of Greece Banks and Markets
S&P 500 Q1 2015 Buybacks Rise 8.7% Over Q4 2014
Colombia Ministry of Finance Authorizes the Inclusion of the S&P Colombia Select Index into the Local Aggregated Equity Index
Asia Index Private Limited to launch S&P BSE India Manufacturing Index
Environmental and Socially Responsible Index Based on the S&P 500 Launched by S&P Dow Jones Indices
S&P 500 Equal Weight Real Estate Index Launched by S&P Dow Jones Indices
S&P Pan Arab Shariah Balanced Index Family Launched By S&P Dow Jones Indices
S&P/ASX 300 Shareholder Yield Index Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Announces Changes to the S&P/TSX Canadian Indices
New York Knicks Join S&P Dow Jones Indices and Habitat for Humanity New York City to Rebuild Homes Devastated by Hurricane Sandy
S&P 500 Benchmarked Assets Reach $7.8 Trillion; $3.05 Trillion Invested in Products Indexed to S&P DJI Indices
S&P Dow Jones Indices and MSCI Announce Updates to Global Industry Classification Standard (GICS®) Methodology
S&P Dow Jones Indices Licenses Several Indices to AccuShares
The Mexican Stock Exchange and S&P Dow Jones Indices Announce Agreement for Index Licensing, Distribution, and Management of BMV Indices
BM&FBOVESPA and S&P Dow Jones Indices Sign Index Agreement
S&P Dow Jones Indices Launches S&P Access China A Dividend Opportunities Index
S&P Access China A Dividend Opportunities Index Launched by S&P Dow Jones Indices
S&P/NZX 50 High Dividend Index Launched by S&P Dow Jones Indices
Dow Jones Brookfield Global Infrastructure Index Selected as New Labor Pension Fund Benchmark in Taiwan
Family of Global Sovereign Inflation-Linked Bond Indices Launched by S&P Dow Jones Indices
S&P ESG Pan-Europe Developed Sovereign Bond Index Launched by S&P Dow Jones Indices and RobecoSAM
S&P 500 Low Volatility Rate Response Index Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Snaps up Two Awards in Asia Asset Management’s ETF and Indexing Awards 2015
U.S. Companies Slow Pace of Dividend Net Increases
Paulo Sampaio Named Head of Latin America Southern Cone for S&P DJI
S&P GSCI Gold and Silver Inverse Indices Launched by S&P Dow Jones Indices
New Smart Beta ESG Index Launched by S&P Dow Jones Indices
S&P 500 2014 Buybacks Post 16.3% Increase
S&P Dow Jones Indices Voted "Best Index Provider MENA" in IFN Awards Service Providers Poll 2014
S&P Dow Jones Indices and MSCI Announce Revisions to the Global Industry Classification Standard (GICS®) Structure in 2016
Asia Index Private Limited to launch S&P BSE AllCap Index Family
S&P Dow Jones Indices Expands South Korea Index Offering with S&P Korea Dividend Opportunities Index
S&P Dow Jones Indices Introduces Tax-aware Index Solutions in Australia
S&P Dow Jones Indices and NZX Limited Enter Into Strategic Index Agreement
S&P Dow Jones Indices Launches Global Dividend Stability/Low Volatility Smart Beta Index
S&P Dow Jones Indices Wins Best Index Provider at MENA Fund Manager Fund Services Awards
S&P MidCap 400 Dividend Aristocrats Launched by S&P Dow Jones Indices
Seeing Global Opportunity, S&P Dow Jones Indices Sets Aggressive Expansion of its Fixed Income Business
S&P Dow Jones Indices Named 2014 Index Provider of the Year by Asia Asset Management
S&P Dow Jones Indices Adds S&P Japan 500 GIVI Index to Factor-Based Offering for Japan
S&P Dow Jones Indices Adds S&P Quality Nordic Index to its Factor-Based Indices Family
S&P Dow Jones Indices Bolsters its South Africa Factor-Based Index Range with S&P Quality South Africa Index
S&P Dow Jones Indices Selected to Calculate Equity and Fixed Income Indices for ECPI
Strong Dividend Growth Continues As Energy Concerns Grow
S&P 500 Q3 2014 Buybacks Increase 25% Over Q2
$781 Billion in Global ETP AUM Based on Indices Published by S&P Dow Jones Indices
S&P Dow Jones Indices and the Lima Stock Exchange Launch S&P/BVL Peru Select Index
S&P 500 Dividend Aristocrats Named Indexing Product of the Year
S&P Dow Jones Indices Expands South Africa Factor-Based Indices with S&P GIVI South Africa Indices
S&P Dow Jones Indices Expands Factor-Based Index Offering with S&P Momentum Indices
S&P 500 VEQTOR Switch Index Launched by S&P Dow Jones Indices
New S&P Emerging Markets Low Volatility Select Index Licensed to Commerzbank
S&P 500 Low Volatility Enhanced Index Launched by S&P Dow Jones Indices
S&P Brazil Sector GDP Weighted Index Launched by S&P Dow Jones Indices
BM&FBOVESPA and S&P Dow Jones Indices Reach Landmark Index Agreement
S&P Dow Jones Indices and MSCI Announce Revisions to the Global Industry Classification Standard (GICS®) Structure In 2016
S&P Dow Jones Indices, Korea Exchange Announce Agreement on  Index Commercial Licensing and New Equity Indices Launch
Dividend Growth Picks-Up in Third Quarter
S&P Dow Jones Indices and Toronto Stock Exchange Launch Two New Factor Based Indices
S&P 500 Q2 Buybacks Decline 27% From Q1 2014
S&P Dow Jones Indices Wins Index Innovation of the Year Asia Award in Structured Products Asia Awards 2014
S&P Dow Jones Indices and the Lima Stock Exchange Announce Indexing Agreement
Change of Price Source for the S&P/DB ORBIT Indices
Forward and Currency Versions of Dow Jones Commodity Index Launched by S&P Dow Jones Indices
Results Announced for 2014 Dow Jones Sustainability Indices Review; DJSI Celebrates 15 Year Anniversary
S&P Dow Jones Indices, Research Affiliates Join Forces to Launch Dow Jones RAFI Commodity Index
S&P Dow Jones Indices Announces September 2014 Quarterly Rebalance of the S&P TOPIX YEN Index
S&P Dow Jones Indices to Calculate New Custom Hybrid Index for Tiedemann Wealth Management
S&P Dow Jones Indices Named “Best Islamic Index Provider” in IFN Awards Best Service Providers Poll 2014
S&P MILA Pacific Alliance Indices Launched by S&P Dow Jones Indices
S&P Quality Indices Launched by S&P Dow Jones Indices
S&P Dow Jones Indices and the Mexican Stock Exchange Announce Agreement for Index Licensing, Distribution, and Management of BMV Indices
Dividends Growth Slows in Second Quarter: S&P Dow Jones Indices
S&P Dow Jones Indices Introduces Dow Jones Commodity Index; Index Based on Straightforward Design, Equal-Weighted Approach
Healthcare Expenditures for Commercial Plans up 3.2% in the Year to February 2014: S&P Healthcare Claims Indices
S&P Dow Jones Indices Expands its Factor Index Family by Launching Low Beta and Intrinsic Value Weighted Indices
S&P/TSX 60 ESG Index Launched by S&P Dow Jones Indices, RobecoSAM and Toronto Stock Exchange
Asia Index Private Limited Launches S&P BSE India Infrastructure Index
Update: Postponement of All Dow Jones Indices' Adoption of GICS Classification System
S&P Dow Jones Indices Announces Winners of Third Annual SPIVA&reg; Awards Program
S&P Dow Jones Indices Launches Extensive Offering of Regional African Indices
S&P Dow Jones Indices Named Best Islamic Index Provider in The Asset Triple A Islamic Finance Awards 2014
S&P Dow Jones Indices Launches Colombia Select Index; Licenses Index to Horizons for ETF Launch
S&P Dow Jones Indices Continues South Africa Expansion; New Indices Meet Growing Demand for Index Based Investing
First Quarter 2014 Sees Record Number of Dividend Increases
Healthcare Expenditures for Commercial Plans up 3.5% in the Year to November 2013: S&P Healthcare Claims Indices
S&P 500 Stock Buybacks Up 19% in 2013
S&P Dow Jones Indices Selected to Calculate Six Custom Hybrid Indices  for RIA Lunt Capital Management
S&P Dow Jones Indices Website Named Best Index Site of the Year for 2013 by ETF.Com
National Credit Default Rates Fell in February 2014 According to the S&P/Experian Consumer Credit Default Indices
Ex-Single Capped Component Version of S&P GSCI Single Commodities Family Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Expands Commodity Index Family with Forward Versions of S&P GSCI and S&P GSCI Single Capped Commodities
Equal Weight Version of S&P Europe 350 Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Launches New Family of South Africa Indices;  Significantly Expands Presence in South Africa
2013 Best ETF Index Provider of the Year in Asia Awarded to S&P Dow Jones Indices by Asia Asset Management
S&P Europe 350 Low Volatility High Dividend Index Launched by S&P Dow Jones Indices
S&P BDC Index Launched by S&P Dow Jones Indices
S&P Emerging Markets Domestic Demand Index Launched by S&P Dow Jones Indices
Winter Shows No Signs of Cooling in Home Prices According to the S&P/Case-Shiller Home Price Indices
S&P Dow Jones Indices, Taiwan Stock Exchange Announce Strategic Index Development and Co-Branding Agreement
S&P GCC Composite Shariah Dividend Index Launched by S&P Dow Jones Indices
S&P Dow Jones Indices, Korea Exchange Sign Agreement on Collaboration in Global Marketing and Sales of KRX Indices
Healthcare Expenditures for Commercial Plans up 3.2% in the Year to August 2013: S&P Healthcare Claims Indices
Asia Index Private Limited Launches S&P BSE India 10 Year Sovereign Bond Index
Fourth Quarter 2013 Dividend Rate Increases $12.7 Billion
S&P 500 Stock Buybacks Increase In Third Quarter; Buybacks at Their Highest Level Since the Fourth Quarter of 2007
Asia Index Private Limited and S&P Dow Jones Indices Are Exclusive Licensors of the S&P BSE End-of-Day Index Data, Data History, and S&P BSE Intellectual Property Rights
S&P Dow Jones Indices to Launch Five S&P/Valmer Mexico Government Bond Indices
S&P Dow Jones Indices Adds Palestine and Zimbabwe Country Indices
S&P Dow Jones Indices Recaps 2013 Equity Market Performance In Europe, Asia, and Emerging Markets; Casts an Eye Toward 2014
S&P Total China BMI Indices Launched by S&P Dow Jones Indices
S&P 500 Dynamic VEQTOR Index Named Innovation of the Year
First S&P 500-Based ETF Launches in China
All Dow Jones Indices to Adopt GICS Classification System
S&P Dow Jones Indices Licenses Three Indices to SSgA
S&P MILA 40 Index Licensed to Horizons ETFs Group
ASX Launches Futures Product for Trading Equity Market Volatility
Capped Component Version of S&P GSCI Single Commodity Family Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Signs MOU with Korea
ASX Launches Futures Over the Resources and Financial Sectors
Dow Jones Industrial Average Hedged JPY Indices Licensed to Nomura Securities
Third Quarter 2013 Dividend Rate Increases $11.9 Billion
New Index Measuring Healthcare Data on 60 Million Insured Americans Shows Healthcare Costs Rising 3.5% in the Year to May 2013
S&P Dow Jones Indices Expands its S&P GSCI Dynamic Roll Family
Asia Index Pvt Ltd. Chosen to Calculate S&P Custom Indices for Mirae Asset Global Investments
S&P 500 Stock Buybacks Increase In Second Quarter
BSE and S&P Dow Jones Indices Announce the Incorporation of their Joint Venture, Asia Index Pvt. Ltd.
Seeing Additional Growth Opportunities, S&P Dow Jones Indices Opens Office in South Africa
S&P Dow Jones Indices Wins Index Innovation of the Year Asia Award in Structured Products Asia Awards 2013
S&P Dow Jones Indices Will Use NASDAQ's Closing Price for NASDAQ Listed Securities
S&P Dow Jones Indices Using Composite Pricing for NASDAQ Listed Securities
S&P Dow Jones Indices Adds Two All Metals Sector Indices to the S&P GSCI Family
S&P Dow Jones Indices Selected to Calculate Second Custom Index for Independent RIAWilbanks Smith & Thomas
S&P 500 Company Sales in Asia Continue to Increase, as European Sales Remain on the Decline
S&P Brazil Dividend Indices Launched by S&P Dow Jones Indices
S&P 500 Companies Post Record Level of Pension Underfunding
S&P Dow Jones Indices, TMX Group Launch High Income Energy Index
S&P Dow Jones Indices Named Index Provider of the Year By Derivatives Intelligence
Index Industry Association Launches Best Practices Indexing Standards and Gains Three New Members
S&P GSCI Dynamic Roll Capped Component 35/20 Launched by S&P Dow Jones Indices
Roll Weighted Version of the S&P GSCI Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Licenses ex Australia LargeMidCap Indices to SSgA
Second Quarter 2013 Dividend Rate Increases $17.6 Billion
Short and Intermediate Duration Municipal Yield Indices Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Announces Calculation Day Changes for Saudi Arabian and Pan Arab Indices
Submissions Currently Being Accepted for Third Annual S&P Dow Jones Indices SPIVA Awards
S&P 500 Stock Buybacks Increase Slightly in First Quarter
S&P Dow Jones Indices Awarded Best Index Provider by StructuredRetailProducts.com
S&P 500 Stock Covered Call Indices Launched by S&P Dow Jones Indices
S&P Emerging Markets Volatility Short-Term Futures Index Launched by S&P Dow Jones Indices
RobecoSAM and S&P Dow Jones Indices introduce DJSI Diversified Family
S&P Nordic Low Volatility Index Launched by S&P Dow Jones Indices
S&P/ASX Balance Index Series Launched by S&P Dow Jones Indices and the Australian Securities Exchange
MILA Sector Indices Launched by S&P Dow Jones Indices
S&P Dow Jones Indices Launches Three Asian-Language Websites
S&P Dow Jones Indices Wins Intellectual Property Dispute
S&P Korea Low Volatility Index Launched by S&P Dow Jones Indices
S&P 500 Buyback Index Launched by S&P Dow Jones Indices
S&P BSE 500 Shariah First Index Launched by BSE and S&P Dow Jones Indices Strategic Partnership
S&P Dow Jones Indices Licenses Pan Asia Dividend Aristocrats Index to State Street Global Advisors
Risk Weighted Version of the S&P GSCI® Launched by S&P Dow Jones Indices
S&P Dow Jones Indices and Nomura Securities to Create Co-Branded Indices Based on NOMURA-BPI Indices
Canadian Derivatives Clearing Corporation Licensed by S&P Dow Jones Indices to Clear OTC Options Based on S&P/TSX Indices
First Quarter 2013 Dividend Rate Increases $14.5 Billion: S&P Dow Jones Indices
S&P Dow Jones Indices Launches Credit Spread Indices Based on S&P 500; trueEX Licenses Indices to Create Credit Spread Futures Contracts
S&P Global Dividend Aristocrats Index Launched by S&P Dow Jones Indices
S&P 500 Stock Buybacks Decrease in Fourth Quarter of 2012
Home Prices Accelerate in January 2013 According to the S&P/Case-Shiller Home Price Indices
Annual Growth Rates Accelerate in January 2013 According to the S&P Healthcare Economic Indices
National Credit Default Rates Decreased in February 2013 According to the S&P/Experian Consumer Credit Default Indices
S&P Dow Jones Indices Announces Winners of Second Annual SPIVA Awards Program
Home Prices Closed Out a Strong 2012 According to the S&P/Case-Shiller Home Price Indices
RobecoSAM and S&P Dow Jones Indices Introduce DJSI Emerging Markets
Annual Growth Rates Broadly Decelerate in December 2012 According to the S&P Healthcare Economic Indices
S&P Dow Jones Indices and ASX Make S&P/ASX 200 VIX Available in Real-Time
National Credit Default Rates Decreased in January 2013 According to the S&P/Experian Consumer Credit Default Indices
BSE and S&P Dow Jones Indices Announce Strategic Partnership in India FAQ
BSE and S&P Dow Jones Indices Announce Strategic Partnership in India
S&P Dow Jones Indices Launches S&P GIVI Shariah Indices
S&P Dow Jones Indices Awarded Best Index Provider by MENA Fund Manager Magazine
Home Prices Extend Gains According to the S&P/Case-Shiller Home Price Indices
S&P SMIT 40 Index to Serve as Basis for Commerzbank ETF
S&P Dow Jones Indices Designs New Indices for Dhaka Stock Exchange
S&P Dow Jones Indices Awarded Index Provider of the Year in Asia by Asia Asset Management
Annual Growth Rates Decelerate in November 2012 According to the S&P Healthcare Economic Indices
National Credit Default Rates Moved Up in Q4 2012 According to the S&P/Experian Consumer Credit Default Indices
Dow Jones U.S. Select Equal Weight REIT Index Launched by S&P Dow Jones Indices
Fourth Quarter 2012 Dividend Rate Increases $8.4 Billion: S&P Dow Jones Indices
S&P Merger Arbitrage Index Launched by S&P Dow Jones Indices
S&P Dow Jones Indices, TMX Group Launch Preferred Share Laddered and Equal Weight Sector Indices
S&P Dow Jones Indices Releases Latest Index Versus Active Funds Scorecard for Australia
Deceleration in Annual Growth Rates for All Nine Indices in June 2012 According to the S&P Healthcare Economic Indices
The McGraw-Hill Companies, CME Group Announce the Launch of S&P Dow Jones Indices
The McGraw-Hill Companies and CME Group Announce U.S. Department of Justice Antitrust Review Has Been Completed for New S&P Dow Jones Indices Joint Venture
Court Rules in Favor of CBOE, McGraw-Hill and CME Against ISE in Index Options Litigation
S&P Indices Launches BRIC High Yield Index; Risk Control Version Also Launched
S&P Indices Licenses S&P 500 to Bosera Asset Management for Index Fund Launch in China
S&P Indices Launches New LargeMidCap Index for Italy
41 ETFs Based on S&P Indices Launched in Q1 as 2012 Gets Off to Strong Start
New S&P Indices Offer Diversified Style Benchmarks for the Israeli Market
CBOE and S&P Indices Take Action to Enforce Injunction Against ISE Regarding S&P 500 Index Options
New Latin America Infrastructure Index Launched by S&P Indices
S&P Launches Dynamic Asset Exchange Indices
S&P: US Healthcare Costs Rise 6.27% Over the 12-Months Ending November 2010
"""

# long_text = 
"""
Apple Inc.
Microsoft Corporation
Amazon.com Inc.
NVIDIA Corporation
Alphabet Inc. Class A
Alphabet Inc. Class C
Berkshire Hathaway Inc. Class B
Tesla Inc.
Meta Platforms Inc. Class A
UnitedHealth Group Incorporated
Exxon Mobil Corporation
Johnson & Johnson
JPMorgan Chase & Co.
Visa Inc. Class A
Procter & Gamble Company
Mastercard Incorporated Class A
Chevron Corporation
Home Depot Inc.
Eli Lilly and Company
AbbVie Inc.
Merck & Co. Inc.
Broadcom Inc.
PepsiCo Inc.
Coca-Cola Company
Pfizer Inc.
Thermo Fisher Scientific Inc.
Costco Wholesale Corporation
Walmart Inc.
Cisco Systems Inc.
McDonald's Corporation
Bank of America Corp
Salesforce Inc.
Abbott Laboratories
Walt Disney Company
Accenture Plc Class A
Linde plc
Adobe Incorporated
Verizon Communications Inc.
Danaher Corporation
Texas Instruments Incorporated
Comcast Corporation Class A
NextEra Energy Inc.
Philip Morris International Inc.
Netflix Inc.
Bristol-Myers Squibb Company
NIKE Inc. Class B
Advanced Micro Devices Inc.
Oracle Corporation
Wells Fargo & Company
Raytheon Technologies Corporation
AT&T Inc.
United Parcel Service Inc. Class B
QUALCOMM Incorporated
Intel Corporation
Amgen Inc.
ConocoPhillips
Honeywell International Inc.
Intuit Inc.
Union Pacific Corporation
Starbucks Corporation
Lowe's Companies Inc.
Boeing Company
International Business Machines Corporation
Elevance Health Inc.
Prologis Inc.
S&P Global Inc.
Lockheed Martin Corporation
Morgan Stanley
Goldman Sachs Group Inc.
Caterpillar Inc.
Medtronic Plc
Gilead Sciences Inc.
General Electric Company
Booking Holdings Inc.
Deere & Company
CVS Health Corporation
BlackRock Inc.
Stryker Corporation
Mondelez International Inc. Class A
Applied Materials Inc.
American Tower Corporation
ServiceNow Inc.
Analog Devices Inc.
American Express Company
TJX Companies Inc
Intuitive Surgical Inc.
Automatic Data Processing Inc.
Regeneron Pharmaceuticals Inc.
Citigroup Inc.
T-Mobile US Inc.
Progressive Corporation
PayPal Holdings Inc.
Marsh & McLennan Companies Inc.
Vertex Pharmaceuticals Incorporated
Chubb Limited
Altria Group Inc.
Cigna Group
Zoetis Inc. Class A
Southern Company
Duke Energy Corporation
Target Corporation
Charles Schwab Corp
Becton Dickinson and Company
Fiserv Inc.
Boston Scientific Corporation
Schlumberger N.V.
CME Group Inc. Class A
EOG Resources Inc.
Northrop Grumman Corp.
Lam Research Corporation
Aon Plc Class A
Equinix Inc.
Humana Inc.
Micron Technology Inc.
Illinois Tool Works Inc.
Colgate-Palmolive Company
CSX Corporation
Air Products and Chemicals Inc.
Eaton Corp. Plc
Waste Management Inc.
Activision Blizzard Inc.
Intercontinental Exchange Inc.
Marathon Petroleum Corporation
Crown Castle Inc.
Freeport-McMoRan Inc.
Synopsys Inc.
HCA Healthcare Inc
Cadence Design Systems Inc.
3M Company
Estee Lauder Companies Inc. Class A
FedEx Corporation
O'Reilly Automotive Inc.
Sherwin-Williams Company
Moderna Inc.
KLA Corporation
Edwards Lifesciences Corporation
General Mills Inc.
General Dynamics Corporation
Valero Energy Corporation
McKesson Corporation
U.S. Bancorp
Pioneer Natural Resources Company
Public Storage
PNC Financial Services Group Inc.
Sempra Energy
American Electric Power Company Inc.
Ford Motor Company
Dominion Energy Inc
General Motors Company
Phillips 66
Emerson Electric Co.
Dollar General Corporation
AutoZone Inc.
Motorola Solutions Inc.
Moody's Corporation
Norfolk Southern Corporation
Chipotle Mexican Grill Inc.
Roper Technologies Inc.
Amphenol Corporation Class A
Kimberly-Clark Corporation
Occidental Petroleum Corporation
NXP Semiconductors NV
Marriott International Inc. Class A
DexCom Inc.
Truist Financial Corporation
Archer-Daniels-Midland Company
Microchip Technology Incorporated
Exelon Corporation
Corteva Inc
Autodesk Inc.
MSCI Inc. Class A
Fortinet Inc.
Arthur J. Gallagher & Co.
Ecolab Inc.
Biogen Inc.
Newmont Corporation
Agilent Technologies Inc.
Parker-Hannifin Corporation
Monster Beverage Corporation
Travelers Companies Inc.
Arista Networks Inc.
TE Connectivity Ltd.
Trane Technologies plc
Realty Income Corporation
Sysco Corporation
IDEXX Laboratories Inc.
Hess Corporation
Cintas Corporation
Xcel Energy Inc.
MetLife Inc.
Dow Inc.
Johnson Controls International plc
Hershey Company
American International Group Inc.
TransDigm Group Incorporated
L3Harris Technologies Inc
Hilton Worldwide Holdings Inc
Yum! Brands Inc.
Ross Stores Inc.
Charter Communications Inc. Class A
Nucor Corporation
Aflac Incorporated
Constellation Brands Inc. Class A
Centene Corporation
IQVIA Holdings Inc
Capital One Financial Corp
Illumina Inc.
Williams Companies Inc.
Simon Property Group Inc.
PACCAR Inc
Consolidated Edison Inc.
Carrier Global Corp.
Kinder Morgan Inc Class P
Paychex Inc.
Devon Energy Corporation
Welltower Inc.
Warner Bros. Discovery Inc. Series A
Mettler-Toledo International Inc.
Electronic Arts Inc.
Fidelity National Information Services Inc.
Bank of New York Mellon Corp
Otis Worldwide Corporation
ON Semiconductor Corporation
ResMed Inc.
VICI Properties Inc
PPG Industries Inc.
DuPont de Nemours Inc.
Copart Inc.
Ameriprise Financial Inc.
Kroger Co.
Public Service Enterprise Group Inc
Dollar Tree Inc.
Cummins Inc.
Rockwell Automation Inc.
Cognizant Technology Solutions Corporation Class A
WEC Energy Group Inc
AMETEK Inc.
Kraft Heinz Company
Prudential Financial Inc.
Allstate Corporation
Keurig Dr Pepper Inc.
D.R. Horton Inc.
Verisk Analytics Inc
Halliburton Company
Old Dominion Freight Line Inc.
Fastenal Company
ONEOK Inc.
American Water Works Company Inc.
GE Healthcare Technologies Inc.
W.W. Grainger Inc.
Baker Hughes Company Class A
Eversource Energy
ANSYS Inc.
SBA Communications Corp. Class A
Keysight Technologies Inc
Aptiv PLC
CoStar Group Inc.
Republic Services Inc.
Edison International
Global Payments Inc.
Zimmer Biomet Holdings Inc.
AmerisourceBergen Corporation
PG&E Corporation
Ulta Beauty Inc.
State Street Corporation
Tractor Supply Company
Digital Realty Trust Inc.
Enphase Energy Inc.
Corning Inc
Discover Financial Services
Lennar Corporation Class A
Diamondback Energy Inc.
Walgreens Boots Alliance Inc.
Willis Towers Watson Public Limited Company
West Pharmaceutical Services Inc.
Arch Capital Group Ltd.
HP Inc.
Constellation Energy Corporation
CDW Corporation
Gartner Inc.
United Rentals Inc.
T. Rowe Price Group
Equifax Inc.
LyondellBasell Industries NV
eBay Inc.
AvalonBay Communities Inc.
Align Technology Inc.
International Flavors & Fragrances Inc.
Ameren Corporation
Genuine Parts Company
Albemarle Corporation
Quanta Services Inc.
Fortive Corp.
Entergy Corporation
FirstEnergy Corp.
Hartford Financial Services Group Inc.
CBRE Group Inc. Class A
Insulet Corporation
Church & Dwight Co. Inc.
DTE Energy Company
Weyerhaeuser Company
Ingersoll Rand Inc.
Vulcan Materials Company
Extra Space Storage Inc.
Delta Air Lines Inc.
McCormick & Company Incorporated
Baxter International Inc.
Monolithic Power Systems Inc.
Martin Marietta Materials Inc.
PPL Corporation
Cardinal Health Inc.
Hologic Inc.
Laboratory Corporation of America Holdings
Equity Residential
Hewlett Packard Enterprise Co.
Teledyne Technologies Incorporated
First Solar Inc.
M&T Bank Corporation
Dover Corporation
VeriSign Inc.
Coterra Energy Inc.
Alexandria Real Estate Equities Inc.
Clorox Company
CenterPoint Energy Inc.
STERIS Plc
Omnicom Group Inc
Take-Two Interactive Software Inc.
Southwest Airlines Co.
Las Vegas Sands Corp.
Nasdaq Inc.
Cooper Companies Inc.
Darden Restaurants Inc.
Conagra Brands Inc.
Invitation Homes Inc.
CMS Energy Corporation
Northern Trust Corporation
Xylem Inc.
Fifth Third Bancorp
Waters Corporation
Skyworks Solutions Inc.
Cincinnati Financial Corporation
Westinghouse Air Brake Technologies Corporation
Kellogg Company
Mid-America Apartment Communities Inc.
Tyson Foods Inc. Class A
Raymond James Financial Inc.
Regions Financial Corporation
Steel Dynamics Inc.
Ventas Inc.
Fair Isaac Corporation
PerkinElmer Inc.
Amcor PLC
Targa Resources Corp.
Expeditors International of Washington Inc.
J.M. Smucker Company
Principal Financial Group Inc.
Broadridge Financial Solutions Inc.
Atmos Energy Corporation
Molina Healthcare Inc.
Ball Corporation
NVR Inc.
EPAM Systems Inc.
AES Corporation
Quest Diagnostics Incorporated
IDEX Corporation
Marathon Oil Corporation
Huntington Bancshares Incorporated
SolarEdge Technologies Inc.
Teradyne Inc.
FactSet Research Systems Inc.
Zebra Technologies Corporation Class A
FLEETCOR Technologies Inc.
Howmet Aerospace Inc.
Lamb Weston Holdings Inc.
Iron Mountain Inc.
Best Buy Co. Inc.
Garmin Ltd.
Mosaic Company
Tyler Technologies Inc.
FMC Corporation
Evergy Inc.
Jacobs Solutions Inc.
Avery Dennison Corporation
Interpublic Group of Companies Inc.
Cboe Global Markets Inc
Textron Inc.
Everest Re Group Ltd.
Citizens Financial Group Inc.
J.B. Hunt Transport Services Inc.
Paycom Software Inc.
Incyte Corporation
CF Industries Holdings Inc.
United Airlines Holdings Inc.
Brown & Brown Inc.
Bunge Limited
Alliant Energy Corp
LKQ Corporation
MGM Resorts International
NetApp Inc.
Expedia Group Inc.
Essex Property Trust Inc.
Royal Caribbean Group
PTC Inc.
PulteGroup Inc.
Packaging Corporation of America
Etsy Inc.
International Paper Company
MarketAxess Holdings Inc.
W. R. Berkley Corporation
Pool Corporation
Synchrony Financial
Seagate Technology Holdings PLC
Akamai Technologies Inc.
UDR Inc.
Leidos Holdings Inc.
APA Corporation
Teleflex Incorporated
Snap-on Incorporated
Trimble Inc.
Viatris Inc.
Bio-Techne Corporation
Domino's Pizza Inc.
Healthpeak Properties Inc.
Catalent Inc
EQT Corporation
Kimco Realty Corporation
Hormel Foods Corporation
NiSource Inc
Camden Property Trust
Host Hotels & Resorts Inc.
Henry Schein Inc.
Wynn Resorts Limited
Brown-Forman Corporation Class B
Nordson Corporation
Western Digital Corporation
Campbell Soup Company
KeyCorp
Loews Corporation
BorgWarner Inc.
Stanley Black & Decker Inc.
C.H. Robinson Worldwide Inc.
Paramount Global Class B
Jack Henry & Associates Inc.
Juniper Networks Inc.
Masco Corporation
Ceridian HCM Holding Inc.
Celanese Corporation
CarMax Inc.
Fox Corporation Class A
Charles River Laboratories International Inc.
Match Group Inc.
Gen Digital Inc.
Bio-Rad Laboratories Inc. Class A
Live Nation Entertainment Inc.
Carnival Corporation
Molson Coors Beverage Company Class B
Qorvo Inc.
Globe Life Inc.
Eastman Chemical Company
Tapestry Inc.
Caesars Entertainment Inc
Regency Centers Corporation
American Airlines Group Inc.
Pinnacle West Capital Corporation
Rollins Inc.
Allegion Public Limited Company
F5 Inc.
Pentair plc
DENTSPLY SIRONA Inc.
A. O. Smith Corporation
Universal Health Services Inc. Class B
NRG Energy Inc.
Huntington Ingalls Industries Inc.
Robert Half International Inc.
Bath & Body Works Inc.
WestRock Company
Franklin Resources Inc.
Boston Properties Inc.
Advance Auto Parts Inc.
Invesco Ltd.
Federal Realty Investment Trust
V.F. Corporation
Sealed Air Corporation
Whirlpool Corporation
News Corporation Class A
Hasbro Inc.
Assurant Inc.
Generac Holdings Inc.
Organon & Co.
DXC Technology Co.
Comerica Incorporated
Norwegian Cruise Line Holdings Ltd.
Alaska Air Group Inc.
Mohawk Industries Inc.
Ralph Lauren Corporation Class A
DaVita Inc.
Newell Brands Inc
Zions Bancorporation N.A.
Fox Corporation Class B
Lincoln National Corp
First Republic Bank
DISH Network Corporation Class A
News Corporation Class B
"""
max_chars = 15000
text_list = split_text(long_text, max_chars)
print(text_list)

# %% Source Code Split

long_text = """


     
								<!DOCTYPE html>
<html lang="en">
<head>
            <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" charset="utf-8"/> 
<meta charset="UTF-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="description" content="S&P Indices" />
<meta name="keywords" content="" />
<meta http-equiv="cache-control" content="max-age=0" />
<meta http-equiv="cache-control" content="no-cache" />
<meta http-equiv="expires" content="0" />
<meta http-equiv="geo-information" content="[regionKorea]" />
<meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
<meta http-equiv="pragma" content="no-cache" /> 
<meta name="lang-id" content="1" /> 



 
 




		
<title>News & Announcements - Media Center | S&P Dow Jones Indices</title>
<meta name="title"  content="News & Announcements - Media Center | S&P Dow Jones Indices">



<meta name="description"  content="S&P Indices">

<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="google-site-verification" content="bEHlHa-cGSBLgtzembemaaCFKRlgdLBK1-OzOo6U_Uw" />


    				                    <link rel="canonical" href="https://www.spglobal.com/spdji/en/media-center/news-announcements/" />
                                            	    <link rel="alternate" hreflang="x-default" href="https://www.spglobal.com/spdji/en/media-center/news-announcements/" />
    	    <link rel="alternate" hreflang="en" href="https://www.spglobal.com/spdji/en/media-center/news-announcements/" />
    	            				                            	    <link rel="alternate" hreflang="es" href="https://www.spglobal.com/spdji/es/media-center/news-announcements/" />
    	    				                            	    <link rel="alternate" hreflang="zh-hant" href="https://www.spglobal.com/spdji/tc/media-center/news-announcements/" />
    	    				                            	    <link rel="alternate" hreflang="ko" href="https://www.spglobal.com/spdji/kr/media-center/news-announcements/" />
    	    				                            	    <link rel="alternate" hreflang="zh-hans" href="https://www.spglobal.com/spdji/zh/media-center/news-announcements/" />
    	    				                            	    <link rel="alternate" hreflang="ja" href="https://www.spglobal.com/spdji/jp/media-center/news-announcements/" />
    	    				                            	    <link rel="alternate" hreflang="pt" href="https://www.spglobal.com/spdji/pt/media-center/news-announcements/" />
    	    <link type="image/x-icon" rel="icon" href="/spdji/en/app/images/application/global/favicon.ico?v=20230407111630" />
	<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/minified/spdji-css-plugins-bundle.min.css?v=20230407111630" media="all" />	
<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/custom/spindices/font-family.css?v=20230407111630" media="all" />
	<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/style.css?v=20230407111630" media="all" />


	<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/filterable-list.css?v=20230407111630" media="all" />
    <link type="text/css" rel="stylesheet" href="/spdji/en/app/css/index-specialization.css?v=20230407111630" media="all" />
	<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/custom-indices.css?v=20230407111630" media="all" />
	<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/press-room.css?v=20230407111630" media="all" />
<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/custom/spindices/modules.css?v=20230407111630" media="all" />
<link type="text/css" rel="stylesheet" href="/spdji/en/app/css/custom/spindices/images-styles.css?v=20230407111630" media="all" />
    
                <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                })(window,document,'script','dataLayer','GTM-P29G7QS');</script>
				
				<!-- Google Tag Manager -->
               <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
               new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
               j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
               'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
              })(window,document,'script','dataLayer','GTM-NKVB4WM');</script>
               <!-- End Google Tag Manager -->
</head>
<body>
	<section class="wrapper">
		<!-- Header Starts here -->
		<header>
			                        									                         																	                         									

									                         													                         													                         														                         					<div class="header-wrapper js-header js-select-dispatch">
    <div class="sites-link__dropdown" id="site_links" aria-hidden="true">
       <div class="content">
               <ul class="menu first-sub vertical drop-open-menu display-non sites-link__links"  role="menu">
                    <li role="menuitem">
                       <a href="https://www.spglobal.com/en/" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Global">S&P Global</a>
                    </li>
                    <li role="menuitem">
                        <a href="/spdji/en/" class="site-header-link is-current ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Dow Jones Indices">S&P Dow Jones Indices</a>
                    </li>
                    <li role="menuitem">
                        <a href="https://www.spglobal.com/engineering/en/" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&amp;P Global Engineering Solutions">S&amp;P Global Engineering Solutions</a>
                    </li>
                    <li role="menuitem">
                        <a href="https://www.spglobal.com/marketintelligence/en/" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Global Market Intelligence">S&P Global Market Intelligence</a>
                    </li>
                    <li role="menuitem">
                        <a href="https://www.spglobal.com/mobility/en/" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&amp;P Global Mobility">S&amp;P Global Mobility</a>
                    </li>
                    <li role="menuitem">
                        <a href="https://www.spglobal.com/commodity-insights/en" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Global Commodity Insights">S&P Global Commodity Insights</a>
                    </li>
                    <li role="menuitem">
                       <a href="https://www.spglobal.com/ratings/en/" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Global Ratings">S&P Global Ratings</a>
                    </li>
                    <li role="menuitem">
                       <a href="https://www.spglobal.com/esg" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Outbound Link_Division" data-gtm-label="S&P Global Sustainable1">S&P Global Sustainable1</a>
                   </li>
               </ul>
               <div class="sites-link__close">
                   <a href="javascript:void(0);" data-gtm-category="Header" data-gtm-action="Click" data-gtm-label="Close"><i class="fa fa-times"></i> Close</a>
               </div>
       </div>
     </div>    
   <nav class="site-header-nav js-site-header-navigation">
       <!-- BEGINNING: adaptive multi application menu -->
        <div class="top-navigation">
           <ul class="adaptive-dropdown menu site-header js-adaptive-dropdown-menu" role="menubar">
               <li role="menuitem" aria-haspopup="true" aria-label="Sites">
                  <div class="top-navigation-container__left">
                 <div class="sites-link " aria-label="s&amp;p global Divisions">
                   <div class="siteDrop">
                       <a href="javascript:void(0);" class="sites-link__cta" aria-haspopup="true" id="division" aria-expanded="false"> S&P Dow Jones Indices </a>
                       </div>
                   </div>
                   <span class="sites-link__info"> Discover more about S&amp;P Global’s offerings </span>
                   </div>
               </li>
           </ul>
       </div>

       <!-- END: adaptive multi application menu -->
       <!-- BEGINNING: multi language sites menu -->
       <ul class="dropdown menu site-header js-dropdown-menu dropdown--support language-menu drop-open-menu" role="menubar">
           <li role="menuitem" class="is-dropdown-submenu-parent opens-right" aria-haspopup="true" aria-label="Support">
               <a href="#" class="site-header-link ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_English" languageID="1">English</a>
               <ul class="menu submenu is-dropdown-submenu first-sub vertical drop-open-menu" data-submenu="" role="menu" style="">
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/es/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_Spanish">Español (Spanish)</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/pt/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_Portuguese">Português (Portuguese)</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/kr/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_Korean">한국어 (Korean)</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/zh/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_SChinese">简体中文 (Simplified Chinese)</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/tc/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_TChinese">繁體中文 (Traditional Chinese)</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/jp/" class="ignorePopup" data-gtm-category="Header" data-gtm-action="Language" data-gtm-label="Language_Japanese">日本語 (Japanese)</a>
                   </li>
               </ul>
           </li>
       </ul>
       <!-- END: multi language sites menu -->
       <!-- BEGINNING: Main menu -->
       <ul class="dropdown menu site-header js-dropdown-menu dropdown--support about-menu drop-open-menu" role="menubar">
           <li role="menuitem" class="is-dropdown-submenu-parent opens-right" aria-haspopup="true" aria-label="Support">
               <a href="#" class="site-header-link">About</a>
               <ul class="menu submenu is-dropdown-submenu first-sub vertical  drop-open-menu" role="menu">
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/en/about-us" class="ignorePopup" data-gtm-category="Header" data-gtm-action="About" data-gtm-label="About_About Us">About Us</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="https://www.spglobal.com/spdji/en/about-us/our-services" class="ignorePopup" data-gtm-category="Header" data-gtm-action="About" data-gtm-label="About_Our Services">Our Services</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="/spdji/en/media-center/news-announcements" class="ignorePopup" data-gtm-category="Header" data-gtm-action="About" data-gtm-label="About_Press Room">Media Center</a>
                   </li>
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="/spdji/en/contact-us" class="ignorePopup" data-gtm-category="Header" data-gtm-action="About" data-gtm-label="About_Contact Us">Contact Us</a>
                   </li>
               </ul>
           </li>
       </ul>
       <!-- END: Main menu -->
       <!-- BEGINNING: Register/Login menu -->
       <ul class="dropdown menu site-header user login-register">
           <li>
               <a data-open="user-login" id="user-login" href="#" class="site-header-link" aria-controls="user-login" aria-haspopup="true" tabindex="0" data-toggle="modal" data-target="#register-login" data-gtm-category="Header" data-gtm-action="Click" data-gtm-label="Register/Login">
                   <span>Register / Login</span>
                   <picture aria-hidden="true">
                       <source srcset="/spdji/en/app/images/login-register.png 1x, /spdji/en/app/images/login-register2x.png 2x" media="(min-width: 1360px)"/>
                       <img src="/spdji/en/app/images/login-register.png" srcset="/spdji/en/app/images/login-register.png 1x, /spdji/en/app/images/login-register2x.png 2x" alt=""/>
                   </picture>
               </a>
           </li>
       </ul>
       <!-- END: Register/Login menu -->
       <ul class="dropdown menu site-header js-dropdown-menu dropdown--support login-menu" role="menubar">
           <li role="menuitem" class="is-dropdown-submenu-parent opens-right" aria-haspopup="true" aria-label="Support">
               <a id="loggedIn" class="site-header-link">
                   <div class="color-white">Hi&nbsp;<span>User</span></div>
                   <picture aria-hidden="true">
                       <source srcset="/spdji/en/app/images/logged-user.png 1x, /spdji/en/app/images/logged-user.png 2x" media="(min-width: 1360px)"/>
                       <img src="/spdji/en/app/images/logged-user.png" srcset="/spdji/en/app/images/logged-user.png 1x, /spdji/en/app/images/logged-user.png 2x" alt=""/>
                   </picture>
               </a>
               <ul class="menu submenu is-dropdown-submenu first-sub vertical  drop-open-menu" role="menu">
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item">
                       <a href="/spdji/en/dashboard/account-settings/">My Preferences</a>
                   </li>					
                   <li role="menuitem" class="is-submenu-item is-dropdown-submenu-item logout" id="logout">
                       <a>Log out</a>
                   </li>
               </ul>
           </li>
       </ul>
   </nav>
   
   <div class="navigation-wrapper">
       <a href="/spdji/en/" class="logo logo-market-intelligence1" title="S&P Dow Jones Indices" data-gtm-category="Navigation" 
       data-gtm-action="Main Navigation" data-gtm-label="S&P Dow Jones Indices Logo">	    			
           <img class="logo-image" alt="Spdji Logo" src="/spdji/en/app/images/logo.svg" width=200 height=50 />
       </a>
       <nav class="nav-primary">
           <ul class="nav-primary-list">
               <li class="nav-item "><a class="nav-title "   name="indices" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices">Indices</a></li>
               <li class="nav-item"><a class="nav-title "  name="research" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights">Research & Insights</a></li>
               <li class="nav-item"><a class="nav-title "  name="exchange" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships">Exchange Relationships</a></li>
               <li class="nav-item"><a class="nav-title "   name="professional" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources">Professional Resources</a></li>
               <li class="nav-item"><a class="nav-title "   name="governance" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance">Governance</a></li>
           </ul>
       </nav>		
       <button class="button-search is-seleced" data-event-name="search" aria-label="search">
           <svg viewBox="0 0 17.5 17.5" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Search">
               <path d="M12.5,11h-0.8l-0.3-0.3c1-1.1,1.6-2.6,1.6-4.2C13,2.9,10.1,0,6.5,0S0,2.9,0,6.5S2.9,13,6.5,13c1.6,0,3.1-0.6,4.2-1.6l0.3,0.3v0.8l5,5l1.5-1.5L12.5,11z M6.5,11C4,11,2,9,2,6.5S4,2,6.5,2S11,4,11,6.5S9,11,6.5,11z"></path>
           </svg>
           <span></span>
           <span></span>
       </button>
       <div class="mobile-menu-icon">
           <button class="button-menu " aria-label="mobile-menu">
               <span></span>
               <span></span>
               <span></span>
           </button>
       </div>			
   </div>  
   <!-- Mobile megamenu starts here -->  
   <div class="navigation-mobile-wrapper MOBILE-MENU" role="menu" aria-multiselectable="true" style="overflow: auto;">
       <div id="accordion">
           <ul class="vertical menu" id="mobile-menu" data-accordion-menu="">
               <li role="menuitem" class="accordion">					
                   <a data-toggle="collapse" href="#indices-mob" id="mob-indices" role="button" aria-expanded="false"
                       aria-controls="indices-mob" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices">Indices
                       <button aria-hidden="true" class="accordion-icon font-18">
                           <span></span>
                           <span></span></button>
                   </a>
                   <div id="indices-mob" class="collapse lh-16 font-16 mobilemenu">
                       <div>
                           <div class="row">
                               <div class="col-sm-12 submenu">
                                   <h6 class="dropdown-header submenu-header font-12">BY CATEGORY</h6>
                                   <a class="dropdown-item" href="/spdji/en/index-family/equity" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Equity">Equity</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/fixed-income" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Fixed Income">Fixed Income</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/commodities" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Commodities">Commodities</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/strategy" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Strategy">Strategy</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/multi-asset" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Multi-Asset">Multi-Asset</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/esg" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_ESG">ESG</a>
                                   	<a class="dropdown-item" href="/spdji/en/index-family/thematics" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Thematics">Thematics</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/digital-assets" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Digital-Assets">Digital Assets</a>
                                   <a class="dropdown-item" href="/spdji/en/index-family/indicators" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Indicators">Indicators</a>
                                   <a class="dropdown-item" href="/spdji/en/custom-indices/solutions" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Custom">Custom Solutions</a>
                               </div>
                               <div class="col-sm-12 submenu">
                                   <h6 class="dropdown-header submenu-header font-12">BY REGION</h6>
                                   <a class="dropdown-item" href="/spdji/en/regional-exposure/global" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Global">Global</a>
                                   <a class="dropdown-item" href="/spdji/en/regional-exposure/americas" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Americas">Americas</a>
                                   <a class="dropdown-item" href="/spdji/en/regional-exposure/europe" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Europe">Europe</a>
                                   <a class="dropdown-item" href="/spdji/en/regional-exposure/middle-east-africa" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Middle East & Africa">Middle East & Africa</a>
                                   <a class="dropdown-item" href="/spdji/en/regional-exposure/asia-pacific" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Asia Pacific">Asia Pacific</a>
                               </div>
								<div class="col-sm-12 submenu IHS-mobile IHS-header">
									<h6 class="dropdown-header submenu-header font-12">IHS MARKIT INDICES</h6>
									<a class="dropdown-item" href="https://www.spglobal.com/spdji/en/indices/products/iboxx.html" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_iBoxx Bond & Loan Indices ">iBoxx Bond & Loan Indices </a>
									<a class="dropdown-item" href="https://www.spglobal.com/spdji/en/indices/products/esg-sustainable-indices.html" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_ESG/Sustainable Indices">ESG/Sustainable Indices</a>
									<a class="dropdown-item" href="https://www.spglobal.com/spdji/en/indices/products/cds-indices.html" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_Credit Default Swap Indices">Credit Default Swap Indices</a>
									<a class="dropdown-item" href="https://www.spglobal.com/spdji/en/indices/products/cambridge-associates-private-investment-benchmarks.html" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_Private Investment Benchmarks">Private Investment Benchmarks</a>
									<a class="dropdown-item" href="https://www.spglobal.com/spdji/en/indices/products/indices.html" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_More IHS Markit Solutions">See All IHS Markit Solutions</a>
								</div>
                           </div>
                       </div>
                   </div>
               </li>
               <li role="menuitem" class="accordion" aria-haspopup="true">
                   <a data-toggle="collapse" href="#research-mob" role="button" id="mob-research" aria-expanded="false" aria-controls="research-mob" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights">Research & Insights
                       <button aria-hidden="true" class="accordion-icon font-18">
                           <span></span>
                           <span></span>
                       </button>	
                   </a>
                   <div id="research-mob" class="collapse">							
                       <ul class="menu vertical nested submenu is-accordion-submenu is-active" role="menu" aria-hidden="false" data-submenu="">
                           <a class="dropdown-item" href="/spdji/en/research-insights" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Overview">Overview</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/research" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Research">Research</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/commentary" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Commentary">Commentary</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/education" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Education">Education</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/performance-reports" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Performance Reports">Performance Reports</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/spiva" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_SPIVA">SPIVA</a>
                           <a class="dropdown-item" href="/spdji/en/investment-themes/overview" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Investment Themes">Investment Themes</a>
                           <a class="dropdown-item ignorePopup" href="https://www.indexologyblog.com" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Indexology Blog">Blog</a>
                           <a class="dropdown-item" href="/spdji/en/events/webinars" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Events">Events</a>
                           <a class="dropdown-item" href="/spdji/en/research-insights/index-tv" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Index TV">Index TV</a>							
                       </ul>									
                   </div>
               </li>
               <li role="menuitem" class="accordion" aria-haspopup="true">
                   <a data-toggle="collapse" href="#exchange-mob" role="a" id="mob-exchange" aria-expanded="false" aria-controls="exchange-mob" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships">Exchange Relationships
                       <button aria-hidden="true" class="accordion-icon font-18">
                           <span></span>
                           <span></span>
                       </button>
                   </a>
                   <div id="exchange-mob" class="collapse lh-16 font-16 mobilemenu">
                       <div>
                           <div class="row">
                               <div class="col-sm-12 submenu">
                                   <a class="dropdown-item" href="/spdji/en/exchange-relationships" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Overview">Overview</a>
                                   <a class="dropdown-item" href="/spdji/en/exchange-relationships/#north-america" onclick="window.location.href ='/spdji/en/exchange-relationships/#north-america';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_North America">North America</a>
                                   <a class="dropdown-item" href="/spdji/en/exchange-relationships/#latin-america" onclick="window.location.href ='/spdji/en/exchange-relationships/#latin-america';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Latin America">Latin America</a>
                                   <a class="dropdown-item" href="/spdji/en/exchange-relationships/#emea" onclick="window.location.href ='/spdji/en/exchange-relationships/#emea';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_EMEA">EMEA</a>
                                   <a class="dropdown-item" href="/spdji/en/exchange-relationships/#asia-pacific" onclick="location.href ='/spdji/en/exchange-relationships/#asia-pacific';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Asia Pacific">Asia Pacific</a>
                               </div>
                           </div>
                       </div>
                   </div>
               </li>
               <li role="menuitem" class="accordion" aria-haspopup="true">
                   <a data-toggle="collapse" href="#professional-mob" role="button" aria-expanded="false" aria-controls="professional-mob" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources">Professional Resources
                       <button aria-hidden="true" class="accordion-icon font-18">
                           <span></span>
                           <span></span>
                       </button>
                   </a>
                   <div id="professional-mob" class="collapse lh-16 font-16 mobilemenu">
                       <div>
                           <div class="row">
                               <div class="col-sm-12 submenu">
                                   <a class="dropdown-item" href="/spdji/en/landing/professional-resources/financial-advisors" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Financial Advisors">Wealth Managers</a>
                                   <a class="dropdown-item" href="/spdji/en/landing/professional-resources/insurance" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Insurance">Insurance</a>
                                   <a class="dropdown-item" href="/spdji/en/landing/professional-resources/institutional-investors" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Institutional Investors">Institutional Investors</a>
                                   <a class="dropdown-item" href="/spdji/en/landing/professional-resources/defined-contribution" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Defined Contribution">Defined Contribution</a>
                               </div>
                           </div>
                       </div>
                   </div>
               </li>
               <li role="menuitem" class="accordion" aria-haspopup="true">
                   <a data-toggle="collapse" href="#governance-mob" role="button" aria-expanded="false" aria-controls="governance-mob" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance">Governance
                       <button aria-hidden="true" class="accordion-icon font-18">
                           <span></span>
                           <span ></span>
                       </button>
                   </a>
                   <div id="governance-mob" class="collapse lh-16 font-16 mobilemenu">
                       <div>
                           <div class="row">
                               <div class="col-sm-12 submenu">
                                   <a class="dropdown-item" href="/spdji/en/governance" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Overview">Overview</a>
                                   <a class="dropdown-item" href="/spdji/en/governance/regulatory-information" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Regulatory Information">Regulatory Information</a>
                                   <a class="dropdown-item" href="/spdji/en/governance/methodologies" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Methodologies">Methodologies</a>
                                   <a class="dropdown-item" href="/spdji/en/governance/consultations" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Consultations">Consultations</a>
                                   <a class="dropdown-item" href="/spdji/en/governance/corporate-engagement" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Corporate Engagement">Corporate Engagement</a>
                               </div>
                           </div>
                       </div>
                   </div>
               </li>
           </ul>
       </div>
           <div class="site-nav-accordion"></div>
   </div>
   <!-- Mobile megamenu ends here -->   
   <!-- Desktop megamenu comes here -->  
   <div class="navigation-secondary-wrapper DESKTOP-MENU">
       <ul class="navigation-secondary-list">
           <li id="indices" class="nodisplay fade menu">
               <!-- BEGINNING: molecules-secondary-nav.twig -->
               <div class="nav-secondary-list four-column">
                   <span class="nav-secondary-category">BY CATEGORY</span>
                   <a href="/spdji/en/index-family/equity" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Equity">Equity</a>
                   <a href="/spdji/en/index-family/fixed-income" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Fixed Income">Fixed Income</a>
                   <a href="/spdji/en/index-family/commodities" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Commodities">Commodities</a>
                   <a href="/spdji/en/index-family/strategy" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Strategy">Strategy</a>
                   <a href="/spdji/en/index-family/multi-asset" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Multi-Asset">Multi-Asset</a>
               </div>
               <div class="nav-secondary-list four-column">
                   <span class="nav-secondary-category">&nbsp;</span>
                   <a href="/spdji/en/index-family/esg" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_ESG">ESG</a>
                   <a href="/spdji/en/index-family/thematics" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Thematics">Thematics</a>
                   <a href="/spdji/en/index-family/digital-assets" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Digital-Assets">Digital Assets</a>
                   <a href="/spdji/en/index-family/indicators" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Indicators">Indicators</a>
                   <a href="/spdji/en/custom-indices/solutions" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Custom">Custom Solutions</a>
               </div>
               <div class="nav-secondary-list four-column">
                   <span class="nav-secondary-category">By Region</span>
                   <a href="/spdji/en/regional-exposure/global" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Global">Global</a>
                   <a href="/spdji/en/regional-exposure/americas" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Americas">Americas</a>
                   <a href="/spdji/en/regional-exposure/europe" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Europe">Europe</a>
                   <a href="/spdji/en/regional-exposure/middle-east-africa" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Middle East & Africa">Middle East & Africa</a>
                   <a href="/spdji/en/regional-exposure/asia-pacific" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Asia Pacific">Asia Pacific</a>
               </div>
                <div class="nav-secondary-list four-column IHS-header">
                <span class="nav-secondary-category">IHS MARKIT INDICES </span>
                <a href="https://www.spglobal.com/spdji/en/indices/products/iboxx.html" class="IHS-navigation-arrow" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_iBoxx Bond & Loan Indices">iBoxx Bond & Loan Indices</a>
                <a href="https://www.spglobal.com/spdji/en/indices/products/esg-sustainable-indices.html" class="IHS-navigation-arrow" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_ESG/Sustainable Indices">ESG/Sustainable Indices </a>
                
                <a href="https://www.spglobal.com/spdji/en/indices/products/cds-indices.html" class="IHS-navigation-arrow" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_Credit Default Swap Indices">Credit Default Swap Indices</a>
                
                <a href="https://www.spglobal.com/spdji/en/indices/products/cambridge-associates-private-investment-benchmarks.html" class="IHS-navigation-arrow" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_Private Investment Benchmarks">Private Investment Benchmarks</a>
                
                <a href="https://www.spglobal.com/spdji/en/indices/products/indices.html" class="IHS-navigation-arrow font-red" class="font-red" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Indices_Featured_IHS Markit_SEE ALL IHS MARKIT SOLUTIONS">SEE ALL IHS MARKIT SOLUTIONS</a>
            </div>
               <!-- END: molecules-secondary-nav.twig -->
           </li>
           <li id="research" class="nodisplay fade menu research-insights-global">
               <div class="nav-secondary-list wid-25">
                   <span class="nav-secondary-category"></span>
                   <a href="/spdji/en/research-insights" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Overview">Overview</a>
                   <a href="/spdji/en/research-insights/research" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Research">Research</a>
                   <a href="/spdji/en/research-insights/commentary" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Commentary">Commentary</a>
                   <a href="/spdji/en/research-insights/education" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Education">Education</a>
                   <a href="/spdji/en/research-insights/performance-reports" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Performance Reports">Performance Reports</a>
               </div>
               <div class="nav-secondary-list wid-25" >
                   <span class="nav-secondary-category"></span>
                   <a href="/spdji/en/research-insights/spiva" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_SPIVA">SPIVA</a>
                   <a href="/spdji/en/investment-themes/overview" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Investment Themes">Investment Themes</a>
                   <a href="https://www.indexologyblog.com" class="ignorePopup" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Indexology Blog">Blog</a>
                   <a href="/spdji/en/events/webinars" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Events">Events</a>
                   <a href="/spdji/en/research-insights/index-tv" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Research & Insights_Index TV">Index TV</a>
               </div>
               <div class='nav-meta-latest two-column wid-18'><span class='nav-secondary-category'>STAY CONNECTED</span><div class='nav-meta-latest-column two-col'><a  href='https://on.spdji.com/SignUp?src=IDS' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Research & Insights_Featured_STAY CONNECTED_Get our latest research and insights in your inbox.'>Get our latest research and insights in your inbox.</a> <p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://on.spdji.com/SignUp?src=IDS'>Sign Up</a></div></div>	<div class='nav-meta-latest two-column wid-18'><span class='nav-secondary-category'>INDEX DASHBOARDS</span><div class='nav-meta-latest-column two-col'><a  href='https://www.spglobal.com/spdji/en/research-insights/performance-reports' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Research & Insights_Featured_INDEX DASHBOARDS_Performance Analytics at a Glance'>Performance Analytics at a Glance</a> <p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://www.spglobal.com/spdji/en/research-insights/performance-reports'>Access the Latest Dashboards</a></div></div>	
           </li>
           <li id="exchange" class="nodisplay fade">
               <nav class="nav-secondary">
                   <div class="nav-secondary-list">
                       <span class="nav-secondary-category"></span>
                       <a href="/spdji/en/exchange-relationships" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Overview">Overview</a>
                       <a href="/spdji/en/exchange-relationships/#north-america" onclick="window.location.href ='/spdji/en/exchange-relationships/#north-america';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_North America">North America</a>
                       <a href="/spdji/en/exchange-relationships/#latin-america" onclick="window.location.href ='/spdji/en/exchange-relationships/#latin-america';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Latin America">Latin America</a>
                       <a href="/spdji/en/exchange-relationships/#emea" onclick="window.location.href ='/spdji/en/exchange-relationships/#emea';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_EMEA">EMEA</a>
                       <a href="/spdji/en/exchange-relationships/#asia-pacific" onclick="location.href ='/spdji/en/exchange-relationships/#asia-pacific';window.location.reload();" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Exchange Relationships_Asia Pacific">Asia Pacific</a>
                   </div>
                   <div class="nav-meta-latest">							
                   
                   </div>
               </nav>					
           </li>
           <li id="professional" class="nodisplay fade">
               <nav class="nav-secondary">
                   <div class="nav-secondary-list">
                       <span class="nav-secondary-category"></span>
                           <a href="/spdji/en/landing/professional-resources/financial-advisors" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Financial Advisors">Wealth Managers</a>
                           <a href="/spdji/en/landing/professional-resources/insurance" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Insurance">Insurance</a>
                           <a href="/spdji/en/landing/professional-resources/institutional-investors" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Institutional Investors">Institutional Investors</a>
                           <a href="/spdji/en/landing/professional-resources/defined-contribution" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Professional Resources_Defined Contribution">Defined Contribution</a>
                   </div>
                   <div class="nav-meta-latest">
                   <div class='nav-meta-latest-column'><span class='nav-meta-latest-category'>INDEX-LINKED PRODUCTS</span><a href='https://www.spglobal.com/spdji/en/index-linked-products/' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Professional Resources_Featured_INDEX-LINKED PRODUCTS_Explore products linked to our indices.'>Explore products linked to our indices.</a><p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://www.spglobal.com/spdji/en/index-linked-products/'>Find Products</a></div>
                   </div>
               </nav>
           </li>			
           <li id="governance" class="nodisplay fade">
               <nav class="nav-secondary">
                   <div class="nav-secondary-list">
                       <span class="nav-secondary-category"></span>
                       <a href="/spdji/en/governance" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Overview">Overview</a>
                       <a href="/spdji/en/governance/regulatory-information" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Regulatory Information">Regulatory Information</a>
                       <a href="/spdji/en/governance/methodologies" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Methodologies">Methodologies</a>
                       <a href="/spdji/en/governance/consultations" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Consultations">Consultations</a>
                       <a href="/spdji/en/governance/corporate-engagement" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Governance_Corporate Engagement">Corporate Engagement</a>
                   </div>
                   <div class="nav-meta-latest">									
                   <div class='nav-meta-latest-column'><span class='nav-meta-latest-category'>METHODOLOGY INFO</span><a href='https://www.spglobal.com/spdji/en/landing/topic/gics' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Governance_Featured_METHODOLOGY INFO_GICS<sup>®</sup>: Global Industry Classification Standard'>GICS<sup>®</sup>: Global Industry Classification Standard</a> <p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://www.spglobal.com/spdji/en/landing/topic/gics'>Explore</a></div><div class='nav-meta-latest-column'><span class='nav-meta-latest-category'>METHODOLOGY INFO</span><a href='https://www.spglobal.com/spdji/en/landing/topic/market-classification/' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Governance_Featured_METHODOLOGY INFO_S&P DJI Market Classification'>S&P DJI Market Classification</a> <p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://www.spglobal.com/spdji/en/landing/topic/market-classification/'>LEARN MORE</a></div><div class='nav-meta-latest-column'><span class='nav-meta-latest-category'>IHS MARKIT</span><a href='https://www.markit.com/Documentation/Product/Indices' class='nav-meta-latest-link' data-gtm-category='Navigation' data-gtm-action='Main Navigation' data-gtm-label='Governance_Featured_IHS MARKIT_View methodologies, annexes, guides and legal documents.'>View methodologies, annexes, guides and legal documents.</a> <p class='nav-meta-latest-content'></p><a class='link-with-arrow ri-learn-more submenu-link' href='https://www.markit.com/Documentation/Product/Indices'>ACCESS DOCUMENTATION</a></div>
                   </div>
               </nav>
           </li>
       </ul>
   </div>
   <!-- Desktop megamenu ends here -->
   <!-- Search field starts here -->  
   <div class="navigation-search-wrapper" >
       <form action="/spdji/en/search/" name="searchform" novalidate="novalidate">
           <div class="search-input-wrapper global-search">
               <input class="search-input" type="text" data-autocomplete="true" name="query" placeholder="SEARCH BY KEYWORD" >
               <div class="autocompleteOptions search-new"></div>
               <span class="search-input-svg">
                   <svg viewBox="0 0 17.5 17.5" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Search">
                       <path d="M12.5,11h-0.8l-0.3-0.3c1-1.1,1.6-2.6,1.6-4.2C13,2.9,10.1,0,6.5,0S0,2.9,0,6.5S2.9,13,6.5,13c1.6,0,3.1-0.6,4.2-1.6l0.3,0.3v0.8l5,5l1.5-1.5L12.5,11z M6.5,11C4,11,2,9,2,6.5S4,2,6.5,2S11,4,11,6.5S9,11,6.5,11z"></path>
                   </svg>
               </span>				
               <div class="index-finder" >
                   <a href="/spdji/en/index-finder" class="button-white arrow" data-gtm-category="Navigation" data-gtm-action="Main Navigation" data-gtm-label="Search">
                       <span>Index Finder</span>
                   </a>
               </div>
           </div>	
       </form>
   </div>
   <!-- Search field ends here --> 
</div>
<script>
		var invalidCredentials = "Invalid login credentials. Please try again.";
</script>
	<div class="modal fade modal-container" id="register-login" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
		<div class="modal-dialog register-login-container modal-dialog-centered " role="document">
			<div class="modal-content register-login-container">
				<div class="modal-header">
					<button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true"></span>
						<span></span>
					</button>
				</div>
				<div class="modal-body">
					<div class="account-login-form">
						<form id="login-form" class="form-validation" action="#">
														<h2 class="login-form-title">Login</h2>
							<p class="error"></p>
							<div class="login-form-login-wrapper">								
								<ul class="form-field-list">
									<li class="form-field-control">									
										<input type="email" id="email" name="email" value="" class="login-form-input-field email form-field-input" tabindex="1" placeholder=" ">
																				<label for="email" class="form-field-label">Email Address</label>
									</li>
									
									<li class="form-field-control">
										<input type="password" id="password" name="password" class="login-form-input-field form-field-input" tabindex="2" placeholder=" ">
																				<label for="password" class="form-field-label">Password</label>
									</li>
								</ul>
								
																<a data-gtm-category="Register/Login" data-gtm-action="Click" data-gtm-label="Forgot Password" class="login-form-forgot-username-password" id="forgotPasswordLink">Forgot Password</a>
								<button data-gtm-category="Register/Login" data-gtm-action="Click" data-gtm-label="Login" class="form-button btn-red" tabindex="3" type="button" id="login-button">
									<span>Login</span>
								</button>								
							</div>														
						</form>
					</div>
					<div class="login-form-register">
												<h5 class="login-form-register-title">Not Registered?</h5>
												<p class="login-form-register-text">Access exclusive data and research, personalize your experience, and sign up to receive email updates.
							
						</p>
												<a href="/spdji/en/registration/" data-gtm-category="Register/Login" data-gtm-action="Click" data-gtm-label="Register" class="form-button btn-blue" tabindex="0" id="register-link" aria-haspopup="true"><span>Register</span></a>
					</div>	
				</div>
			</div>
		</div>
	</div> 
    <div class="modal fade modal-container user-registration" id="forgot-password" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-modal="true" style="display:none">
		<div class="modal-dialog modal-sm form-frame-register modal-dialog-centered " role="document">
		    <div class="modal-content">
				<div class="modal-header">
					 <button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true"></span>
						<span></span>
					 </button>
				</div>
				<div class="modal-body forgot-password-body">
					<div class="form-frame-columns">
						<div class="form-frame-column-two login-form account-login-form password-login-form">
							<form id="forgot-password-form" class="form-validation"> 
																<h2 class="login-form-title">Forgot Password?</h2> 
								<ul class="form-frame-tab-stage">
									<li class="is-current tab-content" id="first-main-tab">
										<ul class="form-field-list">
																						<li class="form-field-control" style="margin-bottom:5px;">
												<input type="text" class="form-field-input login-form-input-field22 required email" 
												id="forgot_pass_email" tabindex="1" placeholder=" " maxlength="50" 
												name="forgot_pass_email">
												<label for="forgot_pass_email" class="form-field-label">Email<span class="red">*</span></label>
											</li>											
										</ul>
									</li>
									<li>
										<ul class="form-field-list captcha-info">
											<li>
												<div class="captcha-container">
													<div class="captcha captcha-input" style="float:left">
																												<label for="captcha" class="floating-form-fields">
															<input type="text" id="captcha" tabindex="1" value="" name="captchaText" class="form-field-input required" placeholder=" ">								
															<label for="captcha" class="form-field-label">Enter the characters displayed															
															<span class="red">*</span>	
														</label>
														</label>
													</div>
													<div class="captcha" style="margin-top:10px;">
														<img class="captcha-image fleft" src="/spdji/en/Captcha.jpg?0.9479912306391111"> 
														<a href="#" class="refresh-captcha" onclick="$('.captcha-image').attr('src', SPI.PageAjaxMap.captcha + '?' + Math.random());return false;"></a>
													</div>
													<input type="hidden" id="useCaptcha" name="useCaptcha" value="true">
												</div>
											</li>
										</ul>
									</li>
								</ul>
								<div class="form-frame-fixed-foot" style="clear:both">
																		<input type="submit" class="form-button btn-red btn-right" value="Submit >" id="btnForgotPassword" data-gtm-action="Click" data-gtm-label="Forgot Password_Submitted" data-gtm-category="Forgot Password">
								</div>
							</form>
						</div>
						<div class="success-msg nodisplay">
							<p></p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>


	<div class="modal fade modal-container" id="register-pre-login" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
		<div class="modal-dialog register-login-container modal-dialog-centered " role="document">
			<div class="modal-content register-login-container">
				<div class="modal-header">
					<button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true"></span>
						<span></span>
					</button>
				</div>
				<div class="modal-body">
					<div class="account-login-form">
						<form id="login-form-pre-login" class="form-validation" action="#">
														<h2 class="login-form-title">Login</h2>
							<p class="error"></p>
							<div class="login-form-login-wrapper">								
								<ul class="form-field-list">
									<li class="form-field-control">									
										<input type="email" id="pre-login-email" name="pre-login-email" value="" class="login-form-input-field email form-field-input" tabindex="1" placeholder=" ">
																				<label for="pre-login-email" class="form-field-label">Email Address</label>
									</li>
									
									<li class="form-field-control">
										<input type="password" id="pre-login-password" name="pre-login-password" class="login-form-input-field form-field-input" tabindex="2" placeholder=" ">
																				<label for="pre-login-password" class="form-field-label">Password</label>
									</li>
						f		</ul>
								
																<a class="login-form-forgot-username-password" id="Prelogin-forgotPasswordLink">Forgot Password?</a>
								<button class="form-button btn-red" tabindex="3" type="button" id="pre-login-button">
									<span>Login</span>
								</button>								
							</div>														
						</form>
					</div>
					<div class="login-form-register">
												<h5 class="login-form-register-title">Not Registered?</h5>
												<p class="login-form-register-text">Access exclusive data and research, personalize your experience, and sign up to receive email updates.
							
						</p>
												<a href="/spdji/en/registration/" class="form-button btn-blue" tabindex="0" id="register-link" aria-haspopup="true"><span>Register</span></a>
					</div>	
				</div>
			</div>
		</div>
	</div>		</header>
		<!-- Header Ends here -->
		<div class="content-wrapper press-room">
		                            
            <div class="content">
                                                <div class="intro-copy" id="press-room-research">
    <div class="intro-copy-first-column">
        <h1 class="intro-copy-title">Media Center</h1>
    </div>
    <div class="intro-copy-second-column">
        <div>S&P Dow Jones Indices' Media Center is a one-stop source for the latest company news, updates on new and innovative index launches and other announcements. Please contact <a href = "mailto: spdji.comms@spglobal.com">spdji.comms@spglobal.com</a> to schedule interviews with our senior executives and analysts.</div>
        <div>
            <a href="#" class="button-load-more arrow contact-us" data-gtm-category="Introduction" data-gtm-action="Next Step" data-gtm-label="Media Center Contact">
                <span>Contact Us</span>
            </a>
        </div>
    </div>
</div>
<hr class="divider"><div class="sub-nav-mask press-room-sec-nav">
        <nav class="sub-nav-wrapper bottom-nav-wrapper">
            <div class="slider">
                <a href="/spdji/en/media-center/news-announcements/" data-value="news" class="nav-module-tab" data-gtm-category="Navigation" data-gtm-action="Tab" data-gtm-label="News & Announcements">News & Announcements</a>
                <a href="/spdji/en/media-center/featured-research-insights/" data-value="research" class="nav-module-tab" data-gtm-category="Navigation" data-gtm-action="Tab" data-gtm-label="Featured Research & Insights">Featured Research & Insights</a>
                <div class="right-icon-widget">
				                <button class="global-icons button-bookmark" aria-label="bookmark" data-gtm-category="Navigation" data-gtm-action="Next Step" data-gtm-label="Save">   
</button>

  <button class="global-icons button-share global-share-icon dropdown-toggle" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" 

 aria-label="share" 
data-gtm-category="Navigation" data-gtm-action="Next Step" data-gtm-label="Share" >
    <svg  id="Layer_1" x="0px" y="0px" viewBox="0 0 16.2 16.2" enable-background=" 0 0 16.2 16.2" xml:space="preserve">
    <g>
        <defs>
            <rect id="SVGID_1_" x="0.1" y="0.2" width="16" height="15.8"></rect>
        </defs>
        <clipPath id="SVGID_2_">
            <use xlink:href="#SVGID_1_" overflow="visible"></use>
        </clipPath>
        <circle clip-path="url(#SVGID_2_)" fill="none" stroke="#888888" stroke-width="2" cx="3.3" cy="8.1" r="2.2"></circle>
        <circle clip-path="url(#SVGID_2_)" fill="none" stroke="#888888" stroke-width="2" cx="13" cy="12.9" r="2.2"></circle>
        <circle clip-path="url(#SVGID_2_)" fill="none" stroke="#888888" stroke-width="2" cx="13" cy="3.4" r="2.2"></circle>
        <line clip-path="url(#SVGID_2_)" fill="none" stroke="#888888" stroke-width="2" x1="5.2" y1="7.1" x2="11" y2="4.3"></line>
        <line clip-path="url(#SVGID_2_)" fill="none" stroke="#888888" stroke-width="2" x1="10.8" y1="11.8" x2="5" y2="9.1"></line>
    </g>
    </svg>
</button>
  <div class="dropdown-menu share-dropdown-menu" aria-labelledby="dropdownMenuButton">
    <ul>
                    <li><a class="dropdown-item btn-twitter" data-gtm-category="Introduction" data-gtm-action="Next Step" data-gtm-label="Share_Twitter" href="#" data-shareurl="https://twitter.com/intent/tweet?text={title}&url={url}"><i class="fa fa-twitter custom-icon"></i></a></li>     
            <li><a class="dropdown-item btn-facebook" data-gtm-category="Introduction" data-gtm-action="Next Step" data-gtm-label="Share_Facebook" href="#" data-shareurl="http://www.facebook.com/sharer/sharer.php?u={url}&t={title}" ><i class="fa fa-facebook custom-icon"></i></a></li>   
                <li><a class="dropdown-item btn-linkedin" data-gtm-category="Introduction" data-gtm-action="Next Step" data-gtm-label="Share_Linkedin" href="#" data-shareurl="http://www.linkedin.com/shareArticle?mini=true&url={url}&title={title}&source=Standard%26Poor%27s"><i class="fa fa-linkedin custom-icon"></i></a></li>
        <li><a class="dropdown-item btn-email"  data-gtm-category="Introduction" data-gtm-action="Next Step" data-gtm-label="Share_Email" onclick="socialShareIcon();" href="#" data-shareurl=""><i class="fa fa-envelope custom-icon"></i></a></li>  
    </ul>
  </div>                </div>
           </div>
      </nav>
 </div>                <div class="pr-news">
                                                            <div class="indices-divider"></div>
<div class="sub-nav-mask filterable-list-tab">
    <nav class="sub-nav-wrapper bottom-nav-wrapper sub-indices-nav" id="pr-news-subnav">
        <div class="slider">
            <a data-fieldname="contentSubType" data-searchvalue="CorporateNews" data-value="corporateNews" class="nav-module-tab is-current-section" data-gtm-category="Navigation" data-gtm-action="Sub Tab" data-gtm-label="Corporate News">Corporate News</a>
            <a data-fieldname="contentSubType" data-searchvalue="IndexLaunch" data-value="indexLaunch" class="nav-module-tab" data-gtm-category="Navigation" data-gtm-action="Sub Tab" data-gtm-label="Index Launches">Index Launches</a>
            <a data-fieldname="contentSubType"data-searchvalue="Announcement"  data-value="indexNews"  class="nav-module-tab" data-gtm-category="Navigation" data-gtm-action="Sub Tab" data-gtm-label="Index Announcements">Index Announcements</a>
        </div>
    </nav>
</div>

																																																																																						

<div class="filterable-list-simple-four search-enabled pr-news-announcement filterable-list filterable-list-simple-four-2" adv-search-content-type="IndexNews" filterable-list-for="index-news" data-actionurl="/spdji/en/util/redesign/press-room/get-pr-news-announcements-solr-json.dot">
    
	<div class="table-filter">
		<button class="filter-toggle-button">Filters <i class="filter-icon"></i></button>
		<div class="table-filter-content" style="display: none;">
			<div class="table-filter-content-data">
				
				<h3 class="table-filter-data-title">Query</h3>
				<div class="search-query">			
					<input type="text" name="query" placeholder="Search..." class="query-text mobile-view">
					<span class="search-input-svg">
						<svg viewBox="0 0 17.5 17.5">
							<path d="M12.5,11h-0.8l-0.3-0.3c1-1.1,1.6-2.6,1.6-4.2C13,2.9,10.1,0,6.5,0S0,2.9,0,6.5S2.9,13,6.5,13c1.6,0,3.1-0.6,4.2-1.6l0.3,0.3v0.8l5,5l1.5-1.5L12.5,11z M6.5,11C4,11,2,9,2,6.5S4,2,6.5,2S11,4,11,6.5S9,11,6.5,11z"></path>
						</svg>
					</span>
				</div>
			</div>
			<div class="table-filter-content-data">
				<h3 class="table-filter-data-title">Date</h3>
				<ul class="vertical bs-dropdown-wrapper dropdown-radio" data-fieldname="date" data-menu-type="radio" data-submenu="" role="menu">
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "date" data-value="">Default</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "date" data-value="asc">Ascending</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "date" data-value="desc" class="active">Descending</a> </li>                    
				</ul>
			</div>
			<div class="table-filter-content-data press-room-title press-room-title-width dropdown-asia-mobile-hide">
				<h3 class="table-filter-data-title">Title</h3>
				<ul class="vertical bs-dropdown-wrapper dropdown-radio" data-fieldname="title" data-submenu="" role="menu" >
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "title" data-value="">Default</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "title" data-value="asc">A - Z</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"><a  data-field = "title" data-value="desc">Z - A</a> </li>
				</ul>
			</div>
			<div class="table-filter-content-data type-wrapper">
				<h3 class="table-filter-data-title">Type</h3>
				<ul class="vertical bs-dropdown-wrapper dropdown-checkbox" data-fieldname="type" data-submenu="" role="menu" style="">
																	<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="awards" >Awards</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="markets-and-economy" >Markets & Economy</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="other-news" >Other News</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="partnerships" >Partnerships</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="people" >People</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a href="javascript:;" data-field = "type" data-value="products" >Products</a> </li>
															</ul>
			</div>
			<div class="table-filter-content-data theme-wrapper">
				<h3 class="table-filter-data-title">Asset Class</h3>
								   

				<ul id="pressroom-assetclass-dropdown" class="vertical bs-dropdown-wrapper dropdown-checkbox mobileview" data-fieldname="assetclass" data-submenu="" role="menu" >
				</ul>
			</div>                
		</div>
    </div>

    <ul class="filterable-list-dropdown-menu filterable-list-header">
		<li class="filterable-list-cell is-dropdown">
			<div class="bs-dropdown-wrapper dropdown-radio" data-fieldname="date" >
				<a class="dropdown-toggle" data-boundary ="scrollParent" data-toggle="dropdown" aria-expanded="false">
					<span>Date</span>
					<span class="sort-icon desc"></span>
					<span class="caret"></span></a>
					<ul class="dropdown menu is-dropdown-submenu submenu vertical dropdown-menu" data-submenu="" role="menu" >
						<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "date" data-value="">Default</a> </li>
						<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "date" data-value="asc">Ascending</a> </li>
						<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "date" data-value="desc" class="active">Descending</a> </li>
					</ul>
			</div>
		</li>	
		<li class="filterable-list-cell is-dropdown press-room-title press-room-title-width">
			<div class="bs-dropdown-wrapper dropdown-radio" data-fieldname="title" >
				<a class="dropdown-toggle dropdown-asia-hide" data-boundary ="scrollParent" data-toggle="dropdown">
					<span>Title</span>
					<span class="sort-icon desc"></span>
					<span class="caret"></span>
				</a>
				<ul class="dropdown menu is-dropdown-submenu submenu first-sub vertical dropdown-menu" data-submenu="" role="menu" >
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "title" data-value="">Default</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "title" data-value="asc">A - Z</a> </li>
					<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "title" data-value="desc">Z - A</a> </li>

				</ul>
			</div>
		</li>
		<li class="filterable-list-cell is-dropdown type-wrapper">
			<div class="bs-dropdown-wrapper dropdown-checkbox" data-fieldname="type" >
				<a class="dropdown-toggle" data-boundary ="scrollParent" data-toggle="dropdown" aria-expanded="false">
					<span>Type</span>
										<span class="panel-icon"></span>
					<span class="caret"></span></a>
					<ul class="dropdown menu is-dropdown-submenu submenu vertical dropdown-menu" data-submenu="" role="menu" >
																	<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="awards"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_Awards>Awards</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="markets-and-economy"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_Markets & Economy>Markets & Economy</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="other-news"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_Other News>Other News</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="partnerships"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_Partnerships>Partnerships</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="people"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_People>People</a> </li>
																							<li class="is-dropdown-submenu-item is-submenu-item" role="menuitem"> <a  data-field = "type" data-value="products"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Filter" data-gtm-label=Type_Products>Products</a> </li>
																</ul>
			</div>
		</li>	
		<li class="filterable-list-cell is-dropdown theme-wrapper">
			<div class=" bs-dropdown-wrapper dropdown-checkbox" data-fieldname="assetclass" >
				<a class="dropdown-toggle" data-toggle="dropdown" data-boundary ="scrollParent" aria-expanded="false">
				    <span>Asset Class</span>
                    <span class="panel-icon"></span>
					<span class="caret"></span></a>
				<ul id="pr-assetclass" class="dropdown menu is-dropdown-submenu submenu  vertical dropdown-menu " data-submenu="" role="menu" >			
				</ul>
			</div>
		</li>
		<li class="filterable-list-cell " role="menuitem" aria-haspopup="true" aria-label="Search">
			<button class="grid-button-search is-seleced" data-event-name="search" aria-label="search" data-gtm-category="Corporate News_Simple List" data-gtm-action="All Search" data-gtm-label="Search">
				<svg viewBox="0 0 17.5 17.5">
					<path d="M12.5,11h-0.8l-0.3-0.3c1-1.1,1.6-2.6,1.6-4.2C13,2.9,10.1,0,6.5,0S0,2.9,0,6.5S2.9,13,6.5,13c1.6,0,3.1-0.6,4.2-1.6l0.3,0.3v0.8l5,5l1.5-1.5L12.5,11z M6.5,11C4,11,2,9,2,6.5S4,2,6.5,2S11,4,11,6.5S9,11,6.5,11z"></path>
				</svg>
				<span></span>
				<span></span>
			</button>
		</li>
	</ul>
    <div class="filterable-list-search-wrapper">
		<div class="search-input-wrapper">
			<form id="search-form" action="/spdji/en/search/">
				<input type="hidden" name="ContentType" class="selected-tab">
				<input type="text" name="query" placeholder="Search..." class="query-text desktop-view">
				<span class="search-input-svg" data-gtm-category="Corporate News_Simple List" data-gtm-action="All Search" data-gtm-label="Search">
					<svg viewBox="0 0 17.5 17.5">
						<path d="M12.5,11h-0.8l-0.3-0.3c1-1.1,1.6-2.6,1.6-4.2C13,2.9,10.1,0,6.5,0S0,2.9,0,6.5S2.9,13,6.5,13c1.6,0,3.1-0.6,4.2-1.6l0.3,0.3v0.8l5,5l1.5-1.5L12.5,11z M6.5,11C4,11,2,9,2,6.5S4,2,6.5,2S11,4,11,6.5S9,11,6.5,11z"></path>
					</svg>
				</span>
			</form>
		</div>
	</div>
    <div class="data-row-template" style="display:none">
		<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname= "date" class="simple-four-date-field data-item" data-gtm-category="Corporate News_Simple List" data-gtm-action="" data-gtm-label=""></span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="#" class="link data-item" contentidentifier="" contenttitle="" data-fieldname="link">Lorem ipsum dolor sit amet</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span class="data-item" data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Asset Class:</span>
				  <span class="data-item" data-fieldname="assetclass"></span>

			</div>
			<div class="filterable-list-cell download-cell">
				<span class="column-label mobile-only">Download:</span>
				<span class="download-wrapper"><a href="#" class="link data-item" contentidentifier="" contenttitle="" data-fieldname="secondary-link"  data-gtm-category="Corporate News_Simple List" data-gtm-action="Download" data-gtm-label=""><!-- test --><img class="data-item" data-fieldname="download-icon"  src="/spdji/en/app/images/simple-list-pdf-icon.png"></a></span>
			</div>
		</div>	
	</div>
    <!-- Filterable List Data row Wrapper starts -->
	<div class="filterable-list-data-row-wrapper">
		<!-- Filterable List Data Row starts  -->
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Apr 4, 2023</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/corporate-news/article/sp-dow-jones-indices-reports-us-common-indicated-dividend-payments-increased-9-7-billion-during-q1-2023-12-month-gain-was-59-7-billion" class="link" contentidentifier="fe58fb7f-6927-458c-ac07-07f4a697a8da" contenttitle="S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $9.7 Billion During Q1 2023; 12-Month Gain was $59.7 Billion" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $9.7 Billion During Q1 2023; 12-Month Gain was $59.7 Billion"> S&P Dow Jones Indices Reports U.S. Common Indicated Dividend Payments Increased $9.7 Billion During Q1 2023; 12-Month Gain was $59.7 Billion</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Mar 21, 2023</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/corporate-news/article/sp-500-q4-2022-buybacks-tick-up" class="link" contentidentifier="99dc427d-2815-4b40-8e7b-fa40c7b988ea" contenttitle="S&P 500 Q4 2022 Buybacks Tick up, As 2022 Sets A Record" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P 500 Q4 2022 Buybacks Tick up, As 2022 Sets A Record"> S&P 500 Q4 2022 Buybacks Tick up, As 2022 Sets A Record</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Feb 28, 2023</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/index-announcements/article/sp-corelogic-case-shiller-index-decline-continued-in-december" class="link" contentidentifier="c8b8bc44-6bc0-4bb8-a280-a0510e59da7a" contenttitle="S&P CORELOGIC CASE-SHILLER INDEX DECLINE CONTINUED IN DECEMBER" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P CORELOGIC CASE-SHILLER INDEX DECLINE CONTINUED IN DECEMBER"> S&P CORELOGIC CASE-SHILLER INDEX DECLINE CONTINUED IN DECEMBER</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Feb 21, 2023</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/index-announcements/article/sp-experian-consumer-credit-default-indices-show-third-consecutive-increase-in-composite-rate-for-january-2023" class="link" contentidentifier="968e158b-c668-468e-80e9-3c68f27bf8c6" contenttitle="S&P/Experian Consumer Credit Default Indices Show Third Consecutive Increase in Composite Rate for January 2023" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P/Experian Consumer Credit Default Indices Show Third Consecutive Increase in Composite Rate for January 2023"> S&P/Experian Consumer Credit Default Indices Show Third Consecutive Increase in Composite Rate for January 2023</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Jan 31, 2023</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/index-announcements/article/sp-corelogic-case-shiller-index-continued-to-decline-in-november" class="link" contentidentifier="d9ed4a6c-845c-420d-ad3b-ef54afc1ad37" contenttitle="S&P CoreLogic Case-Shiller Index Continued To Decline in November" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P CoreLogic Case-Shiller Index Continued To Decline in November"> S&P CoreLogic Case-Shiller Index Continued To Decline in November</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Dec 27, 2022</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/index-announcements/article/sp-corelogic-case-shiller-index-continued-to-decline-in-october" class="link" contentidentifier="1e7aff73-026a-4198-8e65-26931122e5db" contenttitle="S&P CoreLogic Case-Shiller Index Continued To Decline In October" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P CoreLogic Case-Shiller Index Continued To Decline In October"> S&P CoreLogic Case-Shiller Index Continued To Decline In October</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Dec 19, 2022</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/corporate-news/article/sp-500-buybacks-decline-40-but-energy-buybacks-increase-64-5" class="link" contentidentifier="f247a1e9-c67c-42f0-9f28-d4ea3f49a54f" contenttitle="S&P 500 Buybacks Decline 4.0% but Energy Buybacks increase 64.5%" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P 500 Buybacks Decline 4.0% but Energy Buybacks increase 64.5%"> S&P 500 Buybacks Decline 4.0% but Energy Buybacks increase 64.5%</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Nov 29, 2022</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/index-announcements/article/sp-corelogic-case-shiller-index-continued-to-decline-in-september" class="link" contentidentifier="ae24431e-5885-4e30-8e96-62da5e9745b8" contenttitle="S&P CoreLogic Case-Shiller Index Continued To Decline In September" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P CoreLogic Case-Shiller Index Continued To Decline In September"> S&P CoreLogic Case-Shiller Index Continued To Decline In September</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Sep 14, 2022</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/documents/index-news-and-announcements/spdji-indexed-asset-survey-2021.pdf" class="link" contentidentifier="4b8d5832-0825-4c75-9d6e-67ba708c7493" contenttitle="2021 Annual Survey of Indexed Assets" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Download" data-gtm-label="2021 Annual Survey of Indexed Assets"> 2021 Annual Survey of Indexed Assets</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
						<div class="filterable-list-cell download-cell">
				<span class="column-label mobile-only">Download:</span>
				<span class="download-wrapper">
				<a href="/spdji/en/documents/index-news-and-announcements/spdji-indexed-asset-survey-2021.pdf" class="link" contentidentifier="4b8d5832-0825-4c75-9d6e-67ba708c7493" contenttitle="2021 Annual Survey of Indexed Assets" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Download" data-gtm-label="2021 Annual Survey of Indexed Assets">
				
									<img class="data-item test" data-fieldname="download-icon" src="/spdji/en/app/images/global-icons/pdf-icon.svg">
								</a>
				</span> 
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
				<div class="filterable-list-row data-row">
			<div class="filterable-list-cell">
				<span class="column-label mobile-only" >Date:</span>
				<span data-fieldname="date" class="simple-four-date-field">Aug 30, 2022</span>
			</div>
			<div class="filterable-list-cell press-room-title press-room-title-width">
				<span class="column-label mobile-only">Title:</span>
				<span><a href="/spdji/en/corporate-news/article/sp-dow-jones-indices-completes-its-annual-review-of-adherence-with-iosco-principles-for-financial-benchmarks-2022" class="link" contentidentifier="f7dcbc48-9dcd-44f5-a8c0-f72436e7acad" contenttitle="S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks (2022)" data-fieldname="link" data-gtm-category="Corporate News_Simple List" data-gtm-action="Article" data-gtm-label="S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks (2022)"> S&P Dow Jones Indices Completes Its Annual Review of Adherence with IOSCO Principles for Financial Benchmarks (2022)</a></span>
			</div>
			<div class="filterable-list-cell type-wrapper">
				<span class="column-label mobile-only">Type:</span>
				<span data-fieldname="type"></span>
			</div>
			<div class="filterable-list-cell theme-wrapper">
				<span class="column-label mobile-only">Theme:</span>
				<span data-fieldname="assetclass"></span>
			</div>
					</div>		 
		<!-- Filterable List Data Row Ends  -->	
			</div>
	<!-- Filterable List Data row wrapper ends -->

    <!-- Filterable List Load More Link Row  Starts -->
	<div class="filterable-list-row no-border">
		<div class="filterable-list-cell filterable-list-load-more">
			<a class="button-load-more arrow   disabled " pageNumber="1" data-gtm-category="Corporate News_Simple List" data-gtm-action="Click" data-gtm-label="Load More/All">
				<span>Load More</span>
			</a>
		</div>
	</div>
	<!-- Filterable List Load More Link Row  Ends -->
</div>
<!-- Filterable List ends -->
<hr class="divider"><!-- Contact us Starts -->
     <div class="cus-index-soln-2-col-container contact-us-container">
        <div class="cus-index-soln-2-col-wrapper">
            <h2 class="cust-indx-soln-title">Contact Us</h2>
        </div>
        <div class="cus-index-soln-2-col-wrapper">
            <div class="contact-us-card-wrapper">
                                    <div class="contact-us-card">
					
																		                        <div class="contact-us-title">General</div>
                        							                            <div class="contact-us-name">Media Inquiries</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:spdji.comms@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="spdji.comms@spglobal.com">spdji.comms@spglobal.com</a>
                                </div>
                                                                                                </div>
                                <div class="contact-us-card">
					
																		                        <div class="contact-us-title">Global</div>
                        							                            <div class="contact-us-name">April Kabahar</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:april.kabahar@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="april.kabahar@spglobal.com">april.kabahar@spglobal.com</a>
                                </div>
                                                                                        <div class="contact-us-phone">+1 212 438 7530</div>
                                                                    </div>
                                <div class="contact-us-card">
					
																		                        <div class="contact-us-title">Americas</div>
                        							                            <div class="contact-us-name">Lauren Davis</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:lauren.davis@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="lauren.davis@spglobal.com">lauren.davis@spglobal.com</a>
                                </div>
                                                                                        <div class="contact-us-phone">+1 484 269 7118</div>
                                                    							                            <div class="contact-us-name">Alyssa Augustyn</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:alyssa.augustyn@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="alyssa.augustyn@spglobal.com">alyssa.augustyn@spglobal.com</a>
                                </div>
                                                                                                </div>
                                <div class="contact-us-card">
					
																		                        <div class="contact-us-title">EMEA</div>
                        							                            <div class="contact-us-name">Asti Michou</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:asti.michou@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="asti.michou@spglobal.com">asti.michou@spglobal.com</a>
                                </div>
                                                                                        <div class="contact-us-phone">+44 (0) 20 7176 0311</div>
                                                                    </div>
                                <div class="contact-us-card">
					
																		                        <div class="contact-us-title">Asia Pacific</div>
                        							                            <div class="contact-us-name">Nadja Jiang</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:nadja.jiang@spglobal.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="nadja.jiang@spglobal.com">nadja.jiang@spglobal.com</a>
                                </div>
                                                                                        <div class="contact-us-phone">+852-2841-1017</div>
                                                                    </div>
                                <div class="contact-us-card">
					
																		                        <div class="contact-us-title">India</div>
                        							                            <div class="contact-us-name">Adfactors</div>                                                        
                                                                                        <div class="contact-us-email">
                                    <a href="mailTo:spdji@adfactorspr.com" data-gtm-category="Contact Us" data-gtm-action="Click" data-gtm-label="spdji@adfactorspr.com">spdji@adfactorspr.com</a>
                                </div>
                                                                                        <div class="contact-us-phone">+91 22 67574297</div>
                                                                    </div>
                    </div>
    </div>
</div>
<!-- Contact us Ends -->                </div>
            </div>
		</div>
		<!---footer starts here-->
		<footer class="footer-section">
		                            <!-- Session sessionLanguageId : 1 -->
	<section class="footer-global-wrapper">
    <br/>
<ul class="footer-links-primary">
<li>
<a href="https://www.spglobal.com/spdji/en/about-us" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="About S&P Dow Jones Indices">About S&P Dow Jones Indices
</a>
</li>
<li>
<a href="https://www.spglobal.com/spdji/en/about-us/our-services" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Our Services">Our Services</a>
</li>
<li>
<a href="/spdji/en/media-center/news-announcements" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Media Center">Media Center</a>
</li>
<li>
<a href="/spdji/en/contact-us" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Contact Us">Contact Us</a>
</li>
</ul>

<ul class="footer-links-secondary">
<li>
<a href="https://careers.spglobal.com/ListJobs/ByCustom/Segment/Keyword-S-P-Dow-Jones-Indices" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Outbound Link_Division" data-gtm-label="Careers">Careers</a>
</li>
<li>
<a href="https://www.spglobal.com/en/who-we-are/corporate-responsibility/overview" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Outbound Link_Division" data-gtm-label="Corporate Responsibility">Corporate Responsibility</a>
</li>
<li>
<a href="https://www.spglobal.com/en/who-we-are/our-history" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Outbound Link_Division" data-gtm-label="History">History</a>
</li>
<li>
<a href="http://investor.spglobal.com" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Outbound Link_Division" data-gtm-label="Investor Relations">Investor Relations</a>
</li>
<li>
<a href="https://www.spglobal.com/spdji/en/our-leadership" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Leadership">Leadership</a>
</li>
</ul> 
<div class="footer-bottom">
<ul class="social-links">
<li>
<a href="https://on.spdji.com/SignUp?src=IDS" data-gtm-category="Footer" data-gtm-action="Outbound Link" data-gtm-label="Email">
<i class="fa fa-envelope"></i>
</a>
</li>
<li>
<a href="https://twitter.com/SPDJIndices" data-gtm-category="Footer" data-gtm-action="Outbound Link_Social" data-gtm-label="Twitter">
<i class="fa fa-twitter"></i>
</a>
</li>
<li>
<a href="https://www.linkedin.com/company/s&p-dow-jones-indices" data-gtm-category="Footer" data-gtm-action="Outbound Link_Social" data-gtm-label="LinkedIn"> 
<i class="fa fa-linkedin-square"></i>
</a>
</li>
<li>
<a href="https://www.facebook.com/SP-Dow-Jones-Indices-161630018534/" data-gtm-category="Footer" data-gtm-action="Outbound Link_Social" data-gtm-label="Facebook">
<i class="fa fa-facebook"></i>
</a>
</li>
<li>
<a href="https://www.youtube.com/user/SPIndicesChannel" data-gtm-category="Footer" data-gtm-action="Outbound Link_Social" data-gtm-label="YouTube">
<i class="fa fa-youtube"></i>
</a>
</li>
<li>
<a href="/spdji/en/rss" data-gtm-category="Footer" data-gtm-action="Outbound Link_Social" data-gtm-label="RSS Feed">
<i class="fa fa-rss"></i>
</a>
</li>
</ul>
<ul class="copyright-links">
<li>
© 2023 S&P Dow Jones Indices
</li>
<li>
<a href="https://www.spglobal.com/spdji/en/disclaimers" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Legal Disclaimers">Legal Disclaimers</a>
</li>
<li>
<a href="https://www.spglobal.com/en/terms-of-use" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Terms of Use">Terms of Use</a>
</li>
<li>
<a href="https://www.spglobal.com/en/privacy/privacy-policy-english" class="ignorePopup" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Privacy Policy">Privacy Policy</a>
</li>
<li>
<a href="https://www.spglobal.com/en/cookie-notice" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Cookie Notice">Cookie Notice</a>
</li>
<li>
<a href="https://more.spglobal.com/DoNotSell" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Do Not Sell My Personal Information">Do Not Sell My Personal Information</a>
</li>
<li>
<a href="https://www.spglobal.com/spdji/en/complaints-handling-policy" class="ignorePopup" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Complaints">Complaints</a>
</li>
<li>
<button id="ot-sdk-btn" class="ot-sdk-show-settings" data-gtm-category="Footer" data-gtm-action="Support" data-gtm-label="Cookie Settings">Cookie Settings</button>
</li>
</ul>
</div>
</section> 
		</footer>
		<!--footer ends here-->	
	</section>	
		<div class="modal fade modal-container other-popup global-modal-message-dialog" role="dialog" aria-modal="true" >
	<div class="modal-dialog modal-sm form-frame-register modal-dialog-centered" role="document">
		<div class="modal-content">	
			<div class="modal-header">
				<button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true" data-dismiss="modal"></span>
					<span data-dismiss="modal"></span>
				</button>
			</div>
			<div class="modal-body">							
			</div>
		</div>
	</div>
</div>	
<div class="modal fade modal-container" id="third-party-pop" role="dialog" aria-modal="true" >
	<div class="modal-dialog modal-sm form-frame-register modal-dialog-centered" role="document">
		<div class="modal-content">	
			<div class="modal-header">
				<button type="button" class="btn-close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true" data-dismiss="modal"></span>
					<span data-dismiss="modal"></span>
				</button>
			</div>
			<div class="modal-body">							
			</div>
		</div>
	</div>
</div>	

		                <script>
var urlPrefix = '/spdji/en';
var englishPrefix = '/spdji/en';
var indicesLabel = 'Indices';
var addedLbl = 'Added';	
var oktaClientId = "0oa68hw8x9WzCcY2f4x7";
var oktaURL = "https://secure.login.spglobal.com";
var oktaIssuerURL = "https://secure.login.spglobal.com/oauth2/spglobal";
var oktaAccessToken = "";
var caseShillerformattedFetchedDate ="index-detail.caseshiller-fetched-date"; 
</script>
<script src="/spdji/en/app/js/okta-auth-js.min.js" type="text/javascript"></script>
	<script src="/spdji/en/app/js/minified/spdji-js-plugins-bundle.min.js" type="text/javascript"></script>


<script>
var countrySelect = "Select";
var jsSiteLabels = {};
jsSiteLabels.SavePageMap = {
	pageSaved : "Page Saved!"
}
jsSiteLabels.LoginMap = {
	giveLoginDetailsError : "Please enter your registered email address and password",
	accountLockedError : "Your account has been temporarily locked because you have exceeded the maximum number of login attempts. Please refresh the page in 15 minutes and try again."
}
jsSiteLabels.ForgotPasswordMap = {
	emailSentFollowInstructions :"If an account is associated with the email address provided, you will receive an email message with instructions on how to reset your password."
}
jsSiteLabels.ChangePasswordMap = {
	passWordChangeSuccess : "Your password has been reset.",
	resetPasswordTitle : "Reset Your Password?",
	tryResetPassword : "Reset Password",
	trychangePasssword :"Try again"
}
jsSiteLabels.UserLoginModalMap = {
	saveIndex :"Login to Save This Index",
	showSavedSearches : "Login to View Your Saved Searches",
	showRecentSearches :"Login to View Your Recent Searches",
	saveSearch : "Login to Save This Search",
	showSavedCriteria : "Login to View Your Saved Criterias",
	saveIFCriteria : "Login to Save this Search Criteria",
	showIndices :"Login to View Your Indices",
	savePage : "Login to Save This Page",
	logintoDownload : "Log In to Access Data",
	logintoDownloadPremiumData : "Log In to Access Premium Content",
	loginPromptPremiumDataAlert : "Access exclusive data and research, personalize your experience, and sign up to receive email updates.",
	loginMethodologyAddToRegister: "Login to Submit Request"
	
}
jsSiteLabels.EventRegistrationMap = {
	registrationSaved : "Your registration details are saved. Please click anywhere to continue"
}
jsSiteLabels.ServerErrorMap = {
	troubleInteractingWithServer :"Trouble interacting with server"
}
jsSiteLabels.indexFinderErrorMap = {
	noFactsheetDocument :"No Factsheet available for this index",
	noMethodologyDocument : "No Methodology document available for this index",
	noSelectedIndicesToExport :"No indices selected for export",
	emptySearchTerm : "Please provide the keyword"
}
//modules.js related labels
var jsModulesLabels = {};
jsModulesLabels.UserRegistrationMap = {
	stepOneValidationOne : "Please select your professional profile and country and agree to the terms and conditions.",
	stepOneValidationTwo :"Please agree to the terms and conditions.",
	stepOneValidationThree : "Please select your professional profile.",
	registrationServerError :"Registration couldn't be completed at this time. Trouble interacting with server.",
	registrationSuccess :"Registration Successful",
	continueText : "Continue",
	registerStepTwoOfTwo : "REGISTER: STEP 2 OF 2"
}
jsModulesLabels.UserSettingsInitMap = {
	subsRequired: "Your selection to opt in or opt out is required.",
	settingsUpdated : "Your settings have been updated. Please click anywhere to continue."
}
jsModulesLabels.TermsOfUse = {
	errorMessage : "To continue, please click and read our Terms of Use.",
	acknowledgementRequired :"You must click the acknowledgement box to continue."
}
jsModulesLabels.SurveyValidationMessage = {
	surveySuccessMessage : "Survey has been submitted successfully.",
	surveyErrorMessage :"Error while saving consultation survey form."
}
jsModulesLabels.MySnpMap = {
	noSavedIndices :"You have no saved indices.",
	noSavedPages : "You have no saved pages."
}
jsModulesLabels.ShowErrorMap = {
	errorMessage :"Error:"
}
jsModulesLabels.ShareByEmail = {
	emailSent : "Email Sent.",
	emailNotValid : "Please enter a valid email address"
}
jsModulesLabels.ClientServicesMap = {
	requestSubmitted : "Thank you. Your request has been submitted."
}
jsModulesLabels.FeedbackMap = {
	thankYouMessage :"Thank you for your valuable feedback."
}
jsModulesLabels.ResetPasswordMap = {
	resetSuccessMessage : "Your password was reset successfully",
	continueText :"Continue"
}
jsModulesLabels.ServerError = {
	troubleInteractingWithServer : "Trouble interacting with server"
}
var searchQueryLabel = {};
searchQueryLabel.searchQueryMap = {
	searchText : "Search by Keyword",
	paginationOf :"of"
}
var validationErrorMessges = function(){
	var msg = $.validator.messages;
	msg.required = "This field is required",
	msg.email= "Please enter a valid email address",
	msg.url= "Please enter a valid URL",
	msg.date= "Please enter a valid date",
	msg.dateISO="Please enter a valid date (ISO)",
	msg.number="Please enter a valid number",
	msg.digits= "Please enter only digits",
	msg.equalTo= "Please enter the same value again",
	msg.accept= "Please enter a value with a valid extension",
	msg.maxlength="Please enter no more than {0} characters",
	msg.minlength="Please enter at least {0} characters",
	msg.rangelength="Please enter a value between {0} and {1} characters long",
	msg.range= "Please enter a value between {0} and {1}",
	msg.max= "Please enter a value less than or equal to {0}",
	msg.min= "Please enter a value greater than or equal to {0}"
}
jsModulesLabels.signUpForEmailUpdates = {
	thankYouMessage : "Thank you for signing up."
}
</script>	<script src="/spdji/en/app/js/script.js" type="text/javascript"></script>




<script src="/spdji/en/app/js/pr-news-announcement.js" type="text/javascript"></script>
<script src="/spdji/en/app/js/press-room.js?v=20230407111630" type="text/javascript"></script>
<script src="/spdji/en/app/js/pr-featured-reasearch-insights.js" type="text/javascript"></script>
<script>
$(document).ready(function(){
	var s =  new SPI.modules.prFilterableList(".filterable-list-simple-four.pr-news-announcement");
  s.init();
  SPI.PressRoomFeaturedRI();
});
</script>
<script src="/spdji/en/app/js/trunk8.js"></script>
<script type="text/javascript">	
	SPI.currentPage.url = "/media-center/news-announcements/";		

	SPI.currentPage.title = "News & Announcements";
	SPI.currentPage.type = "PAGE_INODE";
	SPI.currentPage.id = "32b7b034-5757-4ec0-ba1b-247dd5ef96bf";
	//SPI.currentPage.languageId = "1";
	SPI.currentPage.languageId = "1";
	SPI.currentPage.pageState = false;
	SPI.currentPage.indexIdForReference = 0;
	SPI.currentPage.articleSpecificShare = "https://www.spglobal.com/spdji/en/";
	SPI.currentPage.sharePageSpecificTitle = "News%20%26%20Announcements%20-%20Media%20Center%20%7C%20S%26P%20Dow%20Jones%20Indices";
	SPI.currentPage.emailPageSpecificURL = "media-center/news-announcements";
	SPI.currentPage.globalShare = "https://www.spglobal.com/spdji/en/";
				SPI.currentPage.mySPIndicesUrl = window.location.origin;
	SPI.currentPage.applicationUrl = window.location.origin + urlPrefix;
		SPI.PageAjaxMap.loginUserValidate = "https://login.spglobal.com/oam/server/auth_cred_submit"; 
	// Variable declared for 14 min 
    SPI.user.hideLoginTimer = 300000;  
	SPI.user.sso = {};
	SPI.currentInstanceName = "LOCALHOST";
			SPI.announcementDRPopupFlag = false;  
					SPI.announcementGroupId = 353544;
				
			SPI.user.userState = false;
		SPI.user.sso.ssoPostLoginActionInd=false;
			var regionsForPersonalization = "[regionKorea]";
			SPI.internalDomainReferences = ["spindices", "standardandpoors", "mcgraw-hill", "djindexes", "djaverages", "seemoreindices", "event.on24.com", "go.spglobal.com", "spdji.com","mhfi","spglobal","indicesweb.ihsmarkit","content.markitcdn","cdn.ihsmarkit","markit","ihsmarkit.com"];
				SPI.excludedExternalLinks = ["http://twitter.com/hsilverb", 
"https://twitter.com/SPDJIndices",
"http://twitter.com/Dave_Guarino",
"http://www.mhfi.com/",
"http://www.mhfi.com/innovation_behind_the_index",
"https://www.mhfi.com/innovation_behind_the_index",
"http://www.youtube.com/user/SPIndicesChannel", 
"http://www.linkedin.com/groups?gid=2426754&trk=myg_ugrp_ovr",
"http://www.facebook.com/pages/SP-Indices/161630018534",
"http://www.housingviews.com",
"http://www.spvixviews.com",
"http://www.indexologyblog.com",
"https://www.indexologyblog.com",
"http://www.standardandpoors.com",
"http://feedproxy.google.com",
"http://app.info.standardandpoors.com",
"http://spindices.webex.com",
"https://spindices.webex.com",
"http://itunes.apple.com/us/podcast/s-p-indices-your-indexing",
"http://www.mcgraw-hill.com/site/careers/college-students",
"https://mh.taleo.net/careersection/10020/jobsearch.ftl?lang=en",
"http://www.spdji.com",
"http://careers.mhfi.com/ListJobs/ByCustom/Corporate-Brand/Keyword-S-P-Dow-Jones-Indices/",
"http://www.djindexes.com",
"http://www.djaverages.com",
"http://www.spice-indices.com",
"http://www.sp-indexdata.com",
"http://now.eloqua.com",
"http://now.eloqua.com/es.asp?s=795&e=690209",
"http://now.eloqua.com/es.asp?s=795&e=700582&elq=9a224591f0a54ac3a96179fc85581a6a",
"http://www.facebook.com/sharer.php",
"http://twitter.com/home?status=",
"formstack.com",
"asset.tv/",
"https://www.spice-indices.com",
"https://www.spglobal.com",
"http://www.spglobal.com",
"https://www.youtube.com/user/McGrawHillFinancial",
"https://www.youtube.com/channel/UCg1TzTKsU6CGEa5OlS0SC3Q",
"http://www.linkedin.com/",
"http://html5.epaperflip.com/",
"http://link.videoplatform.limelight.com",
"https://www.youtube.com/playlist?list=PLdv2EjukkSMGuPGGZXyPY1m4RG21h3bLc",
"https://www.trucost.com/",
"https://indices.kensho.com/",
"https://embed.vidyard.com/",
"https://play.vidyard.com/",
"https://www.youtube.com/channel/UCDGhESnNliw6tgFEiK0jLGQ",
"https://cifp.zoom.us/webinar/register/",
"https://ihsmarkit.com/products/indices.html",
"https://www.linkedin.com/",
"https://ihsmarkit.com/"];
		SPI.user.sso.ssoEnabledIndicator = false;
			SPI.user.sso.ssoEnabledIndicator = true;
							SPI.user.sso.hostCheckCompletionInd = false;
							SPI.user.sso.urlargs="https%3A%2F%2Fwww.spglobal.com%2Fspdji%2Fen%2F%2Fidmsso2%2FTokenToCookieBuilder%3Fdm%3D.spindices.com%26tg2%3D%2Fids%2Fidm-sso-confirmation%2Fsso-confirmation.dot";
									var localeCountryCode = "US";
		
				SPI.solrScore = false;
	</script><!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-P29G7QS"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NKVB4WM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

        <script>
    $(document).ready(function () {
	        SPI.externalLinks();
	    });
</body>
</html>"""
# %% PDF extract
# %% Source 
"""
 - wts 1 : <a href="/spdji/en/documents/indexnews/announcements/20230406-1463457/1463457_mediareleaseadditiontothes&amp;pbsesmeipoindex20230406.pdf" 
         class="link data-item" contentidentifier="" contenttitle="" data-fieldname="secondary-link" 
         data-gtm-category="Index Announcements_Simple List" data-gtm-action="Download" 
         data-gtm-label="Addition to the S&amp;P BSE SME IPO Index" target="_blank" 
         gtm-content-type="Index News - Index Announcements"><!-- test -->
         <img class="data-item" data-fieldname="download-icon" 
         src="/spdji/en/app/images/global-icons/pdf-icon.svg"></a>
         
         : body > section > div > div > div.pr-news > div.filterable-list-simple-four.search-enabled.pr-news-announcement.filterable-list.filterable-list-simple-four-2 > div.filterable-list-data-row-wrapper > div:nth-child(1) > div:nth-child(5) > span.download-wrapper > a
         
- wts 2 : <a href="/spdji/en/documents/index-news-and-announcements/imbaconsultationonhsbcemfxrub4-5-2023.pdf" 
        class="link data-item" contentidentifier="" contenttitle="" data-fieldname="secondary-link" 
        data-gtm-category="Index Announcements_Simple List" data-gtm-action="Download" 
        data-gtm-label="IHS Markit Benchmark Administration Limited Consultation 
        on Removing Russian Ruble from the Universe of Eligible Currencies 
        for the HSBC EM FX Indices" target="_blank" 
        gtm-content-type="Index News - Index Announcements"><!-- test -->
        <img class="data-item" data-fieldname="download-icon" 
        src="/spdji/en/app/images/global-icons/pdf-icon.svg"></a>
        
        : body > section > div > div > div.pr-news > div.filterable-list-simple-four.search-enabled.pr-news-announcement.filterable-list.filterable-list-simple-four-2 > div.filterable-list-data-row-wrapper > div:nth-child(2) > div:nth-child(5) > span.download-wrapper > a
"""

max_length = 15000

def split_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

split_texts = split_text(long_text, max_length)



for index, part in enumerate(split_texts):
    print(f"Part {index + 1}:\n{part}\n")