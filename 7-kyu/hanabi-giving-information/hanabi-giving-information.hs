module Hanabi (ways) where
import Preloaded (Suit(..))
import Data.List (nub)
​
ways :: [(Int, Suit)] -> Int
ways hand = length (nub numbers) + length (nub suits)
  where
    numbers = map fst hand
    suits = map snd hand