module HowMany where

howMany :: Int -> IO() -- ask how many left, and print it out neatly.
howMany left = putStr ((strMany left) ++ "\n")

strMany :: Int -> String -- ask how many left, and return a string.
strMany left = case left of
    0 -> "We're done!"
    1 -> "Just one more..."
    x -> howMany (x-1) ++ "\n And then one more after that..."