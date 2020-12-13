import qualified Data.Text as T

type Bus = Int
type Time = Int

parseIDs :: String -> [Int]
parseIDs s = map (read . T.unpack . (\x -> if x == T.pack "x" then T.pack "1" else x)) (T.splitOn (T.pack ",") (T.pack s))

isBus :: Bus -> Time -> Bool
isBus bus time = mod time bus == 0

findFirst :: Bus -> Bus -> Time -> Int -> Int -> Int -> Int
findFirst b1 b2 time step r1 r2 = if isBus b1 (time + r1) && isBus b2 (time + r2) then time else findFirst b1 b2 (time + step) step r1 r2

stepSize :: Bus -> Bus -> Int
stepSize = lcm

findSolution :: [Bus] -> Time -> Int -> Int -> Int
findSolution [_] time _ _ = time
findSolution (b1:bs) time step r = findSolution bs nextTime nextStep (r+1) where
    b2 = head bs
    nextStep = stepSize step b2
    nextTime = findFirst b1 b2 time step r (r+1)

main :: IO ()
main = do  
    raw <- readFile "./input.txt"
    let input = lines raw
    let ids = parseIDs (input !! 1)

    print ids
    print (findSolution ids 0 (head ids) 0)