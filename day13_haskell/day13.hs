import qualified Data.Text as T

parseIDs :: String -> [Int]
parseIDs s = map (read . T.unpack) (filter (/= T.pack "x") (T.splitOn (T.pack ",") (T.pack s)))

isBus :: Int -> Int -> Bool
isBus time bus = mod time bus == 0

earliestBus :: Int -> Int -> Int -> (Int, Int)
earliestBus time count bus = if isBus ntime bus then (bus, count) else earliestBus time (count+1) bus where
    ntime = time+count

ealierBus :: (Int, Int) -> (Int, Int) -> (Int, Int)
ealierBus b1 b2 = if snd b1 < snd b2 then b1 else b2

main :: IO ()
main = do
    raw <- readFile "./input.txt"
    let input = lines raw
    let start = read (head input) :: Int
    let ids = parseIDs (input !! 1)

    let b = foldr1 ealierBus (map (earliestBus start 0) ids)
    print (fst b * snd b)