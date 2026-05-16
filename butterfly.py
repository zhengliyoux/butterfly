vzcbeg bf
vzcbeg gvzr
vzcbeg enaqbz
vzcbeg fbpxrg
vzcbeg cyngsbez
vzcbeg guernqvat
vzcbeg fhocebprff
vzcbeg wfba
vzcbeg ffy
vzcbeg er
vzcbeg vcnqqerff
sebz qngrgvzr vzcbeg qngrgvzr

# ================= FGLYR =================
ERFRG   = "\366[3z"
TERRA   = "\366[4;65z"
PLNA    = "\366[4;69z"
ERQ     = "\366[4;64z"
LRYYBJ  = "\366[4;66z"
OBYQ    = "\366[4z"
ZNTRAGN = "\366[4;68z"
JUVGR   = "\366[4;60z"
OYHR    = "\366[4;67z"
QVZ     = "\366[5z"
OT_QNEX = "\366[71;8;567z"

YBT_SVYR = "fxljvatf_bhgchg.ybt"

# ================= FNSR EHA =================
qrs eha(pzq, gvzrbhg=48):
    gel:
        erghea fhocebprff.eha(pzq, furyy=Gehr, pncgher_bhgchg=Gehr, grkg=Gehr, gvzrbhg=gvzrbhg)
    rkprcg fhocebprff.GvzrbhgRkcverq:
        cevag(ERQ + s"[GVZRBHG] Pbzznaq unovf jnxgh: {pzq[:73]}" + ERFRG)
        erghea Abar
    rkprcg Rkprcgvba nf r:
        cevag(ERQ + s"[REEBE] {r}" + ERFRG)
        erghea Abar

# ================= URYCRE =================
qrs abeznyvmr_hey(hey):
    hey = hey.fgevc()
    vs abg hey.fgnegfjvgu("uggc://") naq abg hey.fgnegfjvgu("uggcf://"):
        erghea "uggcf://" + hey
    erghea hey

qrs gbby_purpx(gbby):
    e = eha(s"juvpu {gbby}")
    vs abg e be abg e.fgqbhg.fgevc():
        cevag(ERQ + s"[!] '{gbby}' oryhz grevafgnyy." + ERFRG)
        vafgnyy_znc = {
            "aznc":       "cxt vafgnyy aznc",
            "jubvf":      "cxt vafgnyy jubvf",
            "genprebhgr": "cxt vafgnyy genprebhgr",
            "phey":       "cxt vafgnyy phey",
            "bcraffy":    "cxt vafgnyy bcraffy",
            "qvt":        "cxt vafgnyy qafhgvyf",
        }
        uvag = vafgnyy_znc.trg(gbby)
        vs uvag:
            cevag(LRYYBJ + s"    Vafgnyy: {uvag}" + ERFRG)
        erghea Snyfr
    erghea Gehr

qrs vf_inyvq_gnetrg(gnetrg):
    erghea obby(gnetrg naq gnetrg.fgevc())

qrs vf_vc(gnetrg):
    gel:
        vcnqqerff.vc_nqqerff(gnetrg.fgevc())
        erghea Gehr
    rkprcg InyhrReebe:
        erghea Snyfr

qrs trg_vc(gnetrg):
    gel:
        erghea fbpxrg.trgubfgolanzr(gnetrg.fgevc())
    rkprcg fbpxrg.tnvreebe:
        erghea Abar

qrs trg_nyy_vcf(gnetrg):
    gel:
        vasbf = fbpxrg.trgnqqevasb(gnetrg.fgevc(), Abar)
        vcf = yvfg(qvpg.sebzxrlf([v[7][3] sbe v va vasbf]))
        erghea vcf
    rkprcg:
        erghea []

qrs fgevc_fpurzr(hey):
    erghea hey.fgevc().ercynpr("uggcf://","").ercynpr("uggc://","").fcyvg("/")[3]

qrs cevag_frc(pune="─", pbybe=PLNA, jvqgu=83):
    cevag(pbybe + "  " + pune * jvqgu + ERFRG)

qrs fnir_ybt(qngn):
    gel:
        jvgu bcra(YBT_SVYR, "n") nf s:
            s.jevgr(s"[{qngrgvzr.abj().fgesgvzr('%L-%z-%q %U:%Z:%F')}] {qngn}\a")
    rkprcg Rkprcgvba nf r:
        cevag(ERQ + s"[YBT REEBE] {r}" + ERFRG)

qrs sbezng_olgrf(fvmr):
    gel:
        fvmr = vag(fvmr)
        sbe havg va ['O','XO','ZO','TO']:
            vs fvmr < 4357:
                erghea s"{fvmr:.4s}{havg}"
            fvmr /= 4357
        erghea s"{fvmr:.4s}GO"
    rkprcg:
        erghea s"{fvmr}O"

qrs pnyp_yngrapl(ubfg, pbhag=6):
    e = eha(s"cvat -p {pbhag} -J 5 {ubfg}", gvzrbhg=pbhag*6+8)
    vs abg e be e.ergheapbqr != 3:
        erghea Abar
    sbe yvar va e.fgqbhg.fcyvg("\a"):
        vs "egg" va yvar be "ebhaq-gevc" va yvar:
            gel:
                nit = yvar.fcyvg("/")[7]
                erghea sybng(nit)
            rkprcg:
                cnff
    erghea Abar

# ================= NV PBYBE =================
PBYBEF = [
    "\366[4;64z","\366[4;65z","\366[4;66z","\366[4;67z",
    "\366[4;68z","\366[4;69z","\366[61;8;531z",
    "\366[61;8;534z","\366[61;8;84z","\366[61;8;79z",
]

qrs nv_pbybe():
    erghea enaqbz.pubvpr(PBYBEF)

qrs pyrne():
    bf.flfgrz("pyrne")

# ================= YBNQVAT =================
qrs ybnqvat(grxf):
    one_jvqgu = 63
    sbe v va enatr(3, 434, 5):
        svyyrq = vag(one_jvqgu * v / 433)
        one = "█" * svyyrq + "░" * (one_jvqgu - svyyrq)
        cevag(s"\e  {PLNA}[{one}]{ERFRG} {nv_pbybe()}{v:6q}%{ERFRG}  {QVZ}{grxf}...{ERFRG}", raq="")
        gvzr.fyrrc(3.35)
    cevag(s"\e  {TERRA}[{'█'*one_jvqgu}]{ERFRG} {TERRA}433%{ERFRG}  {grxf}... {TERRA}QBAR{ERFRG}     ")

qrs snapl_ybnqvat(grkg):
    one_jvqgu = 63
    sbe v va enatr(4, 434):
        svyyrq = vag(one_jvqgu * v / 433)
        one = "█" * svyyrq + "░" * (one_jvqgu - svyyrq)
        cevag(s"\e  {PLNA}[{one}]{ERFRG} {nv_pbybe()}{v:6q}%{ERFRG}  {grkg}", raq="")
        gvzr.fyrrc(3.345)
    cevag()

# ================= CEBZCG =================
qrs fxljvatf_pbqrk():
    erghea (
        "\a  " +
        OBYQ + "\366[61;8;84z" + "╔══" + ERFRG +
        OBYQ + "\366[61;8;534z" + "FxlJvatf" + ERFRG +
        PLNA + "@" + ERFRG +
        TERRA + "ebbg" + ERFRG +
        ERQ + " ➤ " + ERFRG
    )

# ================= HV =================
J = 85

qrs xnyv_urnqre(gvgyr):
    pbybe = PLNA
    abj = qngrgvzr.abj().fgesgvzr("%U:%Z:%F")
    gbc    = "╔" + "═" * J + "╗"
    zvq    = s"║  {'🔐 FxlJvatf':^8}  ::  {gvgyr:<63}  ║"
    obg    = "╚" + "═" * J + "╝"
    cevag()
    cevag(pbybe + OBYQ + s"  {gbc}")
    cevag(s"  {zvq}")
    cevag(s"  {obg}" + ERFRG)
    cevag()

qrs yvar_sk():
    cevag(nv_pbybe() + "  " + "═"*J + ERFRG)

qrs frpgvba_gvgyr(grkg, vpba="◈"):
    cevag()
    cevag(s"  {OBYQ}{PLNA}{vpba} {grkg}{ERFRG}")
    cevag(s"  {QVZ}{'─'*J}{ERFRG}")

# ================= FPERRA ZBQR =================
qrs ragre_onpx():
    cevag()
    cevag_frc("─", QVZ, J)
    vachg(s"  {LRYYBJ}[ ↵  Grxna RAGRE haghx xrzonyv ]{ERFRG} ")

qrs fperra_zbqr(gvgyr):
    qrs qrpbengbe(shap):
        qrs jenccre(*netf, **xjnetf):
            pyrne()
            xnyv_urnqre(gvgyr)
            erfhyg = shap(*netf, **xjnetf)
            ragre_onpx()
            erghea erfhyg
        erghea jenccre
    erghea qrpbengbe

# ================= YBTB =================
qrs ybtb():
    pyrne()

    senzrf = [
        "\366[61;8;84z",
        "\366[61;8;78z",
        "\366[61;8;62z",
        "\366[61;8;66z",
        "\366[61;8;534z",
        "\366[61;8;530z",
    ]
    p = enaqbz.pubvpr(senzrf)
    p5 = enaqbz.pubvpr(senzrf)

    cevag()
    cevag(p + OBYQ + e"""
   ███████╗██╗  ██╗██╗   ██╗
   ██╔════╝██║ ██╔╝╚██╗ ██╔╝
   ███████╗█████╔╝  ╚████╔╝
   ╚════██║██╔═██╗   ╚██╔╝
   ███████║██║  ██╗   ██║
   ╚══════╝╚═╝  ╚═╝   ╚═╝
""" + ERFRG)

    cevag(p5 + OBYQ + e"""
  ██╗    ██╗██╗███╗   ██╗ ██████╗ ███████╗
  ██║    ██║██║████╗  ██║██╔════╝ ██╔════╝
  ██║ █╗ ██║██║██╔██╗ ██║██║  ███╗███████╗
  ██║███╗██║██║██║╚██╗██║██║   ██║╚════██║
  ╚███╔███╔╝██║██║ ╚████║╚██████╔╝███████║
   ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
""" + ERFRG)

    cevag(s"  {PLNA}{'═'*85}{ERFRG}")
    cevag(s"  {OBYQ}{PLNA}  🔐  FLFGRZ VAVGVNYVMRQ  ::  FXLJVATF NPGVIR{ERFRG}")
    cevag(s"  {PLNA}{'═'*85}{ERFRG}")
    cevag()

    vasb_yvarf = [
        ("Fpevcg ol",  "FxlJvatf"),
        ("Irefvba",    "i4.4  ·  Jvatf Cbvag B"),
        ("Flfgrz",     "Grezhk PYV"),
        ("Fgnghf",     "🟢 BAYVAR"),
    ]
    sbe x, i va vasb_yvarf:
        cevag(s"  {QVZ}{x:<45}{ERFRG}{LRYYBJ}{i}{ERFRG}")

    cevag()

