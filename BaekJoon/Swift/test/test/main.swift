//
//  test2.swift
//  test
//
//  Created by subinyoon on 2022/05/05.
//

import Foundation

// Optional Binding으로 입력값 받기
var input = readLine()

if let input = input {
    print(input)
}

// force unwrapping으로 받기
let input2 = readLine()!
print(input2)

// 정수 하나 입력 받기
var oneNumberInput = Int(readLine()!)!
print(oneNumberInput)
