def menu():
    """Основное меню приложения с обработкой ошибок."""
    global data, result
    data = ""
    result = {}

    while True:
        print("\n1) Ввод данных вручную")
        print("2) Генерация данных")
        print("3) Выполнение алгоритма")
        print("4) Вывод результата")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            input_data()
            result.clear()  # Сбрасываем результаты при вводе новых данных
        elif choice == '2':
            generate_data()
            result.clear()  # Сбрасываем результаты при генерации новых данных
        elif choice == '3':
            if not data:
                print("Ошибка: данные не введены. Пожалуйста, введите данные или сгенерируйте их.")
                continue
            result = analyze_data(data)
            print("Алгоритм выполнен.")
        elif choice == '4':
            output_result(result)
        elif choice == '0':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")