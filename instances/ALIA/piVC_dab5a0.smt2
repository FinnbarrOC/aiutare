(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_26 () Int)
(declare-fun V_24 () Int)
(declare-fun V_23 () Int)
(declare-fun u_0 () Int)
(declare-fun m_0 () Int)
(declare-fun l_0 () Int)
(declare-fun arr_0 () (Array Int Int))
(declare-fun buf () (Array Int Int))
(declare-fun arr () (Array Int Int))
(declare-fun k () Int)
(declare-fun u () Int)
(declare-fun j () Int)
(declare-fun m () Int)
(declare-fun i () Int)
(declare-fun l () Int)
(assert (let ((?v_4 (<= 0 l_0)) (?v_5 (<= l_0 m_0)) (?v_6 (< m_0 u_0)) (?v_7 (< u_0 V_23)) (?v_8 (>= V_23 0)) (?v_1 (> i m)) (?v_0 (+ m 1)) (?v_10 (+ u 1)) (?v_11 (- i l)) (?v_13 (<= i m)) (?v_2 (= k 0)) (?v_15 (select arr i)) (?v_3 (select buf (- k 1))) (?v_14 (select arr j)) (?v_18 (= V_26 (+ (- u l) 1))) (?v_19 (= V_24 V_23)) (?v_20 (= l l_0)) (?v_21 (= m m_0)) (?v_22 (= u u_0)) (?v_9 (+ j 1)) (?v_12 (+ k 1))) (let ((?v_16 (not (= ?v_12 0))) (?v_17 (select (store buf k ?v_14) (- ?v_12 1)))) (and (and (and (and ?v_4 (and ?v_5 (and ?v_6 (and ?v_7 (and (forall ((?V_46 Int)) (=> (and (<= l_0 ?V_46) (<= ?V_46 m_0)) (forall ((?V_47 Int)) (=> (and (<= l_0 ?V_47) (<= ?V_47 ?V_46)) (<= (select arr_0 ?V_47) (select arr_0 ?V_46)))))) (forall ((?V_44 Int)) (=> (and (<= (+ m_0 1) ?V_44) (<= ?V_44 u_0)) (forall ((?V_45 Int)) (=> (and (<= (+ m_0 1) ?V_45) (<= ?V_45 ?V_44)) (<= (select arr_0 ?V_45) (select arr_0 ?V_44))))))))))) ?v_8) (and ?v_1 (and (< k V_26) (and (and (<= l i) (and (<= i ?v_0) (and (<= ?v_0 j) (and (<= j ?v_10) (and (= k (+ ?v_11 (- j ?v_0))) (and (forall ((?V_42 Int)) (=> (and (<= l ?V_42) (<= ?V_42 m)) (forall ((?V_43 Int)) (=> (and (<= l ?V_43) (<= ?V_43 ?V_42)) (<= (select arr ?V_43) (select arr ?V_42)))))) (and (forall ((?V_40 Int)) (=> (and (<= ?v_0 ?V_40) (<= ?V_40 u)) (forall ((?V_41 Int)) (=> (and (<= ?v_0 ?V_41) (<= ?V_41 ?V_40)) (<= (select arr ?V_41) (select arr ?V_40)))))) (and (or (= k V_26) (or ?v_13 (<= j u))) (and (or ?v_2 (or ?v_1 (<= ?v_3 ?v_15))) (and (or ?v_2 (or (> j u) (<= ?v_3 ?v_14))) (and (forall ((?V_38 Int)) (=> (and (<= 0 ?V_38) (<= ?V_38 (- k 1))) (forall ((?V_39 Int)) (=> (and (<= 0 ?V_39) (<= ?V_39 ?V_38)) (<= (select buf ?V_39) (select buf ?V_38)))))) (and ?v_18 (and (forall ((?V_37 Int)) (=> (and (<= 0 ?V_37) (<= ?V_37 (- V_24 1))) (= (select arr ?V_37) (select arr_0 ?V_37)))) (and ?v_19 (and ?v_20 (and ?v_21 ?v_22)))))))))))))))) (and (and ?v_4 (and ?v_5 (and ?v_6 (and ?v_7 (and (forall ((?V_35 Int)) (=> (and (<= l_0 ?V_35) (<= ?V_35 m_0)) (forall ((?V_36 Int)) (=> (and (<= l_0 ?V_36) (<= ?V_36 ?V_35)) (<= (select arr_0 ?V_36) (select arr_0 ?V_35)))))) (forall ((?V_33 Int)) (=> (and (<= (+ m_0 1) ?V_33) (<= ?V_33 u_0)) (forall ((?V_34 Int)) (=> (and (<= (+ m_0 1) ?V_34) (<= ?V_34 ?V_33)) (<= (select arr_0 ?V_34) (select arr_0 ?V_33))))))))))) ?v_8))))) (or (> l i) (or (> i ?v_0) (or (> ?v_0 ?v_9) (or (> ?v_9 ?v_10) (or (not (= ?v_12 (+ ?v_11 (- ?v_9 ?v_0)))) (or (exists ((?V_31 Int)) (and (and (<= l ?V_31) (<= ?V_31 m)) (exists ((?V_32 Int)) (and (and (<= l ?V_32) (<= ?V_32 ?V_31)) (> (select arr ?V_32) (select arr ?V_31)))))) (or (exists ((?V_29 Int)) (and (and (<= ?v_0 ?V_29) (<= ?V_29 u)) (exists ((?V_30 Int)) (and (and (<= ?v_0 ?V_30) (<= ?V_30 ?V_29)) (> (select arr ?V_30) (select arr ?V_29)))))) (or (and (not (= ?v_12 V_26)) (and ?v_1 (> ?v_9 u))) (or (and ?v_16 (and ?v_13 (> ?v_17 ?v_15))) (or (and ?v_16 (and (<= ?v_9 u) (> ?v_17 (select arr ?v_9)))) (or (exists ((?V_27 Int)) (and (and (<= 0 ?V_27) (<= ?V_27 (- ?v_12 1))) (exists ((?V_28 Int)) (let ((?v_23 (store buf k ?v_14))) (and (and (<= 0 ?V_28) (<= ?V_28 ?V_27)) (> (select ?v_23 ?V_28) (select ?v_23 ?V_27))))))) (or (not ?v_18) (or (exists ((?V_25 Int)) (and (and (<= 0 ?V_25) (<= ?V_25 (- V_24 1))) (not (= (select arr ?V_25) (select arr_0 ?V_25))))) (or (not ?v_19) (or (not ?v_20) (or (not ?v_21) (not ?v_22)))))))))))))))))))))
(check-sat)
(exit)
