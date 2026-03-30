import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import altair as alt
import csv

#with open("ticker_biotech.csv", mode="r") as csv_file:
 #   csv_reader = reader(csv_file)
  #  BIOTECH = list(csv_reader)
    
#DEFAULT_BIOTECH = ["ABBV","BMS","PFE"]


cols = st.columns([1, 3])
# Will declare right cell later to avoid showing it when no data.

STOCKS = ["AAPG","AARD","ABBV","ABCL","ABEO","ABOS","ABSI","ABT","ABUS","ABVC","ABVX","ACAD","ACB","ACET","ACH","ACHC","ACHV","ACIU","ACLX","ACON","ACONW","ACRS","ACRV","ACTU","ACXP","ADAG","ADCT","ADGM","ADIL","ADMA","ADPT","ADTX","ADUS","ADVB","ADXN","AEMD","AEON","AGEN","AGIO","AGL","AGMB","AGPU","AHCO","AIDX","AIM","AIMD","AIRS","AIXC","AKAN","AKBA","AKTS","AKTX","ALBT","ALC","ALDX","ALEC","ALGN","ALGS","ALHC","ALKS","ALLO","ALLR","ALMS","ALNY","ALT","ALVO","ALVOW","ALXO","ALZN","AMGN","AMIX","AMLX","AMPH","AMRN","AMRX","AMS","ANAB","ANGO","ANIK","ANIP","ANIX","ANL","ANNX","ANRO","ANTX","ANVS","AORT","APGE","APLM","APLMW","APLS","APM","APRE","APT","APUS","APVO","APYX","AQST","ARAY","ARCT","ARDT","ARDX","ARGX","ARMP","ARQT","ARTL","ARTV","ARVN","ARWR","ASBP","ASBPW","ASMB","ASND","ASRT","ATAI","ATEC","ATHE","ATNM","ATOS","ATPC","ATRA","ATRC","ATYR","AUNA","AUPH","AURA","AUTL","AVAH","AVBP","AVIR","AVNS","AVR","AVTX","AVXL","AXGN","AXSM","AYTU","AZN","AZTR","BAX","BBIO","BBLG","BBLGW","BBNX","BBOT","BCAB","BCAX","BCDA","BCRX","BCTX","BCTXZ","BCYC","BDMD","BDMDW","BDRX","BDSX","BDTX","BDX","BEAM","BEAT","BEATW","BFLY","BFRG","BFRGW","BFRI","BFRIW","BGLC","BGM","BHC","BHVN","BIAF","BIAFW","BIIB","BIOA","BIVI","BJDX","BKD","BKHA","BKHAR","BLCO","BLFS","BLLN","BLRX","BLTE","BLUWU","BMEA","BMGL","BMRA","BMRN","BMY","BNR","BNTC","BNTX","BOLD","BOLT","BON","BRNS","BRTX","BSX","BTAI","BTI","BTMD","BTSG","BTSGU","BTTC","BVS","BWAY","BYSI","CABA","CADL","CAH","CAI","CALC","CANF","CAPR","CAPS","CARL","CATX","CBIO","CBLL","CCCC","CCEL","CCM","CDIO","CDIOW","CDNA","CDRE","CDT","CELC","CELU","CGC","CGEM","CGEN","CGON","CGTX","CHE","CHRS","CI","CING","CINGW","CLDI","CLDX","CLGN","CLLS","CLNN","CLOV","CLPT","CLRB","CLYM","CMIIU","CMMB","CMND","CMPS","CMPX","CNC","CNMD","CNSP","CNTA","CNTB","CNTN","CNTX","COCH","COCP","COEP","COEPW","COGT","COLL","CON","COO","COR","CORT","COSM","COYA","CPHI","CPIX","CPRX","CRBP","CRBU","CRDF","CRDL","CRIS","CRL","CRMD","CRNX","CRON","CRSP","CRVO","CRVS","CSBR","CSTL","CTMX","CTNM","CTOR","CTSO","CTXR","CUE","CUPR","CURX","CV","CVKD","CVM","CVRX","CYCN","CYH","CYPH","CYRX","CYTK","DARE","DAWN","DBVT","DCGO","DCOY","DCTH","DERM","DFTX","DGX","DMAC","DNA","DNLI","DNTH","DOMH","DRIO","DRMA","DRMAW","DRTS","DRTSW","DRUG","DSGN","DTIL","DVA","DWTX","DXCM","DXR","DYAI","DYN","EBS","ECOR","EDAP","EDIT","EDSA","EHAB","EHC","EIKN","ELAB","ELAN","ELDN","ELMD","ELTX","ELUT","ELV","ELVN","EMBC","ENGN","ENGNW","ENLV","ENOV","ENSC","ENSG","ENTA","ENTX","ENVB","EOLS","EPRX","EQ","ERAS","ERNA","ESLA","ESPR","ESTA","ETON","EUDA","EUDAW","EVAX","EVMN","EVO","EW","EWTX","EXAS","EXEL","EXOZ","EYE","FATE","FBIO","FBIOP","FBLG","FBRX","FDMT","FEED","FEMY","FENC","FHTX","FLGT","FMS","FOLD","FONR","FRMM","FTLF","FTRE","FULC","GALT","GANX","GCTK","GDTC","GEHC","GELS","GENB","GERN","GH","GHRS","GILD","GKOS","GLMD","GLPG","GLSI","GLTO","GLUE","GMAB","GMED","GNLX","GNPX","GNTA","GOSS","GOVX","GPCR","GRAL","GRCE","GRDX","GRFS","GRI","GSK","GTBP","GUTS","GYRE","HAE","HALO","HCA","HCM","HCSG","HCWB","HELP","HIMS","HIND","HKPD","HLF","HOLX","HOTH","HOWL","HRMY","HROW","HRTX","HSCS","HSCSW","HSDT","HSIC","HTFL","HUM","HUMA","HUMAW","HURA","HWH","HYFT","HYPD","HYPR","IART","IBIO","IBO","IBRX","ICCC","ICCM","ICLR","ICU","ICUCW","ICUI","IDXX","IDYA","IFRX","IGC","IINN","IKT","ILMN","IMA","IMCC","IMCR","IMDX","IMMP","IMMX","IMNM","IMNN","IMRN","IMRX","IMTX","IMUX","IMVT","INAB","INBS","INBX","INCR","INCY","INDP","INDV","INFU","INGN","INKT","INM","INMB","INMD","INNV","INO","INSM","INSP","INTS","INVA","IOBT","IONS","IOVA","IPEX","IPHA","IPSC","IQV","IRD","IRIX","IRMD","IRON","IRTC","IRWD","ISPC","ISPR","ISRG","ITGR","ITOC","ITRM","IVA","IVF","IVVD","IXHL","JAGX","JANX","JAZZ","JBIO","JNJ","JSPR","JSPRW","JUNS","KALA","KALV","KAPA","KIDS","KLRS","KLTO","KLTOW","KMDA","KMTS","KNSA","KOD","KPRX","KPTI","KRMD","KROS","KRRO","KRYS","KTTA","KTTAW","KURA","KYMR","KYNB","KYTX","KZIA","KZR","LAKE","LBRX","LCTX","LEGN","LENZ","LEXX","LFCR","LFMD","LFMDP","LFST","LFVN","LFWD","LGND","LGVN","LH","LITS","LIVN","LIXT","LLY","LMAT","LMRI","LNAI","LNSR","LNTH","LONA","LPCN","LQDA","LRMR","LSTA","LTRN","LUCD","LUCY","LUCYW","LUNG","LXEO","LXRX","LYEL","LYRA","MAIA","MANE","MASI","MAZE","MBAI","MBIO","MBOT","MBRX","MBX","MCK","MCRB","MD","MDAI","MDAIW","MDGL","MDLN","MDT","MDWD","MDXG","MDXH","MEDP","MEHA","MENS","MESO","MGNX","MGRX","MGTX","MGX","MIRA","MIRM","MIST","MLSS","MLTX","MLYS","MMED","MMM","MMSI","MNKD","MNOV","MNPR","MO","MODD","MOH","MOLN","MOVE","MPLT","MREO","MRK","MRKR","MRNA","MRVI","MSA","MSLE","MTEX","MTNB","MTVA","MXCT","MYGN","MYNZ","MYO","NAGE","NAII","NAKA","NAMS","NAMSW","NATR","NBIX","NBP","NBTX","NBY","NCEL","NCNA","NDRA","NEO","NEOG","NEPH","NERV","NEUP","NGNE","NHC","NIVF","NIVFW","NKTR","NKTX","NMRA","NMTC","NNNN","NNOX","NNVC","NOTV","NPCE","NRC","NRIX","NRSN","NRSNW","NRXP","NRXPW","NRXS","NSPR","NSRX","NTHI","NTLA","NTRA","NTRB","NUS","NUVB","NUVL","NUWE","NVAX","NVCR","NVCT","NVNO","NVO","NVS","NVST","NXGL","NXGLW","NXL","NXTC","NYXH","OABI","OABIW","OBIO","OCGN","OCS","OCSAW","OCUL","OFIX","OGEN","OGI","OGN","OKUR","OKYO","OLMA","OM","OMDA","OMER","ONC","ONCO","ONCY","ONMD","ONMDW","OPCH","OPK","ORGO","ORIC","ORKA","ORMP","OSCR","OSRH","OSRHW","OSTX","OSUR","OTLK","OVID","PACS","PAHC","PALI","PARK","PASG","PAVM","PAVS","PBH","PBM","PBMWW","PBYI","PCRX","PCSA","PCVX","PDEX","PDSB","PEN","PEPG","PFE","PFSA","PGEN","PGNY","PHAR","PHAT","PHG","PHGE","PHIO","PHVS","PIII","PIIIW","PLRX","PLRZ","PLSE","PLSM","PLUR","PLX","PLYX","PM","PMCB","PMI","PMN","PMVP","PNTG","POCI","PODD","PPBT","PPCB","PRAX","PRCT","PRFX","PRGO","PRKS","PRLD","PRME","PROF","PROK","PRQR","PRTA","PRTC","PRVA","PSNL","PSTV","PTCT","PTGX","PTHS","PTN","PULM","PVLA","PYPD","PYXS","QCLS","QDEL","QGEN","QIPT","QNCX","QNRX","QNTM","QTI","QTTB","QURE","RADX","RANI","RAPP","RARE","RCEL","RCKT","RCKTW","RCUS","RDHL","RDNT","RDY","REGN","REPL","REVB","REVBW","RGC","RGEN","RGNT","RGNX","RIGL","RLAY","RLMD","RLX","RLYB","RMD","RMTI","RNA","RNAC","RNAZ","RNTX","RNXT","ROIV","RPRX","RVMD","RVMDW","RVP","RVPH","RXRX","RXST","RYTM","RZLT","SABS","SABSW","SANA","SAVA","SBC","SBCWW","SBFM","SBFMW","SCLX","SCLXW","SCNI","SCNX","SCYX","SDGR","SEM","SENS","SEPN","SER","SERA","SGHT","SGMO","SGMT","SGP","SGRY","SHC","SHPH","SI","SIBN","SIGA","SINT","SION","SKIN","SKYE","SLDB","SLGL","SLN","SLNO","SLS","SLXN","SLXNW","SMMT","SMTI","SNDA","SNDL","SNDX","SNGX","SNN","SNOA","SNSE","SNTI","SNWV","SNY","SNYR","SOLV","SOPH","SPAI","SPRB","SPRC","SPRO","SPRY","SRPT","SRRK","SRTS","SRZN","SRZNW","SSII","STAA","STE","STEX","STIM","STOK","STRO","STSS","STTK","STVN","STXS","SUPN","SVRA","SXTC","SXTP","SXTPW","SYK","SYRE","TAK","TALK","TALKW","TAOX","TARA","TARS","TBPH","TCMD","TCRT","TCRX","TDOC","TECH","TECX","TELA","TELO","TENX","TERN","TEVA","TFX","TGTX","THC","TIL","TIVC","TKNO","TLPH","TLRY","TLSA","TLSI","TLSIW","TLX","TMCI","TMDX","TNDM","TNGX","TNON","TNXP","TNYA","TOI","TOVX","TPST","TRAW","TRDA","TRIB","TRUP","TRVI","TSHA","TTRX","TVGN","TVGNW","TVRD","TVTX","TWST","TXMD","TYRA","UFPT","UHS","ULS","UNCY","UNH","UPB","UPC","UPXI","URGN","USNA","USPH","UTHR","UTMD","VALN","VANI","VCEL","VCYT","VERA","VERU","VIR","VIVS","VKTX","VMD","VNDA","VNRX","VOR","VRAX","VRCA","VRDN","VRTX","VSEE","VSEEW","VSTM","VTAK","VTGN","VTRS","VTVT","VVOS","VYGR","VYNE","WGRX","WHWK","WOK","WRBY","WST","WVE","XAIR","XBIO","XBIT","XCUR","XENE","XERS","XFOR","XGN","XLO","XNCR","XOMA","XOMAO","XOMAP","XRAY","XRTX","XTLB","XTNT","XXII","YDES","YDESW","ZBH","ZBIO","ZJYL","ZLAB","ZNTL","ZSTK","ZTS","ZURA","ZVRA","ZYBT","ZYME"]

