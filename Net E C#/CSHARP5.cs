using System;

public class Juros
{
    public decimal ObtenhaMontante(decimal capitalInicial, decimal taxaJuro, decimal prazo)
    {
        return (decimal) ((double) capitalInicial * (Math.Pow((1 + (double) taxaJuro / 100.0), (double) prazo)));
    }
    
    public decimal ObtenhaJuroTotal(decimal montante, decimal capitalInicial)
    {
        return montante - capitalInicial;
    }
    
    public static void Main(string[] args)
    {
        Juros EX = new Juros();
        decimal CapitalInicial = 10000;
        decimal TaxaJuros = 3;
        decimal Prazo = 3;
        decimal Montante = EX.ObtenhaMontante(CapitalInicial, TaxaJuros, Prazo);
        decimal JurosTotal = EX.ObtenhaJuroTotal(Montante, CapitalInicial);
        
        Console.WriteLine("O resultado do montante é: {0}", Montante);
        Console.WriteLine("O valor do juros é: {0}",JurosTotal);
    }
}
