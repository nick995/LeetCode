public class TwoSum
{
    public static void Main(string[] args)
    {
        int[] case1 = new int[4];
        case1[0] = 2;
        case1[1] = 7;
        case1[2] = 11;
        case1[3] = 15;

        //case1[0] = 3;
        //case1[1] = 2;
        //case1[2] = 3;

        int[] ans = Test(case1, 9);

        Console.WriteLine(ans);

    }

    public static int[] Test(int[] nums, int target)
    {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        for(int i=0; i<nums.Length; i++)
        {
            if (dic.ContainsKey(target-nums[i]))
            {
                return new int[] { dic[target-nums[i]], i };
            }
            else
            {
                //dic.Add(nums[i], i);
                dic[nums[i]] = i;
            }
        }
        return null;
    }
}