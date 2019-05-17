(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_27 () Int)
(declare-fun V_24 () Int)
(declare-fun V_22 () Int)
(declare-fun e () Int)
(declare-fun ix () Int)
(declare-fun buf () (Array Int Int))
(declare-fun a2 () (Array Int Int))
(declare-fun a1 () (Array Int Int))
(assert (let ((?v_0 (and (>= V_22 0) (>= V_24 0))) (?v_2 (= V_27 (+ V_24 V_22))) (?v_1 (> 0 0))) (and (and (and (and (forall ((?V_34 Int)) (=> (and (<= 0 ?V_34) (<= ?V_34 (- V_24 1))) (forall ((?V_35 Int)) (=> (and (<= 0 ?V_35) (<= ?V_35 ?V_34)) (<= (select a1 ?V_35) (select a1 ?V_34)))))) (forall ((?V_32 Int)) (=> (and (<= 0 ?V_32) (<= ?V_32 (- V_22 1))) (forall ((?V_33 Int)) (=> (and (<= 0 ?V_33) (<= ?V_33 ?V_32)) (<= (select a2 ?V_33) (select a2 ?V_32))))))) ?v_0) (and ?v_2 (and (and (forall ((?V_30 Int)) (=> (and (<= 0 ?V_30) (<= ?V_30 (- V_24 1))) (forall ((?V_31 Int)) (=> (and (<= 0 ?V_31) (<= ?V_31 ?V_30)) (<= (select a1 ?V_31) (select a1 ?V_30)))))) (forall ((?V_28 Int)) (=> (and (<= 0 ?V_28) (<= ?V_28 (- V_22 1))) (forall ((?V_29 Int)) (=> (and (<= 0 ?V_29) (<= ?V_29 ?V_28)) (<= (select a2 ?V_29) (select a2 ?V_28))))))) ?v_0))) (or ?v_1 (or (> 0 V_24) (or ?v_1 (or (> 0 V_22) (or ?v_1 (or (> 0 V_27) (or (not (= 0 (+ 0 0))) (or (not ?v_2) (or (not (= V_24 V_24)) (or (not (= V_22 V_22)) (or (exists ((?V_26 Int)) (let ((?v_3 (select a1 ?V_26))) (and (and (<= 0 ?V_26) (<= ?V_26 (- V_24 1))) (not (= ?v_3 ?v_3))))) (or (exists ((?V_25 Int)) (let ((?v_4 (select a2 ?V_25))) (and (and (<= 0 ?V_25) (<= ?V_25 (- V_22 1))) (not (= ?v_4 ?v_4))))) (or (and (not (= 0 V_24)) (exists ((?V_23 Int)) (and (and (<= 0 ?V_23) (<= ?V_23 (- 0 1))) (> (select buf ?V_23) (select a1 0))))) (or (and (not (= 0 V_22)) (exists ((?V_21 Int)) (and (and (<= 0 ?V_21) (<= ?V_21 (- 0 1))) (> (select buf ?V_21) (select a2 0))))) (or (exists ((?V_19 Int)) (and (and (<= 0 ?V_19) (<= ?V_19 (- 0 1))) (exists ((?V_20 Int)) (and (and (<= 0 ?V_20) (<= ?V_20 ?V_19)) (> (select buf ?V_20) (select buf ?V_19)))))) (or (and (or (exists ((?V_18 Int)) (and (and (<= 0 ?V_18) (<= ?V_18 (- 0 1))) (= (select a1 ?V_18) e))) (exists ((?V_17 Int)) (and (and (<= 0 ?V_17) (<= ?V_17 (- 0 1))) (= (select a2 ?V_17) e)))) (forall ((?V_16 Int)) (=> (and (<= 0 ?V_16) (<= ?V_16 (- 0 1))) (not (= (select buf ?V_16) e))))) (and (exists ((?V_15 Int)) (and (and (<= 0 ?V_15) (<= ?V_15 (- 0 1))) (= (select buf ?V_15) e))) (and (forall ((?V_14 Int)) (=> (and (<= 0 ?V_14) (<= ?V_14 (- 0 1))) (not (= (select a1 ?V_14) e)))) (forall ((?V_13 Int)) (=> (and (<= 0 ?V_13) (<= ?V_13 (- 0 1))) (not (= (select a2 ?V_13) e)))))))))))))))))))))))))
(check-sat)
(exit)
