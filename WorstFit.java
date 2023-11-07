import java.util.Scanner;

public class WorstFitPartition {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the total size of main memory: ");
        int memorySize = scanner.nextInt();

        System.out.print("Enter the number of partitions: ");
        int numPartitions = scanner.nextInt();

        int[] partitionSizes = new int[numPartitions];
        boolean[] allocated = new boolean[numPartitions];

        for (int i = 0; i < numPartitions; i++) {
            System.out.print("Enter the size of partition " + (i + 1) + ": ");
            partitionSizes[i] = scanner.nextInt();
        }

        System.out.print("Enter the number of processes: ");
        int numProcesses = scanner.nextInt();

        int[] processSizes = new int[numProcesses];

        for (int i = 0; i < numProcesses; i++) {
            System.out.print("Enter the size of process " + (i + 1) + ": ");
            processSizes[i] = scanner.nextInt();
        }

        for (int i = 0; i < numProcesses; i++) {
            int processSize = processSizes[i];
            boolean allocatedFlag = false;
            int worstFitPartition = -1;
            int worstFitSize = 0;

            for (int j = 0; j < numPartitions; j++) {
                if (!allocated[j] && partitionSizes[j] >= processSize) {
                    if (worstFitPartition == -1 || partitionSizes[j] > worstFitSize) {
                        worstFitPartition = j;
                        worstFitSize = partitionSizes[j];
                    }
                }
            }

            if (worstFitPartition != -1) {
                allocated[worstFitPartition] = true;
                System.out.println("Process " + (i + 1) + " of size " + processSize + "KB is allocated to Partition " + (worstFitPartition + 1));
                int fragmentSize = partitionSizes[worstFitPartition] - processSize;
                System.out.println("Fragment size in Partition " + (worstFitPartition + 1) + ": " + fragmentSize + "KB");
            } else {
                System.out.println("Process " + (i + 1) + " of size " + processSize + "KB cannot be allocated.");
            }
        }

        // Display unused locations
        for (int k = 0; k < numPartitions; k++) {
            if (!allocated[k]) {
                System.out.println("Partition " + (k + 1) + " is unused with size " + partitionSizes[k] + "KB");
            }
        }
    }
}
