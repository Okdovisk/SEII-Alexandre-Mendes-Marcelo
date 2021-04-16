var valor;

function botao(num){
    valor = document.Calc.visor.value += num; 
}

function reset(){
    document.Calc.visor.value = '';
}

function calculate(){
    result = eval(valor);
    document.Calc.visor.value = result.toLocaleString('pt-br');
}