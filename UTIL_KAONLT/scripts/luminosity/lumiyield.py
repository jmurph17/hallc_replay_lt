#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-04-03 17:28:46 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
import uproot as up
import numpy as np
import sys

sys.path.insert(0, '/home/trottar/bin/python/')
import root2py as r2p

rootName = "../../ROOTfiles/lumi_coin_offline_5158_50000.root"

PS1 = 1
PS3 = 1
thres_curr = 2.5

'''
SCALER TREE, TSH
'''

s_tree = up.open(rootName)["TSH"]
s_branch = r2p.pyBranch(s_tree)

H_BCM4A_scalerCharge = s_tree.array("H.BCM4A.scalerCharge")
H_BCM2_scalerCharge = s_tree.array("H.BCM2.scalerCharge")
H_BCM4B_scalerCharge = s_tree.array("H.BCM4B.scalerCharge")
H_BCM1_scalerCharge = s_tree.array("H.BCM1.scalerCharge")
H_BCM4C_scalerCharge = s_tree.array("H.BCM4C.scalerCharge")

H_1Mhz_scalerTime = s_tree.array("H.1MHz.scalerTime")

H_hTRIG1_scaler = s_tree.array("H.pTRIG1.scaler")
H_hTRIG2_scaler = s_tree.array("H.pTRIG2.scaler")
H_hTRIG3_scaler = s_tree.array("H.pTRIG3.scaler")
H_hTRIG4_scaler = s_tree.array("H.pTRIG4.scaler")
H_hTRIG5_scaler = s_tree.array("H.pTRIG5.scaler")
H_hTRIG6_scaler = s_tree.array("H.pTRIG6.scaler")

H_hL1ACCP_scaler = s_tree.array("H.hL1ACCP.scaler")
H_hPRE40_scaler = s_tree.array("H.hPRE40.scaler")
H_hPRE100_scaler = s_tree.array("H.hPRE100.scaler")
H_hPRE150_scaler = s_tree.array("H.hPRE150.scaler")
H_hPRE200_scaler = s_tree.array("H.hPRE200.scaler")
H_pPRE40_scaler = s_tree.array("H.pPRE40.scaler")
H_pPRE100_scaler = s_tree.array("H.pPRE100.scaler")
H_pPRE150_scaler = s_tree.array("H.pPRE150.scaler")
H_pPRE200_scaler = s_tree.array("H.pPRE200.scaler")

H_hEL_LO_LO_scaler = s_tree.array("H.hEL_LO_LO.scaler")
H_hEL_LO_scaler = s_tree.array("H.hEL_LO.scaler")
H_hEL_HI_scaler = s_tree.array("H.hEL_HI.scaler")
H_hEL_REAL_scaler = s_tree.array("H.hEL_REAL.scaler")
H_hEL_CLEAN_scaler = s_tree.array("H.hEL_CLEAN.scaler")
H_hSTOF_scaler = s_tree.array("H.hSTOF.scaler")

H_pEL_LO_LO_scaler = s_tree.array("H.pEL_LO_LO.scaler")
H_pEL_LO_scaler = s_tree.array("H.pEL_LO.scaler")
H_pEL_HI_scaler = s_tree.array("H.pEL_HI.scaler")
H_pEL_REAL_scaler = s_tree.array("H.pEL_REAL.scaler")
H_pEL_CLEAN_scaler = s_tree.array("H.pEL_CLEAN.scaler")
H_pSTOF_scaler = s_tree.array("H.pSTOF.scaler")
H_pPRHI_scaler = s_tree.array("H.PRHI.scaler")
H_pPRLO_scaler = s_tree.array("H.PRLO.scaler")

H_EDTM_scaler = s_tree.array("H.EDTM.scaler")