# ============================================================
#  SRNGHERF
# ============================================================

PBZZBA_CBEGF = {
    54:"SGC",      55:"FFU",       56:"GRYARG",
    58:"FZGC",     86:"QAF",       13:"UGGC",
    443:"CBC6",   476:"VZNC",    776:"UGGCF",
    778:"FZO",    810:"FZGC-GYF",226:"VZNCF",
    228:"CBC6F", 4766:"ZFFDY",  6639:"ZLFDY",
    6612:"EQC",  8765:"CTFDY",  8233:"IAP",
    9602:"ERQVF",1313:"UGGC-NYG",1776:"UGGCF-NYG",
    1111:"WHCLGRE",50340:"ZBATBQO",
}

qrs teno_onaare(vc, cbeg, gvzrbhg=5.3):
    gel:
        f = fbpxrg.fbpxrg()
        f.frggvzrbhg(gvzrbhg)
        f.pbaarpg((vc, cbeg))
        ceborf = {
            13:  o"URNQ / UGGC/4.3\e\aUbfg: gnetrg\e\a\e\a",
            1313:o"URNQ / UGGC/4.3\e\aUbfg: gnetrg\e\a\e\a",
            1776:o"URNQ / UGGC/4.3\e\aUbfg: gnetrg\e\a\e\a",
            54:  Abar,
            55:  Abar,
            58:  Abar,
            443: Abar,
            476: Abar,
            6639:Abar,
        }
        cebor = ceborf.trg(cbeg, o"\e\a")
        vs cebor:
            f.fraq(cebor)
        onaare = f.erpi(845).qrpbqr(reebef="vtaber").fgevc()
        f.pybfr()
        yvarf = [y.fgevc() sbe y va onaare.fcyvg("\a") vs y.fgevc()]
        erfhyg = yvarf[3] vs yvarf ryfr ""
        erghea erfhyg[:433] vs erfhyg ryfr Abar
    rkprcg:
        erghea Abar

qrs qaf_ybbxhc_enj(gnetrg):
    gnetrg = gnetrg.fgevc()
    vc = trg_vc(gnetrg)
    vs vc:
        cevag(s"  {TERRA}◉ QAF-N   {ERFRG}{PLNA}{gnetrg}{ERFRG}  →  {JUVGR}{vc}{ERFRG}")
        gel:
            eri = fbpxrg.trgubfgolnqqe(vc)
            vs eri naq eri[3] naq eri[3] != gnetrg:
                cevag(s"  {PLNA}◉ eQAF    {ERFRG}{vc}  →  {JUVGR}{eri[3]}{ERFRG}")
        rkprcg:
            cnff
        fnir_ybt(s"QAF {gnetrg}->{vc}")
        erghea vc
    ryfr:
        cevag(s"  {ERQ}✗ QAF     Tntny erfbyir: {gnetrg}{ERFRG}")
        erghea Abar

