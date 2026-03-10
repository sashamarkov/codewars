module Ch02.EffectivePlus where
​
import Ch02.Nat (Nat(Zero, Succ))
​
-- Refactor me
plusNat :: Nat -> Nat -> Nat
plusNat x Zero = x
plusNat Zero y = y
plusNat (Succ x) (Succ y) = Succ (Succ (plusNat x y))