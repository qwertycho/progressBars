using progressBar;

progressBar.ProgressBar bar = new(100);
bar.SetProgressChars('#', '_');
bar.SetBrackets('[', ']');

for(int i = 0; i < 100; i++){
  Task.Delay(100).Wait();
  bar.Tick(1);
}
