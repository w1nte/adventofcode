import java.io.File
import java.lang.Error
import java.util.*

abstract class Token() {
    abstract fun getParsed(parser: Parser) : Token
}

abstract class TokenOperator() : Token() {
    abstract fun operate(num1: TokenNumber, num2: TokenNumber) : TokenNumber
}

class TokenNumber(val number: Long) : Token() {
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class TokenAddition() : TokenOperator() {
    override fun operate(num1: TokenNumber, num2: TokenNumber) : TokenNumber { /*println("%d + %d".format(num1.number, num2.number));*/ return TokenNumber(num1.number + num2.number) }
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class TokenMultiplication() : TokenOperator() {
    override fun operate(num1: TokenNumber, num2: TokenNumber) : TokenNumber { /*println("%d * %d".format(num1.number, num2.number));*/ return TokenNumber(num1.number * num2.number) }
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class TokenParenthesesOpen() : Token() {
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class TokenParenthesesClose() : Token() {
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class TokenEnd() : Token() {
    override fun getParsed(parser: Parser): Token { return parser.parse(this) }
}

class Reader(val expr: String) {
    private var pos = 0

    fun peek(k: Int) : Char {
        return if (!isEOF(k)) expr[pos+k] else 0.toChar()
    }

    fun consume() : Char {
        return if (!isEOF()) expr[pos++] else 0.toChar()
    }

    fun isEOF() : Boolean {
        return isEOF(0)
    }

    private fun isEOF(k: Int) : Boolean {
        return (pos+k) >= expr.length
    }
}

class Lexer(val reader: Reader) {
    fun consume() : Token {
        while (true) {
            when (val consumedChar = reader.consume()) {
                in '1'..'9' -> { return readNumber(consumedChar) }
                '+' -> { return TokenAddition() }
                '*' -> { return TokenMultiplication() }
                '(' -> { return TokenParenthesesOpen() }
                ')' -> { return TokenParenthesesClose() }
                0.toChar() -> { return TokenEnd() }
            }
        }
    }

    private fun readNumber(firstChar: Char) : TokenNumber {
        var numberString = firstChar.toString()
        while (reader.peek(0) in '1'..'8') {
            numberString += reader.consume()
        }
        return TokenNumber(numberString.toLong())
    }
}

class Parser(val lexer: Lexer) {

    val numstack = Stack<TokenNumber>()

    fun parse() : Long {
        val firstToken = lexer.consume()
        return (firstToken.getParsed(this) as TokenNumber).number
    }

    fun parse(token: TokenNumber) : Token {
        val token2 = lexer.consume()

        if (token2 is TokenEnd) {
            return token
        } else if (token2 is TokenParenthesesClose) {
            if (numstack.isEmpty()) {
                numstack.add(token)
                return lexer.consume().getParsed(this)
            } else {
                return token
            }
        } else if (token2 is TokenOperator) {
            val token3 = lexer.consume()
            return if (token3 is TokenNumber) {
                token2.operate(token, token3).getParsed(this)
            } else {
                token2.operate(token, token3.getParsed(this) as TokenNumber).getParsed(this)
            }
        }
        return TokenEnd()
    }

    fun parse(token: TokenParenthesesOpen) : Token {
        return lexer.consume().getParsed(this)
    }

    fun parse(token: TokenOperator) : Token {
        var next = lexer.consume()
        if (next is TokenParenthesesOpen) {
            next = next.getParsed(this)
        }

        if (next !is TokenNumber) {
            throw Error("after an operator must be something!")
        }
        return token.operate(numstack.pop(), next).getParsed(this)
    }

    fun parse(token: TokenEnd) : Token {
        return numstack.pop()
    }

    fun parse(token: TokenParenthesesClose) : Token {
        return numstack.pop()
    }
}

fun main() {
    var sum = 0.toBigInteger()
    for (line in File("input.txt").readLines()) {
        val reader = Reader(line)
        val lexer = Lexer(reader)
        val parser = Parser(lexer)

        val result = parser.parse()
        println("%s = %d".format(line, result))
        sum += result.toBigInteger()
    }
    println("sum = %d".format(sum))
}

// 59306292