DEFAULT_STOCKS = ["PFE", "ABBV", "BMY"]


def stocks_to_str(stocks):
    return ",".join(stocks)


if "tickers_input" not in st.session_state:
    st.session_state.tickers_input = st.query_params.get(
        "stocks", stocks_to_str(DEFAULT_STOCKS)
    ).split(",")


# Callback to update query param when input changes
def update_query_param():
    if st.session_state.tickers_input:
        st.query_params["stocks"] = stocks_to_str(st.session_state.tickers_input)
    else:
        st.query_params.pop("stocks", None)


top_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)

with top_left_cell:
    # Selectbox for stock tickers
    tickers = st.multiselect(
        "Stock tickers",
        options=sorted(set(STOCKS) | set(st.session_state.tickers_input)),
        default=st.session_state.tickers_input,
        placeholder="Choose stocks to compare",
        accept_new_options=True,
    )

# Time horizon selector
horizon_map = {
    "1 Months": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "5 Years": "5y",
    "10 Years": "10y",
    "20 Years": "20y",
}

with top_left_cell:
    # Buttons for picking time horizon
    horizon = st.pills(
        "Time horizon",
        options=list(horizon_map.keys()),
        default="6 Months",
    )

tickers = [t.upper() for t in tickers]

# Update query param when text input changes
if tickers:
    st.query_params["stocks"] = stocks_to_str(tickers)
