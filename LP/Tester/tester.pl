:- begin_tests(lists).
:- use_module(library(lists)).
:- set_prolog_flag(answer_write_options,[max_depth(0)]).
:- ["dados.pl"], ["keywords.pl"], ["projeto.pl"].

/****************************************************************************************
 *                                                                                      *
 *  Testes para os predicados do projeto que são publicos                               *
 *                                                                                      *
 ****************************************************************************************/
test(eventosSemSalas) :-
    eventosSemSalas([14,88,191,311,312,342,343]).

test(eventosSemSalasDiaSemana) :-
    eventosSemSalasDiaSemana(segunda-feira,  [191]).

test(eventosSemSalasPeriodo) :-
    eventosSemSalasPeriodo([p1], [88,191,311,312,342,343]).

test(eventosSemSalasPeriodo) :-
    eventosSemSalasPeriodo([], []).
    
test(organizaEventos) :-
    organizaEventos([23, 67, 89, 99, 6], p3, []).

test(organizaEventos) :-
    organizaEventos([23, 67, 89, 99, 6], p2, [6,99]).

test(organizaEventos) :-
    organizaEventos([23, 67, 89, 99, 6], p1, [23,67,89,99]).

test(eventosMenoresQue) :-
    eventosMenoresQue(0.5, [4,7]).

test(eventosMenoresQueBool) :-
    not(eventosMenoresQueBool(45, 0.5)).

test(eventosMenoresQueBool) :-
    eventosMenoresQueBool(4, 0.5).

/*test(procuraDisciplinas) :- 
    procuraDisciplinas(leti,['algebra linear','analise de dados e modelacao estatistica', 'arquitecturas de redes','calculo diferencial e integral i',' calculo diferencial e integral iii','eletromagnetismo e optica', 'engenharia de software','fundamentos da programacao', 'gestao','introducao a economia','introducao a engenharia de telecomunicacoes e informatica','introducao aos circuitos e sistemas electronicos','mecanica e ondas', 'programacao com objectos','propagacao e antenas', 'sistemas de comunicacoes','sistemas digitais', 'sistemas operativos']).*/

test(organizaDisciplinas) :- 
    organizaDisciplinas(['algebra linear','compiladores'], 'leic-t', [['algebra linear'],['compiladores']]).

test(organizaDisciplinas) :- 
    organizaDisciplinas(['algebra linear','analitica empresarial','avaliacao de projetos', 'ciencia de materiais'], legi, [['algebra linear','analitica empresarial','avaliacao de projetos'],['ciencia de materiais']]).

test(organizaDisciplinas) :- 
    not(organizaDisciplinas(['algebra linear','analitica empresarial','avaliacao de projetos', 'ciencia de materiais'], 'leic-t', _)).

test(horasCurso) :-
    horasCurso(p1, 'leic-t', 1, 50.0).

test(evolucaoHorasCurso) :-
    evolucaoHorasCurso('leic-t', [(1,p1,50.0),(1,p2,59.0),(1,p3,0),(1,p4,0),(2,p1,47.0),(2,p2,77.0),(2,p3,0),(2,p4,20.0),(3,p1,32.0),(3,p2,32.0),(3,p3,39.0),(3,p4,19.0)]).

test(ocupaSlot) :-
    ocupaSlot(8.5, 11, 9, 10.5, 1.5).

test(ocupaSlot) :-
    ocupaSlot(9.5, 10, 9, 10.5, 0.5).
    
test(ocupaSlot) :-
    ocupaSlot(8.5, 9.5, 9, 10.5, 0.5).

test(ocupaSlot) :-
    ocupaSlot(10, 11, 9, 10.5, 0.5).

test(ocupaSlot) :-
    not(ocupaSlot(10, 11, 8, 9, _)).

test(numHorasOcupadas) :-
    numHorasOcupadas(p1, grandesAnfiteatros, quarta-feira, 8.0, 12.0, 6.0).

test(numHorasOcupadas) :-
    numHorasOcupadas(p1, grandesAnfiteatros, quarta-feira, 8.0, 10.0, 2.5).

test(ocupacaoMax) :-
    ocupacaoMax(grandesAnfiteatros, 8, 12.5, 9.0).

test(percentagem) :-
    percentagem(5, 9, 55.55555555555556).

test(ocupacaoCritica) :-
    ocupacaoCritica(8, 12.5, 85,  [casosCriticos(segunda-feira,grandesAnfiteatros,89),casosCriticos(segunda-feira,grandesAnfiteatros,94),casosCriticos(segunda-feira,pequenosAnfiteatros,93),casosCriticos(sexta-feira,labsQuimica,89)]).

test(ocupacaoMesa) :-
    ocupacaoMesa([maria, joao, pedrito, jorge, ana, manelito, miguel, guga],[cab1(maria), cab2(joao), honra(joao, guga), lado(ana, manelito),lado(miguel, pedrito), frente(miguel, jorge),naoFrente(pedrito, manelito)],[[miguel,pedrito,guga],[maria,joao],[jorge,ana,manelito]]).

test(ocupacaoMesa) :-
    ocupacaoMesa([a, b, c, d, e, f, g, h], [cab1(e), honra(e, b), naoFrente(a, b),lado(f, g), lado(a, c), naoLado(f, c), naoFrente(f, c), frente(g, d)], [[c,a,d],[e,h],[b,f,g]]).

test(ocupacaoMesa) :-
    ocupacaoMesa([a, b, c, d, e, f, g, h], [cab1(e), honra(e, b), cab2(c),honra(c, a), naoFrente(a, b), naoLado(b, f), lado(f, g), frente(b, h)], [[h,d,a],[e,c],[b,g,f]]).

:- end_tests(lists).