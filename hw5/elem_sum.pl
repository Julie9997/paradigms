% Базовый случай: сумма элементов пустого списка равна нулю
sum_list([], 0).

% Рекурсивный случай: сумма элементов списка равна сумме головы списка и сумме остатка списка
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum), 
    Sum is Head + TailSum.   

% Использования:
?- sum_list([1, 2, 3, 4, 5], Sum).
Sum = 15.