else:
    # Clear the param if input is empty
    st.query_params.pop("stocks", None)

if not tickers:
    top_left_cell.info("Pick some stocks to compare", icon=":material/info:")
    st.stop()


right_cell = cols[1].container(
    border=True, height="stretch", vertical_alignment="center"
)


@st.cache_resource(show_spinner=False, ttl="6h")
def load_data(tickers, period):
    tickers_obj = yf.Tickers(tickers)
    data = tickers_obj.history(period=period)
    if data is None:
        raise RuntimeError("YFinance returned no data.")
    return data["Close"]


# Load the data
try:
    data = load_data(tickers, horizon_map[horizon])
except yf.exceptions.YFRateLimitError as e:
    st.warning("YFinance is rate-limiting us :(\nTry again later.")
    load_data.clear()  # Remove the bad cache entry.
    st.stop()

empty_columns = data.columns[data.isna().all()].tolist()

if empty_columns:
    st.error(f"Error loading data for the tickers: {', '.join(empty_columns)}.")
    st.stop()

# Normalize prices (start at 1)
normalized = data.div(data.iloc[0])

latest_norm_values = {normalized[ticker].iat[-1]: ticker for ticker in tickers}
max_norm_value = max(latest_norm_values.items())
min_norm_value = min(latest_norm_values.items())

