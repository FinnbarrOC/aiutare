(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_9 () Int)
(declare-fun a () (Array Int Int))
(assert (let ((?v_0 (and true (>= V_9 0)))) (and (and ?v_0 ?v_0) (and (forall ((?V_7 Int)) (=> (and (<= 0 ?V_7) (<= ?V_7 5)) (forall ((?V_8 Int)) (let ((?v_1 (store (store a 0 5) 5 7))) (=> (and (<= 0 ?V_8) (<= ?V_8 ?V_7)) (<= (select ?v_1 ?V_8) (select ?v_1 ?V_7))))))) (forall ((?V_5 Int)) (=> (and (<= 0 ?V_5) (<= ?V_5 5)) (forall ((?V_6 Int)) (let ((?v_2 (store (store a 0 1) 5 3))) (=> (and (<= 0 ?V_6) (<= ?V_6 ?V_5)) (<= (select ?v_2 ?V_6) (select ?v_2 ?V_5)))))))))))
(check-sat)
(exit)
