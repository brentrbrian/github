// DESCRIPTION: changing types, convert number to string

fn main()
{
  let number = 2020;
  let number_as_string= number.to_string();
  
  println!("{}",number);
  println!("{}",number_as_string);
  println!("{}",number_as_string=="2020");
}
