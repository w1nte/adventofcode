-- it's so slow, use ghc to compile and then execute it. it still takes a few minutes oof.

type Point = (Int, Int)
data CellState = Floor | Occupied | Empty deriving Eq
type Cell = (Point, CellState)
type Grid = [Cell]

adjacents = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]

charToCell :: Char -> Int -> Int -> Cell
charToCell char x y
    | char == 'L' = ((x, y), Empty)
    | char == '#' = ((x, y), Occupied)
    | otherwise = ((x, y), Floor)

prepareInputLine :: String -> Int -> [Cell]
prepareInputLine line y =
    [charToCell (line !! x) x y | x <- [0..length line - 1]]

prepareInput :: [String] -> Grid
prepareInput lines = concat [prepareInputLine (lines !! y) y | y <- [0..length lines - 1]]

countOccupied :: Grid -> Int
countOccupied [] = 0
countOccupied (c:cn)
    | snd c == Occupied = 1 + c2
    | otherwise = c2 where  
        c2 = countOccupied cn

nextGrid :: Grid -> Grid -> Grid
nextGrid _ [] = []
nextGrid g (c:cn) = nextCellState g c : nextGrid g cn

compareGrids :: Grid -> Grid -> Bool
compareGrids [] [] = True
compareGrids (c1:cn1) (c2:cn2) = snd c1 == snd c2 && compareGrids cn1 cn2

nextGridUntilSame :: Grid -> Grid
nextGridUntilSame g1 = if compareGrids g1 g2 then g2 else nextGridUntilSame g2 where
    g2 = nextGrid g1 g1

nextCellState :: Grid -> Cell -> Cell
nextCellState g ((x, y), s)
    | s == Empty && o == 0 = ((x, y), Occupied)
    | s == Occupied && o >= 4 = ((x, y), Empty)
    | otherwise = ((x, y), s) where
        o = getOccupiedNeighboursNumber g (x, y)

getCell :: Grid -> Point -> Maybe Cell
getCell [] _ = Nothing
getCell (c:cn) p
    | fst c == p = Just c
    | otherwise = getCell cn p

isCellOccupied :: Maybe Cell -> Bool
isCellOccupied c = case c of
    Nothing -> False
    Just x -> snd x == Occupied

getOccupiedNeighboursNumber :: Grid -> Point -> Int
getOccupiedNeighboursNumber g p = length (filter (\i -> i) (map (\a -> isCellOccupied (getCell g (fst a + fst p, snd a + snd p))) adjacents))

main :: IO ()
main = do
    raw <- readFile "./input.txt"
    let grid = nextGridUntilSame (prepareInput $ lines raw)
    print (countOccupied grid)