import java.io.File
import java.util.*


fun getClosingBracketPositionReversed(expr: String): Int {
    var level = 0
    for (i in expr.indices.reversed()) {
        if (expr[i] == ')')
            level++
        else if (expr[i] == '(')
            level--
        if (level == 0)
            return i
    }
    return 0
}

fun evaluate(expr: String, multiplyStack: Stack<Long>): Long {
    val exprTrim = expr.replace(" ", "")
    var num1: Long
    var pos = exprTrim.length - 1
    if (exprTrim[pos] == ')') {
        val endBracketPos = getClosingBracketPositionReversed(exprTrim.slice(0..pos))
        num1 = evaluate(exprTrim.slice((endBracketPos + 1) until pos), multiplyStack)

        // write last result to multiply stack und multiply all values in the stack
        multiplyStack.add(num1)
        num1 = multiplyStack.reduce { acc, i -> acc * i }
        multiplyStack.clear()

        pos = endBracketPos
    } else {
        num1 = exprTrim[pos].toString().toLong()
    }
    if (pos == 0) {
        return num1
    }

    val operator = exprTrim[--pos]
    val num2 = evaluate(exprTrim.slice(0 until pos), multiplyStack)

    if (operator == '+') {
        return num1 + num2
    } else if (operator == '*') {
        multiplyStack.add(num2)
        return num1
    }
    return 0L
}

fun main() {
    var sum = 0L
    for (line in File("input.txt").readLines()) {
        val multiplyStack: Stack<Long> = Stack()
        var result = evaluate(line, multiplyStack)
        multiplyStack.add(result)
        result = multiplyStack.reduce { acc, i -> acc * i }
        println("%s = %d".format(line, result))
        sum += result
    }
    println("sum = %d".format(sum))
}
