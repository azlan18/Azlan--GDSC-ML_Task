import java.util.*;

class Process {
    int arrivalTime;
    int burstTime;
    int completionTime;
    int waitingTime;
    int turnaroundTime;

    public Process(int arrivalTime, int burstTime) {
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
    }
}

public class SJF {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        ArrayList<Process> processes = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter arrival time for process " + (i + 1) + ": ");
            int arrivalTime = sc.nextInt();
            System.out.print("Enter burst time for process " + (i + 1) + ": ");
            int burstTime = sc.nextInt();
            processes.add(new Process(arrivalTime, burstTime));
        }

        // Sort processes by burst time, and in case of a tie, use arrival time as tiebreaker
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (processes.get(j).burstTime > processes.get(j + 1).burstTime
                        || (processes.get(j).burstTime == processes.get(j + 1).burstTime
                                && processes.get(j).arrivalTime > processes.get(j + 1).arrivalTime)) {
                    // Swap the processes
                    Process temp = processes.get(j);
                    processes.set(j, processes.get(j + 1));
                    processes.set(j + 1, temp);
                }
            }
        }

        int currentTime = 0;
        double totalWaitingTime = 0;
        double totalTurnaroundTime = 0;

        System.out.println("Order of execution: ");

        for (Process p : processes) {
            // Calculate waiting time for the current process
            p.waitingTime = currentTime - p.arrivalTime;

            if (p.waitingTime < 0) {
                p.waitingTime = 0;
            }

            // Update current time and completion time
            currentTime += p.burstTime;
            p.completionTime = currentTime;

            // Calculate turnaround time for the current process
            p.turnaroundTime = p.completionTime - p.arrivalTime;

            totalWaitingTime += p.waitingTime;
            totalTurnaroundTime += p.turnaroundTime;

            System.out.println("P" + (processes.indexOf(p) + 1));
        }

        double averageWaitingTime = totalWaitingTime / n;
        double averageTurnaroundTime = totalTurnaroundTime / n;

        System.out.println("AWT = " + averageWaitingTime);
        System.out.println("ATAT = " + averageTurnaroundTime);
    }
}
