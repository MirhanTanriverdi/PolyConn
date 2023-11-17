# PolyConn Project Description

**PolyConn** is an innovative platform designed to foster community engagement and local discovery. It serves as a comprehensive hub where users can connect with their local district communities, explore cafes, and participate in a variety of events. The platform is tailored to enhance the social and cultural experience of its users by offering a range of interactive features and functionalities.

ERD = http://www.plantuml.com/plantuml/dumla/bPHDwvj04CRlVWgF_HU4K0Y54aAWBvTUGg7dPNH7ix3kokne6qo_UxEYMOaRQxqeyupF_6PczUGOYDjQ9sXOyJNzeXoJAZZja_H-lK-LJ3-boZ1MIEdXSFv-F8wAWHhlMWTKN83UVToz9N-IoUUdGzhWqJga9vyF-_tRg3RWt2zBCgvY3Kh7f2mRC-JOZ7W2-1O0eC8WZR4AZKIQEUztKqq3hAm1xLkCGbL8DHZHa2rLeT0KLw6nmnZdQDUXq62grfD4apG26MMgHvgBvrridgkb67Ro6KhSljT81P2IqFaAZB_vlsVjMiMGQnIb9O4T6lPMkRKQmSmuVw13weP9Ry2ba2qai4VtDrOrJeJXhAtG5L1YJ8w3YJCGgq8ruBle8omngtKGNsagzTMFPqFtwFD4V6L1vslpGb-TsDfEdxxrmBi-wW3rSWB9unzqksMPxGV_HT0VvaLme4Xy_XYPhop4R_tBLIRUD_RoxFcV7WF6d3vmBQCdDBAjzLy0

# Core Functionalities:

### **User-Related Features:**

1. **Profile Management**:
    - Users can update their profile information, including age, gender, nationality, language proficiencies, and hobbies.
2. **Joining Districts and Viewing Local Cafes**:
    - Users can join a district community by selecting their district.
    - Users can view a list of cafes within their district.
3. **Event Discovery**:
    - Users can view upcoming events in their district.
    - Users can filter events by type, such as music, sports, and workshops.

### **Event and Reservation Features:**

1. **Event Participation**:
    - Users can RSVP to events by making a reservation.
    - Users can join the guest list of an event (managed through the **`UserEvent`** table).
2. **Event and Reservation History**:
    - Users can view a history of events they have participated in (tracked via **`UserEvent`** and **`Reservation_Participants`**).

### **Event Organizer Features:**

1. **Event Creation and Management**:
    - Event organizers can create events, specifying the name, type, date, and associated district.
    - Event organizers can view the list of attendees (via the **`UserEvent`** table).

### **Cafe Features:**

1. **Cafe Management**:
    - Cafe owners can update information about their cafe, including the address and whether it's suitable for events.

### Possible Future Enhancements:

PolyConn aims to continually evolve and enhance the user experience. Proposed future developments include:

- **Reviews and Ratings**: Introduction of a review system for users to rate and provide feedback on cafes and events.
- **Financial Transactions**: Secure handling of financial aspects such as event fees and subscriptions.
- **Personalized Recommendations**: Utilizing user data to offer personalized event and cafe suggestions.
- **Social Networking**: Building community through social features, like friend connections and interest groups.
- **Analytics for Organizers**: Providing valuable insights to event organizers and cafe owners through analytics.
- **Mobile App Integration**: Expanding accessibility with a mobile application for on-the-go interaction.

The PolyConn project is not just a platform; it's a gateway to a more connected and engaging community experience, bridging the gap between local events, cafes, and people.