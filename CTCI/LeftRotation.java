/**
 * Created by Gautam on 10/2/16.
 */
public class LeftRotation
{
    public static int[] rotate(int a[], int elements, int rotationParameter)
    {
        int temp[] = new int[elements];

        for(int i=0; i<elements; i++)
        {
            temp[i] = a[(i+rotationParameter)%elements];
        }
        return temp;
    }

    public static void main(String args[])
    {
        int a[] = {1,2,3,4,5};
        a = rotate(a,5,4);
        for(int i=0; i<a.length; i++)
        {
            System.out.print(a[i] + " ");
        }
    }
}