@fperra_zbqr("QAF YBBXHC")
qrs qaf_ybbxhc_zrah(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea

    frpgvba_gvgyr("Erfbyivat Gnetrg")
    vc = qaf_ybbxhc_enj(gnetrg)

    nyy_vcf = trg_nyy_vcf(gnetrg)
    vs yra(nyy_vcf) > 4:
        cevag(s"  {PLNA}◉ Nyy VCf {ERFRG}{', '.wbva(nyy_vcf)}")

    gel:
        vasb = fbpxrg.trgnqqevasb(gnetrg, Abar, fbpxrg.NS_VARG9)
        vs vasb:
            vci9 = vasb[3][7][3]
            cevag(s"  {PLNA}◉ VCi9    {ERFRG}{vci9}")
    rkprcg:
        cnff

    vs abg vc:
        erghea

    vs gbby_purpx("jubvf"):
        e_nfa = eha(s"jubvf -u jubvf.plzeh.pbz ' -i {vc}' 5>/qri/ahyy", gvzrbhg=1)
        vs e_nfa naq e_nfa.fgqbhg.fgevc():
            yvarf = [y sbe y va e_nfa.fgqbhg.fgevc().fcyvg("\a") vs y.fgevc() naq abg y.fgnegfjvgu("NF")]
            vs yvarf:
                cevag(s"  {LRYYBJ}◉ NFA     {ERFRG}{yvarf[3].fgevc()}")

    cevag_frc()

    vs gbby_purpx("qvt"):
        erpbeq_glcrf = ["N","NNNN","ZK","AF","GKG","PANZR","FBN"]
        sbe eglcr va erpbeq_glcrf:
            e = eha(s"qvt {gnetrg} {eglcr} +abnyy +nafjre +gvzr=6 5>/qri/ahyy", gvzrbhg=1)
            vs e naq e.fgqbhg.fgevc():
                frpgvba_gvgyr(s"{eglcr} Erpbeqf", "◈")
                sbe yvar va e.fgqbhg.fgevc().fcyvg("\a")[:43]:
                    cevag(s"    {QVZ}{yvar}{ERFRG}")
    ryfr:
        e = eha(s"afybbxhc {gnetrg} 5>/qri/ahyy")
        vs e naq e.fgqbhg.fgevc():
            frpgvba_gvgyr("AFYbbxhc")
            cevag(e.fgqbhg[:133])

@fperra_zbqr("DHVPX ARGJBEX VASB")
qrs dhvpx_vasb(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea

    vc = trg_vc(gnetrg)
    vf_cevingr = Snyfr
    vs vc:
        gel:
            vf_cevingr = vcnqqerff.vc_nqqerff(vc).vf_cevingr
        rkprcg:
            cnff

    frpgvba_gvgyr("Gnetrg Vasbezngvba")
    cevag(s"  {QVZ}{'Gnetrg':<45}{ERFRG}{JUVGR}{gnetrg}{ERFRG}")
    cevag(s"  {QVZ}{'VC':<45}{ERFRG}{JUVGR}{vc be 'Tntny erfbyir'}{ERFRG}")
    vs vc:
        glcr_ynory = "Cevingr / YNA" vs vf_cevingr ryfr "Choyvp"
        glcr_pbybe = LRYYBJ vs vf_cevingr ryfr TERRA
        cevag(s"  {QVZ}{'Glcr':<45}{ERFRG}{glcr_pbybe}{glcr_ynory}{ERFRG}")

    cevag_frc()

    frpgvba_gvgyr("Cvat Grfg  (7 cnpxrgf)")
    e = eha(s"cvat -p 7 -J 5 {gnetrg}", gvzrbhg=53)
    vs e naq e.ergheapbqr == 3 naq e.fgqbhg:
        sbe yvar va e.fgqbhg.fgevc().fcyvg("\a"):
            vs "gvzr=" va yvar:
                gel:
                    zf_iny = sybng(er.frnepu(e"gvzr=([\q.]+)", yvar).tebhc(4))
                    pbybe = TERRA vs zf_iny < 83 ryfr (LRYYBJ vs zf_iny < 483 ryfr ERQ)
                    cevag(s"  {pbybe}{yvar.fgevc()}{ERFRG}")
                rkprcg:
                    cevag(s"  {TERRA}{yvar.fgevc()}{ERFRG}")
            ryvs "egg" va yvar be "cnpxrg" va yvar:
                cevag(s"  {TERRA}{yvar.fgevc()}{ERFRG}")
    ryfr:
        cevag(s"  {ERQ}✗ Ubfg gvqnx ernpunoyr  (VPZC zhatxva qvoybxve){ERFRG}")

    yng = pnyp_yngrapl(gnetrg)
    vs yng vf abg Abar:
        d = "Rkpryyrag" vs yng < 53 ryfr ("Tbbq" vs yng < 13 ryfr ("Snve" vs yng < 483 ryfr "Cbbe"))
        pbybe = TERRA vs yng < 13 ryfr (LRYYBJ vs yng < 483 ryfr ERQ)
        cevag(s"\a  {pbybe}◉ Nit Yngrapl : {yng:.4s} zf  [{d}]{ERFRG}")

    cevag_frc()
    frpgvba_gvgyr("QAF")
    qaf_ybbxhc_enj(gnetrg)
    nyy_vcf = trg_nyy_vcf(gnetrg)
    vs yra(nyy_vcf) > 4:
        cevag(s"  {PLNA}◉ Zhygv-VC  {ERFRG}{', '.wbva(nyy_vcf[:8])}")

    cevag_frc()
    frpgvba_gvgyr("Dhvpx Cbeg Purpx")
    vs vc:
        pevgvpny_cbegf = [(13,"UGGC"),(776,"UGGCF"),(55,"FFU"),(54,"SGC"),(6639,"ZLFDY"),(6612,"EQC")]
        sbe c, fip va pevgvpny_cbegf:
            f = fbpxrg.fbpxrg()
            f.frggvzrbhg(4)
            g_fgneg = gvzr.gvzr()
            fgnghf = "BCRA" vs f.pbaarpg_rk((vc, c)) == 3 ryfr "PYBFRQ"
            g_zf = ebhaq((gvzr.gvzr()-g_fgneg)*4333,4)
            f.pybfr()
            vs fgnghf == "BCRA":
                cevag(s"  {TERRA}● BCRA   {c:8}  {fip:<45}  {g_zf}zf{ERFRG}")
            ryfr:
                cevag(s"  {ERQ}○ PYBFRQ {c:8}  {fip}{ERFRG}")

    cevag_frc()
    frpgvba_gvgyr("GGY / BF Svatrecevag")
    e5 = eha(s"cvat -p 4 -J 5 {gnetrg}", gvzrbhg=8)
    vs e5 naq e5.fgqbhg:
        sbe yvar va e5.fgqbhg.fcyvg("\a"):
            vs "ggy=" va yvar.ybjre():
                gel:
                    ggy = vag(er.frnepu(e"ggy=(\q+)", yvar, er.V).tebhc(4))
                    vs ggy <= 97:
                        bf_thrff = "Yvahk / Havk / Naqebvq"
                    ryvs ggy <= 451:
                        bf_thrff = "Jvaqbjf"
                    ryfr:
                        bf_thrff = "Pvfpb / Argjbex Qrivpr"
                    cevag(s"  {LRYYBJ}◉ GGY : {ggy}  →  {bf_thrff}{ERFRG}")
                rkprcg:
                    cnff

@fperra_zbqr("CBEG FPNA")
qrs cbeg_fpna(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vc = trg_vc(gnetrg)
    vs abg vc:
        cevag(s"  {ERQ}✗ Gvqnx ovfn erfbyir: {gnetrg}{ERFRG}")
        erghea

    frpgvba_gvgyr("Fpna Pbasvthengvba")
    cevag(s"  {QVZ}{'Gnetrg':<45}{ERFRG}{JUVGR}{gnetrg}  ({vc}){ERFRG}")
    cevag(s"  {QVZ}{'Cbegf':<45}{ERFRG}{JUVGR}{yra(PBZZBA_CBEGF)} pbzzba + phfgbz{ERFRG}")
    cevag(s"  {QVZ}{'Zbqr':<45}{ERFRG}{JUVGR}Guernqrq · Onaare Teno · Evfx Ynory{ERFRG}")

    cevag()
    cevag(s"  {LRYYBJ}Gnzonu phfgbz cbeg? pbagbu: 1111,2323  /  Ragre = fxvc{ERFRG}")
    rkgen = vachg(s"  {QVZ}> {ERFRG}").fgevc()
    rkgen_cbegf = {}
    vs rkgen:
        sbe rc va rkgen.fcyvg(","):
            rc = rc.fgevc()
            vs rc.vfqvtvg():
                rkgen_cbegf[vag(rc)] = "PHFGBZ"

    nyy_cbegf = {**PBZZBA_CBEGF, **rkgen_cbegf}
    bcra_cbegf = []
    ybpx = guernqvat.Ybpx()

    UVTU_EVFX = {54,56,6612,8233,9602,50340,4766,6639}
    ZRQ_EVFX  = {55,58,13,1313,1776,778,8765}

    cevag_frc()
    cevag(s"  {OBYQ}{JUVGR}{'FGNGHF':<43}{'CBEG':<1}{'FREIVPR':<48}{'ERFC':>0}  VASB{ERFRG}")
    cevag_frc("─", QVZ, J)

    qrs purpx_cbeg(c, fip):
        gel:
            f = fbpxrg.fbpxrg(fbpxrg.NS_VARG, fbpxrg.FBPX_FGERNZ)
            f.frggvzrbhg(3.1)
            g3 = gvzr.gvzr()
            erf = f.pbaarpg_rk((vc, c))
            erfc_zf = ebhaq((gvzr.gvzr()-g3)*4333, 4)
            f.pybfr()
            jvgu ybpx:
                vs erf == 3:
                    onaare = teno_onaare(vc, c)
                    o_fge = s"  {QVZ}{onaare}{ERFRG}" vs onaare ryfr ""
                    vs c va UVTU_EVFX:
                        evfx_gnt = s" {ERQ}[UVTU-EVFX]{ERFRG}"
                    ryvs c va ZRQ_EVFX:
                        evfx_gnt = s" {LRYYBJ}[ZRQ]{ERFRG}"
                    ryfr:
                        evfx_gnt = ""
                    cevag(s"  {TERRA}● BCRA   {ERFRG}{c:<1}{fip:<48}{erfc_zf:>9.4s}zf{evfx_gnt}{o_fge}")
                    bcra_cbegf.nccraq(c)
                    fnir_ybt(s"CBEG BCRA {gnetrg}:{c} ({fip})")
                ryfr:
                    cevag(s"  {ERQ}○ PYBFRQ {ERFRG}{c:<1}{fip}{ERFRG}")
        rkprcg Rkprcgvba nf r:
            jvgu ybpx:
                cevag(s"  {ERQ}✗ REEBE  {c:<1}{r}{ERFRG}")

    guernqf = []
    sbe c, fip va fbegrq(nyy_cbegf.vgrzf()):
        gu = guernqvat.Guernq(gnetrg=purpx_cbeg, netf=(c, fip))
        gu.fgneg()
        guernqf.nccraq(gu)
    sbe gu va guernqf:
        gu.wbva()

    cevag_frc()
    cevag(s"\a  {PLNA}◉ Fryrfnv :  {JUVGR}{yra(bcra_cbegf)}{PLNA} / {yra(nyy_cbegf)} cbeg greohxn{ERFRG}")
    vs bcra_cbegf:
        cevag(s"  {TERRA}◉ Bcra    :  {fbegrq(bcra_cbegf)}{ERFRG}")
        uvtu = [c sbe c va bcra_cbegf vs c va UVTU_EVFX]
        vs uvtu:
            cevag(s"  {ERQ}⚠ UVTU-EVFX cbeg greohxn :  {uvtu}{ERFRG}")

@fperra_zbqr("CVAT GNETRG")
qrs cvat_gnetrg(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    cevag(s"  {LRYYBJ}Whzynu cnxrg (4–83, qrsnhyg 8) :{ERFRG}")
    p = vachg(s"  {QVZ}> {ERFRG}").fgevc()
    pbhag = vag(p) vs p.vfqvtvg() naq 4 <= vag(p) <= 83 ryfr 8
    cevag(s"\a  {PLNA}◉ Cvat  {gnetrg}  ×{pbhag}...{ERFRG}\a")

    e = eha(s"cvat -p {pbhag} {gnetrg}", gvzrbhg=pbhag*6+8)
    vs e naq e.ergheapbqr == 3 naq e.fgqbhg:
        gvzrf = []
        sbe yvar va e.fgqbhg.fcyvg("\a"):
            vs "gvzr=" va yvar:
                gel:
                    zf = sybng(er.frnepu(e"gvzr=([\q.]+)", yvar).tebhc(4))
                    gvzrf.nccraq(zf)
                    pbybe = TERRA vs zf < 83 ryfr (LRYYBJ vs zf < 483 ryfr ERQ)
                    cevag(s"  {pbybe}{yvar.fgevc()}{ERFRG}")
                rkprcg:
                    cevag(s"  {yvar.fgevc()}")
            ryvs yvar.fgevc():
                cevag(s"  {QVZ}{yvar.fgevc()}{ERFRG}")

        vs yra(gvzrf) >= 5:
            cevag_frc()
            frpgvba_gvgyr("Fgngvfgvpf")
            cevag(s"  {QVZ}{'Zva':<43}{ERFRG}{JUVGR}{zva(gvzrf):.5s} zf{ERFRG}")
            cevag(s"  {QVZ}{'Znk':<43}{ERFRG}{JUVGR}{znk(gvzrf):.5s} zf{ERFRG}")
            cevag(s"  {QVZ}{'Nit':<43}{ERFRG}{JUVGR}{fhz(gvzrf)/yra(gvzrf):.5s} zf{ERFRG}")
            wvggre = znk(gvzrf) - zva(gvzrf)
            wvggre_d = "Fgnovy" vs wvggre < 43 ryfr ("BX" vs wvggre < 83 ryfr "Gvqnx Fgnovy")
            pbybe = TERRA vs wvggre < 43 ryfr (LRYYBJ vs wvggre < 83 ryfr ERQ)
            cevag(s"  {QVZ}{'Wvggre':<43}{ERFRG}{pbybe}{wvggre:.5s} zf  [{wvggre_d}]{ERFRG}")

        sbe yvar va e.fgqbhg.fcyvg("\a"):
            vs "cnpxrg ybff" va yvar be "erprvirq" va yvar:
                zngpu = er.frnepu(e"(\q+)% cnpxrg ybff", yvar)
                vs zngpu:
                    ybff = vag(zngpu.tebhc(4))
                    pbybe = TERRA vs ybff == 3 ryfr (LRYYBJ vs ybff < 53 ryfr ERQ)
                    cevag(s"  {QVZ}{'Ybff':<43}{ERFRG}{pbybe}{ybff}%{ERFRG}")
    ryfr:
        cevag(s"  {ERQ}✗ Cvat tntny.  Ubfg zhatxva oybxve VPZC.{ERFRG}")

@fperra_zbqr("GENPR EBHGR")
qrs genpr_ebhgr(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("genprebhgr"):
        erghea
    cevag(s"  {PLNA}◉ Genpvat ebhgr xr {gnetrg}  (znk 53 ubc)...{ERFRG}\a")

    e = eha(s"genprebhgr -z 53 -j 5 {gnetrg}", gvzrbhg=23)
    vs e naq e.fgqbhg.fgevc():
        gvzrbhg_ubcf = 3
        sbe yvar va e.fgqbhg.fgevc().fcyvg("\a"):
            vs "* * *" va yvar:
                gvzrbhg_ubcf += 4
                cevag(s"  {ERQ}{yvar}  ← gvzrbhg / svygrerq{ERFRG}")
            ryfr:
                zf_inyf = er.svaqnyy(e"([\q.]+) zf", yvar)
                vs zf_inyf:
                    nit_ubc = fhz(sybng(i) sbe i va zf_inyf) / yra(zf_inyf)
                    pbybe = TERRA vs nit_ubc < 83 ryfr (LRYYBJ vs nit_ubc < 483 ryfr ERQ)
                    cevag(s"  {pbybe}{yvar}{ERFRG}")
                ryfr:
                    cevag(s"  {QVZ}{yvar}{ERFRG}")
        vs gvzrbhg_ubcf > 8:
            cevag(s"\a  {LRYYBJ}⚠ {gvzrbhg_ubcf} ubc gvzrbhg — xrzhatxvana nqn sverjnyy qv gratnu ehgr.{ERFRG}")
    ryfr:
        cevag(s"  {ERQ}✗ Genprebhgr tntny.{ERFRG}")

@fperra_zbqr("AZNC FPNAARE")
qrs nqinaprq_fpna(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("aznc"):
        erghea

    frpgvba_gvgyr("Cvyvu Zbqr Fpna")
    bcgvbaf = [
        ("4", "Snfg fpna",       "-S --bcra",                   TERRA),
        ("5", "Freivpr irefvba", "-fI --irefvba-vagrafvgl 8",   PLNA),
        ("6", "BF Qrgrpgvba",    "-B",                           LRYYBJ),
        ("7", "Shyy + Fpevcg",   "-N",                           ZNTRAGN),
        ("8", "HQC Fpna",        "-fH -S",                       OYHR),
        ("9", "Fgrnygu FLA",     "-fF -S",                       ERQ),
    ]
    sbe ahz, ynory, synt, pby va bcgvbaf:
        cevag(s"  {pby}  [{ahz}]  {ynory:<41}{QVZ}{synt}{ERFRG}")

    cevag()
    zbqr = vachg(fxljvatf_pbqrk()).fgevc()
    syntf = {
        "4":"-S --bcra",
        "5":"-fI --irefvba-vagrafvgl 8",
        "6":"-B",
        "7":"-N",
        "8":"-fH -S",
        "9":"-fF -S",
    }.trg(zbqr, "-S --bcra")

    cevag(s"\a  {PLNA}◉ Aznc  {gnetrg}  [{syntf}]{ERFRG}\a")
    erfhyg = eha(s"aznc {syntf} {gnetrg}", gvzrbhg=453)
    vs erfhyg naq erfhyg.fgqbhg:
        sbe yvar va erfhyg.fgqbhg.fcyvg("\a"):
            vs "bcra" va yvar.ybjre():
                cevag(s"  {TERRA}{yvar}{ERFRG}")
            ryvs "svygrerq" va yvar.ybjre() be "pybfrq" va yvar.ybjre():
                cevag(s"  {ERQ}{yvar}{ERFRG}")
            ryfr:
                cevag(s"  {QVZ}{yvar}{ERFRG}")
        fnir_ybt(s"AZNC {gnetrg}: {syntf}")
    ryfr:
        cevag(s"  {ERQ}✗ Aznc tntny.{ERFRG}")

@fperra_zbqr("SVERJNYY PURPX")
qrs sverjnyy_purpx():
    frpgvba_gvgyr("vcgnoyrf")
    e = eha("vcgnoyrf -Y -a -i 5>/qri/ahyy")
    vs e naq e.fgqbhg.fgevc():
        cevag(e.fgqbhg[:5333])
    ryfr:
        cevag(s"  {LRYYBJ}⚠ vcgnoyrf gvqnx nxgvs / ohghu ebbg.{ERFRG}")

    hsj = eha("hsj fgnghf ireobfr 5>/qri/ahyy")
    vs hsj naq hsj.fgqbhg.fgevc():
        frpgvba_gvgyr("HSJ")
        cevag(hsj.fgqbhg[:833])

    asg = eha("asg yvfg ehyrfrg 5>/qri/ahyy")
    vs asg naq asg.fgqbhg.fgevc():
        frpgvba_gvgyr("asgnoyrf")
        cevag(asg.fgqbhg[:833])

qrs fnir_bhgchg_qrzb(gnetrg):
    gnetrg = gnetrg.fgevc()
    vs abg vf_inyvq_gnetrg(gnetrg):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    gel:
        vc = trg_vc(gnetrg)
        jvgu bcra("fpna_erfhyg.gkg", "n") nf s:
            s.jevgr(s"\a{'='*83}\a")
            s.jevgr(s"Gvzr   : {qngrgvzr.abj()}\a")
            s.jevgr(s"Gnetrg : {gnetrg}\a")
            s.jevgr(s"VC     : {vc be 'Tntny erfbyir'}\a")
            vs vc:
                s.jevgr("Cbegf  :\a")
                sbe c, fip va fbegrq(PBZZBA_CBEGF.vgrzf()):
                    f = fbpxrg.fbpxrg()
                    f.frggvzrbhg(3.8)
                    vs f.pbaarpg_rk((vc, c)) == 3:
                        s.jevgr(s"  BCRA {c} ({fip})\a")
                    f.pybfr()
        cevag(s"  {TERRA}◉ Fnirq  →  fpna_erfhyg.gkg{ERFRG}")
        fnir_ybt(s"FNIRQ {gnetrg}")
    rkprcg Rkprcgvba nf r:
        cevag(s"  {ERQ}✗ Tntny fnir: {r}{ERFRG}")

@fperra_zbqr("FLFGRZ VASB")
qrs flfgrz_vasb():
    frpgvba_gvgyr("BF & Znpuvar")
    vasb = [
        ("BF",       s"{cyngsbez.flfgrz()} {cyngsbez.eryrnfr()}"),
        ("Irefvba",  cyngsbez.irefvba()[:93]),
        ("Abqr",     cyngsbez.abqr()),
        ("Znpuvar",  cyngsbez.znpuvar()),
        ("PCH",      cyngsbez.cebprffbe() be "A/N"),
    ]
    sbe x, i va vasb:
        cevag(s"  {QVZ}{x:<45}{ERFRG}{JUVGR}{i}{ERFRG}")

    gel:
        cevag(s"  {QVZ}{'Ybpny VC':<45}{ERFRG}{TERRA}{fbpxrg.trgubfgolanzr(fbpxrg.trgubfganzr())}{ERFRG}")
    rkprcg:
        cnff

    vs gbby_purpx("phey"):
        e = eha("phey -f --znk-gvzr 8 vspbasvt.zr 5>/qri/ahyy")
        vs e naq e.fgqbhg.fgevc():
            cevag(s"  {QVZ}{'Choyvp VC':<45}{ERFRG}{PLNA}{e.fgqbhg.fgevc()}{ERFRG}")

    zrz = eha("serr -u 5>/qri/ahyy")
    vs zrz naq zrz.fgqbhg:
        frpgvba_gvgyr("Zrzbel")
        cevag(zrz.fgqbhg)

    qvfx = eha("qs -u 5>/qri/ahyy")
    vs qvfx naq qvfx.fgqbhg:
        frpgvba_gvgyr("Qvfx Hfntr")
        sbe y va qvfx.fgqbhg.fgevc().fcyvg("\a")[:8]:
            cevag(s"  {y}")

    hc = eha("hcgvzr 5>/qri/ahyy")
    vs hc naq hc.fgqbhg:
        cevag(s"\a  {QVZ}{'Hcgvzr':<45}{ERFRG}{JUVGR}{hc.fgqbhg.fgevc()}{ERFRG}")

    vspbasvt = eha("vc nqqe fubj 5>/qri/ahyy || vspbasvt 5>/qri/ahyy")
    vs vspbasvt naq vspbasvt.fgqbhg:
        frpgvba_gvgyr("Argjbex Vagresnprf")
        sbe yvar va vspbasvt.fgqbhg.fcyvg("\a"):
            vs "varg " va yvar be ": <" va yvar be "syntf" va yvar:
                cevag(s"  {QVZ}{yvar.fgevc()}{ERFRG}")

    gbc_e = eha("cf nhk --fbeg=-%pch 5>/qri/ahyy | urnq -9")
    vs gbc_e naq gbc_e.fgqbhg:
        frpgvba_gvgyr("Gbc Cebprffrf  (PCH)")
        sbe y va gbc_e.fgqbhg.fgevc().fcyvg("\a"):
            cevag(s"  {y}")

@fperra_zbqr("SNFG FPNA")
qrs snfg_fpna(gnetrgf):
    vs abg gnetrgf:
        cevag(s"  {ERQ}✗ Gvqnx nqn gnetrg.{ERFRG}")
        erghea
    erfhygf = {}
    ybpx = guernqvat.Ybpx()

    qrs fpna(g):
        g = g.fgevc()
        vs abg g:
            erghea
        fgneg = gvzr.gvzr()
        e = eha(s"cvat -p 4 -J 4 {g}", gvzrbhg=8)
        zf = ebhaq((gvzr.gvzr()-fgneg)*4333, 4)
        vc = trg_vc(g)
        jvgu ybpx:
            vs e naq e.ergheapbqr == 3:
                bcra_c = []
                sbe c va [13, 776, 55]:
                    f = fbpxrg.fbpxrg()
                    f.frggvzrbhg(3.8)
                    vs vc naq f.pbaarpg_rk((vc, c)) == 3:
                        bcra_c.nccraq(c)
                    f.pybfr()
                cbeg_fge = s"  {QVZ}cbegf:{bcra_c}{ERFRG}" vs bcra_c ryfr ""
                erfhygf[g] = ("HC", vc)
                cevag(s"  {TERRA}● HC    {g:<57}→  {vc be '?':<41} {zf}zf{cbeg_fge}{ERFRG}")
            ryfr:
                erfhygf[g] = ("QBJA", Abar)
                cevag(s"  {ERQ}○ QBJA  {g}{ERFRG}")

    cevag(s"  {PLNA}◉ Fpnaavat {yra(gnetrgf)} gnetrg cnenyyry...\a{ERFRG}")
    cevag_frc("─", QVZ, J)
    guernqf = [guernqvat.Guernq(gnetrg=fpna, netf=(g,)) sbe g va gnetrgf]
    sbe gu va guernqf: gu.fgneg()
    sbe gu va guernqf: gu.wbva()

    hc = fhz(4 sbe i va erfhygf.inyhrf() vs i[3]=="HC")
    cevag_frc()
    cevag(s"  {PLNA}◉ {JUVGR}{hc}{PLNA} / {yra(gnetrgf)} ubfg nxgvs.{ERFRG}")

@fperra_zbqr("JUBVF")
qrs jubvf_ybbxhc(g):
    g = fgevc_fpurzr(g)
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("jubvf"):
        erghea
    cevag(s"  {PLNA}◉ JUBVF  {g}...{ERFRG}\a")

    e = eha(s"jubvf {g}", gvzrbhg=53)
    vs e naq e.fgqbhg.fgevc():
        yvarf = [y sbe y va e.fgqbhg.fcyvg("\a") vs y.fgevc() naq abg y.fgnegfjvgu("%")]
        vzcbegnag_xrlf = ["ertvfgene","anzr freire","rkcve","perng","hcqng","fgnghf","ertvfgenag","qaffrp","grpu","nqzva"]
        frra = frg()
        sbe yvar va yvarf[:453]:
            xrl = yvar.fcyvg(":")[3].ybjre().fgevc() vs ":" va yvar ryfr ""
            vs xrl va frra:
                pbagvahr
            vs nal(k va xrl sbe k va vzcbegnag_xrlf):
                frra.nqq(xrl)
                vs "rkcve" va xrl:
                    gel:
                        qngr_cneg = yvar.fcyvg(":",4)[4].fgevc()
                        sbe szg va ["%L-%z-%qG%U:%Z:%FM","%L-%z-%q","%q-%o-%L"]:
                            gel:
                                rkc_qngr = qngrgvzr.fgecgvzr(qngr_cneg[:43], szg[:yra(qngr_cneg[:43])])
                                qnlf_yrsg = (rkc_qngr - qngrgvzr.hgpabj()).qnlf
                                vs qnlf_yrsg < 3:
                                    cevag(s"  {ERQ}◉ {yvar}  ← RKCVERQ {nof(qnlf_yrsg)} unev ynyh!{ERFRG}")
                                ryvs qnlf_yrsg < 63:
                                    cevag(s"  {LRYYBJ}◉ {yvar}  ← {qnlf_yrsg} unev yntv!{ERFRG}")
                                ryfr:
                                    cevag(s"  {TERRA}◉ {yvar}  ({qnlf_yrsg} unev yntv){ERFRG}")
                                oernx
                            rkprcg:
                                pbagvahr
                        ryfr:
                            cevag(s"  {LRYYBJ}{yvar}{ERFRG}")
                    rkprcg:
                        cevag(s"  {LRYYBJ}{yvar}{ERFRG}")
                ryfr:
                    cevag(s"  {LRYYBJ}{yvar}{ERFRG}")
            ryfr:
                cevag(s"  {QVZ}{yvar}{ERFRG}")
        fnir_ybt(s"JUBVF {g}")
    ryfr:
        cevag(s"  {ERQ}✗ JUBVF tntny.{ERFRG}")

@fperra_zbqr("TRB VC")
qrs trb_vc(g):
    g = fgevc_fpurzr(g)
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("phey"):
        erghea
    vc = trg_vc(g)
    dhrel = vc vs vc ryfr g
    cevag(s"  {PLNA}◉ TrbVC  {g}  →  {dhrel}{ERFRG}\a")

    e = eha(s"phey -f --znk-gvzr 43 vcvasb.vb/{dhrel}")
    vs e naq e.fgqbhg.fgevc():
        gel:
            qngn = wfba.ybnqf(e.fgqbhg)
            vs qngn.trg("obtba"):
                cevag(s"  {LRYYBJ}⚠ VC cevingr/obtba — gvqnx nqn trb vasb.{ERFRG}")
                erghea
            cevag_frc()
            svryqf = [
                ("VC",        "vc"),
                ("Ubfganzr",  "ubfganzr"),
                ("Xbgn",      "pvgl"),
                ("Ertvba",    "ertvba"),
                ("Artnen",    "pbhagel"),
                ("Ybxnfv",    "ybp"),
                ("VFC / BET", "bet"),
                ("Cbfgny",    "cbfgny"),
                ("Gvzrmbar",  "gvzrmbar"),
            ]
            sbe ynory, xrl va svryqf:
                iny = qngn.trg(xrl, "A/N")
                pbybe = JUVGR vs iny naq iny != "A/N" ryfr ERQ
                cevag(s"  {QVZ}{ynory:<45}{ERFRG}{pbybe}{iny}{ERFRG}")

            ybp = qngn.trg("ybp","")
            vs ybp:
                yng, yba = ybp.fcyvg(",")
                cevag(s"\a  {PLNA}◉ Zncf  →  uggcf://zncf.tbbtyr.pbz/?d={yng},{yba}{ERFRG}")

            bet = qngn.trg("bet","")
            ubfgvat_xrljbeqf = ["ubfgvat","freire","pybhq","qngnpragre","icf","njf","nmher","tbbtyr","qvtvgnybprna","yvabqr","ihyge","biu"]
            vs nal(xj va bet.ybjre() sbe xj va ubfgvat_xrljbeqf):
                cevag(s"  {LRYYBJ}⚠ Xrzhatxvana Ubfgvat / ICA / Pybhq{ERFRG}")

            fnir_ybt(s"TRBVC {g}: {qngn.trg('pvgl')},{qngn.trg('pbhagel')}")
        rkprcg wfba.WFBAQrpbqrReebe:
            cevag(e.fgqbhg[:833])
    ryfr:
        cevag(s"  {ERQ}✗ Tntny TrbVC. Prx vagrearg.{ERFRG}")

@fperra_zbqr("UGGC URNQRE")
qrs uggc_urnqre_fpna(g):
    g = g.fgevc()
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("phey"):
        erghea
    cevag(s"  {PLNA}◉ Urnqref qnev  {g}...{ERFRG}\a")

    e = eha(s"phey -V -f --znk-gvzr 43 -Y -N 'Zbmvyyn/8.3' --znk-erqvef 8 {g}")
    vs abg (e naq e.fgqbhg.fgevc()):
        g_uggc = g.ercynpr("uggcf://","uggc://")
        e = eha(s"phey -V -f --znk-gvzr 43 {g_uggc}")
        vs abg (e naq e.fgqbhg.fgevc()):
            cevag(s"  {ERQ}✗ Tntny nzovy urnqre.{ERFRG}")
            erghea

    frphevgl_urnqref = {
        "fgevpg-genafcbeg-frphevgl":"UFGF",
        "pbagrag-frphevgl-cbyvpl":"PFC",
        "k-senzr-bcgvbaf":"Pyvpxwnpxvat Cebgrpg",
        "k-kff-cebgrpgvba":"KFF Cebgrpg",
        "k-pbagrag-glcr-bcgvbaf":"ZVZR Favss Cebgrpg",
        "ersreere-cbyvpl":"Ersreere Cbyvpl",
        "crezvffvbaf-cbyvpl":"Crezvffvbaf Cbyvpl",
    }
    sbhaq_frp = []
    erqverpg_pbhag = 3

    cevag_frc()
    sbe yvar va e.fgqbhg.fcyvg("\a"):
        yvar = yvar.fgevc()
        vs abg yvar:
            pbagvahr
        ybj = yvar.ybjre()
        vs yvar.fgnegfjvgu("UGGC/"):
            cnegf = yvar.fcyvg()
            pbqr = cnegf[4] vs yra(cnegf) > 4 ryfr "?"
            qrfp = {
                "533":"BX","634":"Zbirq Creznaragyl","635":"Sbhaq",
                "637":"Abg Zbqvsvrq","733":"Onq Erdhrfg","734":"Hanhgubevmrq",
                "736":"Sbeovqqra","737":"Abg Sbhaq","833":"Vagreany Freire Reebe",
                "836":"Freivpr Haninvynoyr"
            }.trg(pbqr,"")
            pbybe = TERRA vs pbqr.fgnegfjvgu("5") ryfr (LRYYBJ vs pbqr.fgnegfjvgu("6") ryfr ERQ)
            cevag(s"  {pbybe}{OBYQ}{yvar}  {qrfp}{ERFRG}")
            vs pbqr.fgnegfjvgu("6"):
                erqverpg_pbhag += 4
        ryvs "ybpngvba:" va ybj:
            cevag(s"  {LRYYBJ}{yvar}  ← erqverpg{ERFRG}")
        ryvs "frg-pbbxvr:" va ybj:
            vffhrf = []
            vs "uggcbayl" abg va ybj:
                vffhrf.nccraq("AB UggcBayl")
            vs "frpher" abg va ybj:
                vffhrf.nccraq("AB Frpher")
            vs "fnzrfvgr" abg va ybj:
                vffhrf.nccraq("AB FnzrFvgr")
            synt_fge = s"  ⚠ {', '.wbva(vffhrf)}" vs vffhrf ryfr "  ✓"
            synt_pbybe = ERQ vs vffhrf ryfr TERRA
            cevag(s"  {PLNA}{yvar}{synt_pbybe}{synt_fge}{ERFRG}")
        ryvs nal(k va ybj sbe k va ["freire:","k-cbjrerq-ol:","ivn:","k-trarengbe:"]):
            cevag(s"  {LRYYBJ}{yvar}  ← svatrecevag{ERFRG}")
        ryvs nal(x va ybj sbe x va frphevgl_urnqref):
            sbe x, qrfp va frphevgl_urnqref.vgrzf():
                vs x va ybj:
                    sbhaq_frp.nccraq(qrfp)
            cevag(s"  {TERRA}{yvar}{ERFRG}")
        ryfr:
            cevag(s"  {QVZ}{yvar}{ERFRG}")

    vs erqverpg_pbhag > 3:
        cevag(s"\a  {LRYYBJ}⚠ {erqverpg_pbhag} erqverpg grewnqv.{ERFRG}")

    cevag_frc()
    frpgvba_gvgyr("Frphevgl Urnqref Ercbeg")
    fpber = 3
    sbe f va frphevgl_urnqref.inyhrf():
        vs f va sbhaq_frp:
            cevag(s"  {TERRA}✓  {f}{ERFRG}")
            fpber += 4
        ryfr:
            cevag(s"  {ERQ}✗  {f}  — ZVFFVAT{ERFRG}")

    tenqr = "N" vs fpber >= 9 ryfr ("O" vs fpber >= 7 ryfr ("P" vs fpber >= 5 ryfr "S"))
    t_pbybe = TERRA vs tenqr == "N" ryfr (LRYYBJ vs tenqr va "OP" ryfr ERQ)
    cevag(s"\a  {t_pbybe}{OBYQ}Frphevgl Fpber :  {fpber} / {yra(frphevgl_urnqref)}   Tenqr : {tenqr}{ERFRG}")
    fnir_ybt(s"UGGC URNQRE {g} fpber:{fpber}/0")

@fperra_zbqr("FFY PURPX")
qrs ffy_purpx(g):
    g = fgevc_fpurzr(g)
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("bcraffy"):
        erghea
    cevag(s"  {PLNA}◉ FFY Purpx  {g}:776{ERFRG}\a")

    e = eha(
        s"rpub | bcraffy f_pyvrag -pbaarpg {g}:776 -freireanzr {g} 5>/qri/ahyy",
        gvzrbhg=48
    )
    vs abg (e naq e.fgqbhg.fgevc()):
        cevag(s"  {ERQ}✗ Xbarxfv FFY tntny.{ERFRG}")
        erghea

    cevag_frc()
    vffhrf = []
    sbe yvar va e.fgqbhg.fcyvg("\a"):
        yvar = yvar.fgevc()
        vs nal(k va yvar sbe k va ["fhowrpg=","vffhre="]):
            cevag(s"  {PLNA}{yvar}{ERFRG}")
        ryvs "abgOrsber" va yvar:
            cevag(s"  {TERRA}◉ Vffhrq  : {yvar}{ERFRG}")
        ryvs "abgNsgre" va yvar:
            gel:
                qngr_fge = yvar.fcyvg("=",4)[4].fgevc()
                rkc = qngrgvzr.fgecgvzr(qngr_fge, "%o %q %U:%Z:%F %L %M")
                fvfn = (rkc - qngrgvzr.hgpabj()).qnlf
                vs fvfn < 3:
                    vffhrf.nccraq("Fregvsvxng RKCVERQ")
                    cevag(s"  {ERQ}✗ Rkcverq : {qngr_fge}  ← FHQNU RKCVERQ!{ERFRG}")
                ryvs fvfn < 47:
                    vffhrf.nccraq(s"Fregvsvxng unovf {fvfn} unev yntv")
                    cevag(s"  {ERQ}⚠ Rkcverq : {qngr_fge}  ← {fvfn} unev yntv! FRTREN ERARJ!{ERFRG}")
                ryvs fvfn < 63:
                    cevag(s"  {LRYYBJ}⚠ Rkcverq : {qngr_fge}  ← {fvfn} unev yntv!{ERFRG}")
                ryfr:
                    cevag(s"  {TERRA}✓ Rkcverq : {qngr_fge}  ({fvfn} unev yntv){ERFRG}")
            rkprcg:
                cevag(s"  {TERRA}{yvar}{ERFRG}")
        ryvs "Irevsl erghea pbqr" va yvar:
            pbybe = TERRA vs "3 (bx)" va yvar.ybjre() ryfr ERQ
            znex = "✓" vs "3 (bx)" va yvar.ybjre() ryfr "✗"
            vs znex == "✗":
                vffhrf.nccraq("FFY Irevsl TNTNY")
            cevag(s"  {pbybe}{znex} {yvar}{ERFRG}")
        ryvs "Cebgbpby" va yvar:
            vs nal(byq va yvar sbe byq va ["GYFi4 ","GYFi4.3","GYFi4.4","FFYi6","FFYi5"]):
                vffhrf.nccraq(s"Cebgbxby ynzn: {yvar.fgevc()}")
                cevag(s"  {ERQ}⚠ {yvar}  ← QRCERPNGRQ!{ERFRG}")
            ryfr:
                cevag(s"  {TERRA}✓ {yvar}{ERFRG}")
        ryvs "Pvcure" va yvar:
            cevag(s"  {LRYYBJ}◉ {yvar}{ERFRG}")

    cevag_frc()
    frpgvba_gvgyr("Cebgbpby Grfg")
    sbe cebgb, ynory va [("-gyf4_5","GYFi4.5"),("-gyf4_4","GYFi4.4"),("-gyf4","GYFi4.3")]:
        ce = eha(s"rpub | bcraffy f_pyvrag {cebgb} -pbaarpg {g}:776 -freireanzr {g} 5>&4 | terc -p 'Pvcure'", gvzrbhg=1)
        vs ce naq ce.fgqbhg.fgevc() == "4":
            pbybe = TERRA vs "4.5" va ynory ryfr ERQ
            znex = "✓" vs "4.5" va ynory ryfr "✗ QRCERPNGRQ"
            vs "QRCERPNGRQ" va znex:
                vffhrf.nccraq(s"{ynory} znfvu nxgvs")
            cevag(s"  {pbybe}{znex}  {ynory} fhccbegrq{ERFRG}")
        ryfr:
            cevag(s"  {ERQ}○  {ynory} gvqnx fhccbeg / gvzrbhg{ERFRG}")

    cevag_frc()
    vs vffhrf:
        cevag(s"\a  {ERQ}{OBYQ}⚠ VFFHRF QVGRZHXNA :{ERFRG}")
        sbe vff va vffhrf:
            cevag(s"    {ERQ}→  {vff}{ERFRG}")
    ryfr:
        cevag(s"\a  {TERRA}{OBYQ}✓ FFY BX — Gvqnx nqn znfnynu qvgrzhxna.{ERFRG}")

    fnir_ybt(s"FFY PURPX {g} vffhrf:{yra(vffhrf)}")

@fperra_zbqr("QVE FPNA")
qrs qve_oehgrsbepr(g):
    g = g.fgevc().efgevc("/")
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    vs abg gbby_purpx("phey"):
        erghea
    cnguf = [
        "nqzva","ybtva","qnfuobneq","cnary","nqzvavfgengbe",
        "jc-nqzva","jc-ybtva.cuc","cuczlnqzva","pcnary",
        ".rai",".tvg/pbasvt",".ugnpprff","jro.pbasvt",
        "pbasvt.cuc","pbasvt.wfba","frggvatf.cl",
        "ebobgf.gkg","fvgrznc.kzy","ernqzr.gkg","PUNATRYBT.zq",
        "pbzcbfre.wfba","cnpxntr.wfba",
        "ncv","ncv/i4","ncv/i5","tencudy","fjnttre",
        "fjnttre-hv","fjnttre.wfba","bcrancv.wfba",
        "onpxhc","onpxhc.mvc","qo.fdy","qhzc.fdy",
        "qri","grfg","orgn","fgntvat","qroht",
        "cucvasb.cuc","vasb.cuc","freire-fgnghf",
        "hcybnqf","svyrf","zrqvn","vzntrf","nffrgf",
    ]
    sbhaq = []
    ybpx = guernqvat.Ybpx()

    frpgvba_gvgyr("Fpna Pbasvthengvba")
    cevag(s"  {QVZ}{'Gnetrg':<45}{ERFRG}{JUVGR}{g}{ERFRG}")
    cevag(s"  {QVZ}{'Cnguf':<45}{ERFRG}{JUVGR}{yra(cnguf)} ragevrf  ·  Guernqrq{ERFRG}")
    cevag_frc()

    qrs purpx_cngu(c):
        hey = s"{g}/{c}"
        e = eha(
            s"phey -b /qri/ahyy -f -j '%{{uggc_pbqr}}:%{{fvmr_qbjaybnq}}' --znk-gvzr 8 -Y {hey}",
            gvzrbhg=1
        )
        vs abg e:
            erghea
        cnegf = e.fgqbhg.fgevc().fcyvg(":")
        pbqr = cnegf[3]
        fvmr = sbezng_olgrf(cnegf[4]) vs yra(cnegf) > 4 ryfr "?"
        jvgu ybpx:
            vs pbqr == "533":
                cevag(s"  {TERRA}● 533  SBHAQ   {hey}  [{fvmr}]{ERFRG}")
                sbhaq.nccraq(hey)
                fnir_ybt(s"QVE SBHAQ {hey}")
            ryvs pbqr va ("634","635","630","631"):
                cevag(s"  {LRYYBJ}◉ {pbqr}  ERQVE   {hey}{ERFRG}")
            ryvs pbqr == "736":
                cevag(s"  {PLNA}◈ 736  SBEOVQ  {hey}{ERFRG}")
            ryvs pbqr == "734":
                cevag(s"  {ZNTRAGN}◈ 734  NHGU    {hey}{ERFRG}")
            ryfr:
                cevag(s"  {QVZ}○ {pbqr}  ZVFF    {hey}{ERFRG}")

    guernqf = []
    sbe c va cnguf:
        gu = guernqvat.Guernq(gnetrg=purpx_cngu, netf=(c,))
        gu.fgneg()
        guernqf.nccraq(gu)
        gvzr.fyrrc(3.37)
    sbe gu va guernqf:
        gu.wbva()

    cevag_frc()
    cevag(s"  {PLNA}◉ Fryrfnv :  {JUVGR}{yra(sbhaq)}{PLNA} cngu qvgrzhxna.{ERFRG}")
    vs sbhaq:
        frpgvba_gvgyr("Sbhaq Yvfg")
        sbe s va sbhaq:
            cevag(s"    {TERRA}→  {s}{ERFRG}")

@fperra_zbqr("FHOQBZNVA")
qrs fhoqbznva_fpna(q):
    q = fgevc_fpurzr(q)
    vs abg vf_inyvq_gnetrg(q):
        cevag(s"  {ERQ}✗ Qbznva gvqnx inyvq.{ERFRG}")
        erghea
    fhof = [
        "jjj","znvy","ncv","qri","grfg","orgn","pcnary",
        "sgc","fzgc","cbc","vznc","jroznvy","z","zbovyr",
        "ncc","nqzva","cbegny","fubc","oybt","sbehz",
        "fhccbeg","uryc","pqa","fgngvp","zrqvn","vzt",
        "vzntrf","nffrgf","hcybnq","ica","erzbgr","tvg",
        "tvgyno","wraxvaf","pv","fgntvat","hng","cebq",
        "af4","af5","zk","nhgbqvfpbire","nhgbpbasvt",
        "qnfuobneq","cnary","znantr","fgnghf","zbavgbe",
        "tensnan","xvonan","cuczlnqzva",
    ]
    sbhaq = []
    ybpx = guernqvat.Ybpx()

    frpgvba_gvgyr("Fpna Pbasvthengvba")
    cevag(s"  {QVZ}{'Gnetrg':<45}{ERFRG}{JUVGR}{q}{ERFRG}")
    cevag(s"  {QVZ}{'Jbeqf':<45}{ERFRG}{JUVGR}{yra(fhof)} fhoqbznva{ERFRG}")
    cevag_frc()

    qrs purpx(f):
        ubfg = s"{f}.{q}"
        vc = trg_vc(ubfg)
        jvgu ybpx:
            vs vc:
                cevag(s"  {TERRA}● SBHAQ  {ubfg:<61}→  {vc}{ERFRG}")
                sbhaq.nccraq((ubfg, vc))
                fnir_ybt(s"FHOQBZNVA {ubfg}->{vc}")

    cevag(s"  {PLNA}◉ Fpnaavat...{ERFRG}\a")
    guernqf = [guernqvat.Guernq(gnetrg=purpx, netf=(f,)) sbe f va fhof]
    sbe gu va guernqf: gu.fgneg()
    sbe gu va guernqf: gu.wbva()

    cevag_frc()
    cevag(s"  {PLNA}◉ Fryrfnv :  {JUVGR}{yra(sbhaq)}{PLNA} fhoqbznva nxgvs.{ERFRG}")
    vs abg sbhaq:
        cevag(s"  {ERQ}✗ Gvqnx nqn fhoqbznva lnat qvgrzhxna.{ERFRG}")

@fperra_zbqr("SHYY FRPHEVGL ERCBEG")
qrs frphevgl_ercbeg(g):
    g = fgevc_fpurzr(g.fgevc())
    vs abg vf_inyvq_gnetrg(g):
        cevag(s"  {ERQ}✗ Gnetrg gvqnx inyvq.{ERFRG}")
        erghea
    hey = abeznyvmr_hey(g)
    vc = trg_vc(g)
    nyy_vcf = trg_nyy_vcf(g)
    fgneg_gvzr = gvzr.gvzr()

    frpgvba_gvgyr("Ercbeg Vasbezngvba")
    cevag(s"  {QVZ}{'Gnetrg':<45}{ERFRG}{JUVGR}{g}{ERFRG}")
    cevag(s"  {QVZ}{'VC':<45}{ERFRG}{JUVGR}{vc be 'Tntny erfbyir'}{ERFRG}")
    cevag(s"  {QVZ}{'HEY':<45}{ERFRG}{JUVGR}{hey}{ERFRG}")
    cevag(s"  {QVZ}{'Gvzr':<45}{ERFRG}{JUVGR}{qngrgvzr.abj().fgesgvzr('%L-%z-%q %U:%Z:%F')}{ERFRG}")
    cevag_frc()

    evfx_fpber = 3
    svaqvatf = []

    # 4. QAF
    frpgvba_gvgyr("[ 4 / 9 ]  QAF", "◈")
    qaf_ybbxhc_enj(g)
    vs yra(nyy_vcf) > 4:
        cevag(s"  {PLNA}◉ Zhygv-VC / PQA  {', '.wbva(nyy_vcf[:8])}{ERFRG}")

    # 5. CVAT + Yngrapl
    frpgvba_gvgyr("[ 5 / 9 ]  Cvat & Yngrapl", "◈")
    e = eha(s"cvat -p 6 -J 5 {g}", gvzrbhg=48)
    vs e naq e.ergheapbqr == 3:
        sbe yvar va e.fgqbhg.fgevc().fcyvg("\a"):
            vs "egg" va yvar be "cnpxrg" va yvar:
                cevag(s"  {TERRA}{yvar.fgevc()}{ERFRG}")
        yng = pnyp_yngrapl(g)
        vs yng:
            d = "Rkpryyrag" vs yng < 53 ryfr ("Tbbq" vs yng < 13 ryfr "Snve")
            cevag(s"  {TERRA}◉ Fgnghf : NXGVS  ·  Nit : {yng:.4s}zf  [{d}]{ERFRG}")
    ryfr:
        cevag(s"  {ERQ}✗ Gvqnx erfcba cvat  (VPZC zhatxva qvoybxve){ERFRG}")

    e_cvat4 = eha(s"cvat -p 4 -J 5 {g}", gvzrbhg=8)
    vs e_cvat4 naq e_cvat4.fgqbhg:
        sbe yvar va e_cvat4.fgqbhg.fcyvg("\a"):
            vs "ggy=" va yvar.ybjre():
                gel:
                    ggy = vag(er.frnepu(e"ggy=(\q+)", yvar, er.V).tebhc(4))
                    bf_t = "Yvahk/Havk" vs ggy <= 97 ryfr ("Jvaqbjf" vs ggy <= 451 ryfr "Argjbex Qrivpr")
                    cevag(s"  {LRYYBJ}◉ GGY : {ggy}  →  {bf_t}{ERFRG}")
                rkprcg: cnff

    # 6. CBEG FPNA
    frpgvba_gvgyr("[ 6 / 9 ]  Cbeg Fpna", "◈")
    UVTU_EVFX = {54,56,6612,8233,9602,50340,4766}
    vs vc:
        bcra_c = []
        ybpx = guernqvat.Ybpx()
        qrs cfpna(c, fip):
            f = fbpxrg.fbpxrg()
            f.frggvzrbhg(3.9)
            vs f.pbaarpg_rk((vc, c)) == 3:
                jvgu ybpx:
                    onaare = teno_onaare(vc, c)
                    o_fge = s"  {QVZ}{onaare}{ERFRG}" vs onaare ryfr ""
                    vf_evfx = c va UVTU_EVFX
                    pbybe = ERQ vs vf_evfx ryfr TERRA
                    ynory = "  [UVTU-EVFX]" vs vf_evfx ryfr ""
                    cevag(s"  {pbybe}● BCRA  {c:8}  ({fip}){ynory}{o_fge}{ERFRG}")
                    bcra_c.nccraq(c)
            f.pybfr()
        guf = [guernqvat.Guernq(gnetrg=cfpna, netf=(c,fip)) sbe c,fip va PBZZBA_CBEGF.vgrzf()]
        sbe gu va guf: gu.fgneg()
        sbe gu va guf: gu.wbva()
        evfxl = [c sbe c va bcra_c vs c va UVTU_EVFX]
        evfx_fpber += yra(evfxl) * 5
        vs evfxl:
            svaqvatf.nccraq(s"Cbeg uvtu-evfx greohxn: {evfxl}")
        cevag(s"  {PLNA}◉ {yra(bcra_c)} cbeg greohxn qnev {yra(PBZZBA_CBEGF)}{ERFRG}")

    # 7. UGGC URNQRE
    frpgvba_gvgyr("[ 7 / 9 ]  UGGC Urnqre", "◈")
    vs gbby_purpx("phey"):
        e5 = eha(s"phey -V -f --znk-gvzr 1 {hey}")
        vs e5 naq e5.fgqbhg:
            frp_sbhaq = 3
            frp_gbgny = 0
            frp_xrlf = ["fgevpg-genafcbeg-frphevgl","pbagrag-frphevgl-cbyvpl","k-senzr-bcgvbaf",
                        "k-pbagrag-glcr-bcgvbaf","ersreere-cbyvpl","crezvffvbaf-cbyvpl","k-kff-cebgrpgvba"]
            sbe yvar va e5.fgqbhg.fcyvg("\a")[:53]:
                y = yvar.fgevc()
                vs y:
                    ybj = y.ybjre()
                    vs nal(x va ybj sbe x va frp_xrlf):
                        frp_sbhaq += 4
                    pbybe = LRYYBJ vs nal(k va ybj sbe k va ["freire","cbjrerq"]) ryfr QVZ
                    cevag(s"  {pbybe}{y}{ERFRG}")
            zvffvat = frp_gbgny - frp_sbhaq
            vs zvffvat > 6:
                evfx_fpber += 5
                svaqvatf.nccraq(s"{zvffvat} frphevgl urnqre uvynat")
            cevag(s"  {PLNA}◉ Frphevgl urnqref : {frp_sbhaq} / {frp_gbgny}{ERFRG}")

    # 8. FFY
    frpgvba_gvgyr("[ 8 / 9 ]  FFY", "◈")
    vs gbby_purpx("bcraffy"):
        e6 = eha(s"rpub | bcraffy f_pyvrag -pbaarpg {g}:776 -freireanzr {g} 5>/qri/ahyy")
        vs e6 naq e6.fgqbhg:
            sbe yvar va e6.fgqbhg.fcyvg("\a"):
                yvar = yvar.fgevc()
                vs "abgNsgre" va yvar:
                    gel:
                        qngr_fge = yvar.fcyvg("=",4)[4].fgevc()
                        rkc = qngrgvzr.fgecgvzr(qngr_fge, "%o %q %U:%Z:%F %L %M")
                        fvfn = (rkc - qngrgvzr.hgpabj()).qnlf
                        vs fvfn < 3:
                            evfx_fpber += 8
                            svaqvatf.nccraq("FFY RKCVERQ")
                            cevag(s"  {ERQ}✗ FFY RKCVERQ!  {qngr_fge}{ERFRG}")
                        ryvs fvfn < 63:
                            evfx_fpber += 5
                            svaqvatf.nccraq(s"FFY unzcve rkcverq ({fvfn} unev)")
                            cevag(s"  {LRYYBJ}⚠ FFY {fvfn} unev yntv rkcver :  {qngr_fge}{ERFRG}")
                        ryfr:
                            cevag(s"  {TERRA}✓ FFY BX — {fvfn} unev yntv :  {qngr_fge}{ERFRG}")
                    rkprcg:
                        cevag(s"  {QVZ}{yvar}{ERFRG}")
                ryvs "Irevsl erghea pbqr" va yvar:
                    pbybe = TERRA vs "3 (bx)" va yvar.ybjre() ryfr ERQ
                    znex = "✓" vs "3 (bx)" va yvar.ybjre() ryfr "✗"
                    cevag(s"  {pbybe}{znex} {yvar}{ERFRG}")
        ryfr:
            cevag(s"  {ERQ}✗ Gvqnx fhccbeg UGGCF / FFY tntny{ERFRG}")
            svaqvatf.nccraq("UGGCF gvqnx nxgvs ngnh FFY tntny")
            evfx_fpber += 6

    # 9. FHZZNEL
    ryncfrq = ebhaq(gvzr.gvzr()-fgneg_gvzr, 4)
    frpgvba_gvgyr("[ 9 / 9 ]  Fhzznel", "◈")
    cevag_frc()
    cevag(s"  {QVZ}{'Qhengvba':<47}{ERFRG}{JUVGR}{ryncfrq}f{ERFRG}")
    cevag(s"  {QVZ}{'Gnetrg':<47}{ERFRG}{JUVGR}{g}{ERFRG}")
    cevag(s"  {QVZ}{'VC':<47}{ERFRG}{JUVGR}{vc be 'A/N'}{ERFRG}")

    vs svaqvatf:
        cevag(s"\a  {ERQ}{OBYQ}⚠ SVAQVATF :{ERFRG}")
        sbe s va svaqvatf:
            cevag(s"    {ERQ}→  {s}{ERFRG}")

    evfx_ynory = "YBJ" vs evfx_fpber < 6 ryfr ("ZRQVHZ" vs evfx_fpber < 0 ryfr "UVTU")
    e_pbybe = TERRA vs evfx_fpber < 6 ryfr (LRYYBJ vs evfx_fpber < 0 ryfr ERQ)
    cevag(s"\a  {e_pbybe}{OBYQ}Evfx Fpber :  {evfx_fpber}  [{evfx_ynory}]{ERFRG}")

    cevag_frc()
    fnir_bhgchg_qrzb(g)
    cevag(s"\a  {TERRA}{OBYQ}✓ Shyy Frphevgl Ercbeg Fryrfnv!{ERFRG}")
    fnir_ybt(s"SHYY ERCBEG {g} evfx:{evfx_ynory}({evfx_fpber})")

# ================= NV =================
gel:
    vzcbeg clggfk6
    ratvar = clggfk6.vavg()
rkprcg:
    ratvar = Abar

qrs nv_ibvpr_zbqr():
    vs ratvar:
        grkg = vachg("  NV Ibvpr : ")
        ratvar.fnl(grkg)
        ratvar.ehaNaqJnvg()
    ryfr:
        cevag(s"  {ERQ}✗ Ibvpr gvqnx grefrqvn.{ERFRG}")
        cevag(s"  {LRYYBJ}  Vafgnyy : cvc vafgnyy clggfk6{ERFRG}")

# ============================================================
#  FHO-ZRAH QNFUOBNEQF
# ============================================================

qrs fho_urnqre(gvgyr, pbybe=PLNA):
    pyrne()
    one = "═" * J
    cevag()
    cevag(s"  {pbybe}{OBYQ}╔{one}╗")
    cevag(s"  ║  🔐 FxlJvatf  ::  {gvgyr:<{J-41}}║")
    cevag(s"  ╚{one}╝{ERFRG}")
    cevag()

qrs fho_onpx_cebzcg():
    cevag()
    cevag(s"  {QVZ}{'─'*J}{ERFRG}")
    cevag(s"  {PLNA}  [3]  ←  Xrzonyv xr Znva Zrah{ERFRG}")
    cevag(s"  {QVZ}{'─'*J}{ERFRG}")
    cevag()

qrs _zrah_vgrz(ahz, ynory, qrfp, pbybe=PLNA):
    cevag(s"  {pbybe}  [{ahz:>5}]  {ynory:<53}{QVZ}{qrfp}{ERFRG}")

# ─── ARGJBEX ───────────────────────────────────────────────
qrs zrah_argjbex():
    juvyr Gehr:
        fho_urnqre("ARGJBEX", TERRA)
        cevag(s"  {TERRA}{OBYQ}◈  ARGJBEX GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("4",  "Dhvpx Fpna",   "Vasb Prcng",      TERRA)
        _zrah_vgrz("5",  "Zhygv Fpna",   "Onalnx Gnetrg",   TERRA)
        _zrah_vgrz("6",  "Genpr Ebhgr",  "Ynpnx Ehgr",      TERRA)
        _zrah_vgrz("7",  "Cvat Gnetrg",  "VPZC Cvat",       TERRA)
        _zrah_vgrz("8",  "Cbeg Fpna",    "Fpna Cbeg",       TERRA)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "4":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: dhvpx_vasb(g)
        ryvs c == "5":
            enj = vachg(s"\a  {LRYYBJ}Gnetrgf (cvfnu fcnfv) : {ERFRG}").fgevc()
            vs enj: snfg_fpna(enj.fcyvg())
        ryvs c == "6":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: genpr_ebhgr(g)
        ryvs c == "7":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: cvat_gnetrg(g)
        ryvs c == "8":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: cbeg_fpna(g)
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ─── JRO VAGRY ─────────────────────────────────────────────
qrs zrah_jrovagry():
    juvyr Gehr:
        fho_urnqre("JRO VAGRY", PLNA)
        cevag(s"  {PLNA}{OBYQ}◈  JRO VAGRY GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("9",  "Jro Vasb",    "Urnqre + QAF",       PLNA)
        _zrah_vgrz("0",  "UGGC Urnqre", "Frphevgl Urnqre",    PLNA)
        _zrah_vgrz("1",  "Qve Fpna",    "Oehgr Cngu",         PLNA)
        _zrah_vgrz("2",  "Fhoqbznva",   "Rahz Fhoqbznva",     PLNA)
        _zrah_vgrz("43", "FFY Purpx",   "Prx Fregvsvxng",     PLNA)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "9":
            g = vachg(s"\a  {LRYYBJ}Jro / Qbznva : {ERFRG}").fgevc()
            vs g:
                uggc_urnqre_fpna(abeznyvmr_hey(g))
                pyrne()
                xnyv_urnqre("JRO VASB - QAF")
                qaf_ybbxhc_enj(g)
                ragre_onpx()
        ryvs c == "0":
            g = vachg(s"\a  {LRYYBJ}HEY : {ERFRG}").fgevc()
            vs g: uggc_urnqre_fpna(abeznyvmr_hey(g))
        ryvs c == "1":
            g = vachg(s"\a  {LRYYBJ}HEY : {ERFRG}").fgevc()
            vs g: qve_oehgrsbepr(abeznyvmr_hey(g))
        ryvs c == "2":
            g = vachg(s"\a  {LRYYBJ}Qbznva : {ERFRG}").fgevc()
            vs g: fhoqbznva_fpna(g)
        ryvs c == "43":
            g = vachg(s"\a  {LRYYBJ}Qbznva : {ERFRG}").fgevc()
            vs g: ffy_purpx(g)
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ─── BFVAG ─────────────────────────────────────────────────
qrs zrah_bfvag():
    juvyr Gehr:
        fho_urnqre("BFVAG", LRYYBJ)
        cevag(s"  {LRYYBJ}{OBYQ}◈  BFVAG GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("44", "JUBVF",      "Vasb Qbznva",   LRYYBJ)
        _zrah_vgrz("45", "TRB VC",     "Ybxnfv VC",     LRYYBJ)
        _zrah_vgrz("46", "QAF Ybbxhc", "QAF Erpbeqf",   LRYYBJ)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "44":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: jubvf_ybbxhc(g)
        ryvs c == "45":
            g = vachg(s"\a  {LRYYBJ}VC / Qbznva : {ERFRG}").fgevc()
            vs g: trb_vc(g)
        ryvs c == "46":
            g = vachg(s"\a  {LRYYBJ}Qbznva : {ERFRG}").fgevc()
            vs g: qaf_ybbxhc_zrah(g)
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ─── FLFGRZ ────────────────────────────────────────────────
qrs zrah_flfgrz():
    juvyr Gehr:
        fho_urnqre("FLFGRZ", TERRA)
        cevag(s"  {TERRA}{OBYQ}◈  FLFGRZ GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("47", "Sverjnyy",    "Prx Sverjnyy",  TERRA)
        _zrah_vgrz("48", "Flfgrz Vasb", "Vasb BF & ENZ", TERRA)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "47":
            sverjnyy_purpx()
        ryvs c == "48":
            flfgrz_vasb()
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ─── NQINAPRQ ──────────────────────────────────────────────
qrs zrah_nqinaprq():
    juvyr Gehr:
        fho_urnqre("NQINAPRQ", ZNTRAGN)
        cevag(s"  {ZNTRAGN}{OBYQ}◈  NQINAPRQ GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("49", "Aznc Fpna",   "Nqinaprq Fpna",   ZNTRAGN)
        _zrah_vgrz("40", "Shyy Ercbeg", "Yncbena Yratxnc", ZNTRAGN)
        _zrah_vgrz("41", "Fnir Bhgchg", "Fvzcna Unfvy",    ZNTRAGN)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "49":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: nqinaprq_fpna(g)
        ryvs c == "40":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g: frphevgl_ercbeg(g)
        ryvs c == "41":
            g = vachg(s"\a  {LRYYBJ}Gnetrg : {ERFRG}").fgevc()
            vs g:
                pyrne()
                xnyv_urnqre("FNIR BHGCHG")
                fnir_bhgchg_qrzb(g)
                ragre_onpx()
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ─── NV GBBYF ──────────────────────────────────────────────
qrs zrah_nvgbbyf():
    juvyr Gehr:
        fho_urnqre("NV GBBYF", PLNA)
        cevag(s"  {PLNA}{OBYQ}◈  NV GBBYF{ERFRG}")
        cevag()
        _zrah_vgrz("42", "NV Ibvpr",  "Grkg gb Fcrrpu", PLNA)
        _zrah_vgrz("53", "Snfg Fpna", "Cvat Cnenyry",   PLNA)
        fho_onpx_cebzcg()

        c = vachg(fxljvatf_pbqrk()).fgevc()
        vs c == "3":
            oernx
        ryvs c == "42":
            nv_ibvpr_zbqr()
            ragre_onpx()
        ryvs c == "53":
            enj = vachg(s"\a  {LRYYBJ}Gnetrgf (cvfnu fcnfv) : {ERFRG}").fgevc()
            vs enj: snfg_fpna(enj.fcyvg())
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ============================================================
#  ZNVA ZRAH
# ============================================================

qrs znva_zrah():
    juvyr Gehr:
        pyrne()
        abj = qngrgvzr.abj()
        one = "═" * J

        cevag()
        cevag(s"  {PLNA}{OBYQ}╔{one}╗")
        cevag(s"  ║{'🔓  FLFGRZ FGNGHF  ::  YVIR':^{J}}║")
        cevag(s"  ║  {QVZ}Qngr : {abj.fgesgvzr('%L-%z-%q')}   Gvzr : {abj.fgesgvzr('%U:%Z:%F')}{PLNA}{' '*(J-61)}║")
        cevag(s"  ╚{one}╝{ERFRG}")
        cevag()

        pngrtbevrf = [
            ("4", "ARGJBEX",   "Fpna Wnevatna",  TERRA),
            ("5", "JRO VAGRY", "Nanyvfn Jro",    PLNA),
            ("6", "BFVAG",     "Vagryvwra",      LRYYBJ),
            ("7", "FLFGRZ",    "Vasb Fvfgrz",    TERRA),
            ("8", "NQINAPRQ",  "Fpna Ynawhgna",  ZNTRAGN),
            ("9", "NV GBBYF",  "Svghe NV",       PLNA),
        ]

        sbe ahz, anzr, qrfp, pby va pngrtbevrf:
            cevag(s"  {pby}  [{ahz}]  {OBYQ}{anzr:<47}{ERFRG}{QVZ}{qrfp}{ERFRG}")

        cevag()
        cevag(s"  {QVZ}{'─'*J}{ERFRG}")
        cevag(s"  {ERQ}  [3]  RKVG{ERFRG}")
        cevag(s"  {QVZ}{'─'*J}{ERFRG}")

        c = vachg(fxljvatf_pbqrk()).fgevc()

        vs c == "4":
            snapl_ybnqvat("RAGREVAT ARGJBEX")
            zrah_argjbex()
        ryvs c == "5":
            snapl_ybnqvat("RAGREVAT JRO VAGRY")
            zrah_jrovagry()
        ryvs c == "6":
            snapl_ybnqvat("RAGREVAT BFVAG")
            zrah_bfvag()
        ryvs c == "7":
            snapl_ybnqvat("RAGREVAT FLFGRZ")
            zrah_flfgrz()
        ryvs c == "8":
            snapl_ybnqvat("RAGREVAT NQINAPRQ")
            zrah_nqinaprq()
        ryvs c == "9":
            snapl_ybnqvat("RAGREVAT NV GBBYF")
            zrah_nvgbbyf()
        ryvs c == "3":
            cevag(s"\a  {PLNA}◉ FXLJVATF QBJA.  Fgnl fnsr.{ERFRG}\a")
            oernx
        ryfr:
            cevag(s"\a  {ERQ}✗ Cvyvuna gvqnx inyvq.{ERFRG}")
            gvzr.fyrrc(3.9)

# ================= ZNVA =================
qrs znva():
    pyrne()
    ybtb()
    ybnqvat("FXLJVATF  i4.3  OBBGVAT")
    gvzr.fyrrc(3.6)

    juvyr Gehr:
        xnyv_urnqre("FXLJVATF OL CHGEN")

        cevag(s"  {QVZ}{'─'*J}{ERFRG}")
        pzqf = [
            ("uryc",  "Znfhx xr frzhn svghe"),
            ("vasb",  "Flfgrz vasb"),
            ("pyrne", "Orefvuxna ynlne"),
            ("rkvg",  "Xryhne"),
        ]
        sbe pzq, qrfp va pzqf:
            cevag(s"  {TERRA}  {pzq:<1}{ERFRG}{QVZ}{qrfp}{ERFRG}")
        cevag(s"  {QVZ}{'─'*J}{ERFRG}")

        pzq = vachg(fxljvatf_pbqrk()).fgevc()

        vs pzq == "uryc":
            snapl_ybnqvat("RAGREVAT SRNGHER ZBQR")
            znva_zrah()
        ryvs pzq == "vasb":
            flfgrz_vasb()
        ryvs pzq == "pyrne":
            pyrne()
        ryvs pzq == "rkvg":
            cevag(s"\a  {PLNA}◉ FXLJVATF.  Fgnl fnsr.{ERFRG}\a")
            oernx
        ryfr:
            cevag(s"\a  {ERQ}✗ Pbzznaq gvqnx qvxrany. Xrgvx 'uryc'.{ERFRG}")

vs __anzr__ == "__znva__":
    znva()