def scaler(PS1,PS3,thres_curr):
    
    NBCM = 5
    NTRIG = 6
    NPRE = 4
    NRATE = 6
    SHMSNRATE = 8

    bcm_name = ["BCM1 ", "BCM2 ", "BCM4A", "BCM4B", "BCM4C"]

    trig_name = ["TRIG1", "TRIG2", "TRIG3", "TRIG4", "TRIG5", "TRIG6"]

    PRE_name = ["40", "100", "150", "200"]

    rate_name = ["EL_LO_LO", "EL_LO", "EL_HI", "EL_REAL", "EL_CLEAN", "STOF"]

    SHMS_rate_name = ["EL_LO_LO", "EL_LO", "EL_HI", "EL_REAL", "EL_CLEAN", "STOF", "PR_HI", "PR_LO"]


    bcm_value = [H_BCM1_scalerCharge, H_BCM2_scalerCharge,
                 H_BCM4A_scalerCharge, H_BCM4B_scalerCharge, H_BCM4C_scalerCharge]

    trig_value = [H_hTRIG1_scaler, H_hTRIG2_scaler, H_hTRIG3_scaler,
                  H_hTRIG4_scaler, H_hTRIG5_scaler, H_hTRIG6_scaler]

    acctrig_value = H_hL1ACCP_scaler

    PRE_value = [H_hPRE40_scaler, H_hPRE100_scaler,
                 H_hPRE150_scaler, H_hPRE200_scaler]

    SHMS_PRE_value = [H_pPRE40_scaler, H_pPRE100_scaler,
                      H_pPRE150_scaler, H_pPRE200_scaler]

    rate_value = [H_hEL_LO_LO_scaler, H_hEL_LO_scaler, H_hEL_HI_scaler,
                  H_hEL_REAL_scaler, H_hEL_CLEAN_scaler, H_hSTOF_scaler]

    SHMS_rate_value = [H_pEL_LO_LO_scaler, H_pEL_LO_scaler, H_pEL_HI_scaler,
                       H_pEL_REAL_scaler, H_pEL_CLEAN_scaler, H_pSTOF_scaler, H_pPRHI_scaler, H_pPRLO_scaler]

    EDTM_value = H_EDTM_scaler

    # Variables useful in Process
    # To find total charge
    name = [0]*NBCM
    charge_sum = [0]*NBCM
    time_sum = [0]*NBCM
    time_total = 0
    previous_charge = [0]*NBCM
    previous_time = 0
    current_I = 0
    current_time = 0
    Current = 0

    # To determine computer livetime
    name = [0]*NTRIG
    trig_sum = [0]*NTRIG
    previous_trig = [0]*NTRIG
    pretrigger = 0
    previous_pretrigger = 0
    acctrig_sum = 0
    previous_acctrig = 0

    # To determine HMS electronic livetime
    name = [0]*NPRE
    PRE_sum = [0]*NPRE
    previous_PRE = [0]*NPRE

    # To determine SHMS electronic livetime
    SHMS_PRE_sum = [0]*NPRE
    SHMS_previous_PRE = [0]*NPRE

    # To determine HMS trigger rates
    name = [0]*NRATE
    rate_sum = [0]*NRATE
    previous_rate = [0]*NRATE

    # To determine SHMS trigger rates
    rate_name = [0]*SHMSNRATE
    SHMS_rate_sum = [0]*SHMSNRATE
    SHMS_previous_rate = [0]*SHMSNRATE
    
    # To determine number of EDTM events
    EDTM_sum = 0
    EDTM_current = 0
    previous_EDTM = 0

    for ibcm in range(0, 5):
        current_I = 0
        for i, evt in enumerate(H_1Mhz_scalerTime):
            if (evt != previous_time):
                current_I = (bcm_value[ibcm][i] - previous_charge[ibcm])/(evt - previous_time)
            if (current_I > thres_curr):
                charge_sum[ibcm] += (bcm_value[ibcm][i] - previous_charge[ibcm])
                time_sum[ibcm] += (evt - previous_time)
            if (ibcm == 3 and (current_I > thres_curr)):
                EDTM_current = (EDTM_value - previous_EDTM)
                EDTM_sum += EDTM_current
                acctrig_sum += ((acctrig_value - EDTM_current) - previous_acctrig)
                for itrig in range(0, NTRIG):
                    trig_sum[itrig] += (trig_value[itrig] - previous_trig[itrig])
                for iPRE in range(0, NPRE):
                    PRE_sum[iPRE] += (PRE_value[iPRE] - previous_PRE[iPRE])
                    SHMS_PRE_sum[iPRE] += (SHMS_PRE_value[iPRE] - SHMS_previous_PRE[iPRE])
                for iRATE in range(0, NRATE):
                    rate_sum[iRATE] += (rate_value[iRATE] - previous_rate[iRATE])
                for iRATE in range(0, SHMSNRATE):
                    SHMS_rate_sum[iRATE] += (SHMS_rate_value[iRATE] - SHMS_previous_rate[iRATE])
                previous_acctrig = (acctrig_value - EDTM_current)
                previous_EDTM = EDTM_value
                for itrig in range(0, NTRIG):
                    previous_trig[itrig] = trig_value[itrig]
                for iPRE in range(0, NPRE):
                    previous_PRE[iPRE] = PRE_value[iPRE]
                    SHMS_previous_PRE[iPRE] = SHMS_PRE_value[iPRE]
                for iRATE in range(0, NRATE):
                    previous_rate[iRATE] = rate_value[iRATE]
                for iRATE in range(0, SHMSNRATE):
                    SHMS_previous_rate[iRATE] = SHMS_rate_value[iRATE]
            time_total += (evt - previous_time)
            previous_time = evt
        previous_charge[ibcm] = bcm_value[ibcm][i]

    scalers={
        "time" : time_sum[3],
        "charge" : charge_sum[3],
        "TRIG1_scaler" : sum(trig_sum[0]),
        "TRIG3_scaler" : sum(trig_sum[2]),
        "CPULT_scaler" : 1-sum(acctrig_sum)/((sum(trig_sum[0])/PS1) + (sum(trig_sum[2])/PS3)),
        "CPULT_scaler_uncern" : (sum(acctrig_sum)/((sum(trig_sum[0])/PS1) + (sum(trig_sum[2])/PS3)))*np.sqrt((1/(sum(trig_sum[0])/PS1))+(1/(sum(trig_sum[2])/PS3))+(1/sum(acctrig_sum))),
        "HMS_eLT" : 1 - ((6/5)*(sum(PRE_sum[1])-sum(PRE_sum[2]))/(sum(PRE_sum[1]))),
        "HMS_eLT_uncern" : (sum(PRE_sum[1])-sum(PRE_sum[2]))/(sum(PRE_sum[1]))*np.sqrt((np.sqrt(sum(PRE_sum[1])) + np.sqrt(sum(PRE_sum[2])))/(sum(PRE_sum[1]) - sum(PRE_sum[2])) + (np.sqrt(sum(PRE_sum[1]))/sum(PRE_sum[1]))),
        "SHMS_eLT" : 1 - ((6/5)*(sum(SHMS_PRE_sum[1])-sum(SHMS_PRE_sum[2]))/(sum(SHMS_PRE_sum[1]))),
        "SHMS_eLT_uncern" : (sum(SHMS_PRE_sum[1])-sum(SHMS_PRE_sum[2]))/(sum(SHMS_PRE_sum[1]))*np.sqrt((np.sqrt(sum(SHMS_PRE_sum[1])) + np.sqrt(sum(SHMS_PRE_sum[2])))/(sum(SHMS_PRE_sum[1]) - sum(SHMS_PRE_sum[2])) + (np.sqrt(sum(SHMS_PRE_sum[1]))/sum(SHMS_PRE_sum[1]))),
        "sent_edtm" : sum(EDTM_sum)
        
    }
        
    print("Using prescale factors: PS1 %.0f, PS3 %.0f\n" % (PS1,PS3))
    print("\n\nUsed current threshold value: %.2f uA" % thres_curr)

    for ibcm in range(0,NBCM):
        print("%s charge: %.3f uC, Beam over threshold for %.3f s" % (bcm_name[ibcm], charge_sum[ibcm], time_sum[ibcm]))
        
    print("\n\n")
  
    print("L1ACC counts: %.0f, \n%s Prescaled Pretrigger Counts: %.0f \n%s Prescaled Pretrigger Counts: %.0f \nComputer Livetime: %f +/- %f" % (sum(acctrig_sum), trig_name[0], scalers["TRIG1_scaler"], trig_name[2], scalers["TRIG3_scaler"],scalers["CPULT_scaler"], scalers["CPULT_scaler_uncern"]))
    
    print("HMS Electronic livetime: %f +/- %f" % (scalers["HMS_eLT"], scalers["HMS_eLT_uncern"]))
  
    print("SHMS Electronic livetime: %f +/- %f" % (scalers["SHMS_eLT"], scalers["SHMS_eLT_uncern"]))

    print("EDTM Events: %.0f" % scalers["sent_edtm"])
        
    return[scalers]

