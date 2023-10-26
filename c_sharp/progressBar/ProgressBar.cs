namespace progressBar;
public class ProgressBar{
  
  private int totalAmount = 0;
  private int currentAmount = 0;
  private int barWidth ;

  private char progressChar = '#';
  private char emptyChar = ' ';
  private char startBracket = '[';
  private char endBracket = ']';

  public ProgressBar(int total, int width = 50){
    totalAmount = total;
    barWidth = width;
  }

  public void Tick(int amount = 1){
    currentAmount += amount;
    double perc = CalcPerc();
    if(perc < 1){
      Console.Write($"\r{startBracket}{GetProgressChars(perc)}{endBracket} {Math.Round(perc*100, 0)}%");
    }else{
      Console.Write($"\r{startBracket}{GetProgressChars(perc)}{endBracket} {Math.Round(perc*100, 0)}%\n");
    }
  }

  public void SetBrackets(char start, char end){
    startBracket = start;
    endBracket = end;
  }

  public void SetProgressChars(char full = '#', char empy = ' '){
    progressChar = full;
    emptyChar = empy;
  }

  private string GetProgressChars(double perc){
    int charAmount = (int)(perc * (barWidth-2));
    string chars;
    if(charAmount <= barWidth-2)
    {
      chars = new string(progressChar, charAmount);
    } else{
      chars = new string(progressChar, barWidth-2);
    }

    for(int i = charAmount; i < barWidth-2; i++){
      chars+= emptyChar;
    }

    return chars;
  }

  private double CalcPerc(){
    return ((double)(currentAmount) / (double)(totalAmount));
  }
}
