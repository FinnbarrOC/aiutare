(set-info :smt-lib-version 2.6)
(set-logic ALIA)
(set-info :source |piVC|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-fun V_3 () Int)
(declare-fun a () (Array Int Int))
(assert (let ((?v_0 (and true (>= V_3 0)))) (and (and ?v_0 ?v_0) (or (> 1 1) (or (exists ((?V_4 Int)) (and (and (<= 0 ?V_4) (<= ?V_4 (- 1 1))) (exists ((?V_5 Int)) (and (and (<= 0 ?V_5) (<= ?V_5 ?V_4)) (> (select a ?V_5) (select a ?V_4)))))) (not (= V_3 V_3)))))))
(check-sat)
(exit)
