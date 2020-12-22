import java.io.File


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

fun evaluate(expr: String): Long {
    val exprTrim = expr.replace(" ", "")
    var num1: Long
    var pos = exprTrim.length - 1
    if (exprTrim[pos] == ')') {
        val endBracketPos = getClosingBracketPositionReversed(exprTrim.slice(0..pos))
        num1 = evaluate(exprTrim.slice((endBracketPos + 1) until pos))
        pos = endBracketPos
    } else {
        num1 = exprTrim[pos].toString().toLong()
    }
    if (pos == 0) {
        return num1
    }

    val operator = exprTrim[--pos]
    val num2 = evaluate(exprTrim.slice(0 until pos))

    if (operator == '+') {
        return num1 + num2
    } else if (operator == '*') {
        return num1 * num2
    }
    return 0L
}

fun main() {

    var sum = 0L
    for (line in File("input.txt").readLines()) {
        val result = evaluate(line)
        println("%s = %d".format(line, result))
        sum += result
    }
    println("sum = %d".format(sum))
}

// 59306292 6 * ((5 * 3 * 2 + 9 * 4) * (8 * 8 + 2 * 3) * 5 * 8) * 2 + (4 + 9 * 5 * 5 + 8) * 4
