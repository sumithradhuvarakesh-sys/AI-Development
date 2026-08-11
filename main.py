from planner import create_plan
from tools import search_web, fetch_page
from logger import log_step
MAX_ITERATIONS = 5
def run_agent(user_input):

    print("User:", user_input)

    query = user_input

    for iteration in range(1, MAX_ITERATIONS + 1):

        print("\n==============================")
        print("Iteration:", iteration)
        print("==============================")

        # PERCEIVE
        print("\nPerceive:")
        print("Understanding research question...")

        log_step(
            iteration,
            "Perceive",
            query
        )

        # PLAN
        plan = create_plan(query)

        print("\nPlan:")
        print(plan)

        log_step(
            iteration,
            "Plan",
            plan
        )

        # ACT
        print("\nAct:")

        if plan.startswith("SEARCH:"):

            search_query = plan.replace("SEARCH:", "").strip()

            result = search_web(search_query)

            print("Search result:", result)

            log_step(
                iteration,
                "Act",
                str(result)
            )

            # TOOL FAILURE RECOVERY
            if not result["success"]:

                print("Search failed. Retrying with original question.")

                log_step(
                    iteration,
                    "Recovery",
                    "Search failed"
                )

                query = user_input
                continue

            # Fetch top result
            top_result = result["results"][0]

            url = top_result["url"]

            page = fetch_page(url)

            print("\nFetch result:", page)

            log_step(
                iteration,
                "Act",
                str(page)
            )

            if not page["success"]:

                print("Page fetch failed. Refining search.")

                log_step(
                    iteration,
                    "Recovery",
                    "Page fetch failed"
                )

                query = search_query + " reliable source"
                continue

            # OBSERVE
            print("\nObserve:")
            print("Page successfully fetched.")

            log_step(
                iteration,
                "Observe",
                str(page)
            )

            print("\nResearch completed successfully.")

            log_step(
                iteration,
                "Success",
                "Valid search result and page received"
            )

            return
        else:

            print("\nObserve:")
            print("Planner did not return a valid SEARCH action.")

            log_step(
                iteration,
                "Observe",
                "Invalid planner action"
            )
            query = user_input + " reliable information"

    print("\nMaximum iterations reached.")
    log_step(
        MAX_ITERATIONS,
        "Stop",
        "Maximum iteration limit reached"
    )
user_input = input("Enter your research question: ")

run_agent(user_input)