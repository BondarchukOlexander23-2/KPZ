from Creator.ManagerCall import ManagerCall
from Creator.MobileApp import MobileApp
from Creator.WebSite import WebSite


def main():
    website = WebSite()
    mobile_app = MobileApp()
    manager_call = ManagerCall()

    # Створимо різні підписки
    sub1 = website.create_subscription("domestic")
    sub2 = mobile_app.create_subscription("educational")
    sub3 = manager_call.create_subscription("premium")

    # Виведемо інформацію
    for idx, sub in enumerate([sub1, sub2, sub3], 1):
        print(f"\nSubscription {idx}:")
        print(f"Monthly fee: ${sub.get_monthly_fee()}")
        print(f"Minimum subscription period: {sub.get_min_period()} months")
        print(f"Channels: {', '.join(sub.get_channels())}")
        print(f"Features: {sub.get_features()}")

if __name__ == "__main__":
    main()