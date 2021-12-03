// DESCRIPTION: str, static str

fn main() 
{
  let a:&str = "string a";
  let b:&str = "string b";

  println!("{} {}",a,b);

  let c:&'static str = "string c";
  let d:&'static str = "string d";

  println!("{} {}",c,d);
}