bottom_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)

with bottom_left_cell:
    cols = st.columns(2)
    cols[0].metric(
        "Best stock",
        max_norm_value[1],
        delta=f"{round(max_norm_value[0] * 100)}%",
        width="content",
    )
    cols[1].metric(
        "Worst stock",
        min_norm_value[1],
        delta=f"{round(min_norm_value[0] * 100)}%",
        width="content",
    )


# Plot normalized prices
with right_cell:
    st.altair_chart(
        alt.Chart(
            normalized.reset_index().melt(
                id_vars=["Date"], var_name="Stock", value_name="Normalized price"
            )
        )
        .mark_line()
        .encode(
            alt.X("Date:T"),
            alt.Y("Normalized price:Q").scale(zero=False),
            alt.Color("Stock:N"),
        )
        .properties(height=400)
    )

""
""

# Plot individual stock vs peer average
"""
## Individual stocks vs peer average

For the analysis below, the "peer average" when analyzing stock X always
excludes X itself.
"""

if len(tickers) <= 1:
    st.warning("Pick 2 or more tickers to compare them")
    st.stop()

NUM_COLS = 4
cols = st.columns(NUM_COLS)

for i, ticker in enumerate(tickers):
    # Calculate peer average (excluding current stock)
    peers = normalized.drop(columns=[ticker])
    peer_avg = peers.mean(axis=1)

    # Create DataFrame with peer average.
    plot_data = pd.DataFrame(
        {
            "Date": normalized.index,
            ticker: normalized[ticker],
            "Peer average": peer_avg,
        }
    ).melt(id_vars=["Date"], var_name="Series", value_name="Price")

    chart = (
        alt.Chart(plot_data)
        .mark_line()
        .encode(
            alt.X("Date:T"),
            alt.Y("Price:Q").scale(zero=False),
            alt.Color(
                "Series:N",
                scale=alt.Scale(domain=[ticker, "Peer average"], range=["red", "gray"]),
                legend=alt.Legend(orient="bottom"),
            ),
            alt.Tooltip(["Date", "Series", "Price"]),
        )
        .properties(title=f"{ticker} vs peer average", height=300)
    )

    cell = cols[(i * 2) % NUM_COLS].container(border=True)
    cell.write("")
    cell.altair_chart(chart, use_container_width=True)

    # Create Delta chart
    plot_data = pd.DataFrame(
        {
            "Date": normalized.index,
            "Delta": normalized[ticker] - peer_avg,
        }
    )

    chart = (
        alt.Chart(plot_data)
        .mark_area()
        .encode(
            alt.X("Date:T"),
            alt.Y("Delta:Q").scale(zero=False),
        )
        .properties(title=f"{ticker} minus peer average", height=300)
    )

    cell = cols[(i * 2 + 1) % NUM_COLS].container(border=True)
    cell.write("")
    cell.altair_chart(chart, use_container_width=True)


"""
## Raw data
"""

data


