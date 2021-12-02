import qualified Data.Text as T

parseIDs :: String -> [Int]
parseIDs s = map (read . T.unpack . (\x -> if x == T.pack "x" then T.pack "1" else x)) (T.splitOn (T.pack ",") (T.pack s))

gcdext :: Int -> Int -> (Int, Int)
gcdext a 0 = (1, 0)
gcdext a b = (t, s - q * t) where
    (q, r) = quotRem a b
    (s, t) = gcdext b r

solve :: [Int] -> Int -> Int -> Int
solve [] _ _ = 0
solve (b:bs) i m = e * (b-i) + solve bs (i+1) m where
    (r, s) = gcdext b mb
    e = mb * s
    mb = m `div` b

main :: IO ()
main = do  
    raw <- readFile "./input.txt"
    let input = lines raw
    let ids = parseIDs (input !! 1)

    let m = foldr1 lcm ids
    let s = solve ids 0 m
    print (s - m * (s `div` m))