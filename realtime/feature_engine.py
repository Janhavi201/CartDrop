from collections import deque

class FeatureEngine:

    def __init__(self):

        self.events = deque(maxlen=100)

    def add_event(self, event):

        self.events.append(event)

    def extract_features(self):

        total_events = len(self.events)

        scroll_events = sum(
            1 for e in self.events
            if e["type"] == "scroll"
        )

        cart_events = sum(
            1 for e in self.events
            if e["type"] == "cart"
        )

        return {
            "session_duration": total_events,
            "cart_value": cart_events * 500,
            "product_views": total_events,
            "return_velocity": total_events / 10,
            "scroll_changes": scroll_events,
            "revisit_count": total_events // 5,
            "add_to_cart": cart_events,
            "remove_from_cart": 0,
            "checkout_visits": cart_events // 2,
            "hover_time": total_events * 3,
            "comparison_clicks": scroll_events // 3,
            "wishlist_actions": cart_events // 4
        }