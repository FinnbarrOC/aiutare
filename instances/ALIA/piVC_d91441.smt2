(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_6 () Int)
(declare-fun V_5 () Int)
(declare-fun a_0 () (Array Int Int))
(declare-fun t () Int)
(declare-fun ix () Int)
(declare-fun j () Int)
(declare-fun a () (Array Int Int))
(declare-fun i () Int)
(assert (let ((?v_2 (and true (>= V_5 0))) (?v_4 (select a j)) (?v_0 (- i 1))) (let ((?v_1 (= j ?v_0)) (?v_7 (= V_6 V_5)) (?v_3 (- j 1)) (?v_5 (store a (+ j 1) ?v_4))) (let ((?v_6 (not (= ?v_3 ?v_0)))) (and (and ?v_2 (and (> ?v_4 t) (and (>= j 0) (and (and (<= 1 i) (and (< i V_6) (and (<= (- 1) j) (and (<= j ?v_0) (and (forall ((?V_11 Int)) (=> (and (<= 0 ?V_11) (<= ?V_11 ?v_0)) (forall ((?V_12 Int)) (=> (and (<= 0 ?V_12) (<= ?V_12 ?V_11)) (<= (select a ?V_12) (select a ?V_11)))))) (and (or ?v_1 (<= (select a ?v_0) (select a i))) (and (or ?v_1 (forall ((?V_10 Int)) (=> (and (<= (+ j 1) ?V_10) (<= ?V_10 i)) (> (select a ?V_10) t)))) ?v_7))))))) ?v_2)))) (or (> 1 i) (or (>= i V_6) (or (> (- 1) ?v_3) (or (> ?v_3 ?v_0) (or (exists ((?V_8 Int)) (and (and (<= 0 ?V_8) (<= ?V_8 ?v_0)) (exists ((?V_9 Int)) (and (and (<= 0 ?V_9) (<= ?V_9 ?V_8)) (> (select ?v_5 ?V_9) (select ?v_5 ?V_8)))))) (or (and ?v_6 (> (select ?v_5 ?v_0) (select ?v_5 i))) (or (and ?v_6 (exists ((?V_7 Int)) (and (and (<= (+ ?v_3 1) ?V_7) (<= ?V_7 i)) (<= (select ?v_5 ?V_7) t)))) (not ?v_7)))))))))))))
(check-sat)
(exit)
