object Kolmogorov {

  def main(args:Array[String]) {
    val r = new scala.util.Random(1433224064)
    val nums = Stream.continually(r.nextGaussian).take(32000).toList
    println(nums)
  }

}