'''
ANALYSIS TREE, T
'''

tree = up.open(rootName)["T"]
branch = r2p.pyBranch(tree)

H_cal_etotnorm = tree.array("H.cal.etotnorm")
H_cer_npeSum = tree.array("H.cer.npeSum")
H_gtr_dp = tree.array("H.gtr.dp")
H_tr_tg_th = tree.array("H.gtr.th")
H_tr_tg_ph = tree.array("H.gtr.ph")
H_tr_beta = tree.array("H.tr.beta")
H_tr_chi2 = tree.array("H.tr.chi2")
H_tr_ndof = tree.array("H.tr.ndof")
H_hod_goodscinhit = tree.array("H.hod.goodscinhit")
H_hod_betanotrack = tree.array("H.hod.betanotrack")
H_dc_ntrack = tree.array("H.dc.ntrack")

H_dc_1x1_nhit = tree.array("H.dc.1x1.nhit")
H_dc_1u2_nhit = tree.array("H.dc.1u2.nhit")
H_dc_1u1_nhit = tree.array("H.dc.1u1.nhit")
H_dc_1v1_nhit = tree.array("H.dc.1v1.nhit")
H_dc_1x2_nhit = tree.array("H.dc.1x2.nhit")
H_dc_1v2_nhit = tree.array("H.dc.1v2.nhit")
H_dc_2x1_nhit = tree.array("H.dc.2x1.nhit")
H_dc_2u2_nhit = tree.array("H.dc.2u2.nhit")
H_dc_2u1_nhit = tree.array("H.dc.2u1.nhit")
H_dc_2v1_nhit = tree.array("H.dc.2v1.nhit")
H_dc_2x2_nhit = tree.array("H.dc.2x2.nhit")
H_dc_2v2_nhit = tree.array("H.dc.2v2.nhit")

