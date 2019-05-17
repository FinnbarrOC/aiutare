(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_10 () Int)
(declare-fun V_9 () Int)
(declare-fun arr () (Array Int Int))
(declare-fun t_1 () (Array Int Int))
(assert (let ((?v_0 (and true (>= V_10 0)))) (and (and ?v_0 (and (and (forall ((?V_13 Int)) (=> (and (<= 0 ?V_13) (<= ?V_13 (- V_10 1))) (forall ((?V_14 Int)) (=> (and (<= 0 ?V_14) (<= ?V_14 ?V_13)) (<= (select t_1 ?V_14) (select t_1 ?V_13)))))) (and (= V_9 V_10) (and (forall ((?V_12 Int)) (=> (and (<= 0 ?V_12) (<= ?V_12 (- 0 1))) (= (select t_1 ?V_12) (select arr ?V_12)))) (forall ((?V_11 Int)) (let ((?v_1 (- V_10 1))) (=> (and (<= (+ ?v_1 1) ?V_11) (<= ?V_11 ?v_1)) (= (select t_1 ?V_11) (select arr ?V_11)))))))) ?v_0)) (exists ((?V_7 Int)) (and (and (<= 0 ?V_7) (<= ?V_7 (- V_9 1))) (exists ((?V_8 Int)) (and (and (<= 0 ?V_8) (<= ?V_8 ?V_7)) (> (select t_1 ?V_8) (select t_1 ?V_7)))))))))
(check-sat)
(exit)