P_cal_etotnorm = tree.array("P.cal.etotnorm")
P_hgcer_npeSum = tree.array("P.hgcer.npeSum")
P_aero_npeSum = tree.array("P.aero.npeSum")
P_gtr_dp = tree.array("P.gtr.dp")
P_gtr_th = tree.array("P.gtr.th")
P_gtr_ph = tree.array("P.gtr.ph")
P_tr_beta = tree.array("P.tr.beta")
P_tr_chi2 = tree.array("P.tr.chi2")
P_tr_ndof = tree.array("P.tr.ndof")
P_hod_goodscinhit = tree.array("P.hod.goodscinhit")
P_hod_betanotrack = tree.array("P.hod.betanotrack")
P_dc_ntrack = tree.array("P.dc.ntrack")

P_dc_1x1_nhit = tree.array("P.dc.1x1.nhit")
P_dc_1u2_nhit = tree.array("P.dc.1u2.nhit")
P_dc_1u1_nhit = tree.array("P.dc.1u1.nhit")
P_dc_1v1_nhit = tree.array("P.dc.1v1.nhit")
P_dc_1x2_nhit = tree.array("P.dc.1x2.nhit")
P_dc_1v2_nhit = tree.array("P.dc.1v2.nhit")
P_dc_2x1_nhit = tree.array("P.dc.2x1.nhit")
P_dc_2u2_nhit = tree.array("P.dc.2u2.nhit")
P_dc_2u1_nhit = tree.array("P.dc.2u1.nhit")
P_dc_2v1_nhit = tree.array("P.dc.2v1.nhit")
P_dc_2x2_nhit = tree.array("P.dc.2x2.nhit")
P_dc_2v2_nhit = tree.array("P.dc.2v2.nhit")

H_bcm_bcm4b_AvgCurrent = tree.array("H.bcm.bcm4b.AvgCurrent")

T_coin_pTRIG1_ROC1_tdcTime = tree.array("T.coin.pTRIG1_ROC1_tdcTime")
T_coin_pTRIG3_ROC1_tdcTime = tree.array("T.coin.pTRIG3_ROC1_tdcTime")
T_coin_pTRIG5_ROC1_tdcTime = tree.array("T.coin.pTRIG5_ROC1_tdcTime")
T_coin_pTRIG1_ROC2_tdcTime = tree.array("T.coin.pTRIG1_ROC2_tdcTime")
T_coin_pTRIG3_ROC2_tdcTime = tree.array("T.coin.pTRIG3_ROC2_tdcTime")
T_coin_pTRIG5_ROC2_tdcTime = tree.array("T.coin.pTRIG5_ROC2_tdcTime")

T_coin_pEDTM_tdcTime = tree.array("T.coin.pEDTM_tdcTime")

EvtType = tree.array("fEvtHdr.fEvtType")

def analysis(PS1,PS3,thres_curr):
    
     bcm_before = H_bcm_bcm4b_AvgCurrent
     if (H_bcm_bcm4b_AvgCurrent < 2.5): return True
     
    

def main():
    scaler(PS1,PS3,thres_curr)
    analysis(PS1,PS3,thres_curr)


if __name__ == '__main__':
    main()
    
